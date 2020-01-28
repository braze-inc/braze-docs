# https://github.com/dimitri-koenig/jekyll-plugins
# modified to allow variable url
require 'net/http'
require 'uri'

module Jekyll

  class EmbedMarkdown < Liquid::Tag

    def initialize(tag_name, markup, tokens)
      @url = markup.strip
      super
    end

    def render(context)
      site = context.registers[:site]
      embedmarkdown = site.config['markdown_api']
      if @url.empty?
        embedmarkdown = false
      end
      if ENV["SITE_URL"].to_s.downcase != 'https://www.braze.com' || ENV["RACK_ENV"].to_s.downcase != 'production'
        embedmarkdown = false
      end
      if embedmarkdown
        url = @url.strip

        if url.downcase.end_with?('.md')
          if context['site']['data'].include?(url)
            puts 'Using cache for markdown: ' + url
            return context['site']['data'][url]
          else
            puts 'Fetching content of markdown url: ' + url
            if url =~ URI::regexp
              @results = fetchContent(url)
            else
              puts 'Error fetching markdown: ' + url
            end

            if @results.code != '200'
              puts 'Error returning results: ' + url
              return ''
            else
              if @results.body
                converter = site.find_converter_instance(Jekyll::Converters::Markdown)
                rendered_markdown = converter.convert(@results.body.force_encoding('UTF-8'))
                context['site']['data'][url] = rendered_markdown
                return context['site']['data'][url]
              else
                puts 'Empty content from : ' + url
                return ''
              end
            end
          end
        else
          return ''
        end
      else
        return ''
      end
    end

    def fetchContent(url)
      Net::HTTP.get_response(URI.parse(URI.encode(url.strip)))
    end
  end
end

Liquid::Template.register_tag('markdown_embed', Jekyll::EmbedMarkdown)
