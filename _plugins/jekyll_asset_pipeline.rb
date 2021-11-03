require 'jekyll_asset_pipeline'

module JekyllAssetPipeline
  class SassConverter < JekyllAssetPipeline::Converter
    require 'sassc'

    def self.filetype
      '.scss'
    end

    def convert
      return SassC::Engine.new(@content, syntax: :scss, load_paths: [@dirname]).render
    end
  end

  class CssCompressor < JekyllAssetPipeline::Compressor
    require 'yui/compressor'

    def self.filetype
      '.css'
    end

    def compress
      YUI::CssCompressor.new().compress(@content)
    end
  end

  class JavaScriptCompressor < JekyllAssetPipeline::Compressor
    require 'yui/compressor'

    def self.filetype
      '.js'
    end

    def compress
      YUI::JavaScriptCompressor.new(:munge => true).compress(@content)
    end
  end
end
