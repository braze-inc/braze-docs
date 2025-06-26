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
    # Default behavior: remove .jekyll-metadata to force rebuild
    if File.exist?('.jekyll-metadata')
      FileUtils.rm('.jekyll-metadata')
      puts "Removed .jekyll-metadata to force Jekyll rebuild"
    end
  end
end

# Allow running directly
if __FILE__ == $0
  watcher = IncludesWatcher.new
  watcher.start
end 
