---
nav_title: "ポスト:スケジュールされたメッセージを作成する"
article_title: "ポスト:スケジュールされたメッセージを作成する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされたメッセージを作成する Braze エンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたメッセージを作成する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> このエンドポイントを使用して、キャンペーン、キャンバス、またはその他のメッセージを指定した時間に送信するようにスケジュールし、そのメッセージを参照して更新を行うための識別子を提供します。 

セグメントをターゲットにしている場合、スケジュールされたすべてのメッセージが送信された後に、[リクエストの記録が開発者コンソールに保存されます](https://dashboard.braze.com/app_settings/developer_console/activitylog/)。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`messages.schedule.create`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "segment_id": (optional, string) see segment identifier,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": { 
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `broadcast` | オプション | Boolean | キャンペーンまたはキャンバスのターゲットとなるセグメント全体にメッセージを送信する場合は、true `broadcast` に設定する必要があります。このパラメーターのデフォルトは false です (2017 年 8 月 31 日現在)。<br><br> が true `broadcast` に設定されている場合、`recipients`リストを含めることはできません。ただし、意図せずにこのフラグを設定すると`broadcast: true`、予想よりも多くのユーザーにメッセージが送信される可能性があるため、設定するときは注意してください。|
| `external_user_ids` | オプション | 文字列の配列 | [外部ユーザー識別子を参照してください]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)。|
| `user_aliases` | オプション | ユーザーエイリアスオブジェクトの配列 | [ユーザーエイリアスオブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/user_alias_object/)。|
| `audience` | オプション | コネクテッドオーディエンスオブジェクト | [コネクテッドオーディエンスを参照してください]({{site.baseurl}}/api/objects_filters/connected_audience/)。|
| `segment_id` | オプション | 文字列 | [セグメント識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。|
[| `campaign_id` |オプション|文字列| キャンペーン識別子を参照してください。]({{site.baseurl}}/api/identifier_types/)|
| `recipients` | オプション | 受信者オブジェクトの配列 | [受信者オブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/recipient_object/)。|
| `send_id` | オプション | 文字列 | [送信識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。|
| `override_messaging_limits` | オプション | ブール値 | キャンペーンのグローバルレート制限を無視、デフォルトは false |
| `recipient_subscription_state` | オプション | 文字列 | これを使用して、オプトインしたユーザーのみ (`opted_in`)、サブスクライブしたユーザーまたはオプトインしているユーザーのみ (`subscribed`)、またはサブスクライブしていないユーザーを含むすべてのユーザーにメッセージを送信します ()。`all`<br><br>`all`ユーザーの使用は、トランザクションメールメッセージングに役立ちます。`subscribed`デフォルトはです。|
| `schedule` | 必須 | スケジュールオブジェクト | [スケジュールオブジェクトを参照]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | オプション | メッセージングオブジェクト | [使用可能なメッセージングオブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/#messaging-objects)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## 応答

### 成功レスポンスの例

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}

