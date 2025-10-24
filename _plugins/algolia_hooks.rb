module Jekyll
  module Algolia

    module Hooks
       # @@logs = File.open('../log.txt', 'w')

      def self.before_indexing_each(record, node, context)
        # Do not index deprecation warnings
        #return nil if node.matches?('.deprecation-notice')

        # Add my name as an author to each record
        #record[:author] = 'Myself'
        path_map = ['type','category']
        url = record[:url]
        path_parts = url.split('/')
        path_parts.shift
        path_cnt = 0
        path_pref = '00'
        unless (record[:config_only]  || record[:hidden] || record[:noindex] )
          while path_part = path_parts.shift
            if path_cnt < path_map.length
              path_str = "#{path_map[path_cnt]}"
            else
              path_str = "Path_#{path_pref.next!}"
            end
            record[path_str.to_sym] = path_part
            path_cnt += 1
          end
          # Clean up lineno from code, and limit html and content to 4400 characters
          # for algolia 10k limit
          if record[:html]
            html = Nokogiri::HTML.parse(record[:html])
            html.search('.lineno').remove
            html = html.text.force_encoding('UTF-8').encode('UTF-8', invalid: :replace, undef: :replace, replace: '').gsub(/\s+/,' ').gsub(/[\u0080-\u00ff]/,'')[0 ... 4400]
            record[:html] = html
          end
          if record[:content]
            record[:content] = record[:content].force_encoding('UTF-8').encode('UTF-8', invalid: :replace, undef: :replace, replace: '').gsub(/^\d+\n/,'').gsub(/[\u0080-\u00ff]/,'')[0 ... 4400]
          end
          # fix glossary generating algolia record that's too big
          record.delete(:glossaries)
          record.delete(:comment)
          # remove llm keys added from _plugins/llms_txt_generator.rb
          record.delete(:llm_markdown_content)
          record.delete(:__export_merged_md)

          return record
        else
          return nil
        end
      end
    end
  end
end
