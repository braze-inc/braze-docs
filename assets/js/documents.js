var page_language = site_language;

function generateUUID() { // Public Domain/MIT
    var d = new Date().getTime();//Timestamp
    var d2 = (performance && performance.now && (performance.now()*1000)) || 0;//Time in microseconds since page-load or 0 if unsupported
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16;//random number between 0 and 16
        if(d > 0){//Use timestamp until depleted
            r = (d + r)%16 | 0;
            d = Math.floor(d/16);
        } else {//Use microseconds since page-load if supported
            r = (d2 + r)%16 | 0;
            d2 = Math.floor(d2/16);
        }
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
}
function string_to_slug(str) {
  if (str) {
    str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');
  }
  return str;
}
let algolia_user = Cookies.get('__algolia_user');
if (!algolia_user){
  algolia_user = generateUUID();
}

var search_color_mapping = {
  'endpoint': '#33C699',
  'channel': '#FF9349',
  'partner': '#3ACCDD',
  'tool': '#F7918E',
  'platform': '#27368F',
  'search_tag': '#0759AA',
};

var custom_word_mapping = {
  'REST': 'REST',
  'API': 'API',
  'APIs': 'APIs',
  'iOS': 'iOS',
  'ID': 'ID',
  'IDs': 'IDs',
  'FAQ': 'FAQ',
  'FAQS': 'FAQs',
  'In-App': 'In-App',
  'GPDR': 'GPDR',
  'mParticle': 'mParticle',
  'SDK': 'SDK',
  'SDKs': 'SDKs',
  'IP': 'IP',
  'IPs': 'IPs',
  'SSL': 'SSL',
  'SAML': 'SAML',
  'SSO': 'SSO',
  'TTL': 'TTL',
  'A/B': 'A/B',
  'HTML': 'HTML',
  'GIF': 'GIF',
  'GIFs': 'GIFs',
  'OTT': 'OTT',
  'TV': 'TV',
  'KPIs': 'KPIs',
  'S3': 'S3',
  'FireOS': 'FireOS',
  'tvOS': 'tvOS',
  'macOS': 'macOS',
  'CocoaPods': 'CocoaPods',
  'AndroidX': 'AndroidX',
  'JavaScript': 'JavaScript',
  'a': 'a',
  'the': 'the',
  'by': 'by',
  'with': 'with',
  'to': 'to',
  'from': 'from',
  'an': 'an',
  'SMS': 'SMS',
  'MMS': 'MMS',
  'Platform Wide': 'Platform Wide Features & Behaviors',
  'lab': 'LAB',
};

// Set cookie to auto expire after 30 days of inactivity
Cookies.set('__algolia_user', algolia_user, { expires: 30 });

