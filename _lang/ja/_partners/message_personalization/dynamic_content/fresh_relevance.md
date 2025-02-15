---
nav_title: Fresh Relevance
article_title: Fresh Relevance
description: "このリファレンス記事は、BrazeとFresh Relevanceのパートナーシップについて概説しています。Fresh Relevanceは、多用途のパーソナライゼーションプラットフォームで、BrazeのキャンペーンやCanvasに関連する製品を含めることができます。"
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Fresh Relevance

> [Fresh Relevance][1]は、コマース主導のビジネスが簡単にカスタマイズされたクロスチャネルの体験を作成できるようにする多用途のパーソナライゼーションソリューションです。このプラットフォームは、時間を節約し、技術スタックと統合し、IT チームに頼ることなく、Web サイト、アプリ、メール、SMS、広告全体でコンバージョンを高めるパーソナライズされたカスタマーエクスペリエンスを提供できるようにします。

BrazeとFresh Relevanceの統合により、次のことが可能になります:
* 高度なトリガー付きメールキャンペーンを送信します。例えば、価格の下落、在庫の復活、複数段階の閲覧、またはカート放棄メッセージなどです。
* トリガーされたメールにパーソナライズされたコンテンツを含めます。例えば、顧客が閲覧した商品や同じカテゴリ内のアイテムに基づいた商品推薦などです。
* AI駆動の推奨事項、カウントダウンタイマー、リアルタイムの天気予報、ソーシャルメディアフィードなどを使用して、バルクメールキャンペーンをパーソナライズします。
* データキャプチャポップアップで収集された新しい連絡先をメールデータベースに追加してこのデータベースを拡大します。
* Braze メールリンクから到着した Web サイト訪問者を特定します。

## 前提条件

| 必要条件 | 説明 |
|-------------| ----------- |
| Fresh Relevance アカウント  | このパートナーシップを活用するには、Fresh Relevance アカウントが必要です。 |
| Braze REST API キー | 以下に記載されているエンドポイントに十分な権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][3]。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Braze キャンペーン ID | 送信に使用したいデフォルトのBrazeキャンペーン。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Fresh Relevance で統合を設定するには、[**Messaging Channels**] でBraze チャネルを作成し、必要に応じて適切な Fresh Relevance トリガーまたはコンテンツでこのチャネルを使用する必要があります。 

ステップバイステップの手順については、Fresh Relevanceにログインして、彼らの[ドキュメント][2]に従ってください。

Fresh Relevance システムは、提供された API キーを使用して Braze と通信します。完全な統合では、次のBraze APIエンドポイントを使用します:

* [`/users/alias/new`][4]
* [`/users/track`][5]
* [`/campaigns/triggers/send`][6]
* [`/users/export/ids`][7]
* [`/subscription/status/get`][8]
* [`/v2/subscription/status/set`][9]

[1]: https://www.freshrelevance.com/
[2]: https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[5]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[7]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/