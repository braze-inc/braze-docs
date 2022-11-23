module Jekyll

  module Tags
    class LastModifiedTags < Liquid::Tag

      def initialize(tag_name, dateformat, tokens)
				super
        @dateformat = (dateformat == '') ? "%Y-%^b-%d" : dateformat
      end

      def render(context)
				site = context.registers[:site]
				article_page = context.environments.first['page']['path']
				docs_path = site.config['collections_dir']
				source = File.expand_path(site.config['source']).freeze
				article_file = File.join(source, docs_path, article_page)
				return "<div id='last_modified_date'>Last Modified: #{File.mtime(article_file).strftime(@dateformat)}</div>"
      end
    end
  end
end

Liquid::Template.register_tag('last_modified', Jekyll::Tags::LastModifiedTags)
