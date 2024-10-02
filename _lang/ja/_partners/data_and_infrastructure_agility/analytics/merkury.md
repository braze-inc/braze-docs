---
nav_title: マーキュリー
article_title: マーキュリー
description: "この参考記事では、Brazeとアプリ向けエンタープライズIDプラットフォームであるMerkuryのパートナーシップについて概説している。Brazeの顧客は、`MerkuryID`を活用してサイト訪問者の認識率を高めることができる。"
page_type: partner
search_tag: Partner

---

# マーキュリー

> [Merkuryは](https://merkury.merkleinc.com/)Merkleのエンタープライズ・アイデンティティ・プラットフォームであり、ファーストパーティのCookieレス・アイデンティティ機能を通じて、ブランドが消費者とのエンゲージメント、エクスペリエンス、収益を最大化できるよう支援する。`MerkuryID` は、ブランドの既知・未知の顧客や見込み客の記録、サイトやアプリの訪問履歴、消費者データを単一の永続的な個人IDに統合する。

BrazeとMerkuryの統合により、`MerkuryID` 、Brazeの顧客のサイト訪問者の認識率を高めることができる。ブランドのEメール購読者である訪問者を認識すると、MerkuryはBrazeのプロフィールを更新し、購読者のEメールアドレスを含める。`MerkuryID` の認識能力の向上は、エンゲージメントとパーソナライゼーションの機会を改善し、サイト放棄メールの送信量と関連収益を即座に増加させる。 

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| メルクルアカウント | このパートナーシップを利用するには、メルクルのアカウントが必要である。 |
| メルクル・クライアントID | Merkleの担当者からクライアントIDを取得する。 |
| マーキュリータグ | MerkleのMerkuryタグをウェブサイトに設置する。 |
| Braze RESTおよびSDKエンドポイント | RESTまたはSDKのエンドポイントURL。エンドポイントは、[インスタンスのBraze URLに]({{site.baseurl}}/api/basics/#endpoints)依存する。 |
| Braze REST API キー | `users.track, users.export.ids, users.export.segment, and segments.list` 権限を持つ Braze REST API キー。<br><br>これは、**Braze Dashboard > Developer Console > REST API Key > Create New API Keyで**作成できる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
BrazeへのMerkury IDコネクタのリクエストは、Braze APIレート制限仕様内で動作する。ご不明な点があれば、BrazeまたはMerkleのアカウントマネージャーにお問い合わせいただきたい。<br><br>Merkuryは資格のあるセッションの最後に少なくとも1つのリクエストを送る。
{% endalert %}

## サイド・バイ・サイドのSDK統合

MerkleのクライアントサイドMerkuryタグを使用してBrazeデバイスをキャプチャし、識別のためにMerkury IDコネクタエンドポイントに転送する。

### ステップ1:BrazeウェブSDKタグを設定する

この統合を使用するには、ウェブサイトに[Braze Web SDKを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm)デプロイする必要がある。

### ステップ2:MerkleのMerkuryタグを展開する

Merkuryタグをウェブサイトに配置する。これにより、あなたのウェブサイトでMerkury IDコネクターが利用できるようになる。メルクルアカウントマネージャーより、詳細なガイドが提供される。

### ステップ3:カスタム属性を作成する

以下のフィールドはMerkury Identity Connectorによって入力されるため、Brazeで[カスタム属性として]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes)作成する必要がある。

| 属性名 | データタイプ | 説明 |
| --- | --- | --- |
| `hmid` | String | メルクルのメルクリーID |
| `confidence_score` | 数値 | メルクリーがどの程度自信を持って識別できたか（1～8、低いほど良い） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ステップ4:MerkleにユーザーEメールユニバースを提供する

Merkleは、許可されたメールユニバースのセグメンテーションエクスポートを推奨している。これは、アクティブな許容ユーザーの日次エクスポートでフォローアップできる。

以下のフィールドは必須である：

- `braze_id`
- `external_id`
- メールアドレス

詳細については、Brazeの担当者に問い合わせること。