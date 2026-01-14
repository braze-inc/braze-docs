require 'fileutils'
require 'find'
require 'thread'

# File watching functionality
def watch_includes_folder
  puts "Starting file watcher for _includes folder..."
  load 'includes_watcher.rb'
  watcher = IncludesWatcher.new
  watcher.start
rescue Interrupt
  puts "File watcher interrupted, shutting down..."
rescue => e
  puts "File watcher error: #{e.message}"
end

def pipe(command)
  output = ''
  IO.popen(command) do |io|
    until io.eof?
      buffer = io.gets
      output << buffer
      puts buffer
    end
  end

  output
end

task default: :serve

def jekyll_build(config_file = '_config.yml', lang = 'en')
  public_folder = './public'
  # puts `#{config_file}`
  puts `bundle exec jekyll build --config #{config_file}`
  if (lang != 'en')
    index_file = File.join(public_folder, "index_#{lang}.html")
    FileUtils.copy_file(index_file, File.join('_site', "index.html"))
    FileUtils.copy_file(File.join("_site/docs/#{lang}", "404.html"), File.join('_site', "404.html"))
  end
end
def jekyll_serve(config_file = '_config.yml')
  if ENV["RACK_ENV"] == 'staging'
    pipe "bundle exec jekyll s --port 5006 --config #{config_file}"
  else
    # Force a clean build of the site and the pipeline assets
    puts `rm .jekyll-metadata`
    
    # Start file watcher in a separate thread
    watcher_thread = Thread.new do
      watch_includes_folder
    end
    
    # Set up signal handlers to stop the watcher thread
    Signal.trap('INT') do
      puts "\nStopping Jekyll serve and file watcher..."
      watcher_thread.raise Interrupt
      exit 0
    end
    
    Signal.trap('TERM') do
      puts "\nStopping Jekyll serve and file watcher..."
      watcher_thread.raise Interrupt
      exit 0
    end
    
    begin
      pipe "bundle exec jekyll s --port 5006 --incremental --config #{config_file},_incremental_config.yml"
    ensure
      # Ensure the watcher thread is stopped when Jekyll exits
      watcher_thread.raise Interrupt if watcher_thread.alive?
      watcher_thread.join(2) # Wait up to 2 seconds for clean shutdown
    end
  end
end

namespace :docs_en do
  config_file = './_config.yml'
  task :index do
    if ENV["SITE_URL"] == 'https://www.braze.com' && ENV["RACK_ENV"] == 'production'
      puts `bundle exec jekyll algolia --config #{config_file}`
    end
  end
  task build: [:index] do
      jekyll_build(config_file, 'en')
  end
  task :serve do
    jekyll_serve(config_file)
  end
  task :serve_with_watch do
    jekyll_serve(config_file)
  end
  task :proxy_serve do
    pipe 'bundle exec ruby proxy.rb'
  end
end

namespace :lang do
  task :index, [:lang] do |t, args|
    config_file = "./_config.yml,./_lang/_config_#{args[:lang]}.yml"
    if ENV["SITE_URL"] == 'https://www.braze.com' && ENV["RACK_ENV"] == 'production'
      puts `bundle exec jekyll algolia --config #{config_file}`
    end
  end
  task :build, [:lang] => [:index] do |t, args|
    jekyll_build("./_config.yml,./_lang/_config_#{args[:lang]}.yml", args[:lang])
  end
  task :serve, [:lang] do |t, args|
    jekyll_serve("./_config.yml,./_lang/_config_#{args[:lang]}.yml")
  end
  task :serve_with_watch, [:lang] do |t, args|
    jekyll_serve("./_config.yml,./_lang/_config_#{args[:lang]}.yml")
  end
  task :proxy_serve, [:lang] do |t, args|
    pipe "bundle exec ruby proxy.rb #{args[:lang]}"
  end
end

namespace :assets do
  task :precompile do
    print 'no-op'
  end
end


# Usage: rake "lang[:lang]" ie
# rake "lang[:fr]"
# rake "lang[:ja]"
multitask :lang, [:lang] => [
  'lang:serve',
  'lang:proxy_serve'
]

multitask serve: [
  'docs_en:serve', 'docs_en:proxy_serve'
]

multitask en: [
  'docs_en:serve', 'docs_en:proxy_serve'
]

task :fr do
  Rake::Task["lang"].invoke('fr')
end

task :ja do
  Rake::Task["lang"].invoke('ja')
end

task :ko do
  Rake::Task["lang"].invoke('ko')
end

task :pt_br do
  Rake::Task["lang"].invoke('pt-br')
end

task :es do
  Rake::Task["lang"].invoke('es')
end

task :de do
  Rake::Task["lang"].invoke('de')
end

task :fr_build do
  Rake::Task["lang:build"].invoke('fr')
end

task :ja_build do
  Rake::Task["lang:build"].invoke('ja')
end

task :ko_build do
  Rake::Task["lang:build"].invoke('ko')
end

task :pt_br_build do
  Rake::Task["lang:build"].invoke('pt-br')
end

task :es_build do
  Rake::Task["lang:build"].invoke('es')
end

task :de_build do
  Rake::Task["lang:build"].invoke('de')
end

# Convenience tasks for file watching
task :serve_with_test_watch do
  Rake::Task["docs_en:serve_with_watch"].invoke
end

task :serve_with_lint_watch do
  Rake::Task["docs_en:serve_with_watch"].invoke
end

task :serve_with_build_watch do
  Rake::Task["docs_en:serve_with_watch"].invoke
end

# Usage examples:
# rake serve_with_test_watch          # Serve with file watching (same as serve_with_watch)
# rake serve_with_lint_watch          # Serve with file watching (same as serve_with_watch)
# rake serve_with_build_watch         # Serve with file watching (same as serve_with_watch)
# rake docs_en:serve_with_watch       # Serve English docs with file watching
# rake "lang:serve_with_watch[fr]"    # Serve French docs with file watching
