---
nav_title: Merkury
article_title: Merkury
description: "この参考記事では、Brazeとアプリ向けエンタープライズIDプラットフォームであるMerkuryのパートナーシップについて概説している。Brazeの顧客は、`MerkuryID`を活用してサイト訪問者の認識率を高めることができる。"
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) は、Merkle のエンタープライズアイデンティティプラットフォームです。ファーストパーティ Cookie レスアイデンティティ機能により、ブランドが消費者とのやり取り、エクスペリエンス、収益を最大化できるように支援します。`MerkuryID` は、ブランドの既知および未知の顧客と見込み客のレコード、サイトやアプリの訪問履歴、および消費者データを、1つの永続的な個人 ID に統合します。

_この統合は Merkury によって管理されます。_

## 統合について

Braze と Merkury の統合により、`MerkuryID` を活用して、Braze のお客様のサイト訪問者認識率を向上させることができます。Merkury はブランドのメールサブスクライバーである訪問者を認識すると、Braze プロファイルを更新し、サブスクライバーのメールアドレスをプロファイルに含めます。`MerkuryID` の認識機能の向上により、エンゲージメントとパーソナライゼーションの機会が拡大し、送信されるサイト放棄メールの量と関連収益がすぐに増加します。 

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| Merkle アカウント | このパートナーシップを活用するには、Merkle アカウントが必要です。 |
| Merkleクライアント ID | Merkle の担当者からクライアント ID を取得します。 |
| マーキュリータグ | Merkle の Merkury タグを Web サイトに配置します。 |
| Braze RESTおよびSDKエンドポイント | REST または SDK エンドポイントの URL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
| Braze REST API キー | `users.track, users.export.ids, users.export.segment, and segments.list`の権限を持つBraze REST APIキー。<br><br>これは **Brazeダッシュボード > [開発者コンソール] > [REST API キー] > [新しい API キーを作成]** で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Braze への Merkury アイデンティティコネクターのリクエストは、Braze API レート制限仕様の範囲内で動作します。ご質問がある場合は、Braze または Merkle アカウントマネージャーにお問い合わせください。<br><br>Merkuryは、適格なセッションの終了時に少なくとも1つのリクエストを送信します。
{% endalert %}

## サイドバイサイドの SDK 統合

Merkle のクライアントサイド Merkury タグを使用して Braze デバイスをキャプチャし、識別のためにMerkury ID コネクターエンドポイントに転送します。

### ステップ1:BrazeウェブSDKタグを設定する

この統合を使用するには、Web サイトに[Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) を導入している必要があります。

### ステップ2:Merkle の Merkury タグを導入する

Merkuryタグをウェブサイトに配置する。これにより、Merkury アイデンティティコネクターが Web サイトで使用できるようになります。Merkle アカウントマネージャーから、手順を含む詳細なガイドが提供されます。

### ステップ3:カスタム属性を作成する

以下のフィールドは Merkury アイデンティティコネクターによって入力され、Braze で[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes) として作成する必要があるものです。

| 属性名 | データタイプ | 説明 |
| --- | --- | --- |
| `hmid` | String | Merkle の Merkury ID |
| `confidence_score` | 数値 | Merkury がどの程度の信頼度で識別できたか (1～8、小さいほど良い) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ステップ4:Merkle にユーザーメールユニバースを提供する

Merkle では、許容されるメールユニバースのセグメンテーションエクスポートが推奨されています。これは、アクティブな許容ユーザーの日次エクスポートでフォローアップできる。

以下のフィールドは必須である：

- `braze_id`
- `external_id`
- メールアドレス

詳細については、Brazeの担当者に問い合わせること。

