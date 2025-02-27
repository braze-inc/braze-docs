require 'digest/md5'

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
          tabs = super.scan(/data\-sdk\-tab=\"sdk\-(.*?)\"/)
          tabslist = '<ul class="sdk-ab-nav sdk-ab-nav-tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"
          if tabs.length > 0
            tabs.each_with_index do |tab, ind|
              itemid = (0...12).map { (97 + rand(26)).chr }.join

              tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
              tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

              # scan returns array of results, only care about first match
              tabslist += '    <li id="sdkt_' + itemid + '" class="sdkrow ' + tabslug
              if ind == 0
                tabslist += ' active'
              end
              tabslist += '"><a class="' + @tabclass + '" data-sdk-tab-target="' + @tabid + '" data-sdk-tab="' + tabslug + '">' + tab[0] + '</a></li>' + "\n"
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
          contentid = (0...12).map { (97 + rand(26)).chr }.join

          content = indentation ? super.gsub(/^#{' |\t' * indentation}/, '') : super
          content = converter.convert(content)
          content = content.strip # Strip again to avoid "\n"
          tabslug = @tab.gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?
          content = content.gsub(/<(h[1-6]) id=\"/, '<\1 id="' + tabslug + '_')

          return '<div id="sdkc_' + contentid + '"  class="sdk-ab-tab-pane ' + tabslug + '_tab " data-sdk-tab="sdk-' + @tab + '">' + content + "</div>"
      end
    end

    class SdkSubTabsBlock < Liquid::Block
      def initialize(tag_name, tabonly = 'false', tokens)
          super
          @tabclass = 'sub_sdk-tab_toggle'
          @tabid = 'sub_sdk-tab_' + (0...12).map { (97 + rand(26)).chr }.join
          if tabonly.downcase.strip != 'global'
            @tabclass = 'sub_sdk-tab_toggle_only'
          end
      end
      def render(context)
          tabs = super.scan(/data\-sdk\-sub\_tab=\"(.*?)\"/)
          tabslist = '<ul class="sdk-ab-sub_nav sdk-ab-sub_nav-sub_tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"

          if tabs.length > 0
            tabs.each_with_index do |tab, ind|

              itemid = (0...12).map { (97 + rand(26)).chr }.join
              tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
              tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

              # scan returns array of results, only care about first match
              tabslist += '    <li id="sdkst_' + itemid + '" class="coderow ' + tabslug + '_sub_sdk_tab'
              if ind == 0
                tabslist += ' sub_active'
              end
              tabslist += '"><a class="' + @tabclass + '" data-sdk-sub_tab-target="' + @tabid + '" data-sdk-sub_tab="' + tabslug + '_sub_sdk_tab">' + tab[0] + '</a></li>' + "\n"
            end
          end
          tabslist += '</ul>'  + "\n"
          tabslist + '<div id="' + @tabid + '" class="sdk-ab-sub_tab-content ' + @tabclass + '_sdk_div">' + "\n" + super + "\n</div>\n"
      end
    end

    class SdkSubTabBlock < Liquid::Block
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
          contentid = (0...12).map { (97 + rand(26)).chr }.join

          content = indentation ? super.gsub(/^#{' |\t' * indentation}/, '') : super
          content = converter.convert(content)
          content = content.strip # Strip again to avoid "\n"
          tabslug = @tab.gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?

          return '<div id="sdksc_' + contentid + '"  class="sdk-ab-sub_tab-pane ' + tabslug + '_sub_sdk_tab " data-sdk-sub_tab="' + @tab + '">' + content + "</div>"
      end
    end
end

Liquid::Template.register_tag("sdktabs", Tags::SdkTabsBlock)
Liquid::Template.register_tag("sdktab",  Tags::SdkTabBlock)
Liquid::Template.register_tag("sdksubtabs", Tags::SdkSubTabsBlock)
Liquid::Template.register_tag("sdksubtab",  Tags::SdkSubTabBlock)
