---
nav_title: 演算子
article_title: 液体事業者
page_order: 2
description: "このリファレンスページでは、Liquidがサポートする演算子と関連する例について説明します。"

---

# 演算子

Liquid は、条件文で使用できる多くの\[operators][25] をサポートしています。

|   構文| オペレータの説明|
|---------|-----------|
| ==  | 等しい        |
| !=  | 等しくない|
|  >  | より大きい  |
| その他   | 未満     |
| >=| 以上|
| ;&lt= | 以下 |
| または | 条件Aまたは条件B|
| および | 条件Aと条件B|
| 含む | 文字列または文字列配列に文字列が含まれているかどうかを調べる|
{: .reset-td-br-1 .reset-td-br-2}

## 演算子の例

以下に、これらの演算子がマーケティング キャンペーンs に役立つ例を示します。

### 整数カスタム属性で選択

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

この例題では、顧客の"Total Spend" カスタム属性 が`0` より大きい場合、次のメッセージが表示されます。

```
Thanks for purchasing! Here's another 10% off!
```
顧客の"Total Spend" カスタム属性が存在しないか、`0` と等しい場合、次のメッセージが表示されます。

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

この例では、特定のゲームをプレイした場合、次のメッセージが表示されます。

```
You played our Game! We're so happy!
```

別の指定されたゲームをプレイした場合:

```
You played our other Game! Woop!
```

ゲームをプレイしていない場合、またはそのカスタム属性がプロファイルに存在しない場合は、次のメッセージが表示されます。

```
Hey! Get in here and play this Game!
```

### 位置に基づいてメッセージをアボートする

何でもメッセージを中止することができます。次のサンプルは、ユーザーが指定された領域に基づいていない場合にメッセージをアボートする方法を示しています。これは、昇格、表示、または配信の対象外となる可能性があるためです。

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

また、接続コンテンツに基づいて[メッセージ][1]をアボートすることもできます。


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
