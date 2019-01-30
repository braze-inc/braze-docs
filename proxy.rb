require 'rack/reverse_proxy'
require 'sinatra'

use Rack::ReverseProxy do
  # Set :preserve_host to true globally (default is true already)
  reverse_proxy_options preserve_host: true
  reverse_proxy /^\/academy(\/.*)$/, 'http://localhost:5000/academy/$1'
  reverse_proxy /^\/documentation(\/.*)$/, 'http://localhost:5004/documentation/$1'

  reverse_proxy /^\/docs(\/.*)$/, 'http://localhost:5006/docs/$1'
end

set :port, 4000

get '/' do
  send_file File.join(settings.public_folder, 'index.html')
end
