---
nav_title: Documentation feedback
permalink: /feedback/
hide_toc: true
---

<fieldset style="margin-top: 60px;">
<legend style="font-size: 2.5rem;color: #212123;font-weight:bold;">Documentation Feedback</legend>
<div id="feedback">
    <div id="feedback_section">
    Have ideas to improve our docs or noticed something wrong? We’d love to hear from you! Our team reviews every submission to keep making things better.<br /><br />

    <b>How useful do you find Braze docs, on average?</b><br />

    <div id="feedback_answer_star">
      <div class="rating-list">
        <div class="feedback-star">
          <input type="radio" id="rating_1" name="feedback_rating" value="Very Unhelpful" tabindex="-1">
          <label for="rating_1" class="star-label" tabindex="0" aria-label="Very Unhelpful">
            <i class="fas fa-star" data-value="Very Unhelpful" title="Very Unhelpful"></i><br />1<br />Not Useful</label>
        </div>
        <div class="feedback-star">
          <input type="radio" id="rating_2" name="feedback_rating" value="Unhelpful" tabindex="-1">
          <label for="rating_2" class="star-label" tabindex="0" aria-label="Unhelpful">
            <i class="fas fa-star" data-value="Unhelpful" title="Unhelpful"></i><br />2<br />
          </label>
        </div>
        <div class="feedback-star">
          <input type="radio" id="rating_3" name="feedback_rating" value="Somewhat Helpful" tabindex="-1">
          <label for="rating_3" class="star-label" tabindex="0" aria-label="Somewhat helpful">
            <i class="fas fa-star" data-value="Somewhat Helpful" title="Somewhat Helpful"></i><br />3<br />Somewhat Useful</label>
        </div>

        <div class="feedback-star">
          <input type="radio" id="rating_4" name="feedback_rating" value="Helpful" tabindex="-1">
          <label for="rating_4" class="star-label" tabindex="0" aria-label="Helpful">
            <i class="fas fa-star" data-value="Helpful" title="Helpful"></i><br />4<br />
          </label>
        </div>

        <div class="feedback-star">
          <input type="radio" id="rating_5" name="feedback_rating" value="Very Helpful" tabindex="-1">
          <label for="rating_5" class="star-label" tabindex="0" aria-label="Very Helpful">
            <i class="fas fa-star" data-value="Very Helpful" title="Very Helpful"></i><br />5<br />Very Useful
          </label>
        </div>

      </div>
    </div>
    <div style="margin-top: 15px;">
      <b>Share your feedback</b> <br />
      <textarea id="feedback_comment" placeholder="&quot;I couldn’t find any information about this error message&quot;"></textarea><br />
        Have questions? Contact our support team for assistance.
    </div>
    <button type="submit" name="submit_feedback" value="Submit feedback" class="btn btn-black" id="feedback_submit" role="button" style="margin-top:15px;"> Submit feedback </button>
  </div>
  <div id="feedback_msg">
  </div>

  <hr style="border: 1px solid #CDCDCF;margin-top:48px;"/>

  <h3> Help us make these docs great</h3>

  Braze Docs is an open source project that everyone is welcome to contribute to. Join 288+ contributors and submit your first pull request today. <br /><br />

  <button type="submit" onclick="location.href='{{site.baseurl}}/contributing/home'" value="Contributing" class="btn btn-white">Start contributing</button>

</div>
</fieldset>

<style type="text/css">
#feedback {
  font-size: 16px;
}
#feedback_answer_star {
  display: inline-block;
}
#feedback_answer_star .rating-list {
  display: flex;
  list-style: none !important;
  margin: 0 !important;
  line-height: 1;
  flex-direction: row;
}
#feedback_answer_star .feedback-star {
  position: relative;
  padding: 10px 5px;
  width: 65px;
}
#feedback_answer_star .feedback-star input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  cursor: pointer;
}
#feedback_answer_star .feedback-star .star-label {
  display: block;
  color: #999999 !important;
  font-size: 14px;
  text-align: center;
  padding-top: 5px;
  line-height: 1.5em;
  cursor: pointer;
  margin: 0;
}
#feedback_answer_star .feedback-star.hover-active .star-label {
  color: #000000 !important;
}
#feedback_answer_star .feedback-star input[type="radio"]:checked ~ .star-label,
#feedback_answer_star .feedback-star.active .star-label {
  color: #000000 !important;
}
#feedback_answer_star .feedback-star .star-label > i {
  font-size: 35px;
  margin-bottom: 15px;
}

