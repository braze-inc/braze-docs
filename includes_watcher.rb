#!/usr/bin/env ruby

require 'filewatcher'
require 'fileutils'

# This class is used to watch for changes in the _includes folder and trigger a rebuild of the parent files.
class IncludesWatcher
  def initialize()
    @running = false
  end

  def start
    puts "Starting file watcher..."
    
    # Set up signal handlers for clean shutdown
    setup_signal_handlers
    
    @running = true

    filewatcher = Filewatcher.new(["./_includes/"])
    filewatcher.watch do |changes|
      puts "\n\nchanges: #{changes}"
      if !@running
        puts "File watcher stopped."
        filewatcher.stop
        return
      end

      changes.each do |filename, event|
        on_file_change([filename])
      end
    end
  rescue Interrupt
    puts "File watcher interrupted, shutting down..."
  rescue => e
    puts "File watcher error: #{e.message}"
  ensure
    cleanup
  end

  def stop
    @running = false
  end

  private

  def setup_signal_handlers
    Signal.trap('INT') do
      puts "\nReceived interrupt signal, stopping file watcher..."
      stop
    end
    
    Signal.trap('TERM') do
      puts "\nReceived termination signal, stopping file watcher..."
      stop
    end
  end

  def cleanup
    puts "Cleaning up file watcher..."
    stop()
  end

  def on_file_change(changed_files)
    puts "on_file_change #{changed_files}"
    # Find and trigger regeneration of parent files that include the changed files
    changed_files.each do |changed_file|
      trigger_parent_regeneration(changed_file)
    end
  end

  def trigger_parent_regeneration(changed_file)
    # Convert the changed file path to the include path format
    # Handle both absolute and relative paths
    if changed_file.start_with?('/')
      # Absolute path - convert to relative path from _includes
      include_path = changed_file.sub(/.*\/_includes\//, '')
    else
      # Relative path - remove _includes prefix
      include_path = changed_file.sub('_includes/', '')
    end
    
    puts "Looking for includes of: #{include_path}"
    
    # Find all markdown files in _docs that might include this file
    parent_files = find_parent_files_with_include(include_path)

    puts "found parent files: #{parent_files}"
    
    # Batch process all parent files
    if !parent_files.empty?
      temporarily_modify_files_batch(parent_files)
    end
  end

  def find_parent_files_with_include(include_path)
    parent_files = []
    
    # Search in _docs directory for files that include the changed file
    Dir.glob('_docs/**/*.md').each do |path|
      content = File.read(path)
      # Look for multi_lang_include or regular include statements
      if content.include?("multi_lang_include #{include_path}") || 
         content.include?("include #{include_path}") ||
         content.include?("{% multi_lang_include #{include_path} %}") ||
         content.include?("{% include #{include_path} %}")
        parent_files << path
      end
    end
    
    parent_files
  end

  def temporarily_modify_files_batch(file_paths)
    return if file_paths.empty?
    
    puts "Triggering regeneration of #{file_paths.length} parent files..."
    
    # Store original contents
    original_contents = {}
    file_paths.each do |file_path|
      next unless File.exist?(file_path)
      original_contents[file_path] = File.read(file_path)
    end
    
    # Modify all files at once
    file_paths.each do |file_path|
      next unless File.exist?(file_path)
      temp_content = original_contents[file_path] + "\n<!-- TEMP_REGENERATE_TRIGGER -->\n"
      File.write(file_path, temp_content)
    end
    
    # Wait once for Jekyll to detect all changes
    sleep 0.1
    
    # Restore all files at once
    file_paths.each do |file_path|
      next unless File.exist?(file_path)
      File.write(file_path, original_contents[file_path])
      puts "  ✓ Regenerated: #{file_path}"
    end
    
    puts "Completed regeneration of #{file_paths.length} files"
  rescue => e
    puts "  ✗ Error in batch regeneration: #{e.message}"
  end
end
