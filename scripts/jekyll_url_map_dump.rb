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

  # Run the full site processing pipeline so generators (including custom permalink logic)
  # can update per-document URLs before we read them.
  site.process

  base = site.config["baseurl"].to_s.chomp("/")
  map = {}
  site.collections.each_value do |coll|
    coll.docs.each do |doc|
      key = doc.relative_path.sub(%r{\A/}, "")
      map[key] = base + doc.url
    end
  end

  File.write(out_path, JSON.generate(map))
end
