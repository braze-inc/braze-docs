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
      include_path = changed_file.sub(@includes_path + '/', '')
    end
    
    puts "Looking for includes of: #{include_path}"
    
    # Find all markdown files in _docs that might include this file
    parent_files = find_parent_files_with_include(include_path)

    puts "found parent files: #{parent_files}"
    
    parent_files.each do |parent_file|
      puts "Triggering regeneration of parent file: #{parent_file}"
      temporarily_modify_file(parent_file)
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

  def temporarily_modify_file(file_path)
    return unless File.exist?(file_path)
    
    # Read the original content
    original_content = File.read(file_path)
    
    # Add a temporary comment to trigger regeneration
    temp_content = original_content + "\n<!-- TEMP_REGENERATE_TRIGGER -->\n"
    
    # Write the modified content
    File.write(file_path, temp_content)
    
    # Wait a moment for Jekyll to detect the change
    sleep 0.1
    
    # Restore the original content
    File.write(file_path, original_content)
    
    puts "  ✓ Regenerated: #{file_path}"
  rescue => e
    puts "  ✗ Error regenerating #{file_path}: #{e.message}"
  end
end
