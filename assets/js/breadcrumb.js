$(document).ready(function() {

  var breadcrumb = $('#breadcrumb');
  if (breadcrumb.length){
    var topparent = 'parent_nav_top';
    var curpage = $('#left_navmenu .nav-item.active');
    var bc_list =  curpage.length ? curpage.text() : '';
    var bc_link = '';
    var curtext = '';
    var dataparent = curpage.length ? curpage.attr('data-parent') : null;
    while (dataparent ) {
      curpage = $('#' + dataparent);
      curtext = curpage.text();
      if (curtext){
        bc_link = curpage.find('.nav_link');
        if (bc_link.length && bc_link[0].href) {
          curtext = '<a href="' + bc_link[0].href + '">' + curtext + '</a>'
        }
        bc_list =  curtext + '&nbsp; > &nbsp;' + bc_list;
      }
      dataparent =  curpage.attr('data-parent');
    }
    // var menu_active = $('#header_navbar .nav-item.active ');
    // curtext = menu_active.text();
    // bc_link = menu_active.find('.nav-link');
    // if (bc_link.length) {
    //   curtext = '<a href="' + bc_link[0].href + '">' + curtext + '</a>'
    // }
    // bc_list = curtext + ' ' + bc_list;
    if (bc_list.length) {
      if (typeof page_collection_title !== 'undefined' && page_collection_title && typeof base_url !== 'undefined' && typeof page_collection !== 'undefined' && typeof page_collection_default_path !== 'undefined') {
        bc_list = '<a href="' + base_url + '/' + page_collection + '/' + page_collection_default_path + '">' + page_collection_title + '</a> &nbsp; > &nbsp;' + bc_list;
      }
      breadcrumb.html(bc_list);
      breadcrumb.parent().addClass('has_breadcrumb')
    }
    else {
      // No active nav item: still show collection link when available
      if (typeof page_collection_title !== 'undefined' && page_collection_title && typeof base_url !== 'undefined' && typeof page_collection !== 'undefined' && typeof page_collection_default_path !== 'undefined') {
        bc_list = '<a href="' + base_url + '/' + page_collection + '/' + page_collection_default_path + '">' + page_collection_title + '</a>';
        breadcrumb.html(bc_list);
        breadcrumb.parent().addClass('has_breadcrumb');
      }
      else {
        breadcrumb.hide();
      }
    }
  }
});
