---
nav_title: Certona
article_title:セルトナ
alias: /partners/certona/
description:この記事では、BrazeとCertonaの提携について説明します。Certonaは、顧客のライフサイクル全体にわたってパーソナライゼーションを提供するリアルタイムのオムニチャネルパーソナライゼーションソリューションです。BrazeのConnected ContentパートナーとCertonaを使用して、マルチチャネルキャンペーン全体にコンテンツ推奨を簡単に挿入します。
page_type: partner
search_tag:Partner

---

# セルトナ

> Certona's platform drives personalization across the customer lifecycle. From highly individualized email campaigns to machine-learning-powered product recommendations, Certona ensures that you'はパーソナライゼーションの力を活用しています。

BrazeとCertonaの統合は、Connected Contentを通じてBrazeキャンペーンおよびCanvasでCertonaの機械学習製品推奨を活用します。

## 前提条件

| 要件| 説明|
| ---| ---|
| [Certonaアカウント](https://manage.certona.com/) | このパートナーシップを利用するには、Certonaアカウントが必要です。 |
| [Certona REST API エンドポイント](https://manage.certona.com/) | このエンドポイントは、ユーザーIDに基づいて推奨コンテンツを取得するために、Brazeキャンペーンメッセージで直接使用されます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

CertonaのREST APIを使用して、メッセージにパーソナライズされたコンテンツを挿入します。これは、次のConnected ContentテンプレートをCertona REST APIエンドポイントと一緒にBrazeメッセージコンポーザーに追加することで実行できます。

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

次に、関連するテキストや画像など、呼び出したいコンテンツを定義します。例えば、`{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`。

{% endraw %}

![Certona関連の接続コンテンツがメッセージ本文に含まれているプッシュキャンペーンの画像。][1]

このメッセージを作成者の本文に入れたら、接続されたコンテンツの呼び出しをプレビューして、正しい情報が表示されていることを確認してください。

![「テスト」タブを示す画像で、ユーザーに送信前にメッセージを徹底的にテストするよう促しています。][2]

[1]: {% image_buster /assets/img/certona.png %}
[2]: {% image_buster /assets/img/certona2.png %}