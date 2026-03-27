#!/usr/bin/env ruby
# frozen_string_literal: true

# Compares Jekyll-computed doc URLs between a base ref (default: origin/develop) and HEAD,
# then checks assets/js/broken_redirect_list.js for matching old -> new mappings.
#
# Usage (from repo root):
#   bundle exec ruby scripts/validate_doc_redirects.rb
#   bundle exec ruby scripts/validate_doc_redirects.rb --base origin/develop
#   bundle exec ruby scripts/validate_doc_redirects.rb --skip-fetch
#
# Requires: git, bundler, gems from Gemfile (Jekyll). Uses a temporary git worktree for the base ref.

require "fileutils"
require "json"
require "open3"
require "optparse"
require "set"
require "tempfile"
require "tmpdir"

REPO_ROOT = begin
  out, err, st = Open3.capture3("git", "rev-parse", "--show-toplevel")
  raise "Failed to determine repository root. Is this a git checkout?\n#{err}" unless st.success?

  out.strip
end
DUMP_SCRIPT = File.expand_path("jekyll_url_map_dump.rb", __dir__)
REDIRECT_REL = "assets/js/broken_redirect_list.js"
RX_VALIDURL = /validurls\['([^']+)'\]\s*=\s*'([^']*)'(?:;)?/

def run!(argv)
  options = { base: "origin/develop", fetch: true, json_out: nil }
  OptionParser.new do |o|
    o.banner = "usage: validate_doc_redirects.rb [options]"
    o.on("--base REF", "Git ref to compare against (default: origin/develop)") { |v| options[:base] = v }
    o.on("--skip-fetch", "Do not run git fetch for the base ref") { options[:fetch] = false }
    o.on("--json PATH", "Write machine-readable report to PATH") { |v| options[:json_out] = v }
    o.on("-h", "--help", "Show help") do
      puts o
      exit 0
    end
  end.parse!(argv)

  Dir.chdir(REPO_ROOT) do
    validate!(options)
  end
end

def sh_capture(*cmd)
  out, err, st = Open3.capture3(*cmd)
  raise "command failed: #{cmd.join(' ')}\n#{err}#{out}" unless st.success?

  out
end

def sh!(*cmd)
  system(*cmd, exception: true)
end

def normalize_url_for_compare(url)
  # Use a negative lookbehind so the repeated-slash collapse does not destroy
  # the "//" in an absolute URL scheme (e.g. "https://…" stays "https://…").
  # Lowercasing is intentionally omitted: case-only URL changes are real and
  # should be caught as mismatches rather than silently normalised away.
  u = url.to_s.strip.gsub(%r{(?<!:)//+}, "/")
  # Ruby: "".split("#", 2) => [] — always use indexed parts
  parts = u.split("#", 2)
  path = parts[0] || ""
  frag = parts[1] ? "##{parts[1]}" : nil
  q = nil
  if path.include?("?")
    pq = path.split("?", 2)
    path = pq[0] || ""
    q = pq[1] ? "?#{pq[1]}" : nil
  end
  path = path.chomp("/")
  file_segment = File.basename(path)
  has_extension = !file_segment.empty? && file_segment.match?(/\.[A-Za-z0-9]{2,}$/)
  path += "/" unless path.empty? || has_extension
  "#{path}#{q}#{frag}"
end

def parse_redirect_file(path)
  map = {}
  File.foreach(path, chomp: true) do |line|
    next if line.strip.start_with?("//")
    next unless line.include?("validurls[")

    m = RX_VALIDURL.match(line)
    next unless m

    from = normalize_url_for_compare(m[1])
    to_raw = m[2].to_s.strip
    next if to_raw.empty?

    to = normalize_url_for_compare(to_raw)
    map[from] = to
  end
  map
end

def jekyll_url_map(site_root)
  tmp = Tempfile.new(["jekyll-url-map", ".json"])
  tmp.close
  Dir.chdir(site_root) do
    sh!("bundle", "exec", "ruby", DUMP_SCRIPT, tmp.path)
  end
  JSON.parse(File.read(tmp.path))
ensure
  tmp&.unlink
end

def git_diff_name_status(base_ref)
  range = "#{base_ref}...HEAD"
  out = sh_capture("git", "diff", "--name-status", "-M20%", range, "--", "_docs/")
  rows = []
  out.each_line do |line|
    line = line.chomp
    next if line.empty?

    parts = line.split("\t", -1)
    status = parts[0]
    case status
    when /^R\d*/
      rows << [:rename, parts[1], parts[2]]
    when "M", "A", "D", "T"
      rows << [status.downcase.to_sym, parts[1]]
    else
      rows << [:unknown, line]
    end
  end
  rows
end

def required_redirects(url_map_base, url_map_head, diff_rows)
  needed = {} # old_url_norm => new_url_norm
  md_paths = lambda { |p| p.end_with?(".md") }

  renames = diff_rows.select { |r| r[0] == :rename }
  deleted = diff_rows.select { |r| r[0] == :d }.map { |r| r[1] }.select(&md_paths)
  added = diff_rows.select { |r| r[0] == :a }.map { |r| r[1] }.select(&md_paths)
  modified = diff_rows.select { |r| r[0] == :m }.map { |r| r[1] }.select(&md_paths)

  renamed_sources = renames.map { |(_, old_p, _)| old_p }.to_set

  # Process renames: use git's rename detection to pair old→new paths.
  renames.each do |(_, old_p, new_p)|
    next unless md_paths.call(old_p) && md_paths.call(new_p)

    old_u = url_map_base[old_p]
    new_u = url_map_head[new_p]
    next if old_u.nil? || new_u.nil?
    next if normalize_url_for_compare(old_u) == normalize_url_for_compare(new_u)

    needed[normalize_url_for_compare(old_u)] = normalize_url_for_compare(new_u)
  end

  # Detect URL changes for all paths shared between base and HEAD. Comparing
  # URL maps directly (rather than relying solely on the _docs/ git diff) catches
  # permalink re-URLs driven by _config.yml or _plugins/ changes, where doc files
  # themselves are not modified.
  head_keys = url_map_head.keys.to_set
  url_map_base.each_key do |p|
    next unless md_paths.call(p)
    next unless head_keys.include?(p)
    next if renamed_sources.include?(p)

    old_u = normalize_url_for_compare(url_map_base[p])
    new_u = normalize_url_for_compare(url_map_head[p])
    next if old_u == new_u

    needed[old_u] = new_u
  end

  # Deleted pages: paths present in the base URL map but absent from HEAD's map
  # (and not the source of a rename) need a manual redirect to a replacement URL.
  url_map_base.each_key do |p|
    next unless md_paths.call(p)
    next if head_keys.include?(p)
    next if renamed_sources.include?(p)

    old_u = url_map_base[p]
    next if old_u.nil?

    needed[normalize_url_for_compare(old_u)] = :deleted_no_target
  end

  [needed, { renames: renames.size, modified: modified.size, deleted: deleted.size, added: added.size }]
end

def validate!(options)
  base_ref = options[:base]

  if options[:fetch] && base_ref.match?(/\Aorigin\/[\w\-\.\/]+\z/)
    sh!("git", "fetch", "--quiet", "origin", base_ref.delete_prefix("origin/"))
  end

  resolve_ref = sh_capture("git", "rev-parse", "--verify", base_ref).strip

  tmp_parent = Dir.mktmpdir("braze-redirect-validate")
  worktree = File.join(tmp_parent, "base-tree")
  begin
    sh!("git", "-C", REPO_ROOT, "worktree", "add", "--detach", worktree, resolve_ref)

    puts "Building URL map for #{base_ref} (#{resolve_ref[0..12]})…"
    map_base = jekyll_url_map(worktree)
    puts "Building URL map for HEAD…"
    map_head = jekyll_url_map(REPO_ROOT)
  ensure
    success = system("git", "-C", REPO_ROOT, "worktree", "remove", "-f", worktree, out: File::NULL, err: File::NULL)
    FileUtils.remove_entry(tmp_parent, true)
    unless success
      system("git", "-C", REPO_ROOT, "worktree", "prune", out: File::NULL, err: File::NULL)
      raise "Failed to remove git worktree at #{worktree}"
    end
  end

  # Use resolve_ref (the exact SHA) so the diff is guaranteed to be based on
  # the same commit that was checked out for the base URL map, even if base_ref
  # is a mutable ref (branch or remote-tracking branch) that could advance.
  diff_rows = git_diff_name_status(resolve_ref)
  needed, stats = required_redirects(map_base, map_head, diff_rows)

  redirect_path = File.join(REPO_ROOT, REDIRECT_REL)
  redirects = parse_redirect_file(redirect_path)

  missing = []
  wrong = []
  deleted_warn = []

  needed.each do |from_norm, to_norm|
    if to_norm == :deleted_no_target
      # Manual redirect in broken_redirect_list.js is sufficient when the doc file
      # is gone from HEAD (no Jekyll URL to diff against).
      if redirects[from_norm].nil?
        deleted_warn << { old_url: from_norm, note: "Page removed; add redirect manually to a replacement URL." }
      end
      next
    end

    actual_to = redirects[from_norm]
    if actual_to.nil?
      missing << { old_url: from_norm, expected_new: to_norm }
      next
    end

    next if actual_to == to_norm

    wrong << { old_url: from_norm, expected_new: to_norm, mapped_new: actual_to }
  end

  report = {
    base_ref: base_ref,
    base_sha: resolve_ref,
    diff_stats: stats,
    counts: {
      required_redirects: needed.count { |_, t| t != :deleted_no_target },
      missing: missing.size,
      wrong_target: wrong.size,
      deleted_pages: deleted_warn.size
    },
    missing: missing,
    wrong_target: wrong,
    deleted_pages: deleted_warn
  }

  if options[:json_out]
    File.write(options[:json_out], JSON.pretty_generate(report))
    puts "Wrote #{options[:json_out]}"
  end

  puts ""
  puts "Doc redirect validation (Jekyll URL maps vs #{REDIRECT_REL})"
  puts "  Base: #{base_ref} @ #{resolve_ref[0..11]}"
  puts "  Git diff (#{base_ref}...HEAD under _docs/): #{stats[:renames]} renames, #{stats[:modified]} modified, #{stats[:deleted]} deleted, #{stats[:added]} added"
  puts "  Required old→new mappings (URL changed or page deleted): #{report[:counts][:required_redirects] + report[:counts][:deleted_pages]}"
  puts ""

  if deleted_warn.any?
    puts "Deleted pages (need a manual redirect target in #{REDIRECT_REL}):"
    deleted_warn.each { |row| puts "  - #{row[:old_url]}" }
    puts ""
  end

  if missing.any?
    puts "Missing redirects (add validurls['OLD'] = 'NEW';):"
    missing.each { |row| puts "  - #{row[:old_url]}  →  #{row[:expected_new]}" }
    puts ""
  end

  if wrong.any?
    puts "Wrong redirect target:"
    wrong.each do |row|
      puts "  - #{row[:old_url]}"
      puts "      expected: #{row[:expected_new]}"
      puts "      mapped:   #{row[:mapped_new]}"
    end
    puts ""
  end

  if missing.empty? && wrong.empty? && deleted_warn.empty?
    puts "OK — all required redirects are present and targets match."
    exit 0
  end

  puts "FAILED — fix #{REDIRECT_REL} before merging."
  exit 1
end

run!(ARGV) if $PROGRAM_NAME == __FILE__
