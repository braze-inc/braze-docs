---
nav_title: "Regular Expressions"
article_title: Regular Expressions
page_order: 5

description: "This reference article covers what regular expressions (regex) are, how to begin using them, and offers debugger functionality to validate and test regular expressions."
page_type: reference
tool:
  - Testing Tools
  
---

# Regular expressions with Braze

{% include video.html id="3h5Xbhl-TxE" align="right" %}

>  This reference article covers what regular expressions are, how to begin using them, and offers debugger functionality to validate and test regular expressions.

A regular expression, known commonly as a regex, is a sequence of characters that defines a search pattern. Regular expressions let you validate text groupings and perform find and replace actions. At Braze, we leverage regular expressions to give you a more flexible string matching solution in your segmentation and campaign filtering for your target audience.

In the provided video, we show you how regular expressions can be used and tested on [Regex101][regex]. Below we also offer an inhouse regex tester, a helpful cheatsheet, sample data referenced in the regex LAB video, as well as some frequently asked questions.

## Resources

- [Regular expression basics](https://lab.braze.com/regular-expression-basics-for-braze) LAB course
- <i class="fas fa-file-pdf"></i> [Regex Cheat Sheet][cheatsheet]
- <i class="fas fa-file-alt"></i> [Sample Data RTF][dummydata]

## Regex debugger

{% tabs %}
{% tab Regex Debugger %}

This form allows for basic validation and testing of regular expressions.
​
<div class="alert alert-important" role="alert"><div class="alert-msg"> <b>important: </b><br />
<p>This tool is only meant as a reference, and does not guarantee that the regex matches 100% with the Braze platform. Regular expressions in Braze automatically add the <code>gi</code> modifier. The <a href='https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm'>gi modifier</a> is used to do a case-insensitive search of all occurrences of a regular expression in a string. </p>
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
{% endtabs %}

## Frequently asked questions

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

![]({% image_buster /assets/img/regex/regeximg1.png %})

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

![]({% image_buster /assets/img/regex/regeximg2.png %})

#### How do I filter for specific phone numbers?

Before using regex to filter phone numbers, remember that numbers logged for user profiles must be in [E.164](https://en.wikipedia.org/wiki/E.164) format, as specified in [User phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/).

Assuming you're searching for US phone numbers, use the regex format `1?\d\d\d\d\d\d\d\d\d\d`, where each repetition of `\d` is a digit you want to specify. The first three digits are the area code.

Likewise, the format for UK phone numbers is `^\+4\d\d\d\d\d\d\d\d\d\d\d`. Any other country would be the the respective country code, followed by the necessary number of `\d` repetitions for each remaining digit. So in the case of Lithuania with a country code of "3", their regex would be `^\+3\d\d\d\d\d\d\d\d\d\d`.

For example, let's say you wanted to filter users by phone number for a specific area code, "718". Use the phone number filter, set it to `matches regex`, and enter the following regex:

```
^1?718\d\d\d\d\d\d\d
```

![]({% image_buster /assets/img/regex/regeximg3.png %})


[regex]: https://regex101.com/
[cheatsheet]: {% image_buster /assets/download_file/regex-cheatsheet.pdf %}
[dummydata]: {% image_buster /assets/download_file/regex-dummy-data.rtf %}
