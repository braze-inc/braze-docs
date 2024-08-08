---
nav_title: "ポスト:API トリガー配信によるトランザクションメールの送信"
article_title: "ポスト:API トリガー配信によるトランザクションメールの送信"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、API トリガー配信による Braze エンドポイント経由でトランザクションメールメッセージを送信する方法について詳しく説明します。"

---

{% api %}
# API トリガー配信によるトランザクションメールの送信
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> このエンドポイントを使用して、指定されたユーザーに 1 回限りのトランザクションメッセージを即時に送信します。 

このエンドポイントは、Braze [トランザクションメールキャンペーンとそれに対応するキャンペーン]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) ID の作成と同時に使用されます。

{% alert important %}
トランザクションメールは現在、一部の Braze パッケージの一部としてご利用いただけます。詳細については、Braze カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

[送信トリガーキャンペーンエンドポイントと同様に]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)、このキャンペーンタイプでは、APIを介してメッセージをいつ、誰に送信するかを指定しながら、メッセージコンテンツをBrazeダッシュボード内に格納できます。メッセージを送信するオーディエンスまたはセグメントを受け入れる送信トリガーキャンペーンエンドポイントとは異なり、このエンドポイントへのリクエストはまたはで1人のユーザーを指定する必要があります。このキャンペーンタイプは`user_alias`、`external_user_id`注文確認やパスワードリセットなどのアラートを1：1メッセージで送信することを目的として作成されているためです。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`transactional.send`権限のある API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## パスパラメーター

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `campaign_id` | 必須 | 文字列 | キャンペーンの ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_send_id` | オプション| 文字列| Base64互換の文字列。次の正規表現に対して検証されました。<br><br> `/^[a-zA-Z0-9-_+\/=]+$/`<br><br>このオプションフィールドでは、この特定の送信の内部識別子を渡すことができます。この内部識別子は、Transactional HTTP イベントポストバックから送信されるイベントに含まれます。渡されると、この識別子は重複排除キーとしても使用され、Braze はそれを24時間保存します。<br><br>別のリクエストで同じ識別子を渡しても、Braze による送信の新たなインスタンスは 24 時間発生しません。|
[| `trigger_properties` |オプション|オブジェクト|トリガープロパティを参照してください。]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)このリクエストのユーザーに適用されるパーソナライゼーションキーと値のペア。|
| `recipient` |必須|オブジェクト| このメッセージのターゲットとなるユーザー。`external_user_id`またはを 1 `attributes` つ含めることができます`user_alias`。<br><br>Braze にまだ存在しない外部ユーザー ID を指定した場合、`attributes`オブジェクトにフィールドを渡すと Braze でこのユーザープロファイルが作成され、新しく作成されたユーザーにこのメッセージが送信されることに注意してください。<br><br>`attributes`オブジェクトのデータが異なる複数のリクエストを同じユーザーに送信すると、、`first_name``last_name`、`email`属性が同期的に更新され、メッセージにテンプレート化されます。カスタム属性にはこれと同じ保護機能がないため、この API を使用してユーザーを更新し、異なるカスタム属性値をすばやく連続して渡す場合は注意が必要です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## 応答 

トランザクションメール送信エンドポイントは、`dispatch_id`このメッセージ送信のインスタンスを表すメッセージで応答します。この識別子を Transactional HTTP イベントポストバックのイベントと一緒に使用して、1 人のユーザーに送信された個々の電子メールのステータスを追跡できます。

### 回答例

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## トラブルシューティング

エンドポイントは、エラーコードと人間が読めるメッセージを返す場合もありますが、そのほとんどは検証エラーです。無効なリクエストを行うときに発生する可能性のある一般的なエラーは次のとおりです。

| エラー | トラブルシューティング |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | 入力されたキャンペーン ID はトランザクションキャンペーン用ではありません。|
| `The external reference has been queued.  Please retry to obtain send_id.` | 外部送信IDが最近作成されました。新しいメッセージを送信する場合は、新しい外部送信IDを試してください。|
| `Campaign does not exist` | 入力されたキャンペーン ID は既存のキャンペーンに対応していません。|
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 入力されたキャンペーン ID は、アーカイブされたキャンペーンに対応します。|
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 入力されたキャンペーン ID は、一時停止中のキャンペーンに対応します。|
| `campaign_id must be a string of the campaign api identifier` | 入力されたキャンペーン ID の形式は無効です。|
| `Error authenticating credentials` | 提供された API キーは無効です |
| `Invalid whitelisted IPs ` | リクエストを送信している IP アドレスが IP ホワイトリストに含まれていない (使用されている場合) |
| `You do not have permission to access this resource` | 使用された API キーには、このアクションを実行する権限がありません |
{: .reset-td-br-1 .reset-td-br-2}

Braze のほとんどのエンドポイントには、リクエストが多すぎる場合に 429 応答コードを返すレート制限が実装されています。トランザクション送信エンドポイントの動作は異なります。割り当てられたレート制限を超えると、システムは引き続き API 呼び出しを取り込み、成功コードを返し、メッセージを送信しますが、それらのメッセージは機能の契約上の SLA の対象にならない場合があります。この機能についてさらに情報が必要な場合は、お問い合わせください。

## トランザクション HTTP イベントポストバック

すべてのトランザクションメールは、指定されたURLにHTTPリクエストとして送信されるイベントステータスポストバックによって補完されます。これにより、メッセージステータスをリアルタイムで評価でき、メッセージが配信されない場合は別のチャネルでユーザーに到達するためのアクションを実行でき、Braze で遅延が発生した場合は内部システムにフォールバックできます。

受信イベントを特定のsendインスタンスに関連付けるには、`dispatch_id` [APIレスポンスで返されたBrazeをキャプチャして保存するか](#example-response)、`external_send_id`独自の識別子をフィールドに渡すかを選択できます。このフィールドに渡すことができる値の例としては、注文 ID があります。注文 1234 が完了すると、Braze `external_send_id : 1234` を通じてユーザーに注文確認メッセージが送信され、リクエストに含まれます。やなど`Sent`、`Delivered``external_send_id : 1234`以降のすべてのイベントポストバックがペイロードに含まれ、ユーザーが注文確認メールを正常に受信したことを確認できます。

トランザクション HTTP イベントポストバックの使用を開始するには、Braze ダッシュボードの [設定] > [****メール設定**]** に移動し、[**トランザクションイベントステータスポストバック**] セクションを見つけてください。ポストバックを受け取るには、ご希望のURLを入力してください。

{% alert note %}
[古いナビゲーションを使用している場合]({{site.baseurl}}/navigation)、このページは **[設定の管理] > [メール設定****]** にあります。
{% endalert %}

{% image_buster /assets/img/transactional_webhook_url.png %}

### ポストバック本文

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### メッセージステータス

| ステータス | 説明 |
| ------------ | ----------- |
| `sent` | メッセージが Braze メール送信パートナーに正常に送信されました |
| `processed` | メール送信パートナーは、メッセージを正常に受信し、ユーザーの受信ボックスプロバイダーに送信する準備をしました |
| `aborted` | ユーザーがメール可能なアドレスを持っていないか、メッセージ本文で Liquid abort ロジックが呼び出されたため、Braze がメッセージを正常にディスパッチできませんでした。中止されたすべてのイベントには、`reason`メッセージが中止された理由を示すフィールドがメタデータオブジェクト内に含まれています。|
| `delivered` | メッセージがユーザーのメール受信ボックスプロバイダーによって受け入れられました |
| `bounced` | メッセージはユーザーのメール受信ボックスプロバイダーによって拒否されました。バウンスされたすべてのイベントには、`reason`受信ボックスプロバイダーから提供されたバウンスエラーコードを反映するフィールドがメタデータオブジェクト内に含まれています。
{: .reset-td-br-1 .reset-td-br-2}

### ポストバックの例
\`\`\`json

//送信済みイベント
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "sent",
"metadata": {
"received_at": "2020-08-31T18:58:41.000+00:00",
"enqueued_at": "2020-08-31T18:58:41.000+00:00",
"executed_at": "2020-08-31T18:58:41.000+00:00",
"sent_at": "2020-08-31T18:58:42.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    }

//処理済みイベント
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "processed",
"metadata": {
"processed_at": "2020-08-31T18:58:42.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    }

//中止されました
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "aborted",
"metadata": {
"reason": "User not emailable",
"aborted_at": "2020-08-31T19:04:51.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    }

//配信イベント
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "delivered",
"metadata": {
"delivered_at": "2020-08-31T18:27:32.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    }

//バウンスイベント
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "bounced",
"metadata": {
"bounced_at": "2020-08-31T18:58:43.000+00:00",
"reason": "550 5.1.1 The email account that you tried to reach does not exist",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    }

\`\`\`


{% endapi %}

