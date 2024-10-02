---
nav_title: 液体を含むカタログアイテムのテンプレート作成
article_title: 液体を含むカタログアイテムのテンプレート作成
permalink: "/templating_catalog_items_liquid/"
description: "リキッドを含むアイテムをテンプレート カタログする方法について説明します。"
page_type: reference
hidden: true
---

# リキッドを含むカタログアイテムのテンプレート化

 [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) と同様に、`:rerender` フラグをLiquid タグに含めて、Liquid コンテンツをレンダリングする必要があります。`:rerender` フラグは1 レベルの深さしかないことに注意してください。つまり、入れ子になったリキッドタグ 呼び出しにはアプリされません。

 {% alert important %}
 「リキッド」を含むカタログ項目のテンプレート化は、初期段階で実行されます。早いアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。
 {% endalert %}

カタログアイテムにユーザープロファイル フィールドs(液体パーソナライゼーション タグ内)が含まれている場合、これらの値は、液体を適切にレンダリングするために、テンプレートの前に、液体を介してメッセージ内で事前に定義する必要があります。`:rerender` フラグが指定されていない場合、Raw Liquid コンテンツがレンダリングされます。

たとえば、"Messages"という名前のカタログに、このリキッドを含むアイテムがあるとします。

![][15]{: style="max-width:80%;"}<br>

以下のリキッドコンテンツをレンダリングするには:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

次のように表示されます。

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
カタログリキッドタグは、カタログs 内で再帰的に使用することはできません。
{% endalert %}

[15]: {% image_buster /assets/img_archive/catalog_liquid_templating.png %}
