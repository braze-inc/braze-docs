require 'digest/md5'

module Tags
    class TabsBlock < Liquid::Block
      def initialize(tag_name, tabonly = 'false', tokens)
          super
          @tabclass = 'tab_toggle'
          @tabid = 'tab_' + (0...12).map { (97 + rand(26)).chr }.join
          if tabonly.downcase.strip == 'local'
            @tabclass = 'tab_toggle_only'
          end
      end
      def render(context)
          tabs = super.scan(/data\-tab=\"(.*?)\"/)
          tabslist = '<ul class="ab-nav ab-nav-tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"
          if tabs.length > 0
            tabs.each_with_index do |tab, ind|
              tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
              tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

              # scan returns array of results, only care about first match
              tabslist += '    <li tabindex="0" class="coderow ' + tabslug
              if ind == 0
                tabslist += ' active'
              end
              tabslist += '"><a class="' + @tabclass + '" data-tab-target="' + @tabid + '" data-tab="' + tabslug + '">' + tab[0] + '</a></li>' + "\n"
            end
          end
          tabslist += '</ul>'  + "\n"
          tabslist + '<div id="' + @tabid + '" class="ab-tab-content ' + @tabclass + '_div">' + "\n" + super + "\n</div>\n"
      end
    end

    class TabBlock < Liquid::Block
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
          tabslug = @tab.gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?

          '<div class="ab-tab-pane ' + tabslug + '_tab " data-tab="' + @tab + '">' + content + "</div>"
      end
    end

    class SubTabsBlock < Liquid::Block
      def initialize(tag_name, tabonly = 'false', tokens)
          super
          @tabclass = 'sub_tab_toggle'
          @tabid = 'sub_tab_' + (0...12).map { (97 + rand(26)).chr }.join
          if tabonly.downcase.strip != 'global'
            @tabclass = 'sub_tab_toggle_only'
          end
      end
      def render(context)
          tabs = super.scan(/data\-sub\_tab=\"(.*?)\"/)
          tabslist = '<ul class="ab-sub_nav ab-sub_nav-sub_tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"
          if tabs.length > 0
            tabs.each_with_index do |tab, ind|
              tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
              tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

              # scan returns array of results, only care about first match
              tabslist += '    <li tabindex="0" class="coderow ' + tabslug + '_sub_tab'
              if ind == 0
                tabslist += ' sub_active'
              end
              tabslist += '"><a class="' + @tabclass + '" data-sub_tab-target="' + @tabid + '" data-sub_tab="' + tabslug + '_sub_tab">' + tab[0] + '</a></li>' + "\n"
            end
          end
          tabslist += '</ul>'  + "\n"
          tabslist + '<div id="' + @tabid + '" class="ab-sub_tab-content ' + @tabclass + '_div">' + "\n" + super + "\n</div>\n"
      end
    end

    class SubTabBlock < Liquid::Block
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
          tabslug = @tab.gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?

          '<div class="ab-sub_tab-pane ' + tabslug + '_sub_tab " data-sub_tab="' + @tab + '">' + content + "</div>"
      end
    end
end

Liquid::Template.register_tag("tabs", Tags::TabsBlock)
Liquid::Template.register_tag("tab",  Tags::TabBlock)
Liquid::Template.register_tag("subtabs", Tags::SubTabsBlock)
Liquid::Template.register_tag("subtab",  Tags::SubTabBlock)
