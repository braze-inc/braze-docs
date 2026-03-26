#!/usr/bin/env ruby
# frozen_string_literal: true

# Dumps a JSON object: "_docs-relative-path" => public URL (baseurl + document url).
# Used by validate_doc_redirects.rb. Run from repo root with: bundle exec ruby scripts/jekyll_url_map_dump.rb OUT.json

require "jekyll"
require "json"
require "tmpdir"

out_path = ARGV[0] or abort "usage: jekyll_url_map_dump.rb OUT.json"

Dir.mktmpdir("jekyll-url-map") do |dest|
  site = Jekyll::Site.new(
    Jekyll.configuration(
      "source" => ".",
      "quiet" => true,
      "safe" => false,
      "destination" => dest
    )
  )

  # Read documents and run generators (including custom permalink logic) so that
  # per-document URLs are correct. Skipping render/write avoids building the
  # entire site, which would be prohibitively slow in CI.
  site.read
  site.generate

  base = site.config["baseurl"].to_s.chomp("/")
  map = {}
  site.collections.each_value do |coll|
    coll.docs.each do |doc|
      # doc.relative_path is relative to site.collections_path (e.g. _docs/),
      # not to site.source. Use doc.path to get a repo-root-relative key that
      # matches git diff output (e.g. "_docs/_user_guide/foo.md").
      key = doc.path.delete_prefix("#{site.source}/")
      map[key] = base + doc.url
    end
  end

  File.write(out_path, JSON.generate(map))
end
