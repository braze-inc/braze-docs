---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "この参考記事では、顧客ライフサイクル全体にわたってパーソナライゼーションを提供するリアルタイム・オムニチャネル・パーソナライゼーション・ソリューションであるBrazeとCertonaのパートナーシップについて概説している。Certona と Braze Connected Content パートナーを合わせて使用することで、マルチチャネルキャンペーンにおすすめのコンテンツを簡単に挿入できます。"
page_type: partner
search_tag: Partner

---

# Certona

> Certona のプラットフォームでは、カスタマーライフサイクル全体でパーソナライゼーションが推進されます。高度にパーソナライズされたEメールキャンペーンから、機械学習による製品推奨まで、Certonaはパーソナライゼーションの力を確実に活用する。

_この統合は Certona によって管理されます。_

## 統合について

Braze と Certona の統合では、コネクテッドコンテンツを介して Certona の機械学習製品のレコメンデーションが Braze キャンペーンとキャンバスで利用されます。

## 前提条件

| 必要条件| 説明|
| ---| ---|
| [Certona アカウント](https://manage.certona.com/) | このパートナーシップを活用するには、Certona アカウントが必要です。 |
| [Certona REST APIエンドポイント](https://manage.certona.com/) | このエンドポイントは、Brazeキャンペーンメッセージで直接使用され、ユーザーIDに基づいて推奨コンテンツを引き出す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Certona の REST API を使用して、パーソナライズされたコンテンツをメッセージに挿入する。これを行うには、Certona REST API エンドポイントとともに、次のコネクテッドコンテンツテンプレートを Braze メッセージ作成画面に追加します。

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

次に、関連するテキストや画像など、呼び出したいコンテンツを定義する。たとえば `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}` です。

{% endraw %}

![メッセージ本文に含まれる Certona 関連のコネクテッドコンテンツを使用したプッシュキャンペーン。]({% image_buster /assets/img/certona.png %})

このメッセージを作成画面に追加したら、コネクテッドコンテンツの呼び出しをプレビューし、正しい情報が表示されていることを確認します。

![送信前にメッセージを完全にテストするようにユーザーに促す [Test] タブ。]({% image_buster /assets/img/certona2.png %})


