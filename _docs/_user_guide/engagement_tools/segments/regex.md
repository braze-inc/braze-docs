---
nav_title: "Regular expressions"
article_title: Regular Expressions
page_order: 10

description: "This reference article covers what regular expressions (regex) are, how to begin using them, and offers debugger functionality to validate and test regular expressions."
page_type: reference
tool:
  - Testing Tools
  
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} Regular expressions

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> Regular expression, known commonly as a regex, is a sequence of characters that defines a search pattern. Regular expressions let you validate text groupings and perform find and replace actions. At Braze, we leverage regular expressions to give you a more flexible string matching solution in your segmentation and campaign filtering for your target audience.<br><br>This page covers regular expressions (regex), how to use them, frequently asked questions, and provides a regex debugger to test regular expressions.

In the linked Braze Learning course, we show you how regular expressions can be used and tested on [Regex101](https://regex101.com/). We also offer an [in-house regex tester](#regex-debugger), a helpful reference page, sample data referenced in the regex Braze Learning video, as well as some frequently asked questions.

## Resources

- [Regular expression basics](https://learning.braze.com/regular-expression-basics-for-braze) Braze Learning course
- [Regex Cheat Sheet]({{site.baseurl}}/regex_cheat_sheet/)
- [Sample Data RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## Regex debugger

{% alert important %}
This tool is only meant as a reference, and does not guarantee that the regex matches 100% with the Braze platform. Regular expressions in Braze for segmentation and filters automatically add the `/gi` modifier. The [gi modifier](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) is used to do a case-insensitive search of all occurrences of a regular expression in a string.  
<br>
Regular expressions for custom event trigger properties and trigger filters use the `/g` modifier (case sensitive, see [g modifier](https://www.w3schools.com/jsref/jsref_regexp_g.asp)) and do not use the `/i` modifier. For case insensitivity for custom event trigger properties and trigger filters, use `(?i)` instead. For example, `Matches regex (?i)STOP(?-i)` catches any use of "STOP" in any case (such as "stop", "please stop", and "never stop sending me messages").
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
This form allows for basic validation and testing of regular expressions.
​
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
{% endtabs %}

## Frequently asked questions

#### Does the `does not match regex` filter include blank values?

No. If the value is blank, the user will not be included in the `does not match regex` filter.

#### How do I filter for inbox-specific email addresses when segmenting?

{% raw %}
Use the email address filter, set it to `matches regex`. Then reference the regex for email addresses:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

We can break this regex down to the following three parts:

- `[a-zA-Z0-9.+_-]+` is the beginning of the email address before the at `@` character. So the "name" in "name@example.com".
- `[a-zA-Z0-9.-]+` is the first part of the domain. So the "example" in "name@example.com".
- `[a-zA-Z.-]+` is the last part of the domain. So the "com" in "name@example.com".

{% endraw %}

#### How do I filter for email addresses associated to a specific domain?

Say you want to filter for emails ending with "@braze.com". You would use the email address filter, set it to `matches regex`, and enter "@braze.com" in the regex field. The same applies for any other email domain.

![Filter for an email address that matches regex of "@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})

#### How can I use filter number strings for values ≥ x or ≤ x?

If you're searching for values greater than or equal to (≥) x, use the following regex:

```
^([x-y]|\d{z,})$
```

Where `x-y` is the range of numbers (0-9) of the first digit, and `z` is the one more the number of digits of x. For example, for values greater than or equal to 50, the regex would then be `^([5-9][0-9]|\d{3,})$`.

If you're searching for values less than or equal to (≤) x, use the following regex:

```
^([x-y]|[a-b])$
```

Where `x-y` is the range of numbers (0-9) of the first digit, and `a-b` is the lower bound range of x. For example, for values less than or equal to 50, the regex would then be `^([5-9][0-9]|[0-4][0-9])$`.

#### How do I filter custom attributes that start with a specific string?

Use the caret symbol (`^`) to denote what the string starts with, then enter the name of the custom attribute you want to specify.

For example, if you're trying to target users who live in cities that start with "San", your regex would be `^San \w`. With this regex, you would successfully target users from cities like San Francisco, San Diego, San Jose, and so on.

![Filter for a city that matches regex of "^San \w".]({% image_buster /assets/img/regex/regeximg2.png %})

#### How do I filter for specific phone numbers?

Before using regex to filter phone numbers, remember that numbers logged for user profiles must be in [E.164](https://en.wikipedia.org/wiki/E.164) format, as specified in [User phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/).

Assuming you're searching for US phone numbers, use the regex format `1?\d\d\d\d\d\d\d\d\d\d`, where each repetition of `\d` is a digit you want to specify. The first three digits are the area code.

Likewise, the format for UK phone numbers is `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Any other country would be the the respective country code, followed by the necessary number of `\d` repetitions for each remaining digit. So in the case of Lithuania with a country code of "3", their regex would be `^\+3\d\d\d\d\d\d\d\d\d\d`.

For example, let's say you wanted to filter users by phone number for a specific area code, "718". Use the phone number filter, set it to `matches regex`, and enter the following regex:

```
^1?718\d\d\d\d\d\d\d
```

![Filter for a phone number that matches regex of "^1?718\d\d\d\d\d\d\d".]({% image_buster /assets/img/regex/regeximg3.png %})


