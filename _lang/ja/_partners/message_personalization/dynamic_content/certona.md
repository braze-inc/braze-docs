---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "この参考記事では、顧客ライフサイクル全体にわたってパーソナライゼーションを提供するリアルタイム・オムニチャネル・パーソナライゼーション・ソリューションであるBrazeとCertonaのパートナーシップについて概説している。CertonaをBrazeのConnected Contentパートナーと併用することで、マルチチャネルキャンペーンにコンテンツ推薦を簡単に挿入できる。"
page_type: partner
search_tag: Partner

---

# Certona

> Certonaのプラットフォームは、顧客ライフサイクル全体にわたってパーソナライゼーションを推進する。高度にパーソナライズされたEメールキャンペーンから、機械学習による製品推奨まで、Certonaはパーソナライゼーションの力を確実に活用する。

BrazeとCertonaの統合は、コネクテッド・コンテンツを通じて、BrazeのキャンペーンとCanvasesでCertonaの機械学習による製品推奨を活用する。

## 前提条件

| 必要条件| 説明|
| ---| ---|
| [セルトナアカウント](https://manage.certona.com/) | このパートナーシップを利用するには、セルトナ・アカウントが必要である。 |
| [Certona REST APIエンドポイント](https://manage.certona.com/) | このエンドポイントは、Brazeキャンペーンメッセージで直接使用され、ユーザーIDに基づいて推奨コンテンツを引き出す。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Certona の REST API を使用して、パーソナライズされたコンテンツをメッセージに挿入する。これは、以下のConnected Contentテンプレートを、Certona REST APIエンドポイントとともに、Brazeメッセージコンポーザーに追加することで行うことができる。

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

次に、関連するテキストや画像など、呼び出したいコンテンツを定義する。例えば、`{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}` 。

{% endraw %}

![サートナに関連するコネクテッド・コンテンツがメッセージ本文に含まれるプッシュ・キャンペーンのイメージ。][1]

このメッセージをコンポーザー本体に入れたら、コネクテッド・コンテンツの呼び出しをプレビューし、正しい情報が表示されていることを確認する。

![Test "タブを示す画像は、送信前にメッセージを徹底的にテストすることをユーザーに促している。][2]

[1]: {% image_buster /assets/img/certona.png %}
[2]: {% image_buster /assets/img/certona2.png %}