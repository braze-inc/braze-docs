---
nav_title: "Regular Expressions"
article_title: Regular Expressions
page_order: 5

description: "This reference article covers what regular expressions (regex) are, how to begin using them, and offers debugger functionality to validate and test regular expressions."
page_type: reference
tool:
  - Testing Tools
  
---

# Regular expressions with braze

{% include video.html id="3h5Xbhl-TxE" align="right" %}

>  Regular expressions, known commonly as regex, is a sequence of characters that define a search pattern. Regular expressions let you do validation of text grouping and find and replace actions. <br><br>Regex is used at Braze to give you a more flexible string matching solution in your segmentation and campaign filtering for your target audience. 

In the provided video, we show you how regular expressions can be used and tested on the [Regex101][regex] site. Below we also offer an inhouse regex tester, a helpful cheatsheet, sample data referenced in the Regex LAB video, as well as some frequently asked questions.

[Downloadable Regex Cheat Sheet PDF][cheatsheet]<br>
[Downloadable Sample Data RTF][dummydata]

{% tabs %}
{% tab Regex Debugger %}

This form allows for basic validation and testing of regular expressions.
​
<div class="alert alert-important" role="alert"><div class="alert-msg"> <b>important: </b><br />
<p>This tool is only meant as a reference, and does not guarantee that the regex matches 100% with the Braze Platform. Regex used within Braze are case sensitive, so make sure that your regexes can handle all cases. </p>
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
      if ($('#regex_text').val() ) {
        if (tomatch) {
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
      }
      else {
        $('#regex_results').html('');
      }
    }
  }
  $('#regex_input, #regex_text').keyup(function(k){
    update_inputmatch();
  });
});
</script>
{% endtab %}
{% tab Frequently Asked Questions %}

{% details How do I filter for inbox specific email addresses when segmenting? %}

Use the email address filter, set it to "matches regex". Reference the regex for email addresses, <font color="red">[a-zA-Z0-9.+_-]+ </font>@<font color="blue">[a-zA-Z0-9.-]+</font>\.<font color="green">[a-zA-Z.-]+</font> where:
- <font color="red">[a-zA-Z0-9.+_-]+</font> is the beginning of the email address before the '@' character. So the "name" in "name@example.com".
- <font color="blue">[a-zA-Z0-9.-]+</font> is the first part of the domain. So the "example" in "name@example.com".
- <font color="green">[a-zA-Z.-]+</font> is the last part of the domain. So the "com" in "name@example.com".

{% enddetails %}

{% details How do I filter for email addresses associated to a specific domain? %}

Say you want to filter for emails ending with @braze.com. You would use the email address filter, set it to matches regex, and enter "@braze.com" in the field.

![image1]({% image_buster /assets/img/regex/regeximg1.png %})

{% enddetails%}

{% details How can I use regex on number strings to filter for values ≥ x or ≤ x? %}
If you're searching for __values ≥ x__, the regex to use would be __^([x-y]|\d{z,})$__
where x-y is the range of numbers (0-9) of the first digit, and z is the one more the number of digits of x.<br>__Example__<br>
For values ≥ 50, the regex would then be ^([5-9][0-9]|\d{3,})$

If you're searching for __values ≤ x__, the regex would be __^([x-y]|[a-b])$__
where x-y is the range of numbers (0-9) of the first digit, and a-b is lower bound range of x.<br>__Example__<br>
For values ≤ 50, the regex would then be ^([5-9][0-9]|[0-4][0-9])$
{% enddetails %}
{% details How to filter custom attributes that start with a specific string? %}
Use the __^__ to character to denote what the string starts with and enter the name of you're trying to specify. 

__Example__<br>
If you're trying to target users who live in cities that start with "San", your regex would be __^San \w__. In such a case, you would successfully target users from cities like San Francisco, San Diego, San Jose, etc.

![image2]({% image_buster /assets/img/regex/regeximg2.png %})
{% enddetails %}
{% details How to filter for certain phone numbers with regex %}

Before using regex to filter phone numbers, please take note that numbers logged for user profiles should already be in an [E.164 format](https://en.wikipedia.org/wiki/E.164) as specified in our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/).

Assuming US phone numbers, the regex you'll want to use is in the format __1?\d\d\d\d\d\d\d\d\d\d__, where each "\d" is a digit you want to specify - the first 3 of which would be the area code.

Likewise, the format for __UK phone numbers__ are __^\+4\d\d\d\d\d\d\d\d\d\d\d__ and any other country would be the the respective __country code followed by the necessary number of "\d" characters for each remaining digit__. So in the case of Lithuania with country code 3, their regex would be __^\+3\d\d\d\d\d\d\d\d\d\d.__

__Example__<br>
Let's say you wanted to filter users by phone number for a specific area code, 718. Use the phone number filter, set it to "matches regex", and enter __^1?718\d\d\d\d\d\d\d__  

![image3]({% image_buster /assets/img/regex/regeximg3.png %})
{% enddetails %}
<br><br>
{% endtab %}
{% endtabs %}

[regex]: https://regex101.com/
[cheatsheet]: {% image_buster /assets/download_file/regex-cheatsheet.pdf %}
[dummydata]: {% image_buster /assets/download_file/regex-dummy-data.rtf %}
