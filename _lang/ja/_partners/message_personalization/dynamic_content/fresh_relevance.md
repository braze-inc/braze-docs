---
nav_title: Fresh Relevance
article_title:Fresh Relevance
description:"この参考記事では、Brazeと、Brazeのキャンペーンやキャンバスに関連商品を含めることを可能にする多目的なパーソナライゼーションプラットフォームであるFresh Relevanceとのパートナーシップについて概説している。"
alias: /partners/fresh_relevance/
page_type: partner
search_tag:Partner

---

# Fresh Relevance

> このプラットフォームは、ITチームに頼ることなく、時間を節約し、技術スタックと統合し、Webサイト、アプリ、メール、SMS、広告でコンバージョンを高めるパーソナライズされたカスタマーエクスペリエンスを提供することができる。

BrazeとFresh Relevanceの統合により、以下のことが可能になる：
* 値下げ、再入荷、多段階閲覧、カート放棄などの高度なトリガーメール キャンペーンを送信。
* トリガーメールにパーソナライズされたコンテンツを含める。例えば、顧客が閲覧した商品や同じカテゴリー内の商品に基づいて、おすすめの商品を紹介する。
* AIによるレコメンデーション、カウントダウンタイム、リアルタイムの天気予報、ソーシャルメディアフィードなどを使って、一括メールキャンペーンをパーソナライズさせる。
* データ収集ポップアップで集めた新しいコンタクトでメールデータベースを増やす。
* Brazeのメールリンクから来たWebサイト訪問者を識別する。

## 前提条件

| 必要条件 | 説明 |
|-------------| ----------- |
|   |  |
| Braze REST API キー | 以下のエンドポイントに十分な権限を持つREST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][3]。エンドポイントはインスタンスのBraze URLに依存する。 |
| キャンペーンID | メール送信に使用するデフォルトBrazeキャンペーン。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Fresh Relevanceで統合を設定するには、**Messaging Channelsで**Brazeチャネルを作成し、必要に応じて適切なFresh Relevanceトリガーまたはコンテンツでチャネルを使用する必要がある。 

ステップ・バイ・ステップの手順については、Fresh Relevanceにログインし、[ドキュメントに従って][2]ほしい。

Fresh Relevanceシステムは、提供されたAPIキーを使用してBrazeと通信する。完全な統合では、以下のBraze APIエンドポイントを使用する：

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