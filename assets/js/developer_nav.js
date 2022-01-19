$(document).ready(function () {
  if (page_collection !== "developer_guide") {
    return;
  }
  var exclusion_list = [
    "parent_nav_top_platformintegrationguides_sdkprimer",
    "parent_nav_top_platformintegrationguides_sdkchangelogs",
  ];
  var url_selected = (location.pathname.split("/")[4] || "").replace(/_/g, "");
  var dev_selected = url_selected
    ? `parent_nav_top_platformintegrationguides_${url_selected}`
    : Cookies.get("__dev_selected") || "";
  var platform_objects = $("#nav_top_platformintegrationguides > div.nav-item");
  var platform_list = [];
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
      if (dev_selected) {
        if (dev_selected !== obj_id) {
          hide(obj_id);
        } else {
          show(obj_id);
        }
      }
    }
  });
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
