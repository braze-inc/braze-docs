module Jekyll
  module Alerts
    class AlertTag < Liquid::Block

      def initialize(tag_name, markup, tokens)
        super
        @caption = markup
      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
        # below Jekyll 3.x use this:
        # converter = site.getConverterImpl(::Jekyll::Converters::Markdown)
        type = converter.convert(@caption).gsub(/<\/?p[^>]*>/, '').chomp
        body = converter.convert(super(context))
        "<div class='alert alert-#{type}' role='alert'><div class='alert-msg'> <b>#{type.gsub('-', ' ')}: </b><br />#{body}</div></div>"
      end

    end
  end
end

Liquid::Template.register_tag('alert', Jekyll::Alerts::AlertTag)
