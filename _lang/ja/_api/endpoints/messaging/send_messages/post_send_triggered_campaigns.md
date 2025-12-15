---
nav_title: "POST:APIトリガー配信でキャンペーンを送る"
article_title: "POST:API トリガー配信でキャンペーンを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、API トリガー配信 Braze エンドポイントを使用したキャンペーンの送信の詳細について説明します。"

---
{% api %}
# API トリガー配信を使用したキャンペーンメッセージの送信
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信を使用して、指定したユーザーに即時の1回限りのメッセージを送信します。

API トリガー配信を使用すると、メッセージの内容を Braze ダッシュボード内に保存し、メッセージが送信されるタイミングと送信先を API を使用して指定できます。

セグメンテーションをターゲットにしている場合、リクエストの記録は[開発者コンソールに](https://dashboard.braze.com/app_settings/developer_console/activitylog/)保存される。このエンドポイントを使用してメッセージを送信するには、[API トリガーキャンペーン]({{site.baseurl}}/api/api_campaigns/)を構築する際に[キャンペーン ID](https://www.braze.com/docs/api/identifier_types/) を作成しておく必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|文字列|[キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`send_id`| オプション | 文字列 | [送信識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`trigger_properties`| オプション | オブジェクト | [トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。パーソナライゼーションのキーと値のペアは、このリクエストのすべてのユーザーに適用される。 |
|`broadcast`| オプション | ブール値 | キャンペーンまたはキャンバスが対象とするSegment全体にメッセージを送信する場合は、`broadcast` をtrue に設定する必要があります。このパラメーターはデフォルトで false です (2017 年 8 月 31 日現在)。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定するときは注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きな視聴者にメッセージが送信される可能性があるためです。 |
|`audience`| オプション | 接続されたオーディエンスオブジェクト| [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`recipients`| オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>`send_to_existing_only` が `false` の場合、属性オブジェクトが含まれていなければなりません。<br><br>`recipients` が提供されず、`broadcast` がtrueに設定されている場合、メッセージはキャンペーンがターゲットとしているセグメンテーション全体に送信される。<br><br> `email` が識別子の場合、[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) を受信者オブジェクトに含める必要があります。 |
|`attachments`| オプション | 配列 | `broadcast` が true に設定されている場合、`attachments` リストを含めることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- 受信者配列には最大50個のオブジェクトを含めることができ、各オブジェクトには1つの `external_user_id` 文字列と `trigger_properties` オブジェクトが含まれます。
- `send_to_existing_only` が`true` （デフォルト）の場合、Brazeは既存ユーザーにのみメッセージを送信する。`false` 、アトリビューションオブジェクトを設定すると、Brazeはユーザーが存在しない場合に新しいユーザーを作成する。`send_to_existing_only` を`false` に設定することは、ユーザー・エイリアスではサポートされていない。エイリアスのみのユーザーに送信するには、そのユーザーがすでにBrazeに存在している必要がある。

ユーザのサブスクリプショングループのステータスは、`subscription_groups` パラメータを`attributes` オブジェクトに含めることで更新できます。詳細については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)を参照してください。

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## 対応内容

メッセージ送信エンドポイントのレスポンスには、メッセージのディスパッチ時に参照できるように、メッセージの`dispatch_id` 。`dispatch_id` はメッセージディスパッチの ID で、Braze から送信される各送信に固有の ID です。このエンドポイントを使用すると、バッチ処理されたユーザーセット全体に対して1つの `dispatch_id` を受け取ります。`dispatch_id` の詳細については、[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)に関するドキュメントを参照してください。

リクエストで致命的なエラーが発生した場合のエラーコードと説明については、[エラーとレスポンス]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

## キャンペーンの属性オブジェクト

Brazeには、`attributes` というメッセージングオブジェクトがあり、APIトリガーキャンペーンを送信する前に、ユーザーの属性や値を追加、作成、更新することができる。このAPIコールとして`campaign/trigger/send` エンドポイントを使用すると、キャンペーンを処理して送信する前に、ユーザー属性オブジェクトを処理する。これにより、[競合]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) による問題が発生するリスクを最小限に抑えることができます。

{% alert tip %}
このエンドポイントのキャンバスバージョンをお探し？[APIトリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint)をチェックしてください。
{% endalert %}

{% endapi %}
