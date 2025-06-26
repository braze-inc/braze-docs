#!/usr/bin/env ruby

require 'find'
require 'fileutils'

class IncludesWatcher
  def initialize(includes_path = '_includes')
    @includes_path = includes_path
    @initial_files = {}
    @running = false
  end

  def start
    puts "Starting file watcher for #{@includes_path}..."
    
    # Set up signal handlers for clean shutdown
    setup_signal_handlers
    
    # Get initial list of files with modification times
    update_initial_files
    puts "Watching #{@initial_files.length} files in #{@includes_path}..."
    
    @running = true
    
    # Watch for changes
    loop do
      break unless @running
      
      current_files = {}
      Find.find(@includes_path) do |path|
        if File.file?(path)
          current_files[path] = File.mtime(path)
        end
      end
      
      # Check for new, modified, or deleted files
      new_files = current_files.keys - @initial_files.keys
      modified_files = current_files.select { |path, mtime| @initial_files[path] && @initial_files[path] != mtime }.keys
      deleted_files = @initial_files.keys - current_files.keys
      
      if !new_files.empty? || !modified_files.empty? || !deleted_files.empty?
        changed_files = (new_files + modified_files + deleted_files).uniq
        puts "Detected changes in _includes folder: #{changed_files.join(', ')}"
        on_file_change(changed_files)
        @initial_files = current_files
      end
      
      # Use a shorter sleep and check running status more frequently
      sleep 0.5
    end
    
    puts "File watcher stopped."
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
  end

  def update_initial_files
    @initial_files = {}
    Find.find(@includes_path) do |path|
      if File.file?(path)
        @initial_files[path] = File.mtime(path)
      end
    end
  end

  def on_file_change(changed_files)
    # Remove .jekyll-metadata to force rebuild
    if File.exist?('.jekyll-metadata')
      FileUtils.rm('.jekyll-metadata')
      puts "Removed .jekyll-metadata to force Jekyll rebuild"
    end
    
    # Find and trigger regeneration of parent files that include the changed files
    changed_files.each do |changed_file|
      trigger_parent_regeneration(changed_file)
    end
  end

  def trigger_parent_regeneration(changed_file)
    # Convert the changed file path to the include path format
    include_path = changed_file.sub(@includes_path + '/', '')
    
    # Find all markdown files in _docs that might include this file
    parent_files = find_parent_files_with_include(include_path)
    
    parent_files.each do |parent_file|
      puts "Triggering regeneration of parent file: #{parent_file}"
      temporarily_modify_file(parent_file)
    end
  end

  def find_parent_files_with_include(include_path)
    parent_files = []
    
    # Search in _docs directory for files that include the changed file
    Find.find('_docs') do |path|
      if File.file?(path) && path.end_with?('.md')
        content = File.read(path)
        # Look for multi_lang_include or regular include statements
        if content.include?("multi_lang_include #{include_path}") || 
           content.include?("include #{include_path}") ||
           content.include?("{% multi_lang_include #{include_path} %}") ||
           content.include?("{% include #{include_path} %}")
          parent_files << path
        end
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

# Allow running directly
if __FILE__ == $0
  watcher = IncludesWatcher.new
  watcher.start
end 
