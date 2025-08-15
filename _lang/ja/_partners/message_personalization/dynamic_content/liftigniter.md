---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "このリファレンス記事では、Braze と LiftIgniter のパートナーシップについて説明します。LiftIgniter は、業界をリードするパーソナライゼーションプラットフォームであり、企業によるカスタマーエクスペリエンスの変革を支援しています。"
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter は、業界をリードするパーソナライゼーションプラットフォームです。企業があらゆるタッチポイントでリアルタイムのパーソナライゼーションを行えるようにすることで、カスタマーエクスペリエンスの変革を支援しています。

_この統合は Liftigniter によって管理されます。_

## 統合について

LiftIgniterとBrazeインテグレーションは、Connected Contentを活用して、新聞記事、衣料品、他の小売 (店)アイテムや動画など、面白い話題をお勧めすることができます。

## 前提条件

| 必要条件| 説明|
| ---| ---|
| LiftIgniterアカウント | このパートナーシップを活用するには、[LiftIgniter アカウント](https://console.liftigniter.com/login)が必要です。 |
| LiftIgniter APIの統合 | ここからレコメンデーションを取得できるようにするには、LiftIgniter をサイトまたはアプリに[統合](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview)する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

[LiftIgniterのREST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389)を使用して、パーソナライズされた内容をメッセージに挿入します。LiftIgniter アカウントと LiftIgniter がアプリに統合されたら、次のテンプレートをメッセージ作成画面に追加して、必要に応じて情報を置き換えて (`x-api-key`、`theapikey` など)、メッセージにコンテンツを呼び出します。

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

次に、メッセージを記述し、JSON で呼び出すコンテンツを定義します。たとえば `{{json.items[0].title}}` です。

{% endraw %}

![LiftIgniter 固有のコネクテッドコンテンツ呼び出しを含むプッシュキャンペーン。画像フィールドにはコネクテッドコンテンツロジックも追加されている。][1]

このメッセージを作成画面の本文に入力すると、メッセージをプレビューできます。以下に示すように、画像を取得することもできます。

![送信後に表示されるメッセージのプレビュー画像。][2]


[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}