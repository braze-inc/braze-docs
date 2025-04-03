---
내비게이션 제목 설명서 피드백 퍼머링크: /feedback/ 숨기기\_toc: true
---

<fieldset style="margin-top: 60px;">
<legend style="font-size: 2.5rem;color: #212123;font-weight:bold;">설명서 피드백</legend>
<div id="feedback">
    <div id="feedback_section">
    문서 개선 아이디어가 있거나 잘못된 점을 발견하셨나요? 우리는 당신의 소식을 듣고 싶습니다! 우리 팀은 모든 제출물을 검토하여 더 나은 것을 만들기 위해 노력합니다.<br /><br />

    Braze 문서가 평균적으로 얼마나 유용하다고 생각하십니까?<br />

    <div id="feedback_answer_star">
      <ul class="list-inline rating-list">
        <li class="inline-star feedback-star" tabindex="0">매우 유용한<br />5<br />매우 유용하다</li>
        <li class="inline-star feedback-star" tabindex="0">도움</li>
        <li class="inline-star feedback-star" tabindex="0">다소 도움이 되는<br />3<br />다소 유용한</li>
        <li class="inline-star feedback-star" tabindex="0">도움이 되지 않는</li>
        <li class="inline-star feedback-star" tabindex="0">매우 도움이 되지 않음<br />1<br />유용하지 않음</li>
      </ul>
    </div>
    <div style="margin-top: 15px;">
      피드백을 공유하세요 <br />
      이 오류 메시지에 대한 정보를 찾을 수 없었습니다.<br />
        질문이 있으신가요? 도움이 필요하면 지원팀에 문의하세요.
    </div>
    피드백 제출 피드백 제출
  </div>
  <div id="feedback_msg">
  </div>

  <hr style="border: 1px solid grey;margin-top:30px;"/>

  <h3> 이 문서들을 훌륭하게 만드는 데 도움을 주세요</h3>

  브레이즈 문서는 모든 사람이 기여할 수 있는 오픈 소스 프로젝트입니다. 288명 이상의 기여자와 함께하고 오늘 첫 번째 풀 리퀘스트를 제출하세요. <br /><br />


  기여하기 시작하기 기여하기

</div>
</fieldset>

<style type="text/css">
#feedback {
  font-size: 16px;
}
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
  padding: 10px 5px;
  width: 65px;
  color: #999999 !important;
}
#feedback_answer_star > ul > li:hover,
#feedback_answer_star .rating-list li:hover~li {
  color: #000000 !important;
}
#feedback_answer_star > ul > li.active {
  color: #000000 !important;
}
#feedback_answer_star > ul > li > i {
  font-size: 35px;
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
.feedback-star {
  font-size: 14px;
  text-align: center;
  padding-top: 5px;
  line-height: 1em;
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
        var star = el.children('i');
        if (star.attr('data-value') == feedback_helpful){
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
