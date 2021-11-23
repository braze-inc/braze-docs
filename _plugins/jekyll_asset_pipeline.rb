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
    require 'sassc'

    def self.filetype
      '.css'
    end

    def compress
      return SassC::Engine.new(@content, syntax: :css, load_paths: [@dirname], style: :compressed).render
    end
  end

  class JavaScriptCompressor < JekyllAssetPipeline::Compressor
    require 'uglifier'

    def self.filetype
      '.js'
    end

    def compress
      # YUI::JavaScriptCompressor.new(:munge => true).compress(@content)
      Uglifier.new(:harmony => true).compile(@content)
    end
  end
end
