---
nav_title: "ポスト:API 経由でのみメッセージを即時送信"
article_title: "ポスト:API 経由でのみメッセージを即時送信"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIのみのBrazeエンドポイントを介してメッセージをすぐに送信する方法について詳しく説明します。"

---
{% api %}
# API 経由でのみメッセージをすぐに送信
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> このエンドポイントを使用して、Braze API を介して指定されたユーザーに即時メッセージを送信します。 

リクエストを完了するには、必ず本文にメッセージングオブジェクトを含めてください。

セグメントをターゲットにしている場合、[リクエストの記録は開発者コンソールに保存されます](https://dashboard.braze.com/app_settings/developer_console/activitylog/)。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`messages.send`権限のある API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

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
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "apple_push": (optional, apple push object),
     "android_push": (optional, android push object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "email": (optional, email object),
     "webhook": (optional, webhook object),
     "content_card": (optional, content card object),
     "sms": (optional, SMS object),
     "whats_app": (optional, WhatsApp object)
   }
 }
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `broadcast` | オプション | Boolean | キャンペーンまたはキャンバスのターゲットとなるセグメント全体にメッセージを送信する場合は、true `broadcast` に設定する必要があります。このパラメーターのデフォルトは false です (2017 年 8 月 31 日現在)。<br><br> が true `broadcast` に設定されている場合、`recipients`リストを含めることはできません。ただし、意図せずにこのフラグを設定すると`broadcast: true`、予想よりも多くのユーザーにメッセージが送信される可能性があるため、設定するときは注意してください。|
| `external_user_ids` | オプション | 文字列の配列 | [外部ユーザーIDを参照してください]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)。|
| `user_aliases` | オプション | ユーザーエイリアスオブジェクトの配列| [ユーザーエイリアスオブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/user_alias_object/)。|
| `segment_id ` | オプション | 文字列 | [セグメント識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。|
| `audience` | オプション | コネクテッドオーディエンスオブジェクト | [コネクテッドオーディエンスを参照してください]({{site.baseurl}}/api/objects_filters/connected_audience/)。|
| `campaign_id` | オプション* | 文字列 | 詳細については、[キャンペーン ID]({{site.baseurl}}/api/identifier_types/) を参照してください。<br><br>\*Braze 管理画面でキャンペーンの統計情報 (送信、クリック、バウンスなど) をトラッキングする場合は必須です。|
| `send_id` | オプション | 文字列 | [送信識別子を参照]({{site.baseurl}}/api/identifier_types/) |
| `override_frequency_capping` | オプション | ブール値 | キャンペーンでは無視`frequency_capping`、デフォルトはです。`false`|
| `recipient_subscription_state` | オプション | 文字列 | これを使用して、オプトインしたユーザーのみ (`opted_in`)、サブスクライブしたユーザーまたはオプトインしているユーザーのみ (`subscribed`)、またはサブスクライブしていないユーザーを含むすべてのユーザーにメッセージを送信します ()。`all`<br><br>`all`ユーザーの使用は、トランザクションメールメッセージングに役立ちます。`subscribed`デフォルトはです。|
| `messages` | オプション | メッセージングオブジェクト | [使用可能なメッセージングオブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/#messaging-objects)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## 回答詳細

メッセージ送信エンドポイントの応答には、`dispatch_id`メッセージの送信時に参照するためのメッセージが含まれます。`dispatch_id`はメッセージディスパッチのIDです。つまり、Brazeから送信される各「送信」に固有のIDです。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。

{% endapi %}