String.prototype.upCaseWord = function() {
  return this.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() });
};
String.prototype.replaceUnder = function() {
  return this.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ');
};
Array.prototype.upCaseWord = function() {
  return this.map(function(itm){ return itm.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() }) });
};
Array.prototype.replaceUnder = function() {
  return this.map(function(itm){ return itm.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ')});
};
String.prototype.mapReplace = function(word_map) {
  var mstr = this;
  for (var wd in word_map) {
    if (word_map.hasOwnProperty(wd)) {
        var rep = new RegExp('\\b' + wd + '\\b','gi');
        mstr = mstr.replace(rep,word_map[wd]);
    }
  }
  return mstr;
};

String.prototype.sanitize = function() {
  return this.replace(/\+/g, ' ').replace(/\%20/g, ' ').replace(/\_/g, ' ').replace(/</g,'').replace(/>/g,'').replace(/&lt;/g,'').replace(/&gt;/g,'').replace(/\'/g,'').replace(/\"/g,'');
};

function replaceParams(qs = '', pr = {}) {
	var queryString = qs.replace(/^\?/,'').split('&');
	var params = {};
	queryString.forEach((e) => {
		let param = e.split('=');
		if (param.length >1){
      // Ignore the parameter if it's blank
      if (pr[param[0]] !== '') {
        params[param[0]] = (pr[param[0]] || param[1]);
      }
		}
	});

  var queryStringParam = [];
  for (const k in params) {
    if (params.hasOwnProperty(k)) {
      queryStringParam.push(`${k}=${params[k]}`);
    }
  }
	return `?${queryStringParam.join('&')}`;
};

$(document).ready(function() {
  $("#braze_header").click((e) => {
    setTimeout(function() {
      let hide_backdrop = false;
      $("#braze_header .nav-link.dropdown-toggle").each((eb, ea) => {
        let itm = $(ea);
        if(itm.attr('aria-expanded') == 'true') {
          hide_backdrop = true;
        }
      });
      if (!hide_backdrop) {
        $("#backdrop").removeClass("backdrop-show");
      }
    }, 100);
  });
  $("#braze_header .nav-link.dropdown-toggle").click((e) => {
    $("#braze_header .nav-link.dropdown-toggle").each((e, ea) => {
      ea.children[0].classList.remove("border-focus-show");
    });
    const isOpen = e.currentTarget.ariaExpanded !== "true";
    const borderDiv = e.currentTarget.children[0];
    borderDiv.classList.toggle("border-focus-show", isOpen);
    $("#backdrop").toggleClass("backdrop-show", isOpen);
  });
  $("#backdrop").click((e) => {
    $("#braze_header .nav-link.dropdown-toggle").each((e, ea) => {
      ea.children[0].classList.remove("border-focus-show");
    });
    e.currentTarget.classList.remove("backdrop-show");
  });

  $('#toc').toc({
    headers:  ((typeof toc_headers != 'undefined') ? toc_headers : "h2,h3"),
    minimumHeaders: ((typeof toc_minheaders != 'undefined') ? toc_minheaders : 2),
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
    var query_str = window.location.search;
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

  // set list role attribute for screenreader
  var list_tabs = $('ul');
  list_tabs.each(function(k,v){
    var $this = $(this);
    $this.attr('role','tablist');
  });
  var list_tab = $('ul > li');
  list_tab.each(function(k,v){
    var $this = $(this);
    $this.attr('role','tab');
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
    pg_prev_div.html(`<div class="nav_indicator"><i class="fas fa-long-arrow-alt-left"></i> ${site_i18n['previous'] || 'PREVIOUS'}</div> ${pg_prev.html()}`);
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
    pg_next_div.html(`<div class="nav_indicator">${site_i18n['next'] || 'NEXT'} <i class="fas fa-long-arrow-alt-right"></i></div> ${pg_next.html()}`);
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
      Cookies.set('ln', '', { expires: 365 });
    } else {
      nav_bar.addClass('hide_sidebar');
      nav_icon.removeClass('fa-chevron-left');
      nav_icon.addClass('fa-bars');
      Cookies.set('ln','1',  { expires: 365 });
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
  $('.ab-tab-content .ab-tab-pane:first-child').addClass('active');

  $('.sub_tab_toggle').click(function(e){
    e.preventDefault();
    var $this = $(this);
    var curtab = $this.attr('data-sub_tab');

    $('.sub_tab_toggle_ul.ab-sub_nav-sub_tabs li').removeClass('sub_active');
    $('.sub_tab_toggle_ul.ab-sub_nav-sub_tabs li.' + curtab).addClass('sub_active');
    $('div.sub_tab_toggle_div div.ab-sub_tab-pane').removeClass('sub_active');
    $('div.sub_tab_toggle_div div.' + curtab).addClass('sub_active');
  });

  $('.sub_tab_toggle_only').click(function(e){
    e.preventDefault();

    var $this = $(this);
    var curtab = $this.attr('data-sub_tab');
    var partab = $this.attr('data-sub_tab-target');

    $('#' + partab + '_nav li').removeClass('sub_active');
    $('#' + partab + '_nav li.' + curtab).addClass('sub_active');
    $('#' + partab + ' div.ab-sub_tab-pane').removeClass('sub_active');

    $('#' + partab + ' div.' + curtab).addClass('sub_active');
  });
  $('.ab-sub_tab-content .ab-sub_tab-pane:first-child').addClass('sub_active');

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

  $('.lang-select').on('change', function(e){
    let lang = this.value;
    let path = window.location.pathname;
    let query_str = window.location.search;

    switch (page_language) {
      // if current page is english, process jp on the same page, or redirect to different language
      case 'en':
        switch(lang) {
          case 'ja':
          case 'en':
            let wovn_lang = WOVN.io.getCurrentLang();
            let wovn_lang_code = wovn_lang['code'] || 'en';
            $('.lang-select').each(function(ind) {
              $(this).val(lang).prop('selected', true);
            });
            if (wovn_lang != wovn_lang_code) {
              WOVN.io.changeLang(lang);
            }
          break;
          default:
            window.location.href = path.replace(/\/docs\/?/,`\/docs\/${lang}\/`) + replaceParams(query_str,{'wovn': ''});
          break;
        }
        break;
      // if curent page is not english, then check if it needs to be sent to japanese site otherwise just english
      default:
        let lang_re = new RegExp(`\/docs\/${page_language}\/?`);
        switch(lang) {
          case 'ja':
            window.location.href = path.replace(lang_re,`\/docs\/`) + replaceParams(query_str + '&wovn=ja' ,{'wovn': 'ja'});
          break;
          case 'en':
            window.location.href = path.replace(lang_re,`\/docs\/`) + replaceParams(query_str,{'wovn': ''});
          break;
          default:
            window.location.href = path.replace(lang_re,`\/docs\/${lang}\/`) + replaceParams(query_str,{'wovn': ''});
          break;
        }

      break;
    }

  });

  window.addEventListener('wovnApiReady', function(evt){
    // only run wovn if current language is english
    if (page_language == 'en') {
      let wovn_lang = WOVN.io.getCurrentLang();
      let wovn_lang_code = wovn_lang['code'] || 'en';
      $('.lang-select').each(function(ind) {
        let $this = $(this);
        let current_lang = $this.val();
        if ((current_lang != wovn_lang_code) && (wovn_lang_code == 'ja')) {
          $this.val(wovn_lang_code).prop('selected', true);
        }
      });
    }
  });

  // For non us/jp language update language dropdown
  switch (page_language) {
    case 'en':
    case 'ja':
      break;
    default:
      $('.lang-select').each(function(ind) {
        $(this).val(page_language).prop('selected', true);
      });
    break;
  }
});
