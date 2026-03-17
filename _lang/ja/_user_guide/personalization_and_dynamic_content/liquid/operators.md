---
nav_title: 演算子
article_title: Liquid の演算子
page_order: 2
description: "このリファレンスページでは、Liquid がサポートする演算子と関連する例について説明します。"

---

# 演算子

> Liquid は、条件文で使用できる多くの[演算子](https://docs.shopify.com/themes/liquid/basics/operators)をサポートしています。このページでは、Liquidがサポートしているオペレータをカバーし、メッセージングでそれらをどのように使用できるかのユースケースを提供する。

この表は、サポートされている演算子の一覧である。かっこはLiquidでは無効な文字であり、タグが機能しなくなることに注意せよ。

|   構文| オペレータの説明|
|---------|-----------|
| ==  | 等しい        |
| !=  | 等しくない|
|  >  | より大きい  |
| <   | 未満     |
| >=| 以上|
| <= | 以下 |
| または | 条件Aまたは条件B|
| および | 条件 A および条件 B|
| 含む | 文字列または文字列配列に文字列が含まれているかどうかを調べる|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
演算子は条件式（`if`, `elsif`, `unless`）では使用できるが、`assign`  文、`for`  ループ、 `case`/`when` 文、または配列アクセス括弧では使用できない。詳細な説明については、[「演算子とフィルターの使用場所」]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters)を参照のこと。
{% endalert %}

### かっこを使わない条件のグループ化

Liquidは式をグループ化するためのかっこをサポートしていない。複雑なブール論理式を評価するには、ネストした`if`条件`(a and b) or c`式や中間変数を使うこと。

例えば、値が複合条件を満たすかどうかを確認するには、中間変数を割り当てる：

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## チュートリアル

いくつかのチュートリアルを通して、マーケティングキャンペーンにこれらのオペレーターを使う方法を学んでいこう：

### 整数のカスタム属性を持つメッセージを選ぶ

購入したユーザーまたは購入していないユーザーに、パーソナライズされたプロモーション割引を含むプッシュ通知を送信しましょう。プッシュ通知では、`total_spend` という整数のカスタム属性を使用して、ユーザーの合計金額をチェックします。

1. greater than (`>`) 演算子を使用して条件文を書き、ユーザーの合計金額が`0` より大きいかどうかをチェックします。これは、ユーザーが購入したことを示します。次に、これらのユーザーに送信するメッセージを作成します。

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\.{% raw %}`{% else %}`{% endraw %} タグを追加し、合計金額が `0` と等しいか、存在しないユーザーをキャプチャします。次に、これらのユーザーに送信するメッセージを作成します。

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\.{% raw %}`{% endif %}`{% endraw %} タグで条件ロジックを閉じる。

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![チュートリアルの完全なLiquidコードを含むプッシュ通知コンポーザー。]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

ユーザーのカスタム属性「総支出額」が より大きい場合、そのユーザーには`0`次のメッセージが表示される：

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
もしユーザーの "Total Spend "カスタム属性が存在しなかったり、`0` と等しい場合、以下のメッセージが表示される：

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### 文字列のカスタム属性を持つメッセージを選ぶ

ユーザーにプッシュ通知を送り、各ユーザーが最近プレイしたゲームに基づいてメッセージをパーソナライズさせよう。これは、`recent_game` という文字列カスタム属性を使用して、ユーザーが最後にプレーしたゲームをチェックします。

1. 等号 (`==`) 演算子を使った条件文を書き、ユーザーの最近のゲームが*「Awkward Dinner Party*」であるかどうかをチェックする。次に、これらのユーザーに送信するメッセージを作成します。

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\.`elsif` タグと equals (`==`) 演算子を使用して、ユーザーの最新のゲームが*Proxy War 3 であるかどうかをチェックする：War of Thirst』*のフィードバックを測定する。次に、これらのユーザーに送信するメッセージを作成します。

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\.\``elsif`<?php?>`タグと「不等号」`!=`()および「AND」`and`()演算子を使って、ユーザーが最近のゲームを持っているか（つまり値が空白でないか）、そしてそのゲームが*『気まずいディナーパーティー*』や*『代理戦争3』でないかを確認する。War of Thirst』*のフィードバックを測定する。次に、これらのユーザーに送信するメッセージを作成します。

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\.最近のゲームを持っていないユーザーをキャプチャするには{% raw %}`{% else %}`{% endraw %} タグを追加します。次に、これらのユーザーに送信するメッセージを作成します。

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\.{% raw %}`{% endif %}`{% endraw %} タグで条件ロジックを閉じる。

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![チュートリアルの完全なLiquidコードを含むプッシュ通知コンポーザー。]({% image_buster /assets/img/liquid-if-elsif-games.png %})

さて、ユーザーが最後に『*Awkward Dinner Party*』をプレイした場合、このようなメッセージが表示される：

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

ユーザーの直近のゲームが*Proxy War 3の場合：War of Thirst* 、彼らはこのメッセージを受け取ります：

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

ユーザーが最近プレイしたゲームが*『気まずい晩餐会*』や『*代理戦争3』でない場合：War of Thirst*、彼らはこのメッセージを受け取ります：

```
Limited Time Deal! Get 15% off our best-selling classics!
```

もしユーザーがゲームをプレイしていなかったり、そのカスタム属性がプロファイルに存在しなかったりすると、このメッセージが表示される：

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### 位置に基づいてメッセージをアボートする

あらゆる条件に基づいてメッセージを中止することができます。ユーザーが指定された地域に住んでいない場合、プロモーションやショー、配信の対象にならない可能性があるため、メッセージを中止しよう。

1. equals (`==`) 演算子を使った条件文を書いて、ユーザーのタイムゾーンが`America/Los_Angeles` かどうかをチェックし、それらのユーザーに送信するメッセージを作成する。 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\.`America/Los_Angeles` タイムゾーン外のユーザーへのメッセージの送信を避けるには、{% raw %}`{% else %}`{% endraw %} と{% raw %}`{% endif %}`{% endraw %} タグを{% raw %}`{% abort_message () %}`{% endraw %} タグで囲みます。

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![チュートリアルの完全なLiquidコードを含むプッシュ通知コンポーザー。]({% image_buster /assets/img/abort-if.png %})

また、接続コンテンツに基づいて[メッセージ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/)をアボートすることもできます。

## トラブルシューティング

### プレビューではプロパティの型が誤って変換されることがある 

ダッシュボードでメッセージをプレビューする際、ほとんどの場合、変数（カスタム属性など）は正しい型に変換される。ただし、一部の変数には、プレビューが参照できる明確な型が定義されていない。

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

これらのプロパティについては、プレビューは値から型を推測しようとする。これは、**文字列**として扱うべき値が誤って**数値**として解釈される可能性があることを意味する。例えば、プロパティの値が文字列の場合、プレビューはそれを`"3"`整数に変換する可能性がある。これにより、`+` や `contains`\`-\` `3`といった文字列操作で予期`split`しない動作が発生する恐れがある。

これらのプロパティタイプを使用中に予期しないプレビュー結果が表示された場合、プレビュー時の型推論が送信時の動作と一致しない可能性があることに留意せよ。送信時には、トリガーとなるイベントやAPI呼び出しからの実際のデータ型は保持される。

プレビューで特定の型を強制するには、値を明示的にキャストできる：

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}