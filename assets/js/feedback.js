

$(document).ready(function(){
  if ( $('#feedback').length && (typeof(feedback_site ) != 'undefined')) {
    var feedback_config = {
      dest: 'https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/feedback',
      site: feedback_site,
      article_title: feedback_article_title,
      nav_title: feedback_nav_title,
      params: null,
      helpful: '',
      postdate: null,
      ID: null
    };

    $('#feedback_answer li.inline-thumb i').on('click', function(e){
      e.preventDefault();
      var feedback_cookie_name = '_site_feedback';
      var last_feedback = Cookies.get(feedback_cookie_name);
      var process_submit = true;
      // only allow 1 submission every 1mins and if they dont have a cookie, then ignore
      if (!last_feedback) {
        Cookies.set(feedback_cookie_name, new Date(), { expires: (1/(24 * 60)) });
        // Check to make sure user has a cookie to allow submission
        var last_feedback = Cookies.get(feedback_cookie_name);
        if (!last_feedback) {
          process_submit = false;
        }
      }
      else {
        process_submit = false;
      }

      if (process_submit) {
        var $this = $(this);
        var helpful = $this.closest('i').attr('data-value');
        feedback_config.helpful = helpful;

        $('#feedback_answer').fadeOut("slow");
        if (window.braze) {
          braze.logCustomEvent(
            "Documentation Feedback", {
              "Feedback": helpful,
              "Article Title": feedback_config['article_title'],
              "Nav Title": feedback_config['nav_title'],
              "URL": feedback_config['site'],
              "Language": page_language
            }
          )
        }
        var external_id = window.braze ? window.braze.getUser().getUserId() : '';

        var submit_data = {
          'Helpful': helpful,
          'URL':feedback_config['site'],
          'Article Title': feedback_config['article_title'],
          'Nav Title': feedback_config['nav_title'],
          'Params':window.location.search,
          'Language': page_language,
          'ExternalId': external_id
        };

        var jqxhr = $.ajax({
          url: feedback_config['dest'],
          method: "GET",
          dataType: "json",
          data: submit_data
        }).done(function(dt) {
          $('#feedback_msg').html('');
          if (dt['result'] == 'success'){
            var res_helpful = dt['helpful'];
            feedback_config['ID'] = dt['ID'];
            feedback_config['helpful'] = dt['helpful'];
            feedback_config['postdate'] = dt['postdate'];
            feedback_config['params'] = dt['params'];
            if ((res_helpful == 'Very Helpful') ){
              $('#feedback_comment').attr('placeholder','Your opinion matters! Tell us what you think about the documentation.');
            }
            $('#feedback_msg').html('Thanks for your response.<a href="#" onclick="$(\'#feedback_comment_div\').fadeIn(\'slow\');$(\'#feedback_msg\').fadeOut(\'slow\');return false;">Leave feedback</a>');
            $('#feedback_msg').fadeIn("slow");
          }
          else {
            $('#feedback_msg').html('Error. Please try again at a later time.');
          }
          $('#feedback_msg').fadeIn("slow");
        });
      }
      else {
        $('#feedback_answer').fadeOut();
        $('#feedback_msg').html('')
        $('#feedback_msg').delay(750).fadeIn("slow", function (){
          $(this).html('Thanks for your response');
        });
      }
    });

    $('#feedback_submit_button').on('click',function(e){
      $('#feedback_comment_div').fadeOut('slow');
      if (window.braze) {
        braze.logCustomEvent(
          "Documentation Feedback Comment", {
            "Feedback": feedback_config['helpful'],
            "Article Title": feedback_config['article_title'],
            "Nav Title": feedback_config['nav_title'],
            "URL": feedback_config['site'],
            "Language": page_language,
            "Comment": $('#feedback_comment').val()
          }
        );
      }
      var external_id = window.braze ? window.braze.getUser().getUserId() : '';

      var submit_data = {
        'Helpful': feedback_config['helpful'],
        'URL':feedback_config['site'],
        'Article Title': feedback_config['article_title'],
        'Nav Title': feedback_config['nav_title'],
        'Params': feedback_config['params'],
        'ID': feedback_config['ID'],
        'postdate':feedback_config['postdate'],
        'Language': page_language,
        'Feedback':$('#feedback_comment').val(),
        'ExternalId': external_id
      };
      var jqxhr = $.ajax({
        url: feedback_config['dest'] + '/comment',
        method: "GET",
        dataType: "json",
        data: submit_data
      }).done(function(dt) {
        $('#feedback_msg').html('');
        if (dt['result'] == 'success'){
          $('#feedback_msg').html('We truly value every piece of feedback. Thank you for your response.');
          $('#feedback_msg').fadeIn("slow");
        }
        else {
          $('#feedback_msg').html('Error. Please try again at a later time.');
        }
        $('#feedback_msg').fadeIn("slow");
      });
    });
  }
});
