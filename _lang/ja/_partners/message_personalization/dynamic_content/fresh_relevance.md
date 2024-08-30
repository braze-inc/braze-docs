---
nav_title: Fresh Relevance
article_title: Fresh Relevance
description: "このリファレンス記事は、BrazeとFresh Relevanceのパートナーシップについて概説しています。Fresh Relevanceは、多用途のパーソナライゼーションプラットフォームで、BrazeのキャンペーンやCanvasに関連する製品を含めることができます。"
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Fresh Relevance

> [Fresh Relevance][1]は、コマース主導のビジネスが簡単にカスタマイズされたクロスチャネルの体験を作成できるようにする多用途のパーソナライゼーションソリューションです。プラットフォームは時間を節約し、技術スタックと統合し、ITチームに依存せずに、Webサイト、アプリ、メール、SMS、広告全体でコンバージョンを向上させるパーソナライズされた顧客体験を提供する力を与えます。

BrazeとFresh Relevanceの統合により、次のことが可能になります:
* 高度なトリガー付きメールキャンペーンを送信します。例えば、価格の下落、在庫の復活、複数段階の閲覧、またはカート放棄メッセージなどです。
* トリガーされたメールにパーソナライズされたコンテンツを含めます。例えば、顧客が閲覧した商品や同じカテゴリ内のアイテムに基づいた商品推薦などです。
* AI駆動の推奨事項、カウントダウンタイマー、リアルタイムの天気予報、ソーシャルメディアフィードなどを使用して、バルクメールキャンペーンをパーソナライズします。
* データキャプチャポップアップを通じて収集された新しい連絡先でメールデータベースを成長させます。
* Braze メールリンクから到着した Web サイト訪問者を特定します。

## 前提条件

| 要件 | 説明 |
|-------------| ----------- |
| Fresh Relevanceアカウント  | このパートナーシップを利用するには、Fresh Relevanceアカウントが必要です。 |
| Braze REST API キー | 以下に記載されているエンドポイントに十分な権限を持つBraze REST APIキー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][3]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
| Braze キャンペーン ID | 送信に使用したいデフォルトのBrazeキャンペーン。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Fresh Relevanceで統合を設定するには、**メッセージングチャネル**でBrazeチャネルを作成し、必要に応じて適切なFresh Relevanceトリガーやコンテンツでチャネルを使用する必要があります。 

ステップバイステップの手順については、Fresh Relevanceにログインして、彼らの[ドキュメント][2]に従ってください。

Fresh Relevanceシステムは、提供されたAPIキーを使用してBrazeと通信します。完全な統合では、次のBraze APIエンドポイントを使用します:

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