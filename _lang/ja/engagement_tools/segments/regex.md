---
nav_title: "正規表現"
article_title: 正規表現
page_order: 10

description: "この参考記事では、正規表現（regex）とは何か、どのように正規表現を使い始めるか、そして正規表現を検証しテストするためのデバッガー機能を提供しています。"
page_type: reference
tool:
  - Testing Tools
  
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})({: style="float:right;width:120px;border:0;" class="noimgborder"})](https://learning.braze.com/regular-expression-basics-for-braze)正規表現

<!--{% multi_lang_include video.html id="3h5Xbhl-TxE" align="right" %}-->

> 正規表現は、一般に「regex」として知られ、検索パターンを定義する文字のシーケンスです。正規表現では、テキストのグループ化を検証し、検索と置換を実行できます。Braze では、正規表現を活用し、ターゲットのセグメンテーションやキャンペーンのフィルタリングにおいて、より柔軟な文字列マッチングソリューションを提供します。<br><br>このページでは、正規表現(regex)、その使用方法、よくある質問、正規表現をテストするための正規表現デバッガーについて説明します。

リンク先の Braze Learning コースでは、[Regex101](https://regex101.com/) で正規表現がどのように使用され、テストされるかを紹介しています。また、[社内の正規表現テスター](#regex-debugger)、役立つ参考ページ、正規表現 Braze ラーニングビデオで参照されているサンプルデータ、よくある質問も提供しています。

## リソース

- [正規表現の基礎](https://learning.braze.com/regular-expression-basics-for-braze) Braze ラーニングコース 
- [正規表現チートシート]({{site.baseurl}}/regex_cheat_sheet/)
- [サンプルデータ RTF]({% image_buster /assets/download_file/regex-dummy-data.rtf %})()

## 正規表現デバッガー

{% alert important %}
このツールはあくまで参考であり、正規表現が Braze プラットフォーム と100% 一致することを保証するものではありません。Braze のセグメンテーションおよびフィルタの正規表現では、`/gi` 修飾子が自動的に追加されます。[gi 修飾子](https://w3schools.sinsixx.com/jsref/jsref_regexp_modifier_gi.asp.htm)は、文字列中に出現する正規表現を大文字小文字を区別せずに検索するために使われます。  
<br>
カスタムイベントトリガープロパティおよびトリガーフィルタの正規表現では、`/g` 修飾子(大文字と小文字の区別あり。[g 修飾子](https://www.w3schools.com/jsref/jsref_regexp_g.asp) を参照)を使用し、`/i` 修飾子は使用しません。カスタムイベントトリガープロパティとトリガーフィルタの大文字と小文字を区別しない場合は、代わりに`(?i)` を使用します。例えば `Matches regex (?i)STOP(?-i)` は、いずれの場合 (「stop」、「please stop」および「never stop sending me messages」) でも「STOP」の使用を検出します。
{% endalert %}

{% tabs %}
{% tab Regex Debugger %}
<div>
このフォームでは、基本的な検証と正規表現のテストを行うことができます。
​
正規表現:
​
<div class="input-group">
  <div class="input-group-prepend"><span class="input-group-text">/</span>
  </div>
 <input id="regex_input" value="" class="form-control" placeholder="regex" style="" />
 <div class="input-group-append"><span class="input-group-text">/gi</span>
 </div>
</div>
<br />
値をチェック: <textarea style="" placeholder="マッチ文字列" id="regex_text"></textarea><br /><br />
​
一致結果<span id="reg_count"></span>:<div id="regex_results"></div>
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

## よくある質問

#### `does not match regex` フィルターは空白値を含みますか？

いいえ。値が空白の場合、そのユーザーは `does not match regex` フィルターに含まれません。

#### セグメンテーションの際、受信トレイ固有のメールアドレスをフィルタリングするにはどうすればよいですか？

{% raw %}
メールアドレスフィルターを使い、`matches regex` に設定します。次に、メールアドレスの正規表現を参照します: 

```
[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]+
```

この正規表現は以下の 3 つの部分に分解できます:

- `[a-zA-Z0-9.+_-]+` はメールアドレスの先頭で、その後アットマーク `@` が続きます。つまり、"name@example.com"の "name "である。
- `[a-zA-Z0-9.-]+` はドメインの最初の部分です。つまり、「name@example.com 」の「例」ということになる。
- `[a-zA-Z.-]+` はドメインの最後の部分です。つまり、「name@example.com 」の「com」である。

{% endraw %}

#### 特定のドメインに関連するメールアドレスをフィルタリングする方法を教えてください。

例えば、"@braze.com" で終わるメールをフィルタリングしたいとする。メールアドレスフィルターを使用して `matches regex` に設定し、正規表現フィールドに「@braze.com」と入力します。他のメールドメインでも同様です。

!["@braze.com".]({% image_buster /assets/img/regex/regeximg1.png %})()の正規表現に一致するメールアドレスのフィルタ

#### 値 ≥x または ≤x の場合、フィルターの番号文字列はどのように使用できますか？

(≥) x 以上の値を検索する場合は、以下の正規表現を使います:

```
^([x-y]|\d{z,})$
```

ここで、`x-y` は最初の桁の数字（0～9）の範囲であり、`z` は x の桁数以上の数字です。例えば、50 以上の値の場合、正規表現は`^([5-9][0-9]|\d{3,})$` になります。

(≤) x 以下の値を検索する場合は、以下の正規表現を使います:

```
^([x-y]|[a-b])$
```

ここで、`x-y` は 1 桁目の数字（0～9）の範囲、`a-b` は x の下限範囲です。たとえば、50以下の値の場合、正規表現は`^([5-9][0-9]|[0-4][0-9])$`になります。

#### 特定の文字列で始まるカスタム属性をフィルタリングするには？

キャレット記号 (`^`) で文字列の先頭を表し、指定したいカスタム属性名を入力します。

例えば、"San" で始まる都市に住むユーザーをターゲットにする場合、正規表現は `^San \w` とします。この正規表現を使えば、サンフランシスコ、サンディエゴ、サンノゼなどの都市のユーザーをターゲットにできます。

![正規表現「^San \\w」に一致する市区町村のフィルター。]({% image_buster /assets/img/regex/regeximg2.png %})()

#### 特定の電話番号をフィルタリングする方法を教えてください。

正規表現を使用して電話番号をフィルター処理するには、ユーザープロファイルに記録されている番号が、「[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)」で指定されているように、[E.164](https://en.wikipedia.org/wiki/E.164) 形式でなければいけません。

米国の電話番号を検索すると仮定すると、正規表現フォーマット `1?\d\d\d\d\d\d\d\d\d\d` を使用します。`\d` の各繰り返しは、指定したい桁数です。最初の 3 桁は市外局番です。

同様に、英国の電話番号の書式は `^\+4\d\d\d\d\d\d\d\d\d\d\d` です。その他の国は、それぞれの国番号の後に、残りの各桁について必要な数の `\d` を繰り返します。つまり、国番号が "3" のリトアニアの場合、正規表現は `^\+3\d\d\d\d\d\d\d\d\d\d` になります。

例えば、特定の市外局番 "718" の電話番号でユーザーをフィルタリングしたいとします。電話番号フィルターを使い、`matches regex` に設定し、以下の正規表現を入力します: 

```
^1?718\d\d\d\d\d\d\d
```

![正規表現「^1?718\\d\\d\\d\\d\\d\\d\\d」に一致する電話番号のフィルター。]({% image_buster /assets/img/regex/regeximg3.png %})()


