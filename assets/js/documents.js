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

function unEncodeURIComponent(str) {
  let decodedStr = decodeURIComponent(str);
  decodedStr = decodedStr.replace(/%21|%27|%28|%29|%2A/g, function(match) {
    switch (match) {
      case '%21':
        return '!';
      case '%27':
        return "'";
      case '%28':
        return '(';
      case '%29':
        return ')';
      case '%2A':
        return '*';
      default:
        return match;
    }
  });

  return decodedStr;
}

function setAdaTableRole(role='presentation') {
  // assign a role of presentation, and remove the role if it has a th or thead
  $('table').each(function(){
    if (!$(this).attr('role')) {
      $(this).attr('role',role);
    }
    if (($(this).attr('role') == role) && (($(this).has('th').length > 0) || ($(this).has('thead').length > 0))){
      $(this).attr('role',null);
    }
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
// Track Specific tabs to remember on reload
var tab_track = {
  'android': 'tb_android',
  'swift': 'tb_ios',
  'objective-c': 'tb_ios',
  'java': 'tb_android',
  'kotlin': 'tb_android',
  'snowflake': 'tb_data',
  'redshift': 'tb_data',
  'bigquery': 'tb_data',
  'databricks': 'tb_data',
}
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

function replaceParams(qs = '', pr = {}, replace_blank = false) {
	var queryString = qs.replace(/^\?/,'').split('&');
	var params = {};
  if (replace_blank){
    params = pr;
  }
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
        var hash = unEncodeURIComponent(this.hash);
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
  //var nav_bottom_height = $('#nav_bottom').height();
  var scrollHandler = function() {
    var query_str = window.location.search;
    var y_cord = $(this).scrollTop();
  };
  scrollHandler();
  $(window).scroll(scrollHandler);

  // See if sdk tabs should be changed based on url hash
  const sdk_hash = $(window.location.hash);
  if (sdk_hash.is(':header')) {
    const sdk_el = sdk_hash.closest("[data-sdk-tab]");
    let sdk_tab = sdk_el.attr('data-sdk-tab');
    // add sdk tab to query header
    if (sdk_tab) {
      sdk_tab = sdk_tab.replace('sdk-','');
      let tab_replace = {
        'sdktab': sdk_tab
      };
      let query_str = replaceParams(window.location.search, tab_replace, true) + '#' + sdk_hash.attr('id');
      if (window.location.pathname.substr(-1) != '/')  {
        window.history.replaceState(null, null, window.location.pathname + '/' + query_str);
      }
      else {
        window.history.replaceState(null, null,  window.location.pathname + query_str);
      }
    }
  }


  function setTabState(curtab, query_name = 'tab'){
    let tab_norm = curtab.toLowerCase();
    let tab_replace = {};
    tab_replace[query_name] = encodeURIComponent(tab_norm);
    let query_str = replaceParams(window.location.search, tab_replace, true);
    if (window.location.pathname.substr(-1) != '/')  {
      window.history.replaceState(null, null, window.location.pathname + '/' + query_str);
    } else {
      window.history.replaceState(null, null,  window.location.pathname + query_str);
    }
    switch(query_name) {
      case 'sdktab':     { Cookies.set('sdktab',tab_norm, { expires: 365 }); }
      case 'sdksubtab':  { Cookies.set('sdksubtab',tab_norm, { expires: 365 }); }
      case 'pagetab':    { Cookies.set('pagetab',tab_norm, { expires: 365 }); }
      case 'pagesubtab': { Cookies.set('pagesubtab',tab_norm, { expires: 365 }); }
      default: {
        if (tab_track[tab_norm]){
          Cookies.set(tab_track[tab_norm],tab_norm, { expires: 365 });
        }
      }
    }
    var mermaid_charts = $('.language-mermaid').not('[data-processed="true"]').filter(':visible');
    mermaid.run({ nodes: mermaid_charts });
    setPanZoom(mermaid_charts)
  }

  // see if a details tag should be auto-opened
  var details_list = $('details');
  var url_hash = window.location.hash.replace('#','')
  details_list.each(function(k,v) {
    var $this = $(this);
    if (url_hash == string_to_slug($this.find('summary')[0].innerText)) {
      $this.attr('open',true);
    }
  });

  // set tab list attribute for screenreader
  var list_tabs = $('ul.ab-nav')
  list_tabs.each(function(i){
    var $this = $(this);
    if (!$this.attr('role')) {
      $this.attr('role','tablist');
    }
  });
  var list_tab = list_tabs.children('li')
  list_tab.each(function(i){
    var $this = $(this);
    if (!$this.attr('role')) {
      $this.attr('role','tab');
    }
  });
  // set list
  var list_tabs = $('ul').not('.ab-nav');
  list_tabs.each(function(i){
    var $this = $(this);
    if (!$this.attr('role')) {
      $this.attr('role','list');
    }
  });
  var list_tab = list_tabs.children('li')
  list_tab.each(function(i){
    var $this = $(this);
    if (!$this.attr('role')) {
      $this.attr('role','listitem');
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

  function setPanZoom(mermaid_charts){
    setTimeout(function() {
      mermaid_charts.each(function() {
        var svg_element = $(this).find('svg').first();
        if (svg_element) {
          const height = svg_element.outerHeight();
          const width = svg_element.outerWidth();
          window[svg_element.attr('id')] = svgPanZoom(`#${svg_element.attr('id')}`, {
            zoomEnabled: true,
            controlIconsEnabled: true,
            fit: false,
            contain: true,
            center: true,
            minZoom: 0.1,
            viewportSelector: `#${svg_element.attr('id')}`
          });
          svg_element.height(height)
          svg_element.attr('dim_ratio', height/width);
          window[svg_element.attr('id')].resize();
        }
      });
    }, 500);
  }
  // Resize svg with dim_ration on window resize
  $(window).on('resize', function() {
    $('.language-mermaid').filter('[data-processed="true"]').each(function() {
      const svg_element = $(this).find('svg').first();
      const dimRatio = parseFloat(svg_element.attr('dim_ratio'));
      if (!isNaN(dimRatio)) {
        const newWidth = svg_element.outerWidth();
        const newHeight = newWidth * dimRatio;
        if (newHeight > 0) {
          svg_element.height(newHeight);
          window[svg_element.attr('id')].resize();
        }
      }
    });
  });


  function setTabClass(tabtype, prefix, postfix, curtab){
    var tab_selecter = '.' + tabtype + prefix +'tab_toggle_ul.' + tabtype + 'ab-' + prefix +'nav-' + prefix +'tabs';
    var content_selecter ='div.' + tabtype + prefix +'tab_toggle_div';

    var last_active_tab = {};
    var last_active_content = {};
    $(tab_selecter).each(function (k,v) {
      var el = $(v);
      var li = el.children('li')
      var last_active = li.filter('.' + prefix + 'active');
      if (last_active.length) {
        last_active_tab[el.attr('id')] = last_active.first().attr('id');
      }
      else {
        last_active_tab[el.attr('id')] = li.first().attr('id');
      }
    });

    $(content_selecter).each(function (k,v) {
      var el = $(v);
      var div = el.children('div')
      var last_active = div.filter('.' + tabtype + 'ab-' + prefix + 'tab-pane ' +  prefix + 'active');
      if (last_active.length) {
        last_active_content[el.attr('id')] = last_active.first().attr('id');
      }
      else {
        last_active_content[el.attr('id')] = div.first().attr('id');
      }
    });

    $(tab_selecter + ' li').removeClass(prefix + 'active');
    $(tab_selecter + ' li.' + curtab).addClass(prefix + 'active');
    $(content_selecter + ' div.' + tabtype + 'ab-' + prefix + 'tab-pane').removeClass(prefix + 'active');
    $('div.' + tabtype + prefix +'tab_toggle_div div.' + curtab + postfix).addClass(prefix + 'active');

    $(tab_selecter).each(function (k,v) {
      var el = $(v);
      var li = el.children('li')
      var last_active = li.filter('.' + prefix + 'active');
      if (!last_active.length) {
        $('#' + last_active_tab[el.attr('id')]).addClass(prefix + 'active');
      }
    });
    $(content_selecter).each(function (k,v) {
      var el = $(v);
      var div = el.children('div')
      var last_active = div.filter('.' + tabtype + 'ab-' + prefix + 'tab-pane.' +  prefix + 'active');
      if (!last_active.length) {
        $('#' + last_active_content[el.attr('id')]).addClass(prefix + 'active');
      }
    });
    // Refresh Toc
    $('#toc').toc({
      headers:  ((typeof toc_headers != 'undefined') ? toc_headers : "h2,h3"),
      minimumHeaders: ((typeof toc_minheaders != 'undefined') ? toc_minheaders : 2),
    });
  }

  function setTabOnlyClass(tabtype, prefix, postfix, partab, curtab){
    $('#' + partab + '_nav li').removeClass(prefix + 'active');
    $('#' + partab + '_nav li.' + curtab).addClass(prefix + 'active');
    $('#' + partab + ' div.' + tabtype + 'ab-' + prefix + 'tab-pane').removeClass(prefix + 'active');
    $('#' + partab + ' div.' + curtab + postfix).addClass(prefix + 'active');
  }

  // === unified tabs for sdktab + pagetab ===

  // normalize hash -> query for either family
  (function normalizeHashToQuery(){
    const $hash = $(window.location.hash);
    if (!$hash.length || !$hash.is(':header')) return;
    const carriers = [
      { attr: 'data-sdk-tab',  key: 'sdktab',  strip: /^sdk-/ },
      { attr: 'data-page-tab', key: 'pagetab', strip: /^page-/ },
    ];
    for (const c of carriers) {
      const $el = $hash.closest(`[${c.attr}]`);
      if ($el.length) {
        let v = $el.attr(c.attr) || '';
        v = v.replace(c.strip,'');
        const qp = replaceParams(window.location.search, { [c.key]: v }, true) + '#' + $hash.attr('id');
        const base = window.location.pathname.substr(-1) != '/' ? window.location.pathname + '/' : window.location.pathname;
        window.history.replaceState(null, null, base + qp);
        break;
      }
    }
  })();

  // read unified query params
  const _q = new URLSearchParams(window.location.search);
  const q_tab     = (_q.get('pagetab')    || _q.get('sdktab')    || _q.get('tab')    || '').replace('_sub_tab','');
  const q_subtab  = (_q.get('pagesubtab') || _q.get('sdksubtab') || _q.get('subtab') || '').replace('_sub_tab','');

  // ensure first panes active
  $('.sdk-tab-content .sdk-ab-tab-pane:first-child, .page-tab-content .page-ab-tab-pane:first-child').addClass('active');
  $('.sdk-ab-sub_tab-content .sdk-ab-sub_tab-pane:first-child, .page-ab-sub_tab-content .page-ab-sub_tab-pane:first-child').addClass('sub_active');

  // main-tab clicks (global + local)
  $('.tab_toggle, .sdk-tab_toggle, .page-tab_toggle').off('click.unified').on('click.unified', function(e){
    e.preventDefault();
    const $t = $(this);
    const isSdk  = $t.hasClass('sdk-tab_toggle');
    const isPage = $t.hasClass('page-tab_toggle');
    const prefix = isSdk ? 'sdk-' : (isPage ? 'page-' : '');
    const qname  = isSdk ? 'sdktab' : (isPage ? 'pagetab' : 'tab');
    const curtab = $t.attr(`data-${prefix}tab`);
    setTabClass(prefix,'','_tab', curtab);
    setTabState($t.text(), qname);
  });

  $('.tab_toggle_only, .sdk-tab_toggle_only, .page-tab_toggle_only').off('click.unified').on('click.unified', function(e){
    e.preventDefault();
    const $t = $(this);
    const isSdk  = $t.hasClass('sdk-tab_toggle_only');
    const isPage = $t.hasClass('page-tab_toggle_only');
    const prefix = isSdk ? 'sdk-' : (isPage ? 'page-' : '');
    const qname  = isSdk ? 'sdktab' : (isPage ? 'pagetab' : 'tab');
    const curtab = $t.attr(`data-${prefix}tab`);
    const partab = $t.attr(`data-${prefix}tab-target`);
    setTabOnlyClass(prefix,'','_tab', partab, curtab);
    setTabState($t.text(), qname);
  });

  // sub-tab clicks (global + local)
  $('.sub_tab_toggle, .sub_sdk-tab_toggle, .sub_page-tab_toggle').off('click.unified').on('click.unified', function(e){
    e.preventDefault();
    const $t = $(this);
    const isSdk  = $t.hasClass('sub_sdk-tab_toggle');
    const isPage = $t.hasClass('sub_page-tab_toggle');
    const datakey = isSdk ? 'sdk' : (isPage ? 'page' : '');
    const qname   = isSdk ? 'sdksubtab' : (isPage ? 'pagesubtab' : 'subtab');
    const curtab  = $t.attr(`data-${datakey}sub_tab`);
    setTabClass('', 'sub_', '', curtab);
    setTabState($t.text(), qname);
  });

  $('.sub_tab_toggle_only, .sub_sdk-tab_toggle_only, .sub_page-tab_toggle_only').off('click.unified').on('click.unified', function(e){
    e.preventDefault();
    const $t = $(this);
    const isSdk  = $t.hasClass('sub_sdk-tab_toggle_only');
    const isPage = $t.hasClass('sub_page-tab_toggle_only');
    const datakey = isSdk ? 'sdk' : (isPage ? 'page' : '');
    const qname   = isSdk ? 'sdksubtab' : (isPage ? 'pagesubtab' : 'subtab');
    const curtab  = $t.attr(`data-${datakey}sub_tab`);
    const partab  = $t.attr(`data-${datakey}sub_tab-target`);
    setTabOnlyClass('', 'sub_', '', partab, curtab);
    setTabState($t.text(), qname);
  });

  // initial activation honoring params or cookies
  $('.tab_toggle, .sdk-tab_toggle, .page-tab_toggle').each(function(_, v){
    const $t = $(v);
    const isSdk  = $t.hasClass('sdk-tab_toggle');
    const isPage = $t.hasClass('page-tab_toggle');
    const prefix = isSdk ? 'sdk-' : (isPage ? 'page-' : '');
    const curtab = $t.attr(`data-${prefix}tab`);
    const name   = $t.text().toLowerCase();

    if (q_tab && q_tab === name) return setTabClass(prefix,'','_tab', curtab);

    const cookie =
      (isSdk  && Cookies.get('sdktab'))  ||
      (isPage && Cookies.get('pagetab')) ||
      ((!isSdk && !isPage && tab_track[name]) ? Cookies.get(tab_track[name]) : '');

    if (cookie && cookie === name) setTabClass(prefix,'','_tab', curtab);
  });

  $('.sub_tab_toggle, .sub_sdk-tab_toggle, .sub_page-tab_toggle').each(function(_, v){
    const $t = $(v);
    const isSdk  = $t.hasClass('sub_sdk-tab_toggle');
    const isPage = $t.hasClass('sub_page-tab_toggle');
    const curtab = $t.attr(`data-${isSdk ? 'sdk' : (isPage ? 'page' : '')}sub_tab`);
    const name   = $t.text().toLowerCase();

    if ((q_tab && q_tab === name) || (q_subtab && q_subtab === name)) return setTabClass('', 'sub_', '', curtab);

    const cookie =
      (isSdk  && Cookies.get('sdksubtab')) ||
      (isPage && Cookies.get('pagesubtab')) ||
      ((!isSdk && !isPage && tab_track[name]) ? Cookies.get(tab_track[name]) : '');

    if (cookie && cookie === name) setTabClass('', 'sub_', '', curtab);
  });


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
  $('#main_content a').filter(function() {
    var is_external = this.hostname && this.hostname !== location.hostname && this.text && external_ignore.indexOf(this.hostname) < 0 ;
    if ($(this).hasClass('extignore')) {
      is_external = false;
    }
    else if ($(this).has('img').length > 0) {
      if ($(this).has('img')[0].childNodes.length > 0) {
       is_external = false;
      }
    }
    else if ($(this).has('div').length >0 ) {
      is_external = false;
    }

    var punctuations = ['.','!','?'];
    var has_punchtuation = false;
    var punctuation = null;
    if ($(this)[0]) {
      if ($(this)[0].nextSibling){
        punctuation = ($(this)[0].nextSibling.nodeValue || '').substr(0,1);
        if (punctuations.includes(punctuation)) {
          $(this)[0].nextSibling.nodeValue = ($(this)[0].nextSibling.nodeValue || '').substring(1);
          has_punchtuation = true;
        }
      }
    }

    if (is_external || has_punchtuation){
      $(this).wrap('<span class="inline-link">');
    }

    if (has_punchtuation){
      $(this).after(punctuation);
    }
    if (is_external){
      $(this).after(' <i class="fas fa-external-link-alt"></i>');
      $(this).attr('target', '_blank');
    }
  });
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
    let path_lang = (path.split('/') || [])[2];
    let lang_re = new RegExp(`\/docs\/?`);
    // if url has a 2 char language identifier, replace the identifier
    if (path_lang == page_language){
      lang_re = new RegExp(`\/docs\/${page_language}\/?`);
    }
    window.location.href = path.replace(lang_re,`\/docs\/${lang}\/`);
  });

  $('.lang-select').each(function(ind) {
    $(this).val(page_language).prop('selected', true);
  });

  $('[role="tablist"]').each(function(){
    if (!$(this).attr('tabindex')) {
      $(this).attr('tabindex', 0)
    }
  });
  setAdaTableRole();

  // intialized mermaid
  mermaid.initialize({
    startOnLoad: false,
    theme: "default",
  });
  var mermaid_charts = $('.language-mermaid').not('[data-processed="true"]').filter(':visible');
  mermaid.run({ nodes: mermaid_charts });

  // Add svgPanZoom to the rendered Mermaid charts
  setPanZoom(mermaid_charts)


});
