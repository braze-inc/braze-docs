require 'git'

module Jekyll

  module Tags
    class LastModifiedTags < Liquid::Tag
			@@git = nil
      def initialize(tag_name, dateformat, tokens)
				super
        @dateformat = (dateformat == '') ? "%B %-d, %Y" : dateformat
      end

      def render(context)
				site = context.registers[:site]
				article_page = context.environments.first['page']['path']
				docs_path = site.config['collections_dir']
				if @@git.nil?
					source = File.expand_path(site.config['source']).freeze
					@@git = Git.open(source)
				end
				article_file = File.join(docs_path, article_page)
				last_log = @@git.log(1).path(article_file)
				last_commit_date = @@git.gcommit(last_log).date.strftime(@dateformat)
				return "<div id='last_modified_date'>Last modified on: #{last_commit_date}</div>"
      end
    end
  end
end

Liquid::Template.register_tag('last_modified', Jekyll::Tags::LastModifiedTags)
