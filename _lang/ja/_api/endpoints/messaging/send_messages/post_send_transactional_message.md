---
nav_title: "POST:API トリガー配信を使用してトランザクションメールを送信する"
article_title: "POST:API トリガー配信を使用してトランザクションメールを送信する"
search_tag: エンドポイント
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
トランザクションメールは現在、一部の Braze パッケージで利用できます。詳細は、担当のBrazeカスタマーサクセスマネージャーに連絡する。
{% endalert %}

[送信トリガーキャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)と同様に、このキャンペーンタイプでは、Braze ダッシュボード内にメッセージコンテンツを格納すると同時に、API 経由でメッセージを送信するタイミングと送信先を指定できます。メッセージの送信先となるオーディエンスまたはセグメントを受け入れる送信トリガーキャンペーンエンドポイントとは異なり、このキャンペーンタイプは、注文の確認やパスワードのリセットなどのアラートの1対1のメッセージングに特化しているため、このエンドポイントへのリクエストでは、`external_user_id` または `user_alias` で1人のユーザーを指定する必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`transactional.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## パスパラメーター

| パラメータ | 必須かどうか | データ型 | 説明 |
|---|---|---|---|
| `campaign_id` | 必須かどうか | 文字列 | キャンペーンのID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## リクエストパラメーター

| パラメーター | 必須かどうか | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| オプション | 文字列 |  Base64互換の文字列。以下の正規表現に対して検証される：<br><br> `/^[a-zA-Z0-9-_+\/=]+$/`<br><br>このオプションフィールドは、特定の送信に対する内部識別子を渡すために使用できる。この識別子は、トランザクショナルHTTPイベントのポストバックから送信されるイベントに含まれる。この識別子が渡されると、重複排除キーとしても使用される。Brazeはこのキーを24時間保存する。<br><br>同じ識別子を別リクエストで渡しても、Brazeは24時間以内に新たな送信インスタンスを生成しない。|
|`trigger_properties`|オプション|オブジェクト|[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。このリクエストのユーザーに適用されるパーソナライゼーションのキーと値のペア。 |
|`recipient`|必須|オブジェクト| このメッセージの対象となるユーザー。`attributes` と単一の `external_user_id` または `user_alias` を含めることができます。<br><br>外部ユーザー IDを指定する場合、そのIDがBrazeに存在しないときは、オブジェクト`attributes`に任意のフィールドを渡すと、Brazeにこのユーザープロファイルが作成され、新規作成されたユーザーにこのメッセージが送信されることに注意せよ。<br><br>同じユーザーに対して異なるデータを複数リクエスト送信した場合、\``attributes`object``first_name`、\``last_name``、`、`email`\`属性は同期的に更新され、メッセージにテンプレートとして組み込まれる。カスタム属性にはこれと同じような保護がないため、この API を使用してユーザーを更新し、異なるカスタム属性値を連続して渡す場合は注意して進めてください。|
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

トランザクションメール送信エンドポイントは、このメッセージ送信のインスタンスを表すメッセージ`dispatch_id`を返す。この識別子は、トランザクション HTTP イベントポストバックのイベントと共に使用して、1人のユーザーに送信された個々のメールのステータスを追跡できます。

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
| `The external reference has been queued.  Please retry to obtain send_id.` | このアカウントはexternal_send_id最近作成されたものだ。新しいメッセージを送るつもりなら、external_send_id新しいアカウントを試してみろ。 |
| `Campaign does not exist` | 指定されたキャンペーンIDが既存のキャンペーンと一致しない。 |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 提供されたキャンペーンIDは、アーカイブされたキャンペーンに対応する。 |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 提供されたキャンペーンIDは、一時停止中のキャンペーンに対応する。 |
| `campaign_id must be a string of the campaign api identifier` | 指定されたキャンペーンIDは有効なフォーマットではない。 |
| `Error authenticating credentials` | 提供されたAPIキーが無効である |
| `Invalid whitelisted IPs `| リクエストを送信しているIPアドレスがIPホワイトリストにない（使用されている場合）。 |
| `You do not have permission to access this resource` | 使用されたAPIキーには、このアクションを実行する権限がない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Brazeのほとんどのエンドポイントにはレート制限が実装されており、リクエストが多すぎると429のレスポンスコードを返す。トランザクション送信エンドポイントには、有料の時間単位割り当てがある。これは単位で測定される（例：パッケージに応じて1時間あたり50,000単位）。このエンドポイントには個別のレート制限はない。割り当てられた量を超えて送信できるが、SLAの対象となるのは割り当て量のみだ。割り当て量を超えるリクエストは送信されるが、SLAの対象外となる。このエンドポイントへのリクエストは[、全体の外部APIレート制限]({{site.baseurl}}/api/api_limits/)にカウントされる。その制限（例えば、全エンドポイントで1時間あたり25万リクエスト）を超過した場合、Brazeは429を返し、制限がリセットされるまでリクエストを制限する。取引件数は毎時リセットされる。この機能についてさらに情報が必要な場合は、Brazeサポートに連絡せよ。

## トランザクションHTTPイベントのポストバック

{% multi_lang_include http_event_postback.md %}

{% endapi %}