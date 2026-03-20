# frozen_string_literal: true

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

    class << self
      attr_accessor :git_log_cache, :deps_cache
    end

    self.git_log_cache = {}
    self.deps_cache = {}

    def generate(site)
      return if ENV["JEKYLL_GIT_LAST_MODIFIED"] == "false"

      @site = site
      @source = File.expand_path(site.source)

      unless git_repo?
        Jekyll.logger.warn "GitLastModified:", "Not a Git repo or git missing; leaving last_modified_at unset"
        return
      end

      (site.documents + site.pages).each { |item| apply_last_modified!(item) }
    end

    private

    def apply_last_modified!(item)
      return unless processable?(item)

      abs = content_markdown_abs(item)
      return if abs.nil? || !File.file?(abs)

      dep_abs = dependency_files_for(abs)
      rel_paths = dep_abs.filter_map { |p| relative_to_source(p) }.uniq

      ts = latest_timestamp_for(rel_paths, dep_abs)
      item.data["last_modified_at"] = ts if ts
    end

    def processable?(item)
      return false if item.respond_to?(:output) && item.output == false
      return false if item.data && item.data["output"] == false

      true
    end

    # Prefer English canonical under _docs/ for localized paths; else use the page's own source file.
    def content_markdown_abs(item)
      raw = path_relative_to_source(item)
      return nil if raw.nil? || raw.empty?

      if (m = raw.match(%r{\A_lang/[^/]+/(.+)\z}))
        candidate = "_docs/#{m[1]}"
        cand_abs = File.join(@source, candidate)
        return cand_abs if File.file?(cand_abs)
      end

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

    def dependency_files_for(canonical_md_abs)
      self.class.deps_cache[canonical_md_abs] ||= begin
        set = Set.new
        walk_includes(canonical_md_abs, set, 0)
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
      include_refs(content).each do |inc|
        inc_abs = File.join(@source, "_includes", inc)
        walk_includes(inc_abs, set, depth + 1) if File.file?(inc_abs)
      end
    end

    def read_utf8(path)
      File.read(path, encoding: "UTF-8")
    rescue ArgumentError, Encoding::InvalidByteSequenceError
      File.read(path, mode: "rb").force_encoding("UTF-8")
    end

    # Yields include paths relative to _includes/ (English canonical — matches multi_lang_include for :en).
    def include_refs(content)
      refs = []
      content.scan(TAG_BODY) do |_tag, inner|
        rest = inner.to_s.strip
        next if rest.lstrip.start_with?("{{")

        path_token = first_include_path_token(rest)
        next if path_token.nil? || path_token.empty?
        next if path_token.include?("{{") || path_token.include?("}}")
        next unless safe_include_path?(path_token)

        refs << path_token.tr("\\", "/")
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
      !file.include?("..") && !file.match?(%r{/{2,}})
    end

    def git_repo?
      _, status = Open3.capture2("git", "-C", @source, "rev-parse", "--is-inside-work-tree", err: File::NULL)
      status.success?
    end

    def latest_timestamp_for(rel_paths, abs_paths)
      key = rel_paths.sort.join("\0")
      return self.class.git_log_cache[key] if self.class.git_log_cache.key?(key)

      iso = nil
      if rel_paths.any?
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
