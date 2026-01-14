---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "この参考記事では、BrazeとLob.com の提携について概説しています。Lob.com を利用すれば、手紙やはがき、小切手などのダイレクトメールを郵送することができます。"
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) は、ユーザーにダイレクトメールを送ることができるオンラインサービスである。

_この統合は Lob によって管理されます。_

## 統合について

この統合により、次のことが可能になります。

- Braze Webhooks とLob API を使用して、メールのような文字、はがき、小切手をメールで送信します。
- Braze Data Transformation と Lob Webhook を使用して、カスタム属性およびイベントとして Braze で Lob イベントを共有します。

## 前提条件

|必要条件| 説明|
| ---| ---|
|Lob アカウント | このパートナーシップを活用するには、Lob アカウントが必要です。 |
| Lob API キー | Lob API キーは、Lob ダッシュボードのお客様の名前の下にある設定セクションで確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze webhook を使用したメールの送信

### ステップ 1: Lob エンドポイントの選択

Lob で実行する内容に応じて、Webhook のHTTP リクエストで対応するエンドポイントを使用する必要があります。各エンドポイントの詳細については、[Lob のAPI リファレンスドキュメント](https://lob.com/docs#intro) を参照してください。

| 基本URL | 利用可能なエンドポイント |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ2:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやキャンバスで使用する Lob Webhook テンプレートを作成するには、Braze ダッシュボードの [**テンプレート**] > [**Webhook テンプレート**] に移動します。 

単発の Lob Webhook キャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際に Braze で [**Webhook**] を選択します。

新しいWebhookテンプレートに、次のフィールドに記入してください:

- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

Lob には、認証用の HTTP ヘッダーと HTTP メソッドが必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、[**設定**] タブで `<LOB_API_KEY>` をご使用の Lob API キーに置き換える必要があります。このキーの直後に「:」が付加されており、またこのキーは64進数でエンコードされている必要があります。 

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Braze Webhook ビルダー作成タブに表示されているリクエスト本文のコードと Webhook URL。]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Request body

Lob ポストカードエンドポイントのリクエスト本文の例を次に示します。このリクエスト本文は Braze の 基本 Lobテンプレートで提供されますが、他のエンドポイントを使用する場合は、それに応じて Liquid フィールドを調整する必要があります。

{% raw %}
```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```
{% endraw %}

### ステップ3:リクエストをプレビューする

この時点で、あなたのキャンペーンはテストと送信の準備ができているはずです。エラーが発生した場合は、LobダッシュボードとBraze開発者コンソールのエラーメッセージログを確認する。例えば、以下のエラーは、認証ヘッダーのフォーマットが正しくないために発生した。 

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

![時間、アプリ名、チャンネル、エラーメッセージを示すメッセージエラーログ。エラーメッセージには、メッセージアラートとステータスコードが含まれる。]({% image_buster /assets/img_archive/error_log.png %})

## Lob ウェブフックを使用したイベントの共有 

[Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview) を使用すると、外部プラットフォームから Braze へのデータフローを自動化するための webhook を構築および管理できます。各変換には、他のプラットフォームが Webhook の宛先に使用できる一意のエンドポイントが割り当てられます。

{% alert important %}
Lobのデータ変換テンプレートは、[`/users/track` のエンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track)使用してイベントを送信し、データポイントをログに記録する。LobのWebhook設定でレート制限を設定し、データのオーバーログを避けることをお勧めする。
{% endalert %}

### ステップ 1: Braze で変換を作成する

1. Braze ダッシュボードで、[**データ設定**] > [**データ変換**] に移動し、[**変換の作成**] を選択します。
2. 変換を表す短いわかりやすい名前を入力します。
3. **編集経験**で、**テンプレートを使用**を選択し、Lobを検索してチェックボックスをオンにします。
4. 完了したら、[**変換を作成**] を選択します。次のステップで使用する変換エディターにリダイレクトされます。

### ステップ2: Lob テンプレートの入力

このテンプレートを使用すると、Lob イベントの1 つを、Braze で使用できるカスタムイベントまたは属性に変換できます。インラインコメントに従い、テンプレートの作成を終了します。

{% alert tip %}
Lob の webhook ペイロード構造の詳細については、[Lob を参照してください。Webhook を使用する](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks)。
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### ステップ 3: Lob で Webhook を作成する

1. テンプレートの作成が完了したら、[**アクティブ化する**] を選択し、**Webhook URL** をクリップボードにコピーします。
2. Lob で、[新しい webhook を作成し](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1)、Braze のwebhook URL を使用して webhook を受信します。
