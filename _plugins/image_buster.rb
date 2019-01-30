#
# Jekyll Image_buster
#
require 'yaml'
require 'digest/md5'

module Jekyll
  class ImageBuster
    @@default_config = {
      'dev'            => false
    }
    @@current_config = nil

    def initialize(context)
      @context  = context
      @config = ImageBuster.config(@context)
    end

    def self.config(context)
      if @@current_config.nil?
        gen_config = nil
        if context.registers[:site].config.key?('image_buster')
          gen_config = Utils.deep_merge_hashes(
            @@default_config,
            context.registers[:site].config['image_buster']
          )
        else
          gen_config = @@default_config
        end

        if context.registers[:site].config.key?('dev')
          if context.registers[:site].config['dev']
            gen_config['dev'] = true
          else
            gen_config['dev'] = false
          end
        end

        #if context.registers[:site].config['serving'] ||
        #   context.registers[:site].config['watch']
        #  gen_config['dev'] = true
        #end

        @@current_config = gen_config
      end

      @@current_config
    end

    class Tag < Liquid::Tag
      def initialize(tag_name, markup, tokens)
        super
        @markup = markup.strip!
      end

      def render(context)
        unless ImageBuster.config(context)['dev']
          filename = @markup =~ /^\// ? @markup[1..-1].strip : @markup
          md5 = Digest::MD5.file(filename).hexdigest
          baseurl = context.registers[:site].baseurl
          final_markup = "#{baseurl}#{@markup}?#{md5}"
        end
        final_markup
      end
    end
  end
end

Liquid::Template.register_tag('image_buster', Jekyll::ImageBuster::Tag)
