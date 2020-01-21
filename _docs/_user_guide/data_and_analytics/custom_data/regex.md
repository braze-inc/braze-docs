---
nav_title: "Regex"
page_order: 5

description: "This reference article covers what Regex is, how to begin using it at Braze, and offers debugger functionality."
page_type: reference
tool:
  - Dashboard
  - Docs
---

# Regex

{% include video.html id="XY5uXoKIvFY" align="right" %}

>  Regular expression, known commonly as RegEx, is a sequence of characters that define a search pattern. RegEx is used at Braze

[Downloadable Regex Cheat Sheet][cheatsheet]

# Regex Debugger

This page allows for basic validation and testing of regex.
​
<div class="alert alert-important" role="alert"><div class="alert-msg"> <b>important: </b><br />
<p>This tool is only meant as a reference, and does not guarantee that the regex matches 100% with the Braze Platform.</p>
</div></div>
<div>
Regex:
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
Check Value(s): <textarea style="" placeholder="match string" id="regex_text"></textarea><br /><br />
​
Matched Results<span id="reg_count"></span>: <div id="regex_results"></div>
</div>
<style type="text/css">
#regex_text {
  -moz-appearance: textfield-multiline;
  -webkit-appearance: textarea;
  border: 1px solid #ced4da !important;
  overflow: auto;
  padding: 2px;
  resize: both;
  white-space: pre-wrap;
  width:100%;
  height: 250px;
  padding: 5px 15px 5px 1.2em;
  border-radius: 0.25rem;
}
#regex_input {
  border: 1px solid #ced4da !important;
  padding: 0 15px 0 5px;
}
#regex_input.invalid {
  background-color: #f8eef7;
}
.regex_highlight {
  background-color: #66d4b333;
}
#regex_results {
  width: 100%;
  min-height: 2em;
  padding: 5px 15px 5px 0.2em;
}
</style>
​
<script type="text/javascript">
$( document ).ready(function() {
  function update_inputmatch() {
    var tomatch = $('#regex_input').val();
    var validreg = true;
    $('#regex_input').removeClass('invalid');
    try {
      var regex = new RegExp(tomatch,'gi');
      $('#regex_results').html('');
    } catch(e) {
      $('#regex_input').addClass('invalid');
      validreg = false;
      $('#regex_results').html('Invalid Regular Expression').prepend('&nbsp;&nbsp;&nbsp;');
    }
    if (validreg){
      if ($('#regex_text').val() && tomatch) {
        var input_str = $('#regex_text').val().split(/\r?\n/);
        var input_replaced = [];
        var reg_count = 0;
        for (var i = 0; i < input_str.length; i++) {
          var inp_rep = ''
          var matched = input_str[i].match(regex);
          if (matched) {
            inp_rep = '<i class="far fa-check-square"></i> ';
            reg_count++;
          }
          else {
            inp_rep = '<i class="far fa-square"></i> ';
          }
          inp_rep += input_str[i].replace(regex,'<span class="regex_highlight">$&</span>');
          input_replaced.push(inp_rep)
        }
        if (reg_count) {
          $('#reg_count').html(' (' + reg_count + ')');
        }
        else {
          $('#reg_count').html('');
        }
        $('#regex_results').html(input_replaced.join('<br />'));
      }
      else {
        $('#regex_results').html('');
      }
    }
​
  }
  $('#regex_input, #regex_text').keyup(function(k){
    update_inputmatch();
  });
});
</script>

[cheatsheet]: 