require 'digest/md5'

module Tags
  class PageTabsBlock < Liquid::Block
    def initialize(tag_name, tabonly = 'false', tokens)
      super
      @tabclass = 'page-tab_toggle'
      @tabid = 'page-tab_' + (0...12).map { (97 + rand(26)).chr }.join
      if tabonly.downcase.strip == 'local'
        @tabclass = 'page-tab_toggle_only'
      end
    end

    def render(context)
      tabs = super.scan(/data\-page\-tab=\"page\-(.*?)\"/)
      # include BOTH page-* and sdk-* classnames so existing CSS works
      tabslist = '<ul class="page-ab-nav sdk-ab-nav page-ab-nav-tabs sdk-ab-nav-tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"
      if tabs.length > 0
        tabs.each_with_index do |tab, ind|
          itemid = (0...12).map { (97 + rand(26)).chr }.join

          tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

          # li gets both pagerow and sdkrow to pick up styles
          tabslist += '    <li id="paget_' + itemid + '" class="pagerow sdkrow ' + tabslug
          tabslist += ' active' if ind == 0
          tabslist += '"><a class="' + @tabclass + '" data-page-tab-target="' + @tabid + '" data-page-tab="' + tabslug + '">' + tab[0] + '</a></li>' + "\n"
        end
      end
      tabslist += '</ul>'  + "\n"
      tabslist + '<div id="' + @tabid + '" class="page-tab-content sdk-tab-content ' + @tabclass + '_div">' + "\n" + super + "\n</div>\n"
    end
  end

  class PageTabBlock < Liquid::Block
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
      content = content.strip
      tabslug = @tab.gsub(/[^0-9a-z]/i, '')
      tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?
      content = content.gsub(/<(h[1-6]) id=\"/, '<\1 id="' + tabslug + '_')

      # include BOTH page-* and sdk-* pane classes so CSS shows tabs
      return '<div id="pagec_' + contentid + '" class="page-ab-tab-pane sdk-ab-tab-pane ' + tabslug + '_tab " data-page-tab="page-' + @tab + '">' + content + "</div>"
    end
  end

  class PageSubTabsBlock < Liquid::Block
    def initialize(tag_name, tabonly = 'false', tokens)
      super
      @tabclass = 'sub_page-tab_toggle'
      @tabid = 'sub_page-tab_' + (0...12).map { (97 + rand(26)).chr }.join
      if tabonly.downcase.strip != 'global'
        @tabclass = 'sub_page-tab_toggle_only'
      end
    end

    def render(context)
      tabs = super.scan(/data\-page\-sub\_tab=\"(.*?)\"/)
      tabslist = '<ul class="page-ab-sub_nav sdk-ab-sub_nav page-ab-sub_nav-sub_tabs sdk-ab-sub_nav-sub_tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"

      if tabs.length > 0
        tabs.each_with_index do |tab, ind|
          itemid = (0...12).map { (97 + rand(26)).chr }.join
          tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

          # keep coderow for existing CSS, add pagerow as alias
          tabslist += '    <li id="pagest_' + itemid + '" class="pagerow coderow ' + tabslug + '_sub_page_tab'
          tabslist += ' sub_active' if ind == 0
          tabslist += '"><a class="' + @tabclass + '" data-page-sub_tab-target="' + @tabid + '" data-page-sub_tab="' + tabslug + '_sub_page_tab">' + tab[0] + '</a></li>' + "\n"
        end
      end
      tabslist += '</ul>'  + "\n"
      tabslist + '<div id="' + @tabid + '" class="page-ab-sub_tab-content sdk-ab-sub_tab-content ' + @tabclass + '_page_div">' + "\n" + super + "\n</div>\n"
    end
  end

  class PageSubTabBlock < Liquid::Block
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
      content = content.strip
      tabslug = @tab.gsub(/[^0-9a-z]/i, '')
      tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?

      return '<div id="pagesc_' + contentid + '" class="page-ab-sub_tab-pane sdk-ab-sub_tab-pane ' + tabslug + '_sub_page_tab " data-page-sub_tab="' + @tab + '">' + content + "</div>"
    end
  end
end

Liquid::Template.register_tag("pagetabs",    Tags::PageTabsBlock)
Liquid::Template.register_tag("pagetab",     Tags::PageTabBlock)
Liquid::Template.register_tag("pagesubtabs", Tags::PageSubTabsBlock)
Liquid::Template.register_tag("pagesubtab",  Tags::PageSubTabBlock)
