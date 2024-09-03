---
nav_title: トゥービオ
article_title: トゥービオ
description: "この参考記事では、Brazeとデータ・アズ・ア・サービス企業であるToovio社との提携について概説している。Toovio社は、実用的なデータを発見し、最も重要な要素を使用して、事前に定義された目標に基づき、段階的に成果を上げることを支援する。"
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# トゥービオ

> [Toovioは](https://toovio.com/)、人工知能を搭載したデータ・アズ・ア・サービス企業であり、実用的なデータを発見し、最も重要な要素を使用して、事前に定義された目標に基づき、段階的に成果を上げることができる。

BrazeとToovioのパートナーシップは、ほぼリアルタイムのメッセージ・トリガー、パフォーマンスを向上させるツール、Toovioの高度なキャンペーン測定ツールへのアクセスを提供する。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| トゥービオアカウント | このパートナーシップを利用するには、トゥービオのアカウントが必要だ。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze Currents | Braze Currentsにより、Brazeクライアントは、Brazeプラットフォームの外部で処理するために、イベントまたは行動データをBrazeデータパートナー（AWS S3、Google Cloud Storage、またはMicrosoft Azure Blob Storage）にストリーミングすることができる。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

以下の統合により、Toovioは特定の顧客をターゲットとしたトリガーを生成し、ほぼリアルタイムでコミュニケーションをとることができる。Toovioが決定したトリガーは、Braze[`/users/track` エンドポイントを][3]経由してBrazeに送信される。

### ステップ1:データパートナーを定義する

カレントのフィードのドロップ先をToovioと共有する必要がある。これにより、Toovioはユーザーのイベントおよび行動データにアクセスし、処理することができる。

### ステップ2:トリガー・キャンペーンを設定する

Toovioがターゲットとする顧客イベントに基づいて、Braze[APIトリガーキャンペーンを][4]作成する。さらに、キャンペーンのトリガーとなるターゲットユーザーの属性と値を定義する必要がある。

### ステップ3:Tovioアカウントを設定する

Toovioの[info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request)まで、件名を「新規顧客リクエスト」とし、アカウントを開設する。トゥービオは顧客と協力して、トリガーと基礎となるモデルを設定する。

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/
[2]: {{site.baseurl}}/api/api_key/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
