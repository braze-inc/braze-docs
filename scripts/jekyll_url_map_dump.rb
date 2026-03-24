#!/usr/bin/env ruby
# frozen_string_literal: true

# Dumps a JSON object: "_docs-relative-path" => public URL (baseurl + document url).
# Used by validate_doc_redirects.rb. Run from repo root with: bundle exec ruby scripts/jekyll_url_map_dump.rb OUT.json

require "jekyll"
require "json"

out_path = ARGV[0] or abort "usage: jekyll_url_map_dump.rb OUT.json"

site = Jekyll::Site.new(
  Jekyll.configuration(
    "source" => ".",
    "quiet" => true,
    "safe" => false
  )
)
site.read

base = site.config["baseurl"].to_s.chomp("/")
map = {}
site.collections.each_value do |coll|
  coll.docs.each do |doc|
    key = File.join("_docs", doc.relative_path)
    map[key] = base + doc.url
  end
end

File.write(out_path, JSON.generate(map))
