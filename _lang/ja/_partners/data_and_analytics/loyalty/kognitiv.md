---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire は、お客様が各自のロイヤルティ戦略を実装、評価できるようにし、プログラムの有効性を高めるための革新的な機能とカスタマイズされたメンバーコミュニケーションを提供するロイヤルティテクノロジーシステムです。"
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com) はロイヤルティテクノロジーシステムであり、カスタマーエンゲージメントを強化し、顧客の支出を増やし、ロイヤルティの高い行動を称賛する、結果に基づくロイヤルティプログラムによって、比類のない顧客体験を実現できるように支援します。

_この統合は Kognitiv Inspire によって管理されます。_

## 統合について

Braze と Kognitiv の統合により、ロイヤルティ戦略を実装、評価できるようになり、プログラムの有効性を高めるための革新的な機能とカスタマイズされたメンバーコミュニケーションが提供されます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| コグニティブアカウント | このパートナーシップを活用するには、[Kognitiv](http://kognitiv.com) アカウントが必要です。 |
| Kognitiv APIキー | Kognitiv REST API キー。これは**API Security Tokens**ページで作成できる。 |
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

- **パーソナライズされたロイヤルティプログラムの登録**:シームレスなプログラム登録と、会員が希望するチャネルを通じて配信されるカスタマイズされたウェルカム通知で、会員のロイヤルティジャーニーを促進します。
- **リワードの発行とエンゲージメント通知**:会員のマイルストーンを祝うリワードの発行や通知により、ロイヤルティを維持します。
- **戦略的な会員の階層化とセグメンテーション**:ブランド固有のニーズに合わせて、支出、エンゲージメント、単純または複雑なビジネス・ルールに基づいて会員を階層化およびセグメント化することで、よりパーソナライズされたエンゲージメントを可能にする。
- **リアルタイムでのプロモーション参加資格の通知**:限定プロモーションの参加資格を即時に通知することで、各会員に特別感を与えます。

## 統合

KognitivのWebhookを使って、ロイヤルティイベント発生時にBrazeにリクエストを送る。以下の例では、KognitivとBrazeを使用して報酬を発行し、KognitivユーザーをBrazeに登録し、ウェルカムメールを送信する方法を説明する。

{% raw %}
### Braze によるリワードの発行

次の Kognitiv の例では、会員リワードを発行します。Kognitiv Inspire はそのリワード発行イベントを、Webhook を使用して Braze にカスタムイベントとして伝えます。報酬を伝えるフォローアップメールを送信するには、そのカスタムイベントをトリガーとするキャンペーンまたはキャンバスを作成する。

**Webhook URL**:`<braze-api-rest-endpoint>`
**リクエスト本文**: `Raw Text`

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:ベアラー `<Kognitiv-api-key>`
  - **Content-Type** application/json

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

次の Kognitiv の例では、新規ユーザーが KLS に登録すると、Braze に新規ユーザーが作成されます。このユーザーのウェルカムメールをスケジュールするには、特定のカスタム属性に基づいてトリガーするキャンペーンまたはキャンバスをBrazeで作成する。

**Webhook URL**: `<braze-api-rest-endpoint>`<br>
**リクエスト本文**: `Raw Text`

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:ベアラー `<Kognitiv-api-key>`
  - **Content-Type** application/json

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

Braze を Kognitiv Inspire と統合すると、Kognitiv の広範な API ポートフォリオ、最先端の Webhook 機能、およびシームレスな一括転送のための堅牢なデータインポートおよびエクスポート機能を利用できるようになります。Kognitiv Inspire の機能と統合機能の詳細については、Kognitiv[リソースガイド](https://info.kognitivloyalty.com)を参照するか、Kognitive に連絡してガイド付きデモを依頼してください。

### エンドポイント

**REST API 認証**
- US 地域: `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA 地域: `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC 地域： `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (ベース URL)**
- US 地域: `https://app.kognitivloyalty.com/api`
- CA/EMEA 地域: `https://ca.kognitivloyalty.com/api`
- APAC 地域： `https://aus.kognitivloyalty.com/api`

**ウェブサービスのエンドポイント（ベースURL）**
- US 地域: `https://app.kognitivloyalty.com/WS`
- CA/EMEA 地域: `https://ca.kognitivloyalty.com/WS`
- APAC 地域： `https://aus.kognitivloyalty.com/WS`

アクセストークンと SFTP エンドポイントの設定に関する詳細については、Kognitiv にデモを依頼してください。


