module Api
  class ApiInfoBlock < Liquid::Block
    def initialize(tag_name, tabonly = 'false', tokens)
        super
        # @tabclass = 'tab_toggle'
        @apiid = 'api_' + (0...12).map { (97 + rand(26)).chr }.join
    end
    def render(context)
      site = context.registers[:site]
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)
      content = converter.convert(super)
      "<div id='#{@apiid}' class='api_div'>#{content}</div>"
    end
  end

  class ApiMethodBlock < Liquid::Block
      def initialize(tag_name, methodtype, tokens)
          super
          @methodtype = methodtype.downcase.strip
      end

      def render(context)
          site = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)
          content = converter.convert(super)
          "<div class='api_type'><div class='method #{@methodtype} '>#{ @methodtype }</div>#{content}</div>"
      end
  end
  class ApiTagsBlock < Liquid::Block
      def initialize(tag_name, param, tokens)
          super
      end

      def render(context)
        content = super.strip
        "<div class='api_tags' data-tags='#{content}' data-tags-lower='#{content.downcase}'></div>"
      end
  end
  class ApiReferenceBlock < Liquid::Block
      def initialize(tag_name, param, tokens)
          super
          @reftype = param.downcase.strip
      end

      def render(context)
        content = super.strip
        reftext = ''
        case @reftype
        when "swagger"
          reftext = 'Test me with Swagger'
        when "postman"
          reftext = 'See me in Postman'
        end
        "<div class='api_reference #{@reftype}'><a href='#{content}' class='seeme'>#{reftext}</a></div>"
      end
  end
end

Liquid::Template.register_tag("api", Api::ApiInfoBlock)
Liquid::Template.register_tag("apimethod",  Api::ApiMethodBlock)
Liquid::Template.register_tag("apitags",  Api::ApiTagsBlock)
Liquid::Template.register_tag("apiref",  Api::ApiReferenceBlock)
