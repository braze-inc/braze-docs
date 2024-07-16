---
nav_title: コグニティ インスパイア
article_title:コグニティ インスパイア
description:「Kognitiv Inspireは、ロイヤルティ戦略の実施と評価を可能にするロイヤルティ・テクノロジー・システムであり、革新的な機能と会員に合わせたコミュニケーションを提供し、プログラムの効果を高める。
alias: /partners/kognitiv/
page_type: partner
search_tag:Partner
---

# コグニティ インスパイア

> [Kognitiv Inspireは][1]ロイヤルティ・テクノロジー・システムで、カスタマー・エンゲージメントを高め、支出を増大させ、顧客行動を称賛する結果重視のロイヤルティプログラムを通じて、他に類を見ないカスタマーエクスペリエンスを実現する。

BrazeとKognitivの統合により、ロイヤルティ戦略の実施と評価が可能になり、革新的な機能と会員に合わせたコミュニケーションを提供し、プログラムの効果を高めることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Kognitivアカウント | このパートナーシップを利用するには[Kognitiv][1]アカウントが必要である。 |
| Kognitiv API キー | Kognitiv REST API キー。これは**API Security Tokens**ページで作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

- **パーソナライズされたロイヤルティプログラムの登録**：シームレスにプログラムに登録し、好みのチャネルを通じてカスタマイズされたウェルカム通知を配信することで、会員のロイヤルティジャーニーを促進する。
- **報酬の発行とエンゲージメント通知**：各メンバーのマイルストーンを祝う報酬や通知を発行することで、ロイヤルティの輝きを維持する。
- **戦略的な会員の階層化とセグメンテーション**：ブランド固有のニーズに合わせて、支出、エンゲージメント、単純または複雑なビジネスルールに基づいて会員を階層化およびセグメンテーションすることで、よりパーソナライズされたエンゲージメントを実現する。
- **昇格資格をリアルタイムで通知**する：限定プロモーションへの参加資格を即座に通知することで、各会員に特別感を与える。

## 統合

KognitivのWebhookを使って、ロイヤルティイベント発生時にBrazeにリクエストを送る。以下の例は、KognitivとBrazeを使用して報酬を発行し、BrazeにKognitivユーザーを登録し、歓迎メールを送信する方法を示している。

{% raw %}
### Braze発行報酬

次のKognitivの例は、メンバー報酬を発行している。Kognitiv Inspireは、その報酬発行イベントをカスタムイベントとしてWebhook経由でBrazeに伝える。報酬を伝えるフォローアップメールを送信するには、そのカスタムイベントをトリガーとするキャンペーンまたはキャンバスを作成する。

**WebhookのURL**：`<braze-api-rest-endpoint>`
**リクエスト・ボディ** `Raw Text`

- **HTTPメソッド**：POST
- **リクエストヘッダー**：
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

### ユーザーを作成し、ウェルカムメールを送信する。

以下のKognitivの例では、KLSに登録するとBrazeに新しいユーザーが作成される。このユーザーにウェルカムメールをスケジュールさせるには、特定のカスタム属性に基づいてトリガーされるキャンペーンまたはキャンバスをBrazeで作成する。

**WebhookのURL**： `<braze-api-rest-endpoint>`<br>
**リクエスト・ボディ** `Raw Text`

- **HTTPメソッド**：POST
- **リクエストヘッダー**：
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

BrazeとKognitiv Inspireを統合すると、Kognitivの広範なAPIポートフォリオ、最先端のWebhook機能、シームレスに一括転送できる堅牢なデータのインポート/エクスポート機能にアクセスできるようになります。Kognitiv Inspireの機能と統合機能の詳細については、Kognitiv[リソースガイドを][2]参照するか、ガイド付きデモを希望する場合は同社に連絡する。

### エンドポイント

**REST APIの認証**
- 米国地域である： `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA地域： `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC地域： `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (ベースURL)**
- 米国地域である： `https://app.kognitivloyalty.com/api`
- CA/EMEA地域： `https://ca.kognitivloyalty.com/api`
- APAC地域： `https://aus.kognitivloyalty.com/api`

**Webサービスエンドポイント（ベースURL）**
- 米国地域である： `https://app.kognitivloyalty.com/WS`
- CA/EMEA地域： `https://ca.kognitivloyalty.com/WS`
- APAC地域： `https://aus.kognitivloyalty.com/WS`

アクセストークンおよびSFTPエンドポイントの設定に関する詳細については、Kognitivまでデモを問い合わせること。

[1]: http://kognitiv.com
[2]: https://info.kognitivloyalty.com