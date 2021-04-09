

var query_str = window.location.search;
$(document).ready(function() {

  function string_to_slug(str) {
    if (str) {
      str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');
    }
    return str;
  }



  $('#toc').toc({
    headers: 'h2, h3',
    minimumHeaders: toc_minheaders
  });
  // Use Bootstrap's "Scrollspy" plugin to dynamically expand/collapse ToC
  if ($('#toc nav').length) {
    $('#toc_col').removeClass('notoc');
    //$('#toc_toggle').removeClass('notoc');

    $('body').scrollspy('refresh');
    $(window).on('activate.bs.scrollspy', function() {
      var active_toc = $('#toc').find("a.nav-link.active").last().attr("href");
      var hash = active_toc;
      if (!hash){
        hash = '.';
        active_toc = '.';
        if (window.location.pathname.substr(-1) != '/') {
          hash = window.location.pathname + '/' ;
        }
      }
      else {
        if (window.location.pathname.substr(-1) != '/')  {
          hash = window.location.pathname + '/' + hash;
        }
      }
      // else {
      //   if (typeof (appboy) !== 'undefined') {
      //     appboy.logCustomEvent("Documentations Page Scrolling", {"URL": window.location.pathname,"Anchor": hash});
      //   }
      // }
      window.history.replaceState(null, null, hash);
        var tcol = $('#toc_col'); //.scrollTop('#toc_' + hash, 200);
        // scroll left nav also
        tcol.scrollTop($('#toc_' + active_toc.substring(1)).offset().top - $('#toc').offset().top - 10);
    });



    // Add smooth scrolling on all links inside the navbar
    $("#toc a").on('click', function(event) {

      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
        // Store hash
        var hash = this.hash;
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function() {
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });

      } // End if

    });

  }
  else {
    //$('#toc_col').addClass('notoc');

  }
  var y_last = 0;
  //var nav_bottom_height = $('#nav_bottom').height();
  var scrollHandler = function() {
    var y_cord = $(this).scrollTop();
    var bzheader_height = $('#braze_header').height();
    // var scroll_dir = 'down';
    // if (y_last > y_cord) {
    //   scroll_dir = 'up'
    // }

    // Scrolled pass banner, adjust status monitor status
    if (y_cord > (bzheader_height * 1/3)) {
      $('#header_nav').addClass('scrollnav');
      $('#nav_bar' ).addClass('scrollnav');
      $('#contentcards' ).addClass('scrollnav');
      $('#main_content' ).addClass('scrollnav');
      $('#toc_col' ).addClass('scrollnav');
      if (y_cord > (bzheader_height * 5/6)) {
        $('#toc_col' ).addClass('scrollbottom');
      }
      else {
        $('#toc_col' ).removeClass('scrollbottom');
      }
      //$('#nav_bottom').height(nav_bottom_height);
    } else {
      $('#header_nav').removeClass('scrollnav');
      $('#nav_bar' ).removeClass('scrollnav');
      $('#contentcards' ).removeClass('scrollnav');
      $('#main_content' ).removeClass('scrollnav');
      $('#toc_col' ).removeClass('scrollnav');
      $('#toc_col' ).removeClass('scrollbottom');

      //$('#nav_bottom').height($('#nav_bottom').height() + delta_scroll);

      if ($('#toc nav').length) {
        if (window.location.pathname.substr(-1) != '/')  {
          window.history.replaceState(null, null, window.location.pathname + '/' + query_str);
        }
        else {
          window.history.replaceState(null, null, '.' + query_str);
        }
      }
    }
    y_last = y_cord;
  };
  scrollHandler();
  $(window).scroll(scrollHandler);

  // see if a details tag should be auto-opened
  var details_list = $('details');
  var url_hash = window.location.hash.replace('#','')
  details_list.each(function(k,v) {
    var $this = $(this);
    if (url_hash == string_to_slug($this.find('summary')[0].innerText)) {
      $this.attr('open',true);
    }
  });


  // Footer navigation
  var parent_top = 'nav_top';

  var nav_active = $('#' + parent_top + ' div.nav-item.active');
  var nav_bottom = $('#bottom_page_nav');



  var pg_prev_div = $("#page_prev");
  var pg_next_div = $("#page_next");
  var pg_prev_link = $("#page_prev_link");
  var pg_next_link = $("#page_next_link");

  var data_parent = nav_active.parent();
  var cnt = 0;
  var max_parent = 99;
  while ((data_parent.parent().attr('id') != parent_top) && (data_parent.attr('id') != parent_top) && (cnt < max_parent)){
      data_parent = data_parent.parent();
      cnt++;
  }
  var nav_links = data_parent.find('div.nav-item.active, .nav_link');
  var nav_index = nav_links.index(nav_active) ;
  if (nav_index > 0) {
    var pg_prev = nav_links.eq(nav_index - 1);//nav_active.prevAll('[data-parent="' + data_parent + '"]').first();
    nav_bottom.addClass('flex');
    pg_prev_link.attr('href',pg_prev.attr('href') );
    pg_prev_div.html('<div class="nav_indicator"><i class="fas fa-long-arrow-alt-left"></i> PREVIOUS</div>' + pg_prev.html() );
    pg_prev_div.css('display', 'inline-block');
    if (nav_index < (nav_links.length -1)) {
      pg_prev_div.css('border-right', '0px');
    }
  }
  else {
    pg_prev_div.hide();
  }

  if (nav_index < (nav_links.length -1)) {
    var pg_next = nav_links.eq(nav_index + 1);//nav_active.nextAll('[data-parent="' + data_parent + '"]').first();
    nav_bottom.addClass('flex');
    pg_next_link.attr('href',pg_next.attr('href') );
    pg_next_div.html('<div class="nav_indicator">NEXT <i class="fas fa-long-arrow-alt-right"></i></div>' + pg_next.html() );
    pg_next_div.css('display', 'inline-block');
  }
  else {
    pg_next_div.hide();
  }
  // link image fix for underline
  $('#article-main a:has(> img)').css('display','inline-block');

  $('#sidebar_toggle').click(function(e){
    var nav_bar = $('#nav_bar');
    var nav_icon = $('#sidebar_toggle i');
    var curstate = nav_bar.hasClass('hide_sidebar');
    if (curstate) {
      nav_bar.removeClass('hide_sidebar');
      nav_icon.removeClass('fa-bars');
      nav_icon.addClass('fa-chevron-left');
      Cookies.remove('ln');
    } else {
      nav_bar.addClass('hide_sidebar');
      nav_icon.removeClass('fa-chevron-left');
      nav_icon.addClass('fa-bars');
      Cookies.set('ln','1');
    }
  });
  if (Cookies.get('ln')) {
    $('#sidebar_toggle').trigger('click');
  }
  // Updated Tab switcher
  $('.tab_toggle').click(function(e){
    e.preventDefault();
    var $this = $(this);
    var curtab = $this.attr('data-tab');

    $('.tab_toggle_ul.ab-nav-tabs li').removeClass('active');
    $('.tab_toggle_ul.ab-nav-tabs li.' + curtab).addClass('active');
    $('div.tab_toggle_div div.ab-tab-pane').removeClass('active');
    $('div.tab_toggle_div div.' + curtab + '_tab').addClass('active');

  });
  $('.tab_toggle_only').click(function(e){
    e.preventDefault();

    var $this = $(this);
    var curtab = $this.attr('data-tab');
    var partab = $this.attr('data-tab-target');

    $('#' + partab + '_nav li').removeClass('active');
    $('#' + partab + '_nav li.' + curtab).addClass('active');
    $('#' + partab + ' div.ab-tab-pane').removeClass('active');

    $('#' + partab + ' div.' + curtab + '_tab').addClass('active');

  });
  $('.ab-tab-content .ab-tab-pane:first-child').addClass('active')


  String.prototype.upCaseWord = function() {
    return this.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() });
  };
  String.prototype.replaceUnder = function() {
    return this.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ');
  };
  Array.prototype.replaceUnder = function() {
    return this.map(function(itm){ return itm.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ')});
  };
  Array.prototype.upCaseWord = function() {
    return this.map(function(itm){ return itm.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() }) });
  };
  $('#search-form input').autocomplete({ hint: false ,debug: algolia_debug}, [{
      source: $.fn.autocomplete.sources.hits(index, { hitsPerPage: 5 }),
      displayKey:  'nav_title',
      templates: {
        suggestion: function(suggestion) {
          var content = '';
          var title = '';
          var type = '';
          var category = '';
          var platform = '';
          var subname = '';
          var heading = '';

          if ('nav_title' in suggestion) {
            title = suggestion.nav_title.replaceUnder();
          }
          else {
            title = suggestion.title.replaceUnder();
          }
          if ('type' in suggestion) {
            type = suggestion.type.replaceUnder().upCaseWord();
          }
          if ('category' in suggestion) {
            category =  suggestion.category.replaceUnder();
          }

          if ('platform' in suggestion) {
            platform = suggestion.platform.replaceUnder();
          }
          if ('headings' in suggestion) {
            if (suggestion['headings']) {
              heading = suggestion['headings'][suggestion['headings'].length - 1];
            }
          }
          if (platform || category) {
            subname = '(' + type + ': '+ platform;
            if (platform) {
              subname += ' - ';
            }
            subname += category.upCaseWord() + ')';
          }
          if ('content' in suggestion._highlightResult){
            if ('value' in suggestion._highlightResult.content){
              content = suggestion._highlightResult.content.value.replaceUnder().replace(/<(.|\n)*?>/g, '');
            }
          }

          if (content.length > 400) {
            content = content.substring(0,400);
            content += '...';
          }
          var url = suggestion.url;
          if (heading){
            url += '#' + string_to_slug(heading);
          }
          var resulttemplate = '<a href="' + base_url + url + '"><div class="title">' +
            title + ' <div class="category">' + subname.replace(/\_/g,' ') + '</div></div> <div class="content">'  +
            content + '</div><hr /></a>';
          return resulttemplate;
          //
          //return  suggestion._highlightResult.title.value;
        },
        empty: '<div class="no_results">No results were found with your current search. Try to change the search query.</div><hr />',
        footer: '<div id="algolia_footer">' +
        '<div id="algolia-docsearch-advanced"><a href="#" onclick="$(\'#search-form\').submit();">Advanced Search</a></div></div>'
      }

    }]
  ).on('autocomplete:cursorchanged', function() {
  }).on('autocomplete:cursorremoved', function() {
  }).on('autocomplete:selected', function(event, suggestion, dataset) {
    var heading = '';

    if ('headings' in suggestion) {
      if (suggestion['headings']) {
        heading = suggestion['headings'][suggestion['headings'].length - 1];
      }
    }
    var url = suggestion.url;

    if (heading){
      url += '#' + string_to_slug(heading);
    }

    window.location = base_url + url;

  }).keydown(function(e){
    switch (e.which ) {
      // esc, clear results
      case 27:
        $(this).autocomplete('val', '');
        break;
    }
  });

  $('#search_clear').on('click',function(e){
    $('#search-form input').autocomplete('val', '');;
  });

  $('#menu_search').on('focusin',function(e){
    if (  $('#menu_search').val().length ) {
      $('#search-form input').autocomplete('open');
    }
  });

  $('#doc_search_clear').on('click',function(e){
    $('#search-form input').autocomplete('val', '');;
  });

  $('#doc_menu_search').on('focusin',function(e){
    if (  $('#doc_menu_search').val().length ) {
      $('#search-form input').autocomplete('open');
    }
  });

  var sf_style = $('#search-form').attr('style') ?  $('#search-form').attr('style') : '';
  var sfac_style = $('#search-form  .algolia-autocomplete').attr('style') ? $('#search-form  .algolia-autocomplete').attr('style') : '';
  var header_style = $('#header_menu').attr('style') ? $('#header_menu').attr('style') : '';


  $('#menu_search').on('focus',function(e){
  //  if($(window).width() >= 768) {
      $('#header_nav').addClass('search_focus');
      $('#search_clear i').addClass('fa-times');
  //  }
  }).on('blur',function(e){
  //  if($(window).width() >= 768) {
      $('#header_nav').removeClass('search_focus');
      $('#search_clear i').removeClass('fa-times');
  //  }
  });

  $('#doc_menu_search').on('focus',function(e){
        $('#doc_search_clear i').addClass('fa-times');
    }).on('blur',function(e){
        $('#doc_search_clear i').removeClass('fa-times');
    });

  var external_ignore = ['braze.statuspage.io','www.braze.com']
  var links = $('#main_content a').filter(function() {
     var tofilter = this.hostname && this.hostname !== location.hostname && this.text && external_ignore.indexOf(this.hostname) < 0 ;
     if ($(this).hasClass('extignore')) {
       tofilter = false;
     }
     else if ($(this).has('img').length > 0) {
       if ($(this).has('img')[0].childNodes.length > 0) {
         tofilter = false;
       }
     }
     else if ($(this).has('div').length >0 ) {
        tofilter = false;
     }
     return tofilter
  }).after(' <i class="fas fa-external-link-alt"></i>')
  $('.highlight .highlight .rouge-code pre').each(function(k) {
    $this = $(this);
    if ($this.html().length > 120) {
      $this.css('min-height','36px');
    }
    var lines = $this.text().split("\n");
    if (lines.length <= 2) {
      $this.addClass('prewrap');
    }
  });
});
