module Tags
  class GalleryBlock < Liquid::Block
    def initialize(tag_name, param, tokens)
        super
    end
    def render(context)

      site = context.registers[:site]
      converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

      images = [".gif", ".jpg", ".jpeg", ".png", ".svg"]
      content = super.split("\n")

      galleryid = 'gallery_' + (0...12).map { (97 + rand(26)).chr }.join
      galleryitems = []
      content.each do | item |
        unless (item.empty?)
          items = item.split(' ')
          mainimage = items.shift
          isimage = images.any? { |imgtype| mainimage.downcase.include?(imgtype) }

          if (isimage)
            htmlcontent = "<img class='swiper-image swiper-popover' src='#{mainimage}'/>\n"
            # check if there's popover info
            if (items.length)
              htmlcontent += "<div class='swiper-description'>#{ converter.convert(items.join(' ')) }</div>"
            end
            galleryitems.push("<div class='swiper-slide'>#{ htmlcontent }</div>")
          end
        end
      end
      basesetting = "{slidesPerView: 1,spaceBetween: 30,loop: false, pagination: { el: '.swiper-pagination', clickable: true }, navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev'}}"

      "<div class='swiper-container' id='#{ galleryid }'><div class='swiper-wrapper'>\n#{galleryitems.join("\n")}\n</div><div class='swiper-pagination'></div><div class='swiper-button-next'></div><div class='swiper-button-prev'></div></div>\n" +
      "<script type='text/javascript'>var swiper = new Swiper('##{galleryid}', #{basesetting});</script>"
    end
  end
end

Liquid::Template.register_tag("gallery", Tags::GalleryBlock)
