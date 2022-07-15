

$(document).ready(function(){
  if ( $('#feedback').length && (typeof(feedback_site ) != 'undefined')) {
    var feedback_config = {
      dest: 'https://script.google.com/macros/s/AKfycbyeErceUoe9xIdSmmfgDsFncY9Fm_dg92MGSs_9FOYKoMLiSms/exec',
      site: feedback_site,
      params: null,
      helpful: '',
      postdate: null,
      ID: null
    };
    $('#feedback_helpful_yes, #feedback_helpful_but, #feedback_helpful_no').on('click', function(e){
      e.preventDefault();
      var $this = $(this);
      var helpful = $this.attr('data-value');
      feedback_config.helpful = helpful;


      if (typeof (appboy) !== 'undefined') {
        appboy.logCustomEvent("Documentations Feedback", {"Feedback": helpful,"URL": feedback_config['site']});
      }

      $('#feedback_answer').fadeOut("slow");
      var submit_data = {'Helpful': helpful,'URL':feedback_config['site'],'Params':window.location.search};
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
          // if ((res_helpful == 'Yes But') || (res_helpful == 'No') ){
          $('#feedback_comment_div').fadeIn('slow');
          // }
          // else {
          //   $('#feedback_msg').html('Thanks for your response.<a href="#" onclick="$(\'#feedback_comment_div\').fadeIn(\'slow\');$(\'#feedback_msg\').fadeOut(\'slow\');return false;">Leave Feedback</a>');
          //   $('#feedback_msg').fadeIn("slow");
          // }
        }
        else {
          $('#feedback_msg').html('Error. Please try again at a later time.');
        }
        $('#feedback_msg').fadeIn("slow");
      });
    });

    $('#feedback_submit_button').on('click',function(e){
      $('#feedback_comment_div').fadeOut('slow');
      var submit_data = {'Helpful': feedback_config['helpful'],'URL':feedback_config['site'],'Params': feedback_config['params'],'ID': feedback_config['ID'],'postdate':feedback_config['postdate'],'Feedback':$('#feedback_comment').val()};
      if (typeof (appboy) !== 'undefined') {
        appboy.logCustomEvent("Documentations Feedback Comment", {"Feedback": feedback_config['helpful'],"URL": feedback_config['site'],"Comment": $('#feedback_comment').val()});
      }
      var jqxhr = $.ajax({
        url: feedback_config['dest'],
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
