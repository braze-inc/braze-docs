
$(document).ready(function() {
    var snippets = $('.rouge-code');
    var asset_path = '/docs';
    if (site_language && ( site_language != 'en')) {
      asset_path += "/" + site_language;
    }
    snippets.each(function(k,v){
      var randid = Math.random().toString(36).replace(/[^a-z]+/g, '').substr(2, 10);
      $(this).prepend('<button class="btn" data-clipboard-snippet data-toggle="Copied!" id="' + randid + '"><img class="clippy" src="' + asset_path + '/assets/img/copy_icon.png" alt="Copy to clipboard" style="max-width:30px;max-height:30px;"></button>');
      $(this).prepend('<div id="dv_' + randid + '"></div>');
    });

    var clipboardSnippets = new ClipboardJS('[data-clipboard-snippet]',{
        target: function(trigger) {
            return trigger.nextElementSibling;
        }
    });
    clipboardSnippets.on('success', function(e) {
      var dvid = '#dv_' + e.trigger.id;

      $(dvid).html('Copied').animate({'opacity': 1},300,function(){
        $(dvid).delay(600).animate({'opacity': 0},500)
      });
    });
    clipboardSnippets.on('error', function(e) {
      var dvid = '#dv_' + e.trigger.id;
      $(dvid).html('Error').animate({'opacity': 1},300,function(){
        $(dvid).delay(600).animate({'opacity': 0},500)
      });
        //showTooltip(e.trigger, fallbackMessage(e.action));
    });


  });