#feedback_comment {
  margin-top: 15px;
  width: 100%;
  max-width: 680px;
  height: 140px !important;
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
#feedback button[type=submit] {
  font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  text-transform: capitalize;
  border-radius: 3px;
  padding: 1rem 2rem;
  border: 1px solid black !important;
}
#feedback button.btn-white {
  font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  text-transform: capitalize;
  border-radius: 3px;
  padding: 1rem 2rem;
  border: 1px solid black !important;
  background-color: #ffffff;
  color: #202024;
}
#feedback button.btn-white:hover {
  background-color: #202024 !important;
  color: #ffffff !important;
}
#feedback button[type=submit]:focus, #feedback button[type=submit]:hover {
  color: #000000;
  background-color: #FFFFFF;
}
#main_content h3 {
  margin-top: 48px;
}
</style>
<script type="text/javascript">
  var feedback_site = '{{site.baseurl}}{{page.url}}';
  var feedback_article_title = '{{page.article_title}}';
  var feedback_nav_title = '{{page.nav_title}}';
  var feedback_helpful = '';

  $('input[name="feedback_rating"]').on('change', function(e){
      feedback_helpful = $(this).val();

      // Update visual state for all stars
      $('.feedback-star').removeClass('active');
      var selectedStar = $(this).closest('.feedback-star');
      var selectedValue = $(this).val();

      // Mark selected star and all previous stars as active
      $('.feedback-star').each(function() {
        var starValue = $(this).find('input').val();
        if (starValue === selectedValue || shouldHighlightStar(starValue, selectedValue)) {
          $(this).addClass('active');
        }
      });
  });

  // Handle hover effect from left to right
  $('.feedback-star').on('mouseenter', function() {
    var hoveredIndex = $(this).index();
    $('.feedback-star').removeClass('hover-active');
    $('.feedback-star').each(function(index) {
      if (index <= hoveredIndex) {
        $(this).addClass('hover-active');
      }
    });
  });

  $('.rating-list').on('mouseleave', function() {
    $('.feedback-star').removeClass('hover-active');
  });

  // Handle keyboard interaction for accessibility
  $('.star-label').on('keydown', function(e) {
    if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      $(this).prev('input[type="radio"]').prop('checked', true).trigger('change');
    }
  });

  function shouldHighlightStar(starValue, selectedValue) {
    var ratings = ['Very Unhelpful', 'Unhelpful', 'Somewhat Helpful', 'Helpful', 'Very Helpful' ];
    var starIndex = ratings.indexOf(starValue);
    var selectedIndex = ratings.indexOf(selectedValue);
    return starIndex <= selectedIndex;
  }


  $('#feedback_submit').on('click',function(e){
    var external_id = window.braze ? window.braze.getUser().getUserId() : '';
    var title = 'Documentations Feedback';
    var comment = $('#feedback_comment').val().trim();
    var feedback_div = $('#feedback_msg');
    var submit_data = {
      'Helpful': feedback_helpful,
      'URL': feedback_site,
      'Article Title': title,
      'Nav Title': title,
      'Params': window.location.search,
      "Language": page_language,
      'Feedback': comment,
      'ExternalId': external_id,
    };
    if (!feedback_helpful || !comment){
      feedback_div.fadeIn();
      feedback_div.addClass('error');
      feedback_div.html('Please provide a rating and feedback');
      feedback_div.fadeOut(2000).removeClass('error');
      return;
    }
    $('#feedback_submit').hide();

    if (window.braze) {
      window.braze.logCustomEvent(
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
