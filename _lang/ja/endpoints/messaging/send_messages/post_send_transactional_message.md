---
nav_title: "POST:API トリガー配信を使用してトランザクションメールを送信する"
article_title: "POST:API トリガー配信を使用してトランザクションメールを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、API トリガー配信 Braze エンドポイントを使用したトランザクションメールメッセージの送信に関する詳細について説明します。"

---

{% api %}
# API トリガー配信を使用してトランザクションメールを送信する
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> このエンドポイントを使用して、指定したユーザーに即時の単発トランザクション・メッセージを送信する。

このエンドポイントは、Braze[トランザクションメールキャンペーンと]({{site.baseurl}}/api/api_campaigns/transactional_campaigns)対応するキャンペーンIDの作成と同時に使用される。

{% alert important %}
トランザクションメールは現在、一部の Braze パッケージで利用できます。詳しくはBrazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

[送信トリガーキャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)と同様に、このキャンペーンタイプでは、Braze ダッシュボード内にメッセージコンテンツを格納すると同時に、API 経由でメッセージを送信するタイミングと送信先を指定できます。メッセージの送信先となるオーディエンスまたはセグメントを受け入れる送信トリガーキャンペーンエンドポイントとは異なり、このキャンペーンタイプは、注文の確認やパスワードのリセットなどのアラートの1対1のメッセージングに特化しているため、このエンドポイントへのリクエストでは、`external_user_id` または `user_alias` で1人のユーザーを指定する必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`transactional.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
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

| パラメーター | required | データ型 | 説明 |
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
| `The external reference has been queued.  Please retry to obtain send_id.` | external_send_id 、最近作成されたものである。新しいメッセージを送信する場合は、新しいexternal_send_id 。 |
| `Campaign does not exist` | 指定されたキャンペーンIDが既存のキャンペーンと一致しない。 |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 提供されたキャンペーンIDは、アーカイブされたキャンペーンに対応する。 |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 提供されたキャンペーンIDは、一時停止中のキャンペーンに対応する。 |
| `campaign_id must be a string of the campaign api identifier` | 指定されたキャンペーンIDは有効なフォーマットではない。 |
| `Error authenticating credentials` | 提供されたAPIキーが無効である |
| `Invalid whitelisted IPs `| リクエストを送信しているIPアドレスがIPホワイトリストにない（使用されている場合）。 |
| `You do not have permission to access this resource` | 使用されたAPIキーには、このアクションを実行する権限がない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Brazeのほとんどのエンドポイントにはレートリミットが実装されており、リクエストが多すぎると429レスポンスコードを返す。トランザクション送信エンドポイントは異なる動作をする。割り当てられたレート制限を超えた場合、当社のシステムはAPIコールの取り込みを継続し、成功コードを返し、メッセージを送信するが、これらのメッセージは機能の契約SLAの対象外となる可能性がある。この機能についての詳細が必要な場合は、Brazeサポートに問い合わせること。

## トランザクションHTTPイベントのポストバック

{% multi_lang_include http_event_postback.md %}

{% endapi %}
