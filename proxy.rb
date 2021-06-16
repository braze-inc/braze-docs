require 'rack/reverse_proxy'
require 'sinatra'

use Rack::ReverseProxy do
  # Set :preserve_host to true globally (default is true already)
  reverse_proxy_options preserve_host: true

  reverse_proxy /^\/docs(\/.*)$/, 'http://127.0.0.1:5006/docs/$1'
end

set :port, 4000
set :bind, '0.0.0.0'

get '/' do
  send_file File.join(settings.public_folder, 'index.html')
end
