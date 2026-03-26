#!/usr/bin/env ruby

require 'find'
require 'time'
require 'json'

LANGUAGES = ['en', 'de', 'es', 'fr_fr', 'ja', 'ko', 'pt_br'].freeze
ALLOWED_FOLDERS = ['_home', '_user_guide', '_developer_guide', '_api', '_partners', '_help', '_contributing'].freeze
INCREMENTAL_SINCE = '2 weeks ago'.freeze

def check_git!
  unless system('git rev-parse --git-dir > /dev/null 2>&1')
    puts "Error: Not in a git repository or git not available"
    exit 1
  end
end

def folder_patterns(directory)
  ALLOWED_FOLDERS.map { |f| "'#{directory}/#{f}/**/*.md'" }.join(' ')
end

def format_git_date(raw)
  Time.parse(raw).utc.strftime('%Y-%m-%dT%H:%M:%S+00:00')
end

# Full scan: get last-commit date for every tracked .md file in one pass.
def get_all_git_dates(directory)
  puts "Getting git history for all files..."

  patterns = folder_patterns(directory)
  cmd = "git ls-files #{patterns} | xargs -I {} git log -1 --format='{}|%cI' -- {}"
  result = `#{cmd}`.strip

  git_dates = {}
  return git_dates if result.empty? || $?.exitstatus != 0

  result.split("\n").each do |line|
    next if line.strip.empty?
    parts = line.split('|')
    next unless parts.length == 2

    begin
      git_dates[parts[0]] = format_git_date(parts[1])
    rescue => e
      puts "Warning: Could not parse date for #{parts[0]}: #{e.message}"
    end
  end

  puts "Found git history for #{git_dates.length} files"
  git_dates
end

# Incremental: single git-log call to get files changed recently and their
# most-recent commit date.
def get_recent_git_dates(directory)
  puts "Getting files changed since #{INCREMENTAL_SINCE}..."

  patterns = folder_patterns(directory)
  cmd = "git log --since='#{INCREMENTAL_SINCE}' --name-only --pretty=format:'%cI' -- #{patterns}"
  result = `#{cmd}`.strip

  git_dates = {}
  current_date = nil

  result.split("\n").each do |line|
    line = line.strip.delete("'")
    next if line.empty?

    if line.match?(/^\d{4}-\d{2}-\d{2}T/)
      current_date = line
    elsif current_date && line.end_with?('.md')
      unless git_dates.key?(line)
        begin
          git_dates[line] = format_git_date(current_date)
        rescue => e
          puts "Warning: Could not parse date: #{e.message}"
        end
      end
    end
  end

  puts "Found #{git_dates.length} files modified since #{INCREMENTAL_SINCE}"
  git_dates
end

def today_timestamp
  Time.now.utc.strftime('%Y-%m-%dT%H:%M:%S+00:00')
end

def get_single_file_date(path)
  date_str = `git log -1 --format='%cI' -- '#{path}'`.strip
  return today_timestamp if date_str.empty?

  format_git_date(date_str)
rescue => e
  puts "Warning: Could not parse date for #{path}: #{e.message}"
  today_timestamp
end

def load_existing_data(output_file)
  return {} unless File.exist?(output_file)

  data = JSON.parse(File.read(output_file))
  data.transform_values! { |v| v.length <= 10 ? "#{v}T00:00:00+00:00" : v }
  puts "Loaded #{data.length} existing entries from #{output_file}"
  data
rescue JSON::ParserError => e
  puts "Warning: Could not parse existing data file (#{e.message}), running full scan"
  {}
end

def generate_file_listing(directory, output_file, full: false)
  unless Dir.exist?(directory)
    puts "Error: Directory '#{directory}' does not exist"
    exit 1
  end

  existing_data = full ? {} : load_existing_data(output_file)
  incremental = !existing_data.empty?

  git_dates = if incremental
                get_recent_git_dates(directory)
              else
                get_all_git_dates(directory)
              end

  file_data = existing_data.dup
  missing_files = []

  ALLOWED_FOLDERS.each do |folder|
    folder_path = File.join(directory, folder)
    next unless Dir.exist?(folder_path)

    Find.find(folder_path) do |path|
      next if File.directory?(path)
      next unless path.end_with?('.md')

      relative_path = path.sub(/^#{Regexp.escape(directory)}\//, '')

      if git_dates[path]
        file_data[relative_path] = git_dates[path]
      elsif incremental && !existing_data.key?(relative_path)
        missing_files << path
      elsif !incremental && !git_dates.key?(path)
        file_data[relative_path] = today_timestamp
      end
    end
  end

  unless missing_files.empty?
    puts "Backfilling #{missing_files.length} new files not in existing data..."
    missing_files.each do |path|
      relative_path = path.sub(/^#{Regexp.escape(directory)}\//, '')
      file_data[relative_path] = get_single_file_date(path)
    end
  end

  if incremental
    before = file_data.length
    file_data.reject! do |key, _|
      full_path = File.join(directory, key)
      missing = !File.exist?(full_path)
      puts "Pruning deleted file: #{key}" if missing
      missing
    end
    pruned = before - file_data.length
    puts "Pruned #{pruned} deleted entries" if pruned > 0
  end

  File.open(output_file, 'w') do |file|
    file.write(JSON.pretty_generate(file_data))
  end

  mode_label = incremental ? "incremental" : "full"
  puts "File listing generated (#{mode_label}): #{output_file} (#{file_data.length} files)"
end

# ── CLI ──────────────────────────────────────────────────────────────────────

full_mode = ARGV.delete('--full')

if ARGV.length > 2
  puts "Usage: ruby #{$0} [locale] [output_file] [--full]"
  puts ""
  puts "Options:"
  puts "  locale       Language code (#{LANGUAGES.join(', ')}) or 'all'. Default: en"
  puts "  output_file  Custom output path (ignored with 'all'). Default: _data/sitemap_<locale>.json"
  puts "  --full       Force a full git scan even when existing data is available"
  puts ""
  puts "Examples:"
  puts "  ruby #{$0}                  # incremental update for en"
  puts "  ruby #{$0} all              # incremental update for all languages"
  puts "  ruby #{$0} all --full       # full scan for all languages"
  puts "  ruby #{$0} ja               # incremental update for ja"
  puts "  ruby #{$0} en --full        # full scan for en"
  puts "  ruby #{$0} en custom.json   # custom output path"
  exit 1
end

check_git!

locale = ARGV[0] || 'en'
output_file = ARGV[1]

if locale == 'all'
  LANGUAGES.each do |lang|
    directory = lang == 'en' ? '_docs' : "_lang/#{lang}"
    out = "_data/sitemap_#{lang}.json"
    puts "\n=== Processing #{lang} ==="
    generate_file_listing(directory, out, full: full_mode)
  end
else
  unless LANGUAGES.include?(locale)
    puts "Error: Unknown locale '#{locale}'. Supported: #{LANGUAGES.join(', ')}, all"
    exit 1
  end
  directory = locale == 'en' ? '_docs' : "_lang/#{locale}"
  out = output_file || "_data/sitemap_#{locale}.json"
  generate_file_listing(directory, out, full: full_mode)
end
