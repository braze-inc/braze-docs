# _plugins/details_tag.rb
# source http://movb.de/jekyll-details-support.html

module Jekyll
  module Tags
    class DetailsTag < Liquid::Block

      def initialize(tag_name, markup, tokens)
        super
        @caption = markup
      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
        # below Jekyll 3.x use this:
        # converter = site.getConverterImpl(::Jekyll::Converters::Markdown)
        caption = converter.convert(@caption).gsub(/<\/?p[^>]*>/, '').chomp
        body = converter.convert(super(context))
        "<div id='#{caption.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '') }' class='details_title'></div><details ><summary>#{caption}</summary><div class='detail_div'>#{body}</div></details>"
      end

    end
  end
end

Liquid::Template.register_tag('details', Jekyll::Tags::DetailsTag)
