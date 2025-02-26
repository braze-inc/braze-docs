
$(document).ready(function(){
  $.extend($.expr[":"], {
    "containsIN": function(elem, i, match, array) {
      return (elem.textContent || elem.innerText || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
  });
  var filter_action = $('#filter-action');
  var nav_input = $('#nav_filter_input');
  filter_action.click(function(e){
    nav_input.val('');
    filter_action.removeClass('fa-times');
    nav_input.focus();
    nav_input.trigger('keyup');
  })
  nav_input.keyup(function(e){
    var cur_input = $(this);
    var left_div = $('#left_navmenu div');
    var left_navmenu_div = $('#left_navmenu div.nav-item');
    var left_nav = $('#left_navmenu #nav_top');
    var filter_msg = $('#filter-msg');
    left_navmenu_div.unmark();
    switch (cur_input.val().length) {
      case 0:
      case 1:
        filter_msg.html('').hide();
        filter_msg.addClass('d-none');
        left_div.removeClass('filtered')
        left_div.removeClass('showall');

        filter_action.removeClass('fa-times');
        left_nav.show();
      break;
      case 2:
        filter_msg.removeClass('d-none');

        left_navmenu_div.addClass('showall');
        filter_action.addClass('fa-times');
      default:
      left_navmenu_div.addClass("filtered");
      var cur_found = $('#left_navmenu div.nav-item:containsIN("' + cur_input.val() + '")');
      cur_found.removeClass('filtered');
      if (cur_found.length){
        filter_msg.html('').hide();
        left_nav.show();
      }
      else {
        var resultmsg = '<div>Oops! We didn\'t find anything for that.</div><div><a href="/docs/search/?query=' + cur_input.val() + '">Try an Advanced Search instead!</a></div>';
        filter_msg.html(resultmsg).show();
        left_nav.hide();
      }
      // cur_found.removeClass("filtered");
      // cur_found.removeClass("showall");
      /* show all found including up to 4 parent element */
      cur_found.each(function(e, d) {
        var cur_item = $(this);
        var data_parent = $("#" + cur_item.attr("data-parent"));
        data_parent.removeClass("filtered");
        data_parent.addClass("showall");
        $("#" + cur_item.attr("data-parent")).find("div > a").each(function (e,d){
            $($(this).attr("data-target")).removeClass("filtered");
            $($(this).attr("data-target")).addClass("showall");
        });

        $("#" + data_parent.attr("data-parent")).removeClass("filtered");
        $("#" + data_parent.attr("data-parent")).addClass("showall");
        $("#" + data_parent.attr("data-parent")).find("div > a").each(function (e,d){
            $($(this).attr("data-target")).removeClass("filtered");
            $($(this).attr("data-target")).addClass("showall");
        });
        data_parent = $('#' + data_parent.attr("data-parent"));
        data_parent.removeClass("filtered");
        data_parent.addClass("showall");
        $("#" + data_parent.attr("data-parent")).removeClass("filtered");
        $("#" + data_parent.attr("data-parent")).addClass("showall");
        $("#" + data_parent.attr("data-parent")).find("div > a").each(function (e,d){
            $($(this).attr("data-target")).removeClass("filtered");
            $($(this).attr("data-target")).addClass("showall");
        });


        data_parent = $('#' + data_parent.attr("data-parent"));
        data_parent.removeClass("filtered");
        data_parent.addClass("showall");
        $("#" + data_parent.attr("data-parent")).removeClass("filtered");
        $("#" + data_parent.attr("data-parent")).addClass("showall");
        $("#" + data_parent.attr("data-parent")).find("div > a").each(function (e,d){
            $($(this).attr("data-target")).removeClass("filtered");
            $($(this).attr("data-target")).addClass("showall");
        });

      });
      /* if a nav menu item, then show all child elements */
      cur_found.find("div > a").each(function(e, d) {
        var cur_item= $(this);
        $(cur_item.attr("data-target") ).addClass("showall");
        $(cur_item.attr("data-target") ).removeClass("filtered");
        $(cur_item.attr("data-target") + ' div.nav-item').addClass("showall");

        $(cur_item.attr("data-target") + ' div.nav-item').removeClass("filtered");

      });
      left_navmenu_div.mark(cur_input.val());
      break;
    }
  }).keydown(function(e){
    if ( e.which == 13 ) {
      e.preventDefault();
    }
    else if (e.which == 27) {
      filter_action.trigger('click');
    }
  });



});
