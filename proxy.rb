require 'rack/reverse_proxy'
require 'sinatra'

lang = ARGV.length > 0 ? ARGV[0].downcase : nil

use Rack::ReverseProxy do
  # Set :preserve_host to true globally (default is true already)
  reverse_proxy_options preserve_host: true
  reverse_proxy /^\/docs(\/.*)$/, 'http://localhost:5006/docs/$1'
end

set :port, 4000

get '/' do
  if !(lang.nil?) && (lang != 'en')
    send_file File.join(settings.public_folder, "index_#{lang}.html")
  else
    send_file File.join(settings.public_folder, 'index.html')
  end
end
