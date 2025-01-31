---
nav_title: Documentation Feedback
permalink: /feedback/
hide_toc: true
---

# Documentation Feedback

<div id="feedback">
    <div id="feedback_section">
    <div id="feedback_title">Please rate how useful the Braze documentation is for you</div>
    <br />
      <div id="feedback_answer_star">
        <ul class="list-inline rating-list">
          <li class="inline-star" tabindex="0"><i class="fas fa-star" data-value="Very Helpful" title="Very Helpful"></i></li>
          <li class="inline-star" tabindex="0"><i class="fas fa-star" data-value="Helpful" title="Helpful"></i></li>
          <li class="inline-star" tabindex="0"><i class="fas fa-star" data-value="Somewhat Helpful" title="Somewhat Helpful"></i></li>
          <li class="inline-star" tabindex="0"><i class="fas fa-star" data-value="Unhelpful" title="Unhelpful"></i></li>
          <li class="inline-star" tabindex="0"><i class="fas fa-star" data-value="Very Unhelpful" title="Very Unhelpful"></i></li>
        </ul>
      </div>
      <div>
          <textarea id="feedback_comment" placeholder="How can we improve this page?"></textarea>
      </div>
      <button type="submit" name="submit_feedback" value="SUBMIT FEEDBACK" class="btn btn-black" id="feedback_submit" role="button"> SUBMIT FEEDBACK </button>
    </div>
    <div id="feedback_msg">
    </div>
</div>

<style type="text/css">
#feedback_answer_star {
  display: inline-block;
}
#feedback_answer_star > ul {
  display: flex;
  list-style: none !important;
  margin: 0 !important;
  line-height: 1;
}
#feedback_answer_star > ul > li {
  list-style: none;
  color: #ddd;
  padding: 10px 5px;
  width: 50px;
}
#feedback_answer_star > ul > li > i {
  font-size: 35px;
}

#feedback_comment {
  margin-top: 15px;
  width: 100%;
  max-width: 680px;
  height: 300px;
  border: 2px solid grey !important;
  border-radius: 3px;
}
#feedback_msg {
  margin-top: 10px;
}
  
#feedback_msg.error {
  color: red;
  font-weight: bold;
}

</style>
<script type="text/javascript">
  var feedback_site = '{{site.baseurl}}{{page.url}}';
  var feedback_article_title = '{{page.article_title}}';
  var feedback_nav_title = '{{page.nav_title}}';
  var feedback_helpful = '';

  $('#feedback_answer_star li').on('click', function(e){
      e.preventDefault();
      var li = $(this);
      var ul = li.parent();
      var i = li.children('i');
      feedback_helpful = i.attr('data-value') || '';
      var lis = ul.children('li');
      var is_sel = false;
      lis.each(function (f,c){
        var el = $(this)
        if (el.children('i').attr('data-value') == feedback_helpful){
          is_sel = true;
        }
        if (is_sel){
          el.addClass('active');
        }
        else {
          el.removeClass('active');
        }
      })
  });


  $('#feedback_submit').on('click',function(e){
    var title = 'Documentations Feedback';
    var comment = $('#feedback_comment').val().trim();
    var feedback_div = $('#feedback_msg');
    var submit_data = {
      'Helpful': feedback_helpful,
      'URL': feedback_site,
      'Article Title':  title,
      'Nav Title': title,
      'Params': window.location.search,
      "Language": page_language,
      'Feedback': comment
    };
    if (!feedback_helpful || !comment){
      feedback_div.fadeIn();
      feedback_div.addClass('error');
      feedback_div.html('Please provide a rating and feedback');
      feedback_div.fadeOut(2000).removeClass('error');
      return;
    }
    $('#feedback_submit').hide();

    if (typeof (appboy) !== 'undefined') {
      appboy.logCustomEvent(
        "Documentations Feedback Comment", {
          "Feedback": feedback_helpful,
          "Article Title": title,
          "Nav Title": title,
          "URL": feedback_site,
          "Language": page_language,
          "Comment": comment
        }
      );
    }

    var jqxhr = $.ajax({
        url: 'https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/feedback',
        method: "GET",
        dataType: "json",
        data: submit_data
      }).done(function(dt) {
        feedback_div.html('');
        if (dt['result'] == 'success'){
          $('#feedback_section').hide();
          feedback_div.html('We truly value every piece of feedback. Thank you for your response.');
          feedback_div.fadeIn("slow");
        }
        else {
          feedback_div.html('Error. Please try again at a later time.');
          $('#feedback_submit').show();
        }
        feedback_div.fadeIn("slow");
      });
  });
</script>
