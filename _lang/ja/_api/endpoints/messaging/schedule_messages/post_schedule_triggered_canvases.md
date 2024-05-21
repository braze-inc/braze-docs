---
nav_title: "ポスト:API トリガーキャンバスのスケジュール設定"
article_title: "ポスト:API トリガーキャンバスのスケジュール設定"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Schedule API によってトリガーされる Canvases Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# API によってトリガーされる Canvases のスケジュール設定
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/create
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信を介して Canvas メッセージをスケジュールし、メッセージの送信をトリガーするアクションを決定できます。 

Canvas の最初のステップで送信されるメッセージにテンプレート化されるものを渡す `canvas_entry_properties` ことができます。

このエンドポイントでメッセージを送信するには、Canvas の構築時に作成された [Canvas ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `canvas.trigger.schedule.create` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the
  // Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|必須項目|文字列|「 [キャンバス識別子]({{site.baseurl}}/api/identifier_types/)」を参照してください。|
| `recipients` |オプション |受信者オブジェクトの配列 | [受信者オブジェクト (recipients object)]({{site.baseurl}}/api/objects_filters/recipient_object/) を参照。|
| `audience` |オプション |接続されたオーディエンスオブジェクト | [「接続されたオーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)」を参照してください。|
|`broadcast`|オプション |ブーリアン |キャンペーンまたはキャンバスがターゲットとするセグメント全体にメッセージを送信する場合は、true に設定する `broadcast` 必要があります。このパラメーターの既定値は false です (2017 年 8 月 31 日現在)。<br><br> `broadcast`が true に設定されている場合、`recipients`リストを含めることはできません。ただし、 を設定するときは `broadcast: true`、このフラグを意図せずに設定すると、予想よりも多くのオーディエンスにメッセージが送信される可能性があるため、注意が必要です。 |
| `canvas_entry_properties` |オプション |オブジェクト |この送信のすべてのユーザーのパーソナライゼーションのキーと値のペア。[「Canvas エントリのプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object)」を参照してください。|
| `schedule` |必須項目 |スケジュール オブジェクト | [スケジュール・オブジェクト (schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/)) を参照。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties": {}
    }
  ],
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
  "broadcast": false,
  "canvas_entry_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## 応答

### 成功応答の例

```
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}