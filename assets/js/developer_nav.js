$(document).ready(function () {
	if(page_collection == 'developer_guide') {
		var dev_selected = Cookies.get('__dev_selected') || '';
		var platform_objects = $('#nav_top_platformintegrationguides > div.nav-item');
		var platform_list = [];
		var select_html = '<div id="dev_select_div"><select id="dev_select"><option value="">All</option>';
		platform_objects.each(function(k){
			var $this = $(this);
			var obj_id = $this.attr('id');
			platform_list.push(obj_id);
			select_html += `<option value="${obj_id}" `;
			if (dev_selected == obj_id){
				select_html += ' selected="selected"'
			}
			select_html += `>${$this.text().trim()}</option>`;
			if (dev_selected != '') {
				var sel_item = $('#' + obj_id + ' a');

				if (dev_selected != obj_id) {
					$('#' + obj_id).hide();
					if (sel_item.attr('aria-expanded') == 'true') {
						sel_item.trigger('click');
					}
				}
				else {
					$('#' + obj_id).show();
					if (sel_item.attr('aria-expanded') == 'false') {
						sel_item.trigger('click');
					}
				}
			}
		});
		$('#parent_nav_top').css('width','100%');
		select_html += '</select></div>';
		$('#parent_nav_home div .nav_block').append(select_html);
		$('#dev_select').change(function(e){
			var $this = $(this);
			var cur_sel = $this.val();
			Cookies.set('__dev_selected', cur_sel);
			if (cur_sel == ''){
				$(platform_list).each(function(i,v){
						$("#" + v).show()
				});
			}
			else {
				$(platform_list).each(function(i,v){
					if ($("#" + v + ' a').attr('aria-expanded') == 'true') {
						$("#" + v + ' a').trigger('click');
					}
					$("#" + v).hide();
				});
				$('#' + cur_sel).show();
				var sel_item = $('#' + cur_sel + ' a');
				if (sel_item.attr('aria-expanded') == 'false') {
					sel_item.trigger('click');
				}
			}
		})
	}
});
