---
nav_title: テンプレート カタログ アイテム 含む Liquid
article_title: テンプレート カタログ アイテム 含む Liquid
permalink: "/templating_catalog_items_liquid/"
description: "Liquid を含むカタログアイテムをテンプレート化する方法を学びます。"
page_type: reference
hidden: true
---

# Liquidを含むカタログアイテムのテンプレート化

 [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)と同様に、Liquidコンテンツをレンダリングするには、Liquidタグに`:rerender`フラグを含める必要があります。`:rerender` フラグは1レベルのみであるため、ネストされたLiquidタグ呼び出しには適用されません。

 {% alert important %}
 Liquidを含むカタログアイテムのテンプレート化は早期アクセス中です。早期アクセスに参加したい場合は、Brazeのアカウントマネージャーにお問い合わせください。
 {% endalert %}

カタログアイテムにユーザープロファイルフィールド（Liquidパーソナライゼーションタグ内）が含まれている場合、Liquidを適切にレンダリングするために、テンプレート化の前にLiquidを介してメッセージ内でこれらの値を事前に定義する必要があります。`:rerender` フラグが提供されていない場合、生のLiquidコンテンツがレンダリングされます。

例えば、「メッセージ」という名前のカタログにこのLiquidを含むアイテムがある場合:

![][15]{: style="max-width:80%;"}<br>

次のLiquidコンテンツをレンダリングするには:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

これは次のように表示されます:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
カタログ Liquid タグはカタログ内で再帰的に使用することはできません。
{% endalert %}

[15]: {% image_buster /assets/img_archive/catalog_liquid_templating.png %}
