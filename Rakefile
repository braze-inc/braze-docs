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



namespace :academy do
  task :puma do
    Dir.chdir 'Archive' do
      Dir.chdir 'academy' do
        puts `bundle exec puma -t 0:4 -p 5000`
      end
    end
  end
  task :serve do
    pipe 'cd Archive && cd academy && bundle exec jekyll s -q --skip-initial-build --port 5000'
  end
end

namespace :documentation do
  task :puma do
    Dir.chdir 'Archive' do
      Dir.chdir 'documentation' do
        puts `bundle exec puma -t 0:4 -p 5004`
      end
    end
  end
  task :serve do
    pipe 'cd Archive && cd documentation && bundle exec jekyll s -q --skip-initial-build --port 5004'
  end
end


namespace :docs do
  task :index do
    if ENV["SITE_URL"] == 'https://www.braze.com' && ENV["RACK_ENV"] == 'production'
      puts `bundle exec jekyll algolia`
    end
  end
  task :build do
      puts `bundle exec jekyll build`
  end
  task puma: [:build,:index] do
      puts `bundle exec puma -t 8:32 -p 5006`
  end
  task :serve do
    pipe 'bundle exec jekyll s --port 5006'
  end
end

namespace :success do
  task :serve do
    pipe 'bundle exec ruby proxy.rb'
  end
end

namespace :assets do
  task :precompile do
    print 'no-op'
  end
end

multitask serve: [
  'docs:serve', 'success:serve'
]
