---
nav_title: 液体を含むカタログアイテムのテンプレート作成
article_title: 液体を含むカタログアイテムのテンプレート作成
permalink: "/templating_catalog_items_liquid/"
description: "リキッドを含むアイテムをテンプレート カタログする方法について説明します。"
page_type: reference
hidden: true
---

# リキッドを含むカタログアイテムのテンプレート化

 [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) と同様に、`:rerender` フラグを Liquid タグに含めて、Liquid コンテンツをレンダリングする必要があります。`:rerender` フラグはレベル1の深さしかないことに注意してください。つまり、階層化 Liquid タグ 呼び出しには適用されません。

 {% alert important %}
 Liquid を含むカタログアイテムのテンプレート化は、早期アクセス段階です。早いアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。
 {% endalert %}

カタログアイテムにユーザープロファイルフィールド (Liquid パーソナライゼーションタグ内) が含まれている場合は、Liquid を適切にレンダリングするために、テンプレートの前に Liquid を使用してメッセージ内でこれらの値を事前に定義する必要があります。`:rerender` フラグが指定されていない場合、生の Liquid コンテンツがレンダリングされます。

たとえば、「Messages」という名前のカタログに、この Liquid を含むアイテムがあるとします。

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
