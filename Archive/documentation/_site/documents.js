


$(document).ready(function() {
  $('#toc').toc({
    headers: 'h1, h2, h3',
    minimumHeaders: toc_minheaders
  });
  // Use Bootstrap's "Scrollspy" plugin to dynamically expand/collapse ToC
  if ($('#toc nav').length) {
    $('#toc_col').removeClass('notoc');
    //$('#toc_toggle').removeClass('notoc');

    $('body').scrollspy('refresh');
    $(window).on('activate.bs.scrollspy', function() {

      var hash = $('#toc').find("a.nav-link.active").last().attr("href");
      if (!hash){
        hash = '.'
      }
      // else {
      //   if (typeof (appboy) !== 'undefined') {
      //     appboy.logCustomEvent("Documentations Page Scrolling", {"URL": window.location.pathname,"Anchor": hash});
      //   }
      // }
      window.history.replaceState(null, null, hash);
        var tcol = $('#toc_col'); //.scrollTop('#toc_' + hash, 200);
        // scroll left nav also
        tcol.scrollTop($('#toc_' + hash.substring(1)).offset().top - $('#toc').offset().top - 10);
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
      //$('#nav_bottom').height(nav_bottom_height);
    } else {
      $('#header_nav').removeClass('scrollnav');
      $('#nav_bar' ).removeClass('scrollnav');
      //$('#nav_bottom').height($('#nav_bottom').height() + delta_scroll);

      if ($('#toc nav').length) {
        window.history.replaceState(null, null, '.');
      }
    }
    y_last = y_cord;
  };
  scrollHandler();
  $(window).scroll(scrollHandler);

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


  // Old tabs switcher

  // Note: tried DRYing up into one class and using toggleClass, but it got
  // slow (I think because having two active classes in the same bar was invalid)
  $(".objc-toggle").click(function(e){
      var distanceAboveTarget = $(e.target).offset().top - document.documentElement.scrollTop;
      $(".swift-pane").removeClass("active");
      $(".swift-row").removeClass("active");
      $(".objc-pane").addClass("active");
      $(".objc-row").addClass("active");
      $('body, html').scrollTop($(e.target).offset().top - distanceAboveTarget);
      $('[data-spy="scroll"]').each(function () {
        $('[data-spy="scroll"]').each(function () {
          $(this).scrollspy('refresh')
      })
  })
  });
  $(".swift-toggle").click(function(e){
      var distanceAboveTarget = $(e.target).offset().top - document.documentElement.scrollTop;
      $(".objc-row").removeClass("active");
      $(".objc-pane").removeClass("active");
      $(".swift-pane").addClass("active");
      $(".swift-row").addClass("active");
      $('body, html').scrollTop($(e.target).offset().top - distanceAboveTarget);
      $('[data-spy="scroll"]').each(function () {
          $(this).scrollspy('refresh')
      })
  });

  function string_to_slug (str) {
    str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');

    return str;
  }

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
          //console.log(hit)
          if ('nav_title' in suggestion) {
            title = suggestion.nav_title.replace('%20', ' ').replace('_', ' ');
          }
          else {
            title = suggestion.title.replace('%20', ' ').replace('_', ' ');
          }
          if ('type' in suggestion) {
            type = suggestion.type.replace('%20', ' ').replace('_', ' ');
          }
          if ('category' in suggestion) {
            category =  suggestion.category.replace('%20', ' ').replace('_', ' ');
          }


          if ('platform' in suggestion) {
            platform = suggestion.platform.replace('%20', ' ').replace('_', ' ');
          }
          if ('headings' in suggestion) {
            if (suggestion['headings']) {
              heading = suggestion['headings'][suggestion['headings'].length - 1];
            }
          }
          if (platform || category) {
            subname = '('  + platform;
            if (platform) {
              subname += ' - ';
            }
            subname += category + ')';
          }


          if ('content' in suggestion._highlightResult){
            if ('value' in suggestion._highlightResult.content){
              content = suggestion._highlightResult.content.value.replace('%20', ' ').replace('_', ' ');
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
  ).on('autocomplete:selected', function(event, suggestion, dataset) {
  }).keydown(function(e){
    if (e.which == 27) {
      $(this).autocomplete('val', '');;
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

});
