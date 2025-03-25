// https://github.com/ghiculescu/jekyll-table-of-contents
// Modified to generate nav tags for bootstrap 4.1 scrollspy
(function($){
  $.fn.toc = function(options) {
    var defaults = {
      noBackToTopLinks: true,
      minimumHeaders: 3,
      headers: 'h1, h2, h3, h4, h5, h6',
      listType: 'nav', // values: [ol|ul]
      listPrefix: 'toc_',
      showEffect: 'fadeIn', // values: [show|slideDown|fadeIn|none]
      showSpeed: 'fast', // set to 0 to deactivate effect
      toc_header: `${ site_i18n['page_nav_title'] || "On this page"}...`,
      toc_header_class: 'toc_header',
      toc_container_class: 'toc_container',
      toc_item_class: 'nav_item',
      toc_link_class: 'nav-link',
      bootstrapStyling: ' class="nav"' // appended to each list element
    },
    settings = $.extend(defaults, options);

    var headers = $(settings.headers).filter(function() {
      // get all headers with an ID
      var previousSiblingName = $(this).prev().attr( "name" );
      if (!this.id && previousSiblingName) {
        this.id = $(this).attr( "id", previousSiblingName.replace(/\./g, "-") );
      }
      if ($(this).html().length == 0 || !$(this).is(":visible")) {
        return false;
      }
      return this.id;
    }), output = $(this);
    if (!headers.length || headers.length < settings.minimumHeaders || !output.length) {
      return;
    }

    if (0 === settings.showSpeed) {
      settings.showEffect = 'none';
    }

    var render = {
      show: function() { output.hide().html(html).show(settings.showSpeed); },
      slideDown: function() { output.hide().html(html).slideDown(settings.showSpeed); },
      fadeIn: function() { output.hide().html(html).fadeIn(settings.showSpeed); },
      none: function() { output.html(html); }
    };

    var get_level = function(ele) {
      var lvl = 1
      if (ele.nodeName.substring(0,1) == 'H')  {
        lvl = parseInt(ele.nodeName.replace("H", ""), 10);
      }
      return lvl;
    }
    var highest_level = headers.map(function(_, ele) { return get_level(ele); }).get().sort()[0];
    var return_to_top = '<i class="icon-arrow-up back-to-top"> </i>';

    var level = get_level(headers[0]),
      this_level,
      html = " <"+ settings.listType + settings.bootstrapStyling +" aria-label='Table of Content' title='Table of Content'><div class='" + settings.toc_header_class + "'>" + settings.toc_header + "</div><div class='" + settings.toc_container_class + "'>";
    headers.on('click', function() {
      if (!settings.noBackToTopLinks) {
        window.location.hash = this.id;
      }
    })
    .addClass('clickable-header')
    .each(function(_, header) {
      this_level = get_level(header);
      if (!settings.noBackToTopLinks && this_level === highest_level) {
        $(header).addClass('top-level-header').after(return_to_top);
      }
      // extra div tags at html += before <a> to prevent highlighting of parent
      if (this_level === level) // same level as before; same indenting
        html += "<div><a class='" + settings.toc_link_class + "' href='#" + header.id + "'  id='" + settings.listPrefix + header.id + "' >" + header.innerHTML + "</a></div> ";
      else if (this_level <= level){ // higher level than before; end parent ol
        for(i = this_level; i < level; i++) {
          html += "</"+settings.listType+">"
        }
        html += "<div><a class='" + settings.toc_link_class + "' href='#" + header.id + "'  id='" + settings.listPrefix + header.id + "' >" + header.innerHTML + "</a></div> ";
      }
      else if (this_level > level) { // lower level than before; expand the previous to contain a ol
        for(i = this_level; i > level; i--) {
          html += "<"+ settings.listType + settings.bootstrapStyling +" aria-label='ToC " + header.innerHTML + "'>"
        }
        html += "<div><a class='" + settings.toc_link_class + "' href='#" + header.id + "'  id='" + settings.listPrefix + header.id + "' >" + header.innerHTML + "</a></div> ";
      }
      level = this_level; // update for the next one
    });
    html += "</div></"+settings.listType+">";
    if (!settings.noBackToTopLinks) {
      $(document).on('click', '.back-to-top', function() {
        $(window).scrollTop(0);
        window.location.hash = '';
      });
    }

    render[settings.showEffect]();
  };
})(jQuery);
