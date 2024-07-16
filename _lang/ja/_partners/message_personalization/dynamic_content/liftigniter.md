---
nav_title: リフトイグナイター
article_title:リフトイグナイター
alias: /partners/liftigniter/
description:この記事では、BrazeとLiftIgniter（主要なパーソナライゼーションプラットフォーム）との提携について説明し、企業が顧客体験を変革するのを支援します。
page_type: partner
search_tag:Partner

---

# リフティグナイター

> LiftIgniterは、あらゆる接点でリアルタイムパーソナライズを通じて顧客体験を変革するのを支援する、主要なパーソナライズプラットフォームです。

LiftIgniterとBrazeの統合は、Connected Contentを活用して、ニュース記事、衣料品、その他の小売商品やビデオなどの興味深いトピックを推薦することを可能にします。

## 前提条件

| 要件| 説明|
| ---| ---|
| LiftIgniter アカウント | このパートナーシップを利用するには、[LiftIgniterアカウント](https://console.liftigniter.com/login)が必要です。 |
| LiftIgniter API 統合 | あなたはLiftIgniterをあなたのサイトまたはアプリに[統合](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview)して、そこから推薦を引き出せるようにする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

[LiftIgniterのREST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389)を使用して、メッセージにパーソナライズされたコンテンツを挿入します。LiftIgniterのアカウントを取得し、LiftIgniterがアプリに統合されたら、次のテンプレートをメッセージコンポーザーに追加して、必要に応じて情報を置き換えながら（`x-api-key`、`theapikey`など）、メッセージにコンテンツを呼び出します。

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

次に、メッセージを書き、JSONで呼び出したい内容を定義します。例えば、`{{json.items[0].title}}`。

{% endraw %}

![LiftIgniter固有の接続コンテンツ呼び出しを含むプッシュキャンペーンを示す画像。画像フィールドに接続されたコンテンツロジックも追加されています。][1]

このメッセージを作成者の本文に入れると、メッセージをプレビューできます。画像を引き込むこともできます。次の例に示します。

![メッセージが送信された後のプレビュー画像です。][2]

[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}