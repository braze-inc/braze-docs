# frozen_string_literal: true

require "date"
require "open3"
require "pathname"
require "set"
require "time"

module Jekyll
  class GitLastModifiedGenerator < Generator
    safe true
    priority :low

    TAG_BODY = %r!
      \{%-?\s*(include|multi_lang_include|mdexp_multi_lang_include)\s+
      (.+?)
      \s*-?\%\}
    !mx.freeze

    MARKDOWN_EXTS = %w[.md .markdown .mkd].freeze

    # Directory names under _lang/ — keep in sync with multi_lang_include.rb (IncludeAbsoluteTag::LANGUAGE_MAP).
    MULTI_LANG_LANGUAGE_MAP = {
      "fr" => "fr_fr",
      "pt-br" => "pt_br",
    }.freeze

    class << self
      attr_accessor :git_log_cache, :deps_cache
    end

    self.git_log_cache = {}
    self.deps_cache = {}

    def generate(site)
      # Disable all last_modified_at computation (no meta tags / visible line from this plugin).
      return if ENV["JEKYLL_GIT_LAST_MODIFIED"] == "false"

      self.class.git_log_cache.clear
      self.class.deps_cache.clear

      @site = site
      @source = File.expand_path(site.source)
      @resolved_lang = resolve_site_lang
      @use_git = git_repo?

      unless @use_git
        Jekyll.logger.info "GitLastModified:", "Git unavailable; using filesystem mtimes for last_modified_at"
      end

      (site.documents + site.pages).each { |item| apply_last_modified!(item) }
    end

    private

    def resolve_site_lang
      cfg = (@site.config["language"] || "en").to_s
      MULTI_LANG_LANGUAGE_MAP[cfg] || cfg
    end

    # Match multi_lang_include: prefer _lang/<lang>/_includes/<file>, then _includes/<file>.
    # Jekyll's built-in {% include %} always resolves under _includes/ (no locale prefix).
    def resolve_include_abs(inc)
      if @resolved_lang != "en"
        lang_abs = File.join(@source, "_lang", @resolved_lang, "_includes", inc)
        return lang_abs if File.file?(lang_abs)
      end
      File.join(@source, "_includes", inc)
    end

    def include_abs_for_tag(tag_name, inc)
      tag_name == "include" ? File.join(@source, "_includes", inc) : resolve_include_abs(inc)
    end

    def apply_last_modified!(item)
      return unless processable?(item)
      return if item.data["last_modified_at"]

      abs = content_markdown_abs(item)
      if abs.nil? || !File.file?(abs)
        rel = path_relative_to_source(item)
        if rel && !rel.empty?
          fa = File.join(@source, rel)
          abs = fa if File.file?(fa)
        end
      end
      return if abs.nil? || !File.file?(abs)

      dep_abs, rel_paths = dependency_and_rel_paths_for(abs)
      ts = latest_timestamp_for(rel_paths, dep_abs, use_git: @use_git)
      ts ||= date_from_frontmatter(item)
      item.data["last_modified_at"] = ts if ts
    end

    def dependency_and_rel_paths_for(abs)
      if markdown_file?(abs)
        dep_abs = dependency_files_for(abs)
        rel_paths = dep_abs.filter_map { |p| relative_to_source(p) }.uniq
        [dep_abs, rel_paths]
      else
        dep_abs = [abs]
        rel_paths = [relative_to_source(abs)].compact
        [dep_abs, rel_paths]
      end
    end

    def markdown_file?(path)
      MARKDOWN_EXTS.include?(File.extname(path).downcase)
    end

    def date_from_frontmatter(item)
      d = item.data["date"]
      return nil if d.nil?

      case d
      when Time then d.utc
      when Date then Time.utc(d.year, d.month, d.day)
      when String then Time.parse(d).utc
      else
        nil
      end
    rescue ArgumentError
      nil
    end

    def processable?(item)
      return false if item.respond_to?(:output) && item.output == false
      return false if item.data && item.data["output"] == false

      true
    end

    # Resolve the Markdown file whose Git history and {% include %} graph define last_modified_at.
    # Paths under _lang/<locale>/... use that locale file; English articles stay under _docs/ as before.
    def content_markdown_abs(item)
      raw = path_relative_to_source(item)
      return nil if raw.nil? || raw.empty?

      return File.join(@source, raw) if raw.start_with?("_docs/") && File.file?(File.join(@source, raw))

      under_docs = File.join(@source, "_docs", raw)
      return under_docs if File.file?(under_docs)

      fallback = File.join(@source, raw)
      return fallback if File.file?(fallback)

      nil
    end

    def path_relative_to_source(item)
      p = item.path.to_s
      pathname = Pathname.new(p)
      rel = if pathname.absolute?
              pathname.relative_path_from(Pathname.new(@source))
            else
              pathname
            end
      rel.to_s.tr("\\", "/")
    end

    def relative_to_source(abs_path)
      abs_path = File.expand_path(abs_path)
      return nil unless abs_path.start_with?("#{@source}/") || abs_path == @source

      Pathname.new(abs_path).relative_path_from(Pathname.new(@source)).to_s.tr("\\", "/")
    end

    def dependency_files_for(markdown_abs)
      self.class.deps_cache[markdown_abs] ||= begin
        set = Set.new
        walk_includes(markdown_abs, set, 0)
        set.to_a
      end
    end

    MAX_INCLUDE_DEPTH = 64

    def walk_includes(abs_path, set, depth)
      return if depth > MAX_INCLUDE_DEPTH
      return unless abs_path.start_with?(@source)
      return unless File.file?(abs_path)

      return if set.include?(abs_path)

      set.add(abs_path)

      content = read_utf8(abs_path)
      include_refs(content).each do |tag_name, inc|
        inc_abs = include_abs_for_tag(tag_name, inc)
        walk_includes(inc_abs, set, depth + 1) if File.file?(inc_abs)
      end
    end

    def read_utf8(path)
      File.read(path, encoding: "UTF-8")
    rescue ArgumentError, Encoding::InvalidByteSequenceError
      File.read(path, mode: "rb").force_encoding("UTF-8")
    end

    # Returns [tag_name, path] pairs. Path is relative to _includes/ for resolution (see include_abs_for_tag).
    # mdexp_multi_lang_include uses a separate export-time resolver in markdown_copy_llm.rb; not mirrored here.
    def include_refs(content)
      refs = []
      content.scan(TAG_BODY) do |tag_name, inner|
        rest = inner.to_s.strip
        next if rest.lstrip.start_with?("{{")

        path_token = first_include_path_token(rest)
        next if path_token.nil? || path_token.empty?
        next if path_token.include?("{{") || path_token.include?("}}")
        next unless safe_include_path?(path_token)

        refs << [tag_name, path_token.tr("\\", "/")]
      end
      refs.uniq
    end

    def first_include_path_token(rest)
      if (m = rest.match(/\A(["'])(.*?)\1/m))
        return m[2]
      end

      rest.split(%r{\s+}, 2).first
    end

    def safe_include_path?(file)
      f = file.to_s.tr("\\", "/")
      return false if f.empty?
      return false if f.start_with?("/")
      return false if f.include?(":")
      !f.include?("..") && !f.match?(%r{/{2,}})
    end

    def git_repo?
      _, status = Open3.capture2("git", "-C", @source, "rev-parse", "--is-inside-work-tree", err: File::NULL)
      status.success?
    end

    def cache_key_for(rel_paths, abs_paths)
      if rel_paths.any?
        "r:#{rel_paths.sort.join("\0")}"
      else
        files = abs_paths.select { |p| File.file?(p) }.map { |p| File.expand_path(p) }.sort
        "a:#{files.join("\0")}"
      end
    end

    def latest_timestamp_for(rel_paths, abs_paths, use_git:)
      key = cache_key_for(rel_paths, abs_paths)
      return self.class.git_log_cache[key] if self.class.git_log_cache.key?(key)

      iso = nil
      if use_git && rel_paths.any?
        cmd = ["git", "-C", @source, "log", "-1", "--format=%cI", "--", *rel_paths]
        iso, s = Open3.capture2(*cmd, err: File::NULL)
        iso = iso.to_s.strip
        iso = nil unless s.success? && !iso.empty?
      end

      parsed = parse_iso(iso) if iso
      parsed ||= max_mtime(abs_paths)

      self.class.git_log_cache[key] = parsed
    end

    def parse_iso(iso)
      Time.parse(iso).utc
    rescue ArgumentError
      nil
    end

    def max_mtime(abs_paths)
      mtimes = abs_paths.select { |p| File.file?(p) }.map { |p| File.mtime(p) }
      return nil if mtimes.empty?

      mtimes.max.utc
    end
  end
end
