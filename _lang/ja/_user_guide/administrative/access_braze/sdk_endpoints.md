---
nav_title: API と SDK のエンドポイント
article_title: API と SDK のエンドポイント
page_order: 1
page_type: reference
description: "このリファレンス記事には、利用可能な Braze インスタンスのダッシュボード URL、API エンドポイント、SDK エンドポイントの一覧があります。"

---

# API と SDK のエンドポイント

> Braze インスタンスにより、Braze へのログイン、API へのアクセス、および SDK の連携に必要な URL が決まります。Braze SDK の詳細については、Braze ラーニングコース「[Braze 101][1]」を参照してください。

Braze は、ダッシュボード、SDK、REST エンドポイントのさまざまなインスタンスを管理しており、これを「クラスター」と呼びます。Braze のオンボーディングマネージャーが、あなたの所属するクラスターを通知します。

[dashboard.braze.com](https://dashboard.braze.com) にログインすると、自動的に適切なクラスターアドレスに移動します。

|インスタンス|URL|RESTエンドポイント|SDKエンドポイント|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
SDK を連携する場合は、SDK エンドポイントを使用してください。REST API を呼び出す場合は、REST エンドポイントを使用してください。
{% endalert %}

API へのアクセスの詳細については、「[API の概要][2]」の記事を参照してください。 


[1]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/