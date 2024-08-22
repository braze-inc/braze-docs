---
nav_title: "POST:APIトリガーキャンペーンをスケジュールする"
article_title: "POST:APIトリガーキャンペーンをスケジュールする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「API トリガーキャンペーンのスケジュール」Brazeエンドポイントについての詳細を概説します。"

---
{% api %}
# API トリガー・キャンペーンのスケジュール
{% apimethod post core_endpoint|{1} %}
/campaigns/trigger/schedule/create
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成したキャンペーンメッセージをAPI トリガー配信で送信します。これにより、メッセージの送信をトリガーするアクションを決めることができます。 

メッセージ自体にテンプレート化される `trigger_properties` を渡すことができます。

このエンドポイントを使用してメッセージを送信するには、[API トリガーキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)を構築する際に[キャンペーン ID]({{site.baseurl}}/api/identifier_types/) を作成しておく必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.schedule.create` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' category='メッセージエンドポイント' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
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
|`campaign_id`|必須|string| [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください|
| `send_id` | オプション | string | [送信識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 | 
| `recipients` | オプション | 受信者オブジェクトの配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。 |
| `audience` | オプション | 接続された観客オブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`broadcast`| オプション | ブール値 | キャンペーンやキャンバスがターゲットとするセグメント全体にメッセージを送信する場合は、`broadcast` を true に設定する必要がある。このパラメータはデフォルトで false です (2017年8月31日現在)。<br><br> `broadcast` をtrueに設定すると、`recipients` リストを含めることはできない。ただし、`broadcast: true` 、意図せずこのフラグを設定してしまうと、予想以上に多くの読者にメッセージを送ってしまう可能性があるため、設定には注意が必要である。 |
| `trigger_properties` | オプション | オブジェクト | この送信に含まれるすべてのユーザーのパーソナライゼーションキーと値のペア。[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。 |
| `schedule` | required | スケジュールオブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
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
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## 応答

### 成功応答の例

```json
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
