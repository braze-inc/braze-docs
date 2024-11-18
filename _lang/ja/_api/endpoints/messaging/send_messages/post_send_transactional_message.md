---
nav_title: "POST:API トリガー配信でトランザクションメールを送信する"
article_title: "POST:API トリガー配信でトランザクションメールを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、API トリガー配信 Braze エンドポイントを使用したトランザクションメールメッセージの送信に関する詳細について説明します。"

---

{% api %}
# API トリガー配信でトランザクションメールを送信する
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> このエンドポイントを使用して、指定したユーザーに即時の単発トランザクション・メッセージを送信する。

このエンドポイントは、Braze[トランザクションメールキャンペーンと]({{site.baseurl}}/api/api_campaigns/transactional_campaigns)対応するキャンペーンIDの作成と同時に使用される。

{% alert important %}
トランザクションメールは現在、一部の Braze パッケージで利用できます。詳細については、Brazeカスタマー・サクセス・マネージャーまでお問い合わせください。
{% endalert %}

[送信トリガーキャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)と同様に、このキャンペーンタイプでは、Braze ダッシュボード内にメッセージコンテンツを格納すると同時に、API 経由でメッセージを送信するタイミングと送信先を指定できます。メッセージの送信先となるオーディエンスまたはセグメントを受け入れる送信トリガーキャンペーンエンドポイントとは異なり、このキャンペーンタイプは、注文の確認やパスワードのリセットなどのアラートの1対1のメッセージングに特化しているため、このエンドポイントへのリクエストでは、`external_user_id` または `user_alias` で1人のユーザーを指定する必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`transactional.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## パスパラメーター

| パラメータ | 必須 | データ型 | 説明 |
|---|---|---|---|
| `campaign_id` | 必須 | 文字列 | キャンペーンのID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 要求本文:

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

| パラメータ | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| オプション | 文字列 |  Base64互換の文字列。以下の正規表現に対して検証される：<br><br> `/^[a-zA-Z0-9-_+\/=]+$/`<br><br>このオプションのフィールドを使用すると、この特別な送信の内部識別子を渡すことができます。この識別子は、トランザクション HTTP イベントポストバックから送信されるイベントに含まれます。渡されると、この識別子は重複排除キーとしても使用され、Brazeはこれを24時間保存する。<br><br>別のリクエストで同じ識別子を渡すと、24時間はBrazeによる新しい送信インスタンスは生成されない。|
|`trigger_properties`|オプション|オブジェクト|[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。このリクエストでユーザーに適用されるパーソナライゼーションのキーと値のペア。 |
|`recipient`|必須|オブジェクト| このメッセージの対象となるユーザー。`attributes` と単一の `external_user_id` または `user_alias` を含めることができます。<br><br>Brazeにまだ存在しない外部ユーザーIDを指定した場合、`attributes` オブジェクトにフィールドを渡すと、Brazeにこのユーザープロファイルが作成され、新しく作成されたユーザーにこのメッセージが送信されることに注意。<br><br>`attributes` オブジェクトのデータが異なる複数のリクエストを同じユーザーに送信する場合、`first_name`、`last_name`、および `email` 属性は同期的に更新され、メッセージにテンプレートとして組み込まれます。カスタム属性にはこれと同じような保護がないため、この API を使用してユーザーを更新し、異なるカスタム属性値を連続して渡す場合は注意して進めてください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

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

送信トランザクションメールエンドポイントは、このメッセージ送信のインスタンスを表すメッセージの `dispatch_id` で応答します。この識別子は、トランザクション HTTP イベントポストバックのイベントと共に使用して、1人のユーザーに送信された個々のメールのステータスを追跡できます。

### 回答例

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## トラブルシューティング

エンドポイントはまた、場合によってはエラーコードと人間が判読可能なメッセージを返す場合もありますが、そのほとんどは検証エラーです。以下は、無効なリクエストをしたときによく出るエラーである。

| エラー | トラブルシューティング |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | 提供されたキャンペーンIDはトランザクションキャンペーン用ではない。 |
| `The external reference has been queued.  Please retry to obtain send_id.` | external_send_id は最近作成されました。新しいメッセージを送信する場合は、新しい external_send_id を試してください。 |
| `Campaign does not exist` | 指定されたキャンペーンIDが既存のキャンペーンと一致しない。 |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 提供されたキャンペーンIDは、アーカイブされたキャンペーンに対応する。 |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 提供されたキャンペーンIDは、一時停止中のキャンペーンに対応する。 |
| `campaign_id must be a string of the campaign api identifier` | 指定されたキャンペーンIDは有効なフォーマットではない。 |
| `Error authenticating credentials` | 提供されたAPIキーが無効である |
| `Invalid whitelisted IPs `| リクエストを送信しているIPアドレスがIPホワイトリストにない（使用されている場合）。 |
| `You do not have permission to access this resource` | 使用されたAPIキーには、このアクションを実行する権限がない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Brazeのほとんどのエンドポイントにはレートリミットが実装されており、リクエストが多すぎると429レスポンスコードを返す。トランザクション送信エンドポイントは異なる動作をする。割り当てられたレート制限を超えた場合、当社のシステムはAPIコールの取り込みを継続し、成功コードを返し、メッセージを送信するが、これらのメッセージは機能の契約SLAの対象外となる可能性がある。この機能についての詳細が必要な場合は、お問い合わせいただきたい。

## トランザクションHTTPイベントのポストバック

すべてのトランザクションメールは、指定した URL に HTTP リクエストとして返送されるイベントステータスポストバックによって補完されます。これにより、リアルタイムでメッセージのステータスを評価し、メッセージが未配信の場合は別のチャネルでユーザーに到達するようにアクションを取ったり、Brazeに待ち時間が発生している場合は内部システムにフォールバックしたりすることができる。

受信イベントを特定の送信インスタンスに関連付けるには、[API 応答](#example-response)で返される Braze `dispatch_id` をキャプチャして保存するか、独自の識別子を `external_send_id` フィールドに渡すかを選択できます。このフィールドに渡す値の例としては、注文 ID が考えられます。この場合、注文 1234 が完了すると、Braze を介して注文確認メッセージがトリガーされ、`external_send_id : 1234` がリクエストに含まれます。`Sent` や `Delivered` などの後続のすべてのイベントポストバックのペイロードには `external_send_id : 1234` が含まれ、これにより、ユーザーが注文確認メールを正常に受信したことを確認できます。

トランザクションHTTPイベントポストバックの使用を開始するには、Brazeダッシュボードの**「設定」**>「**メール設定**」を開き、「**トランザクションイベントステータスポストバック**」のセクションを見つける。ポストバックを受け取りたいURLを入力する。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは \[**設定の管理**] > \[**メール設定**] にあります。
{% endalert %}

![]({% image_buster /assets/img/transactional_webhook_url.png %})

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

|  ステータス | 説明 |
| ------------ | ----------- |
| `sent` | メッセージがBrazeのメール送信パートナーに正常に送信された |
| `processed` | 電子メール送信パートナーがメッセージを正常に受信し、ユーザーの受信トレイ・プロバイダに送信する準備をした。 |
| `aborted` | Brazeは、ユーザーがメール送信可能なアドレスを持っていないか、メッセージ本文でLiquid abortロジックが呼び出されたために、メッセージを正常に送信できなかった。すべての中止されたイベントのメタデータオブジェクト内には、メッセージが中止された理由を示す `reason` フィールドが含まれています |
|`delivered`| メッセージがユーザーのメール受信箱プロバイダーに受け入れられた |
|`bounced`| メッセージがユーザーのメール受信プロバイダーによって拒否された。すべてのバウンスイベントのメタデータオブジェクト内には、受信トレイプロバイダーによって提供されたバウンスエラーコードを反映する `reason` フィールドが含まれています |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ポストバックの例
```json

// Sent Event
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

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
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

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
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

```


{% endapi %}
