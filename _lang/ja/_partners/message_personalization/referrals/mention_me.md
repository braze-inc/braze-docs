---
nav_title: Mention Me
article_title: Mention Me と Braze との統合
description: Mention Me 統合設定ガイド
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> [Mention Me](https://www.mention-me.com/) と Braze を組み合わせることで、プレミアム顧客を獲得し、揺るぎないブランドロイヤルティを育むための入り口とすることができます。ファーストパーティの紹介データを Braze にシームレスに統合することで、ブランドのファンをターゲットにした、詳細にパーソナライズされたオムニチャネル体験を提供することができます。

_この統合は Mention Me によって管理されます。_

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件          | 説明                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Mention Me アカウント   | このパートナーシップを活用するには、[Mention Me](https://mention-me.com/login) アカウントが必要です。                                                                     |
| Braze REST API キー  | `users.track` および`templates.email.create` 権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

* Mention Me が紹介した顧客の連絡先データとオプトインをリアルタイムで Braze に送信します
* 紹介データを使ってクーポンのリマインダーメールを作成します
* 紹介データを使用して高価値の顧客をセグメント化することでターゲットを絞り、他のマーケティングチャネルのパフォーマンスを強化します

## Mention Me から Braze に送信されるデータ

この統合を設定すると、Mention Me で顧客属性とイベントが自動的に作成されるため、事前にこれらの作業を行う必要がなくなります。

関連するイベントやカスタム属性のリンクには Braze に登録された顧客のメールアドレスが使用されます。Mention Me は、オプトインのステータスに関係なく、Mention Me を介してイベントをトリガーした見込み客や既存顧客のイベントと連絡先プロファイル属性を送信します。

詳細については、[連絡先プロファイルの属性とイベント](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze)を参照してください。

## Mention Me の統合

{% alert tip %}
詳細なステップバイステップのチュートリアルについては、[Mention Me の Braze 設定ドキュメント](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me)を参照してください。
{% endalert %}

Mention Me と Braze との統合

1. Mention Me で [[Braze integration](https://mention-me.com/merchant/~/integrations/braze)] ページに移動し、[**Connect**] を選択します。
2. [**Create New Authorization**] を選択し、[すでに作成済みの API キー](#prerequisites)を追加して、Braze インスタンスを選択します。
3. 同期する国を 1 つ以上選択します。
4. 完了したら、[**Connect**] を選択します。
