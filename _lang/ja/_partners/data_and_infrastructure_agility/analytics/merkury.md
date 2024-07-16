---
nav_title: Merkury
article_title:マーキュリー
description:"この参考記事では、Brazeとアプリ向けエンタープライズIDプラットフォームであるMerkuryの提携について概説している。"`MerkuryID` を活用することで、Braze顧客のサイト訪問者の認識率を高めることができる。
page_type: partner
search_tag:Partner

---

# マーキュリー

> [Merkuryは](https://merkury.merkleinc.com/)Merkleのエンタープライズ・アイデンティティ・プラットフォームであり、ブランドがファーストパーティのCookieレス・アイデンティティ機能を通じて消費者のエンゲージメント、エクスペリエンス、収益を最大化できるよう支援する。`MerkuryID` は、ブランドの既知および未知の顧客や見込み客の記録、サイトやアプリの訪問履歴、消費者データを単一の永続的な個人IDに統合する。

BrazeとMerkuryの統合により、`MerkuryID` 、Braze顧客のサイト訪問者の認識率を高めることができる。ブランドのメール購読者である訪問者を認識すると、MerkuryはBrazeプロファイルを更新し、購読者のメールアドレスを含める。`MerkuryID` の認識能力の向上により、エンゲージメントとパーソナライゼーションの機会が向上し、サイト放棄メールの送信量と関連収益が即座に増加する。 

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| Merkleアカウント | このパートナーシップを利用するには、Merkleアカウントが必要である。 |
| MerkleクライアントID | クライアントIDをMerkle担当者から取得する。 |
| マーキュリータグ | WebサイトにMerkleのタグを設置する。 |
| Braze RESTおよびSDKエンドポイント | RESTまたはSDKエンドポイントのURL。エンドポイントは[インスタンスのBraze URLに]({{site.baseurl}}/api/basics/#endpoints)依存する。 |
| Braze REST API キー | `users.track, users.export.ids, users.export.segment, and segments.list` 権限を持つ Braze REST API キー。<br><br>これは、**Brazeダッシュボード > Developer Console > REST API Key > Create New API Keyで**作成できる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
BrazeへのMerkury IDコネクタのリクエストは、Braze APIレート制限仕様内で動作する。ご不明な点はBrazeまたはMerkleアカウントマネージャーにお問い合わせください。<br><br>Merkuryは、資格のあるセッションの終わりに、少なくとも1つのリクエストを送信する。
{% endalert %}

## サイド・バイ・サイドSDKの統合

MerkleのクライアントサイドMerkuryタグを使用してBrazeデバイスをキャプチャし、識別のためにMerkury IDコネクタエンドポイントに転送する。

### ステップ1:Braze web SDKタグを設定する。

この統合を使用するには、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm)サイトに[Braze Web SDKを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm)デプロイする必要がある。

### ステップ2:MerkleのMerkuryタグを導入する

WebサイトにMerkuryタグを配置する。これにより、あなたのWebサイトでMerkury IDコネクタが利用できるようになる。詳しい手順は、Merkleアカウントマネージャーから提供される。

### ステップ3:カスタム属性を作成する

以下のフィールドはMerkury IDコネクタによって入力されるため、[カスタム属性として]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes)Brazeで作成する必要がある。

| 属性名 | データタイプ | 説明 |
| --- | --- | --- |
| `hmid` | String | MerkleのMerkury ID |
| `confidence_score` | 数値 | メルクーリがどの程度自信を持って識別できたか（1～8、低いほど良い） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ステップ 4:ユーザーのメールユニバースをMerkleに提供する。

Merkleでは、メール送信権限のセグメンテーションエクスポートを推奨している。これは、アクティブユーザーの日次エクスポートでフォローアップできる。

以下のフィールドは必須である：

- `braze_id`
- `external_id`
- メールアドレス

詳しくはBrazeの担当者に問い合わせを。