---
nav_title: Documentación Feedback
permalink: /feedback/
hide_toc: true
---

<fieldset style="margin-top: 60px;">
<legend style="font-size: 2.5rem;color: #212123;font-weight:bold;">Comentarios sobre la documentación</legend>
<div id="feedback">
    <div id="feedback_section">
    ¿Tienes ideas para mejorar nuestros documentos o has detectado algún error? ¡Nos encantaría saber de ti! Nuestro equipo revisa cada envío para seguir mejorando.<br /><br />

    <b>¿Cómo de útiles te parecen los documentos de Braze, por término medio?</b><br />

    <div id="feedback_answer_star">
      <ul class="list-inline rating-list">
        <li class="inline-star feedback-star" tabindex="0"><i class="fas fa-star" data-value="Very Helpful" title="Muy útil"></i><br />5<br />Muy útil</li>
        <li class="inline-star feedback-star" tabindex="0"><i class="fas fa-star" data-value="Helpful" title="Útil"></i></li>
        <li class="inline-star feedback-star" tabindex="0"><i class="fas fa-star" data-value="Somewhat Helpful" title="Algo útil"></i><br />3<br />Algo útil</li>
        <li class="inline-star feedback-star" tabindex="0"><i class="fas fa-star" data-value="Unhelpful" title="Poco útil"></i></li>
        <li class="inline-star feedback-star" tabindex="0"><i class="fas fa-star" data-value="Very Unhelpful" title="Muy poco útil"></i><br />1<br />No es útil</li>
      </ul>
    </div>
    <div style="margin-top: 15px;">
      <b>Comparte tu opinión</b> <br />
      <textarea id="feedback_comment" placeholder="&quot;No he podido encontrar ninguna información sobre este mensaje de error&quot;"></textarea><br />
        ¿Tienes alguna pregunta? Contacta con nuestro equipo de soporte.
    </div>
    <button type="submit" name="submit_feedback" value="ENVIAR COMENTARIOS" class="btn btn-black" id="feedback_submit" role="button" style="margin-top:15px;"> ENVIAR COMENTARIOS </button>
  </div>
  <div id="feedback_msg">
  </div>

  <hr style="border: 1px solid grey;margin-top:30px;"/>

  <h3> Ayúdanos a hacer grandes estos documentos</h3>

  Braze Docs es un proyecto de código abierto al que todo el mundo puede contribuir. Únete a más de 288 colaboradores y envía tu primer pull request hoy mismo. <br /><br />


  <button type="submit" onclick="location.href='{{site.baseurl}}/contributing/home'" value="Contribuir " class="btn">Empezar a contribuir</button>

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
