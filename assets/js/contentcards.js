$(document).ready(function() {
  $('#cc_prompt').on('click',function(e){
    e.preventDefault();
    var $this = $(this);
    var curcontainer = $('#contentcards');
    if (curcontainer.find('div').length ){
      $this.removeClass('cc_show');
      curcontainer.hide();
      braze.hideContentCards();
    }
    else {
      braze.showContentCards(curcontainer[0]);
      curcontainer.show();
      $this.addClass('cc_show');
      curcontainer.find('.ab-feed-buttons-wrapper .ab-close-button').on('click',function(e){
        $this.removeClass('cc_show');
        curcontainer.hide();
      });
    }
  });

});
