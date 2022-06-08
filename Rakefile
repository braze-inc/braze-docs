def thread_pool
  @thread_pool ||= ThreadPool.new options.thread_pool_size
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
  end
end
def jekyll_serve(config_file = '_config.yml')
  if ENV["RACK_ENV"] == 'staging'
    pipe "bundle exec jekyll s --port 5006 --config #{config_file}"
  else
    # Force a clean build of the site and the pipeline assets
    puts `rm .jekyll-metadata`
    pipe "bundle exec jekyll s --port 5006 --incremental --config #{config_file},_incremental_config.yml"
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
  task :proxy_serve do
    pipe 'bundle exec ruby proxy.rb'
  end
end

namespace :docs_fr do
  config_file = './_config.yml,./_lang/_config_fr.yml'
  task :build do
    jekyll_build(config_file, 'fr')
  end
  task :serve do
    jekyll_serve(config_file)
  end
  task :proxy_serve do
    pipe 'bundle exec ruby proxy.rb fr'
  end
end

namespace :assets do
  task :precompile do
    print 'no-op'
  end
end

multitask fr: [
  'docs_fr:serve', 'docs_fr:proxy_serve'
]

multitask en: [
  'docs_en:serve', 'docs_en:proxy_serve'
]

multitask serve: [
  'docs_en:serve', 'docs_en:proxy_serve'
]
