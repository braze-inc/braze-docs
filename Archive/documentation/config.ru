require 'rack/jekyll'
require 'yaml'
require './_build/cachesettings'
require 'rack/deflater'

use CacheSettings, {
      /.*\.png/ => {:cache_control => "max-age=31536000, public"},
      /.*\.gif/ => {:cache_control => "max-age=31536000, public"},
      /.*\.css/ => {:cache_control => "max-age=31536000, public"},
      /.*\.js/ => {:cache_control => "max-age=31536000, public"}
    }
use Rack::Deflater

FileUtils.touch('/tmp/app-initialized')
run Rack::Jekyll.new
