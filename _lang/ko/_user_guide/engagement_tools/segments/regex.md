---
nav_title: "정규표현식"
article_title: 정규표현식
page_order: 10

description: "이 참조 문서에서는 정규식(정규식)이 무엇인지, 정규식 사용을 시작하는 방법, 정규식의 유효성을 검사하고 테스트하는 디버거 기능에 대해 설명합니다."
page_type: reference
tool:
  - Testing Tools
  
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/regular-expression-basics-for-braze){: style="float:right;width:120px;border:0;" class="noimgborder"} 정규표현식

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> 일반적으로 정규식으로 알려진 정규표현식은 검색 패턴을 정의하는 문자 시퀀스입니다. 정규표현식을 사용하면 텍스트 그룹화의 유효성을 검사하고 찾기 및 바꾸기 작업을 수행할 수 있습니다. Braze에서는 정규표현식을 활용하여 타겟팅 오디언스를 위한 세분화 및 캠페인 필터링에서 보다 유연한 문자열 매칭 솔루션을 제공합니다.<br><br>이 페이지에서는 정규식(정규식)과 사용 방법, 자주 묻는 질문을 다루고 정규식을 테스트할 수 있는 정규식 디버거를 제공합니다.

링크된 Braze 학습 과정에서는 [Regex101에서](https://regex101.com/) 정규표현식을 어떻게 사용하고 테스트할 수 있는지 보여드립니다. 또한 [사내 정규식 테스터](#regex-debugger), 유용한 참조 페이지, 정규식 학습 동영상에 참조된 샘플 데이터, 자주 묻는 질문도 제공합니다.

## 리소스

- [정규표현식 기초](https://learning.braze.com/regular-expression-basics-for-braze) Braze 학습 과정
- [정규식 치트 시트]({{site.baseurl}}/regex_cheat_sheet/)
- [샘플 데이터 RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})

## 정규식 디버거

{% alert important %}
이 도구는 참고용으로만 제공되며 정규식이 Braze 플랫폼과 100% 일치한다는 보장은 없습니다. 세분화 및 필터를 위한 Braze의 정규표현식은 `/gi` 수정자를 자동으로 추가합니다. [gi 수정자는](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm) 문자열에서 대소문자를 구분하지 않고 정규표현식이 포함된 모든 항목을 검색하는 데 사용됩니다.  
<br>
커스텀 이벤트 속성정보 및 트리거 필터에 대한 정규표현식은 `/g` 수정자(대소문자 구분, [g 수정자](https://www.w3schools.com/jsref/jsref_regexp_g.asp) 참조)를 사용하며 `/i` 수정자는 사용하지 않습니다. 커스텀 이벤트 속성정보 및 트리거 필터에 대/소문자를 구분하지 않으려면 `(?i)` 을 대신 사용하세요. 예를 들어 `Matches regex (?i)STOP(?-i)` 은 'STOP'의 모든 사용 사례(예: "중지", "제발 중지", "메시지 전송을 멈추지 마세요")를 포착합니다.
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
이 양식을 사용하면 정규표현식에 대한 기본적인 유효성 검사 및 테스트를 수행할 수 있습니다.
​
정규식:
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="정규식" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
값을 확인합니다: <textarea style="" placeholder="문자열 일치" id="regex_text"></textarea><br /><br />
​
일치하는 결과<span id="reg_count"></span>: <div id="regex_results"></div>
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

## 자주 묻는 질문

#### `does not match regex` 필터에 빈 값이 포함되어 있나요?

값이 비어 있으면 해당 사용자는 `does not match regex` 필터에 포함되지 않습니다.

#### 세그먼트를 세분화할 때 받은편지함별 이메일 주소를 필터링하려면 어떻게 해야 하나요?

{% raw %}
이메일 주소 필터를 사용하여 `matches regex` 로 설정합니다. 그런 다음 이메일 주소에 대한 정규식을 참조하세요:

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

이 정규식은 다음 세 부분으로 나눌 수 있습니다:

- `[a-zA-Z0-9.+_-]+` 는 이메일 주소의 시작 부분에 `@` 문자를 추가합니다. 따라서 "name@example.com"의 "이름"입니다.
- `[a-zA-Z0-9.-]+` 는 도메인의 첫 번째 부분입니다. 따라서 "name@example.com"의 "예"는 다음과 같습니다.
- `[a-zA-Z.-]+` 는 도메인의 마지막 부분입니다. 따라서 "name@example.com"의 "com".

{% endraw %}

#### 특정 도메인에 연결된 이메일 주소를 필터링하려면 어떻게 해야 하나요?

"@braze.com"로 끝나는 이메일을 필터링하고 싶다고 가정해 보겠습니다. 이메일 주소 필터를 사용하여 `matches regex` 로 설정하고 정규식 필드에 "@braze.com"을 입력합니다. 다른 이메일 도메인도 마찬가지입니다.

"@braze.com"의 정규식과 일치하는 이메일 주소로 필터링합니다.]({% image_buster /assets/img/regex/regeximg1.png %})

#### ≥ x 또는 ≤ x 값에 필터 번호 문자열을 사용하려면 어떻게 해야 하나요?

(≥) x보다 크거나 같은 값을 검색하는 경우 다음 정규식을 사용합니다:

```
^([x-y]|\d{z,})$
```

여기서 `x-y` 은 첫 번째 자리의 숫자 범위(0~9)이고 `z` 은 x의 자릿수 중 하나 더 많은 자리입니다. 예를 들어 50보다 크거나 같은 값의 경우 정규식은 `^([5-9][0-9]|\d{3,})$` 이 됩니다.

(≤) x보다 작거나 같은 값을 검색하는 경우 다음 정규식을 사용합니다:

```
^([x-y]|[a-b])$
```

여기서 `x-y` 은 첫 번째 자리의 숫자 범위(0~9)이고 `a-b` 은 x의 하한 범위입니다. 예를 들어 50보다 작은 값의 경우 정규식은 `^([5-9][0-9]|[0-4][0-9])$` 이 됩니다.

#### 특정 문자열로 시작하는 커스텀 속성을 필터링하려면 어떻게 해야 하나요?

캐럿 기호(`^`)를 사용하여 문자열의 시작 부분을 표시한 다음 지정하려는 커스텀 속성의 이름을 입력합니다.

예를 들어, "San"으로 시작하는 도시에 거주하는 사용자를 타겟팅하려는 경우 정규식은 `^San \w` 입니다. 이 정규식을 사용하면 샌프란시스코, 샌디에이고, 산호세 등의 도시에서 온 사용자를 성공적으로 타겟팅할 수 있습니다.

"^산 \\w"의 정규식과 일치하는 도시를 필터링합니다.]({% image_buster /assets/img/regex/regeximg2.png %})

#### 특정 전화번호를 필터링하려면 어떻게 하나요?

정규식을 사용하여 전화번호를 필터링하기 전에 고객 프로필에 기록된 전화번호는 사용자 전화번호에 지정된 [E.164](https://en.wikipedia.org/wiki/E.164) 형식이어야 합니다( [사용자 전화번호에]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) 지정된 대로).

미국 전화번호를 검색한다고 가정할 때 정규식 형식 `1?\d\d\d\d\d\d\d\d\d\d` 을 사용하며, 여기서 `\d` 의 각 반복은 지정하려는 숫자입니다. 처음 세 자리는 지역 코드입니다.

마찬가지로 영국 전화번호의 형식은 `^\+4\d\d\d\d\d\d\d\d\d\d\d` 입니다. 다른 국가는 해당 국가 코드를 입력한 후 나머지 숫자마다 필요한 `\d` 반복 횟수를 입력합니다. 따라서 국가 코드가 "3"인 리투아니아의 경우 정규식은 `^\+3\d\d\d\d\d\d\d\d\d\d` 입니다.

예를 들어 특정 지역 번호인 '718'의 전화번호로 사용자를 필터링한다고 가정해 보겠습니다. 전화번호 필터를 사용하여 `matches regex` 로 설정하고 다음 정규식을 입력합니다:

```
^1?718\d\d\d\d\d\d\d
```

\![정규식 "^1?718\\d\\d\\d\\d\\d\\d\\d"와 일치하는 전화번호를 필터링합니다.]({% image_buster /assets/img/regex/regeximg3.png %})


