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
            html = html.text.gsub(/\s+/,' ')[0 ... 4400]
            record[:html] = html
          end
          if record[:content]
            record[:content].gsub!(/^\d+\n/,'')
            record[:content] = record[:content][0 ... 4400]
          end
          # @@logs << record.to_s + "\n"
          record
        else
          # @@logs << record.to_s + "\n"
          nil
        end
      end
    end
  end
end
