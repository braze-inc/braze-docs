module Tags
    class SdkTabsBlock < Liquid::Block
      def initialize(tag_name, tabonly = 'false', tokens)
          super
          @tabclass = 'sdk-tab_toggle'
          @tabid = 'sdk-tab_' + (0...12).map { (97 + rand(26)).chr }.join
          if tabonly.downcase.strip == 'local'
            @tabclass = 'sdk-tab_toggle_only'
          end
      end
      def render(context)
          tabs = super.scan(/data\-tab=\"sdk\-(.*?)\"/)
          tabslist = '<ul class="sdk-ab-nav sdk-ab-nav-tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"
          if tabs.length > 0
            tabs.each_with_index do |tab, ind|
              # scan returns array of results, only care about first match
              tabslist += '    <li class="sdkrow ' + tab[0].gsub(' ', '-').gsub(/[^\w-]/, '')
              if ind == 0
                tabslist += ' active'
              end
              tabslist += '"><a class="' + @tabclass + '" data-tab-target="' + @tabid + '" data-tab="' + tab[0].gsub(' ', '-').gsub(/[^\w-]/, '') + '">' + tab[0] + '</a></li>' + "\n"
            end
          end
          tabslist += '</ul>'  + "\n"
          tabslist + '<div id="' + @tabid + '" class="sdk-tab-content ' + @tabclass + '_div">' + "\n" + super + "\n</div>\n"
      end
    end

    class SdkTabBlock < Liquid::Block
      def initialize(tag_name, tab, tokens)
          super
          @tab = tab.strip.downcase
      end

      def render(context)
          return "" if @tab.empty?

          site      = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)

          lines = super.rstrip.split(/\r\n|\r|\n/).select { |line| line.size > 0 }
          indentation = lines.map do |line|
              match = line.match(/^(\s+)[^\s]+/)
          match ? match[1].size : 0
          end
          indentation = indentation.min

          content = indentation ? super.gsub(/^#{' |\t' * indentation}/, '') : super
          content = converter.convert(content)
          content = content.strip # Strip again to avoid "\n"
          tabslug = @tab.gsub(' ', '-').gsub(/[^\w-]/, '')

          return '<div class="sdk-ab-tab-pane ' + tabslug + '_tab " data-tab="sdk-' + @tab + '">' + content + "</div>"
      end
    end

end

Liquid::Template.register_tag("sdktabs", Tags::SdkTabsBlock)
Liquid::Template.register_tag("sdktab",  Tags::SdkTabBlock)
