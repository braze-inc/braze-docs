---
nav_title: 条件付きメッセージング・ロジック
article_title: 条件付きリキッドメッセージ・ロジック
page_order: 6
description: "この参考記事では、キャンペーンでタグをどのように使用できるか、また使用すべきかについて解説している。"

---

# 条件付きメッセージング・ロジック

> [タグ](https://docs.shopify.com/themes/liquid-documentation/tags)を使用すると、メッセージングキャンペーンにプログラミングロジックを含めることができます。タグは、条件付きステートメントの実行や、変数の代入やコードブロックの反復のような高度なユースケースにも使用できます。<br><br>このページでは、null、nil、空白の属性値をどのように考慮するか、カスタム属性をどのように参照するかなど、タグをどのように使用できるか、また使用すべきかを説明する。

## タグのフォーマット

{% raw %}
タグは `{% %}` で囲む必要があります。
{% endraw %}

あなたの生活を少し楽にするために、Brazeはリキッド構文を正しくフォーマットした場合、緑と紫で起動するカラーフォーマットを搭載している。緑色の書式はタグを識別するのに役立ち、紫色の書式はパーソナライズされた部分を強調する。

もし条件付きメッセージングを使うのに苦労しているなら、カスタム属性や他のリキッド要素を挿入する前に、条件構文を書き出してみてほしい。

例えば、まずメッセージ・フィールドに以下を追加する：  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

緑色で強調表示されることを確認し、`X` を選択した Liquid またはコネクテッドコンテンツに置き換えて、メッセージフィールドの隅にある青色の `+` を使用して `0` を希望する値に置き換えます。
<br><br>
そして、`else` の条件文の間に、必要に応じてメッセージのバリエーションを追加する：
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## 条件論理

[インテリジェントロジックの多くのタイプを、条件文などのメッセージ](http://docs.shopify.com/themes/liquid-documentation/basics)内に含めることができます。次の例では、[conditionals](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) を使用してキャンペーンを国際化します。
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### 条件付きタグ

#### `if` と `elsif`

条件付きロジックは、`if` タグで始まり、最初にチェックする条件を示します。後続の条件は `elsif` タグを使用し、前の条件が満たされない場にチェックされます。この例では、ユーザーのデバイスが英語に設定されていない場合、このコードは、ユーザーのデバイスがスペイン語に設定されているかどうかを確認し、それが失敗した場合は、デバイスが以下に設定されているかどうかを確認します。ユーザーのデバイスがこれらの条件のいずれかに当てはまる場合、ユーザーは該当する言語でメッセージを受け取る。

#### `else`

条件ロジックにはオプションで `{% else %}` ステートメントを含めることができます。設定した条件のどれにも当てはまらない場合、`{% else %}` ステートメントによって送信すべきメッセージが指定されます。この例では、ユーザーの言語が英語、スペイン語、中国語でない場合、デフォルトは英語になります。

#### `endif`

`{% endif %}` タグは、条件ロジックが終了したことを知らせます。条件付きロジックを含むメッセージには `{% endif %}` タグを必ず含める必要があります。条件ロジックに`{% endif %}` タグを含めないと、Brazeがメッセージを解析できないのでエラーになる。

{% alert note %}
条件タグ（`if`, `elsif`, `unless`）は演算子をサポートするが、フィルターはサポートしない。条件式内でフィルター処理された値を評価するには、まずフィルター結果を変数に代入し、その変数を参照するのだ。詳細については、[演算子とフィルターの使用箇所を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters)参照せよ。
{% endalert %}

### チュートリアル: 位置情報コンテンツの配信

このチュートリアルを完了すると、"if"、"elsif"、および"else"ステートメントを含むタグを使用して、ユーザーの場所に基づいてコンテンツを配信できるようになります。

1. 最初に `if` タグを使用して、ユーザーの市区町村がニューヨークにある場合に送信するメッセージを指定します。ユーザーの市区町村がニューヨークの場合、この最初の条件が満たされ、ユーザーはニューヨーカーのアイデンティティを指定するメッセージを受け取ります。

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\.次に、`elseif` タグを使用して、ユーザーの市区町村がロサンゼルスにある場合に送信するメッセージを設定します。

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\.別の`elseif` タグを使用して、ユーザーの市区町村がシカゴにある場合に送信するメッセージを設定します。

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\.次に、`{% else %}` タグを使用して、ユーザーの市区町村がサンフランシスコ、ニューヨーク、シカゴにない場合に送信するメッセージを指定します。

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\.最後に、`{% endif %}` タグを使用して、条件付きロジックが実行されるように指定します。

```liquid
{% endif %}
```

{% endraw %}

{% details Full Liquid code %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at our New York location. 
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## null、nil、および空白の属性値を処理する

条件ロジックは、ユーザープロファイルに設定されていない属性値を考慮するのに便利な方法である。

### NULL および NIL 属性値

NULLまたはnil値は、カスタム属性の値が設定されていない場合に発生する。例えば、まだ名を設定していないユーザーは、Braze に名が記録されません。

状況によっては、姓を設定しているユーザーと設定していないユーザーとで、まったく異なるメッセージを送りたい場合もあるだろう。

以下のタグは、「first name」属性が NULL のユーザーに対するメッセージを指定することができます。

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

![ヌルの'first name' 属性を使用した、Braze ダッシュボードのメッセージ例。]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

NULL の属性値は、値型と厳密には関連付けられていないことに注意してください (例えば、「null」の string は「null」 の array と同じです)。そのため、上記の例では、NULL 属性値が未設定の名 (文字列) を参照しています。

{% endraw %}

### 空白の属性値

空白の値は、ユーザープロファイルで属性が設定されていないか、空白文字列 (` `) が設定されているか、`false` として設定されている場合に発生します。Liquid の処理エラーを避けるため、空白値は他の変数より先にチェックするようにします。

以下のタグは、「first name」属性が空白のユーザーに対するメッセージを指定することができます。

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## カスタム属性を参照する

[で作成したカスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)を使用すると、Liquidメッセージングでこれらのカスタム属性を参照できます。

条件付きロジックを使用する場合、正しい構文を使用していることを確認するために、カスタム属性のデータ型を知っておく必要がある。ダッシュボードの**カスタム属性**ページから、カスタム属性に関連するデータタイプを探し、各データタイプに記載されている以下の例を参照する。

![カスタム属性のデータ型を選択する。提供された例は、データ型Favorite_Categoryが文字列である属性を示している。]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
文字列と配列には一重引用符が必要ですが、ブール値と整数には必要ありません。
{% endalert %}

#### ブール値

[Booleans]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) はバイナリ値で、`true` または`false` のいずれかに設定できます(`registration_complete: true` など)。ブール値にはアポストロフィは付かない。

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### 数値

[数値]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers)は、整数または浮動小数点数の数値です。たとえば、ユーザーには `shoe_size: 10` や `levels_completed: 287` などの属性があります。数値にはアポストロフィは付かない。

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

整数に対しては、より小さい（(<)<）やより大きい（>）といった他の[基本的な演算子](https://shopify.dev/docs/themes/liquid/reference/basics/operators)も使える。

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### string

[string]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) は英数字で構成され、ユーザーに関するデータを保存します。例えば、`favorite_color: red` や `phone_number: 3025981329` などです。文字列の値にはアポストロフィをつけなければならない。

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

文字列の場合、Liquidでは"=="と "contains "の両方を使うことができる。

#### 配列

[array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays)は、ユーザーに関する情報のリストです。例えば、ユーザーには `last_viewed_shows: stranger things, planet earth, westworld` などの属性があります。配列の値はアポストロフィで囲む必要がある。

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

配列の場合、"contains "を使わなければならず、"=="は使えない。 

#### 時刻

イベントが発生した時刻のタイムスタンプ。[Time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) 値は、条件付きロジックで使用するために[math フィルタ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) を持つ必要があります。

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


