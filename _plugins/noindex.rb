# plugin to check the if the site is production using the heroku ENV variable.
# If not production website, then add a robot noindex meta header.
# also don't index if the page is in the hidden folder.
# Usage:  {% noindex {{ page.path }} %}

module Jekyll
  class NoIndex < Liquid::Tag

    def initialize(tag_name, hiddenpage, tokens)
      super
      @hidden = hiddenpage.strip
    end

    def render(context)
      hiddenpage = Liquid::Template.parse(@hidden).render(context)
      currentpage = context.registers[:page]
      hidepage = currentpage['hidden'].nil? ? false : currentpage['hidden']
      noindex = currentpage['noindex'].nil? ? false : currentpage['noindex']

      if  (ENV['SITE_URL'].to_s.downcase != 'https://www.braze.com') || (hiddenpage.start_with? '_hidden') || (hidepage) || (noindex)
        "<meta name=\"robots\" content=\"noindex, nofollow\" >"
      else
        "<meta name=\"google-site-verification\" content=\"kI0o3QRqDw5zhtd9W5umZTzLTDe6X1tp-gybtFg_7bQ\" />"
      end
    end

  end

end

Liquid::Template.register_tag('noindex', Jekyll::NoIndex)
