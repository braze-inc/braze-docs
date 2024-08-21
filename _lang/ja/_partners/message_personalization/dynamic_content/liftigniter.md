---
nav_title: リフトアイグナイタ
article_title: リフトアイグナイタ
alias: /partners/liftigniter/
description: "この参考文献では、企業がカスタマーエクスペリエンスを変革するのに役立つ、主要なパーソナライゼーション プラットフォームであるBrazeとリフトイグナイタの提携について概説する。"
page_type: partner
search_tag: Partner

---

# Liftigniter

> リフトイグナイタは主要なパーソナライゼーション プラットフォームであり、企業があらゆるタッチポイントにわたるリアルタイムのパーソナライゼーションを通じてカスタマーエクスペリエンスを変革するのに役立っています。

LiftIgniterとBrazeインテグレーションは、Connected Contentを活用して、新聞記事、衣料品、他の小売 (店)アイテムや動画など、面白い話題をお勧めすることができます。

## 前提条件

| 要件| 説明|
| ---| ---|
| LiftIgniterアカウント | この提携の前倒しタグを行うには、[LiftIgniterアカウント](https://console.liftigniter.com/login)が必要です。 |
| LiftIgniter APIの統合 | ここから推奨を引き出すには、[LiftIgniter をサイトまたはアプリに統合する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

[LiftIgniterのREST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389)を使用して、パーソナライズされた内容をメッセージに挿入します。LiftIgniterアカウントとLiftIgniterがアプリに統合されたら、次のテンプレートをメッセージ作成画面に追加して、必要に応じて情報を置き換えてメッセージにコンテンツを呼び出します(`x-api-key`、`theapikey`など)。

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

次に、メッセージを記述し、JSON で呼び出すコンテンツを定義します。たとえば、`{{json.items[0].title}}` です。

{% endraw %}

![LiftIgniter固有の接続内容コールを含むプッシュキャンペーンを示す"画像。"画像 フィールドには、接続内容ロジックも追加されています。][1]

このメッセージを作曲者本文に入力すると、メッセージをプレビューできます。以下に示すように、"画像s をプルインすることもできます。

![送信後に表示されるメッセージのプレビュー "画像。][2]

[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}