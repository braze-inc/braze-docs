---
nav_title: Toovio
article_title: Toovio
description: "このリファレンス記事では、Braze と Toovio のパートナーシップについて説明します。Toovio は、実用的なデータを検出し、最も重要な要素を使用して事前に定義されている目標に基づき段階的に成果を上げることができるようにする data-as-a-service 企業です。"
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) は、人工知能を採用している data-as-a-service企業であり、実用的なデータを検出し、最も重要な要素を使用して事前に定義されている目標に基づき段階的に成果を上げることを支援します。

_この統合は Toovio によって管理されます。_

## 統合について

Braze と Toovio のパートナーシップにより、ほぼリアルタイムでのメッセージトリガー、増分パフォーマンスを促進するツール、Toovio の高度なキャンペーン測定ツールが利用可能になります。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Toovio アカウント | このパートナーシップを活用するには、Toovio アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze Currents | Braze Currents により、Brazeクライアントは、Brazeプラットフォーム外部での処理のためにイベントまたは行動データを Braze データパートナー (AWS S3、Google Cloud Storage、または Microsoft Azure Blob Storage) にストリーミングできます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

以下の統合により、Toovio は特定の顧客をターゲットとしたトリガーを生成し、ほぼリアルタイムで通信できます。Toovio により決定されたトリガーは、Braze [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を経由して Braze に送信されます。

### ステップ1:データパートナーを定義する

カレントのフィードのドロップ先をToovioと共有する必要がある。これにより、Toovioはユーザーのイベントおよび行動データにアクセスし、処理することができる。

### ステップ2:トリガーキャンペーンを設定する

Toovio がターゲットとする顧客イベントに基づいて、Braze [API トリガーキャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を作成します。さらに、キャンペーンのトリガーとなるターゲットユーザーの属性と値を定義する必要がある。

### ステップ3:Tovioアカウントを設定する

アカウントを設定するには、「New Customer Request」という件名のメールで Toovio ([info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request)) にご連絡ください。Toovio はクライアントと協力して、トリガーおよび基盤となるモデルを設定します。


