---
nav_title: "POST:APIトリガーのキャンバスをスケジュールする"
article_title: "POST:APIトリガーのキャンバスをスケジュールする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「API トリガーキャンバスのスケジュール」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# APIトリガーのキャンバスをスケジュールする
{% apimethod post core_endpoint|{1} %}
/canvas/trigger/schedule/create
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信を介してキャンバスメッセージをスケジュールします。これにより、メッセージの送信をトリガーするアクションを決めることができます。 

キャンバスの最初のステップで送信されるメッセージにテンプレート化される `canvas_entry_properties` を渡すことができます。

このエンドポイントを使用してメッセージを送信するには、キャンバスを構築するときに作成される[キャンバス ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.trigger.schedule.create` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' category='メッセージエンドポイント' %}

## Request body

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

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|必須|string| [キャンバス識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `recipients` | オプション | 受信者オブジェクトの配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。 |
| `audience` | オプション | 接続された観客オブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`broadcast`| オプション | ブール値 | キャンペーンやキャンバスがターゲットとするセグメント全体にメッセージを送信する場合は、`broadcast` を true に設定する必要がある。このパラメーターはデフォルトで false です (2017年8月31日現在)。<br><br> `broadcast` をtrueに設定すると、`recipients` リストを含めることはできない。ただし、`broadcast: true` 、意図せずこのフラグを設定してしまうと、予想以上に多くの読者にメッセージを送ってしまう可能性があるため、設定には注意が必要である。 |
| `canvas_entry_properties` | オプション | オブジェクト | この送信に含まれるすべてのユーザーのパーソナライゼーションキーと値のペア。[キャンバスエントリープロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object)を参照してください。 |
| `schedule` | required | スケジュールオブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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