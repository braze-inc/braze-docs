---
nav_title: 開封ロイヤルティ
article_title: 開封ロイヤルティ
description: "Brazeと開封ロイヤリティの統合により、ポイント残高、ティアの変更、有効期限警告などのロイヤルティデータをリアルタイムでBrazeに直接同期することができる。"
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# 開封ロイヤルティ

> [開封ロイヤリティは](https://www.openloyalty.io/)クラウドベースのロイヤルティプログラムプラットフォームで、顧客ロイヤルティプログラムや報酬プログラムを構築・管理することができる。BrazeとOpen Loyaltyの統合は、ポイント残高、ティアの変更、有効期限警告などのロイヤルティデータをリアルタイムでBrazeに直接同期する。これにより、ユーザーのロイヤルティステータスが変化したときに、パーソナライズされたメッセージ（メール、プッシュ、SMS）をトリガーすることができる。

_この統合は開封ロイヤルティによって維持されている。_

## 統合について

この統合は、Brazeデータ変換を使用して、開封ロイヤルティからWebhookを取得し、Brazeユーザープロファイルにマッピングする。

* **リアルタイム更新**：ロイヤルティイベント（ポイント獲得、ティアアップグレード）をBrazeにプッシュする。
* **パーソナライゼーション**:Brazeテンプレートでロイヤルティ属性（現在の残高、次のティア名）を使用する。
* **双方向**だ：カスタマーエンゲージメントデータに基づき、オープンロイヤルティの顧客カスタム属性を更新。

## ユースケース

この統合は、以下のデータフローをカバーしている：

1. **Brazeにイベントを同期する（受信）**：オープンロイヤルティからBrazeにデータを送信することで、ポイントの変更、ティアのアップグレード、報酬の交換をトラッキング追跡。データ変換は、このデータをユーザー・イベントに変換する。
2. **開封済みロイヤルティ会員の変更（アウトバウンド）**：VIP」ラベルの追加やカスタム属性の更新など、Brazeでのユーザー行動に基づいて、Open Loyaltyの会員データを自動的に更新。

## 前提条件

始める前に、以下のものが必要だ：

| 必要条件 | 説明 |
| :--- | :--- |
| ロイヤルティ口座開封 | このパートナーシップを利用するには、開封ロイヤルティ・テナントの管理者アカウントが必要である。 |
| 開封ロイヤルティ REST API キー | Open Loyalty REST APIキー（BrazeからOpen Loyaltyにデータを送信する統合の場合）。<br><br> **設定＞管理者＞APIキーで**作成する。 |
| REST APIキー | `users.track` 権限を持つ Braze REST API キー。<br><br> ダッシュボードの**「設定」**>「**APIキー**」からこのキーを作成する。 |
| Braze Data Transformation | Webhookリスナーを設定するには、Brazeの「データ設定」タブにアクセスする必要がある。 |
| IDの一致 | ユーザーのBrazeの`external_id` は、Open Loyaltyの`loyaltyCardNumber` （または別のデフォルト識別子）と一致していなければならない。 |
| テナント ID | あなたの開封ロイヤルティテナントID（送信更新に必要）。 |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## 統合

主な統合は、データ変換を使用して、Brazeに開封ロイヤリティのWebhookイベントを同期する。

### ステップ 1: BrazeでWebhook URLを生成する。

まず、Brazeでデータ変換を作成し、データを受信するためのユニークなURLを生成する。

1.  Brazeで、**Data Settings > Data Transformationを**開封する。
2.  **Create Transformationを**クリックする。
3.  以下のフィールドに記入する：
     * **変身名だ**：説明的な名前を付ける（例えば、"開封ロイヤルティポイント更新イベント"）。
     * 送信先を**選択**する：**POSTを選択する：ユーザーを追跡** 。
4.  **Create Transformationを**クリックする。
5.  右側の**Webhook URLを**探し、**コピーを**クリックする。

{% alert important %}
このURLは大切に保管しておくこと。次のステップで必要になる。
{% endalert %}

### ステップ 2:オープンロイヤルティでWebhookサブスクリプションを作成する。

開封ロイヤリティに、先ほど生成したURLに特定のイベントを送信するよう指示する。

1.  開封ロイヤリティ管理パネルにログインする。
2.  **General > Webhooksに**移動する。
3.  **Add new webhookを**クリックし、サブスクリプションを設定する：
    * **イベント名で**ある：トラッキング 追跡したいイベントを選択する（例えば、`AvailablePointsAmountChanged` 、`CustomerLevelChanged` 、`CampaignEffectWasApplied` ）。
    * **url**：ステップ1のBraze Webhook URLを貼り付ける。
    * 以下のヘッダーを追加する：
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Webhook サブスクリプションを保存する。

### ステップ 3:データ変換を設定する

受信した開封ロイヤリティペイロードをBrazeのプロパティにマッピングするJavaScriptロジックをBrazeに記述する。

1.  Brazeで、ステップ1で作成したデータ変換を開封する。
2.  Open Loyaltyでイベントをトリガーし（例えば、メンバーのポイントを変更したり、ティアを割り当てたり）、**Webhook詳細**ペインにサンプルペイロードを生成する。
3.  **変換コード**エディターで、受信データをマッピングするスクリプトを書く。以下の例を参考にしてほしい：

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,
     
      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",
     
      // timestamp
      "time": new Date().toISOString(),
     
      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. **Validateを**クリックして、コードがサンプル・ペイロードに対して実行されることを確認し、**Activateを**クリックする。


## Brazeで開封ロイヤリティを使う

インバウンドの統合が完了したら、**アウトバウンドの更新を**設定し、Brazeの行動に基づいて開封ロイヤルティメンバーを変更する。

### ステップ 1: Braze Webhookキャンペーンの設定

このプロセスでは、Braze Webhookを使用してOpen Loyalty Member APIに`PATCH` リクエストを送信する（たとえば、「VIP」ラベルを追加する）。

1.  Brazeで、新しい**Webhookキャンペーンを**作成する（またはキャンバス内のWebhookを使用する）。
2.  **Compose Webhookを**クリックする。
3.  **Webhook URL**:開封ロイヤリティインスタンス、テナントID、ユーザーID用のBrazeインスタンス変数を使ってURLを構築する。
    * フォーマットだ：
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. 以下のフィールドに記入する：   
    * **リクエスト方法**： `PATCH`
    * **リクエストヘッダー**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **リクエスト本文**:`Raw text` を選択し、ペイロードを貼り付ける：

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### ステップ 2:トリガーを設定する

1.  **デリバリー**または**エントリーのスケジュール**タブに移動する。
2.  以下のフィールドに記入する：
    * **配達方法**：アクションベースだ。
    * **トリガー**だ：関連するトリガーを定義する（例えば、ユーザーがBrazeに特定のセグメンテーションを入力する）。
    * **打ち上げだ**：キャンペーンを開始する。

## トラブルシューティング

### インバウンドイベントを検証する
データ変換がアクティブになると、データがカスタムイベントとしてBrazeに表示される。**カスタムイベントを実行する**トリガーでキャンペーンを作成し、定義したイベント（例えば、`Loyalty Event Triggered` ）が利用可能かどうかを確認することで、これを検証する。

### アウトバウンドWebhookを検証する
Brazeのメッセージアクティビティログを確認し、Webhookが`200 OK` ステータスを返したことを確認する。
* **401エラー**：開封済みロイヤルティAPIトークンを確認する。
* **404エラー**：BrazeのユーザーIDがOpen Loyaltyに存在しない。