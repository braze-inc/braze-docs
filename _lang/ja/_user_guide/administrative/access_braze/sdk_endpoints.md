---
nav_title: API と SDK のエンドポイント
article_title: API と SDK のエンドポイント
page_order: 1
page_type: reference
description: "このリファレンス記事には、利用可能な Braze インスタンスのダッシュボード URL、API エンドポイント、SDK エンドポイントの一覧があります。"

---

# API と SDK のエンドポイント

> Braze インスタンスにより、Braze へのログイン、API へのアクセス、および SDK の連携に必要な URL が決まります。Braze SDK の詳細については、Braze ラーニングコース「[Braze 101](https://learning.braze.com/braze-101)」を参照してください。

Braze は、ダッシュボード、SDK、REST エンドポイントのさまざまなインスタンスを管理しており、これを「クラスター」と呼びます。Braze のオンボーディングマネージャーが、あなたの所属するクラスターを通知します。

[dashboard.braze.com](https://dashboard.braze.com) にログインすると、自動的に適切なクラスターアドレスに移動します。

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
SDK を連携する場合は、SDK エンドポイントを使用してください。REST API を呼び出す場合は、REST エンドポイントを使用してください。
{% endalert %}

APIへのアクセスの詳細については、[APIの概要記事を]({{site.baseurl}}/api/basics/)参照のこと。 
