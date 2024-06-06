---
nav_title: オペレーター
article_title: リキッドオペレーター
page_order: 2
description: "このリファレンスページでは、Liquid がサポートしている演算子と、関連する例を示します。"

---

# オペレーター

Liquidは、条件文で使用できる多くの[演算子][25]をサポートしています。

| 構文|演算子の説明
|---------|-----------|
| ==  | 等しい        |
| !=  | 一致しない|
|  >  | より大きい  |
未満 (過去)
| を超えるか等しいか。
| 以下である。
| 条件Aまたは条件B
| 条件Aと条件B
| 文字列または文字列配列が文字列を含むかどうかをチェックする。
{: .reset-td-br-1 .reset-td-br-2}

## オペレーターの例

ここでは、これらのオペレータがマーケティングキャンペーンにどのように役立つかの例をいくつか紹介する：

### 整数カスタム属性でメッセージを選択

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

この例では、顧客の "Total Spend "カスタム属性が`0` より大きい場合、その顧客はメッセージを受け取ります：

```
Thanks for purchasing! Here's another 10% off!
```
もし顧客の "Total Spend "カスタム属性が存在しないか、`0` と等しい場合、以下のメッセージが表示されます：

```
Buy now! Would 5% off convince you?
```

### 文字列カスタム属性でメッセージを選択

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == 'Game1' %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == 'Game2' %}
You played our other Game! Woop!{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

この例では、あるゲームをプレイした場合、次のようなメッセージが表示されます：

```
You played our Game! We're so happy!
```

他の指定された試合に出場した場合：

```
You played our other Game! Woop!
```

ゲームをプレイしていないか、プロフィールにカスタム属性が存在しない場合、次のようなメッセージが表示されます：

```
Hey! Get in here and play this Game!
```

### 位置情報に基づく中止メッセージ

あらゆることに基づいてメッセージを中止することができる。次の例では、ユーザーが指定された地域に住んでいない場合、プロモーション、ショー、または配信の資格がない可能性があるため、メッセージを中止する方法を示しています。

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

また、Connected Content に基づいて[メッセージを中止][1]することもできます。


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
