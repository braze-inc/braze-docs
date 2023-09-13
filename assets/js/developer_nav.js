$(document).ready(function () {
  if (page_collection !== "developer_guide") {
    return;
  }
  var exclusion_list = [
    "parent_nav_top_platformintegrationguides_sdkprimer",
    "parent_nav_top_platformintegrationguides_sdkchangelogs",
    "TV and OTT Integrations",
  ];

  var url_selected = (location.pathname.split("/")[4] || "").replace(/_/g, "");
  if (site_language != 'en') {
    url_selected = (location.pathname.split("/")[5] || "").replace(/_/g, "");
  }
  var dev_selected = (url_selected
    ? `parent_nav_top_platformintegrationguides_${url_selected}`
    : Cookies.get("__dev_selected") || "").toLowerCase();
  var platform_objects = $("#nav_top_platformintegrationguides > div.nav-item");
  var platform_list = [];
  var hide_list = [];
  var show_list = [];
  var select_html =
    '<div id="dev_select_div"><select id="dev_select"><option value="">Select Platform</option>';
  platform_objects.each(function (k) {
    var $this = $(this);
    var obj_id = $this.attr("id");
    if (exclusion_list.indexOf(obj_id) === -1) {
      platform_list.push(obj_id);
      select_html += `<option value="${obj_id}" `;
      if (dev_selected === obj_id) {
        select_html += ' selected="selected"';
      }
      select_html += `>${$this.text().trim()}</option>`;
      if (exclusion_list.indexOf(dev_selected) === -1) {
        if (dev_selected !== obj_id) {
          hide_list.push(obj_id);
        }
        else {
          show_list.push(obj_id);
        }
      }
    }
  });

  // if no platform is selected, or in the discolure menu, show all platforms
  if ( !dev_selected && !url_selected || (location.pathname.indexOf('disclosures') > -1) ||(location.pathname.indexOf('customization_guides') > -1) || (location.pathname.indexOf('platform_wide') > -1) ) {
    platform_objects.each(function (nav_index,nav_item) {
      // var id = $(this).attr('id');
      var cur_nav = $(nav_item);
      if (cur_nav.length) {
        var id = cur_nav.first().attr('id');
        var navigation_item = $("#" + id + " a");
        if (navigation_item.attr("aria-expanded") === "true"){
          $('#' + navigation_item.attr('id')).trigger("click");
        }
      }
    });
  }
  else {
    for (let hl = 0; hl < hide_list.length; hl++) {
      hide(hide_list[hl]);
    }
    for (let sl = 0; sl < show_list.length; sl++) {
      show(show_list[sl]);
    }
  }



  $("#parent_nav_top").css("width", "100%");
  select_html += "</select></div>";
  $("#parent_nav_home div .nav_block").append(select_html);
  $("#dev_select").change(function (e) {
    var $this = $(this);
    var cur_sel = $this.val();
    Cookies.set("__dev_selected", cur_sel);
    if (!cur_sel) {
      $(platform_list).each(function (i, v) {
        $("#" + v).show();
      });
    } else {
      $(platform_list).each(function (i, v) {
        if (exclusion_list.indexOf(v) == -1) {
          if ($("#" + v + " a").attr("aria-expanded") == "true") {
            $("#" + v + " a").trigger("click");
          }
          $("#" + v).hide();
        }
      });
      show(cur_sel);
    }
  });
  $("#guide_featured_list a, #guide_list a").click(function (e) {
    var $this = $(this);
    var navlink = $this.attr("data-navlink");
    if (navlink) {
      navlink = "parent_nav_top_platformintegrationguides_" + navlink;
      if (platform_list.indexOf(navlink) > -1) {
        Cookies.set("__dev_selected", navlink);
      }
    }
  });

  function hide(dropdown_id) {
    var navigation_id = $("#" + dropdown_id + " a");
    $("#" + dropdown_id).hide();
    if (navigation_id.attr("aria-expanded") === "true") {
      navigation_id.trigger("click");
    }
  }

  function show(dropdown_id) {
    var navigation_id = $("#" + dropdown_id + " a");
    $("#" + dropdown_id).show();
    if (navigation_id.attr("aria-expanded") === "false") {
      navigation_id.trigger("click");
    }
  }

});
