---
nav_title: コグニティブ・インスパイア
article_title: コグニティブ・インスパイア
description: "コグニティブ・インスパイアは、ロイヤリティ戦略の実施と評価を可能にするロイヤリティ・テクノロジー・システムであり、革新的な機能と会員に合わせたコミュニケーションを提供し、プログラムの効果を高める。"
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# コグニティブ・インスパイア

> [Kognitiv Inspireは][1]ロイヤリティ・テクノロジー・システムであり、顧客エンゲージメントを増幅し、支出を増大させ、忠実な行動を称える結果重視のロイヤリティ・プログラムを通じて、比類ない顧客体験を引き出す手助けをする。

BrazeとKognitivの統合により、ロイヤリティ戦略の実施と評価が可能になり、革新的な機能と会員に合わせたコミュニケーションを提供し、プログラムの効果を高めることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| コグニティブアカウント | このパートナーシップを利用するには、[コグニティブの][1]アカウントが必要である。 |
| Kognitiv APIキー | Kognitiv REST API キー。これは**API Security Tokens**ページで作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

- **パーソナライズされたロイヤリティ・プログラムの登録**：シームレスなプログラム登録と、会員が希望するチャネルを通じて配信されるカスタマイズされたウェルカム通知で、会員のロイヤリティ・ジャーニーを促進する。
- **報酬発行と婚約通知**：各メンバーのマイルストーンを祝うリワードや通知を発行することで、ロイヤリティの火花を絶やさないようにする。
- **戦略的な会員の階層化とセグメンテーション**：ブランド固有のニーズに合わせて、支出、エンゲージメント、単純または複雑なビジネス・ルールに基づいて会員を階層化およびセグメント化することで、よりパーソナライズされたエンゲージメントを可能にする。
- **昇格資格をリアルタイムで通知**する：限定プロモーションの参加資格を即座に通知することで、各会員に特別感を与える。

## 統合

KognitivのWebhookを使って、ロイヤルティイベント発生時にBrazeにリクエストを送る。以下の例では、KognitivとBrazeを使用して報酬を発行し、KognitivユーザーをBrazeに登録し、ウェルカムメールを送信する方法を説明する。

{% raw %}
### ブレイズ発行報酬

次のコグニティブの例では、会員に報奨金を発行している。Kognitiv Inspireは、その報酬発行イベントをカスタムイベントとしてBrazeにウェブフック経由で伝える。報酬を伝えるフォローアップメールを送信するには、そのカスタムイベントをトリガーとするキャンペーンまたはキャンバスを作成する。

**ウェブフックのURL**：`<braze-api-rest-endpoint>`
**リクエスト・ボディ** `Raw Text`

- **HTTPメソッド**：POST
- **ヘッダーを要求する**：
  - **認可する**：ベアラー `<Kognitiv-api-key>`
  - **コンテンツタイプ**application/json

#### Request body

```json
{ 
  "events" : [ 
    { 
    "external_id" : "{{memberId}}", 
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38", 
    "name" : "rewards_issued", 
    "time" : "{{issuedDate}}", 
    "issued_date" : "{{issuedDate}}", 
    "issued_location_name" : "{{issuedLocationName}}", 
    "reward_type" : "{{rewardType}}" 
    } 
  ] 
}
```

### ユーザーを作成し、ウェルカムメールを送信する

以下の Kognitiv の例では、KLS への登録時に Braze に新規ユーザーを作成している。このユーザーのウェルカムメールをスケジュールするには、特定のカスタム属性に基づいてトリガーするキャンペーンまたはキャンバスをBrazeで作成する。

**ウェブフックのURL**： `<braze-api-rest-endpoint>`<br>
**リクエスト・ボディ** `Raw Text`

- **HTTPメソッド**：POST
- **ヘッダーを要求する**：
  - **認可する**：ベアラー `<Kognitiv-api-key>`
  - **コンテンツタイプ**application/json

#### Request body

```json
{ 
  "attributes": [ 
    { 
      "app_id": "93ec5a59-3752-4a45-855b6109ba38", 
      "bio": "Software Architect", 
      "country": "{{memberAddressCO}}", 
      "email": "{{memberEmail}}", 
      "email_subscribe": "opted_in", 
      "external_id": "{{memberId}}", 
      "first_name": "{{memberFirstName}}", 
      "home_city": "{{memberAddressCity}}", 
      "time_zone": "America/Chicago", 
      "total_points_balance": "{{memberPointsAvailable}}", 
      "CreatedKLS": "{{issuedTimestamp}}", 
      "email_contact_allowed" : "{{memberEmailContactAllowed}}", 
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}", 
      "date_joined": "{{issuedDate}}" 
    } 
  ] 
}
```
{% endraw %}

## Kognitiv Inspireのドキュメントと統合機能

BrazeをKognitiv Inspireと統合すると、Kognitivの広範なAPIポートフォリオ、最先端のウェブフック機能、シームレスな一括転送のための堅牢なデータのインポートおよびエクスポート機能にアクセスできるようになる。Kognitiv Inspireの機能と統合機能の詳細については、Kognitiv[リソースガイドを][2]参照するか、ガイド付きデモを希望する場合は同社に連絡する。

### エンドポイント

**REST APIの認可**
- 米国地域である： `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA地域： `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC地域： `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API（ベースURL）**
- 米国地域である： `https://app.kognitivloyalty.com/api`
- CA/EMEA地域： `https://ca.kognitivloyalty.com/api`
- APAC地域： `https://aus.kognitivloyalty.com/api`

**ウェブサービスのエンドポイント（ベースURL）**
- 米国地域である： `https://app.kognitivloyalty.com/WS`
- CA/EMEA地域： `https://ca.kognitivloyalty.com/WS`
- APAC地域： `https://aus.kognitivloyalty.com/WS`

アクセストークンおよびSFTPエンドポイントの設定に関する詳細については、Kognitivにデモを問い合わせること。

[1]: http://kognitiv.com
[2]: https://info.kognitivloyalty.com