---
nav_title: "POST:APIのみを使用してメッセージを即座に送信する"
article_title: "POST:APIのみを使用してメッセージを即座に送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIのみを使用したBrazeエンドポイントによるメッセージの即時送信についての詳細を説明します。"

---
{% api %}
# APIのみを使用してメッセージを即座に送信する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> このエンドポイントを使用して、Braze API で指定したユーザーに即時メッセージを送信します。

セグメントをターゲットにしている場合、リクエストの記録は[開発者コンソール](https://dashboard.braze.com/app_settings/developer_console/activitylog/)に保存されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
このエンドポイントを API キャンペーンで使用する場合、リクエストが成功するためには、受信者が既に Braze に存在している必要があります。これは、`external_user_ids` または `user_aliases` パラメーターでユーザーを指定する際に適用されます。
{% endalert %}

### API送信で新規ユーザーを作成する

APIを使用して送信の一部としてユーザーを作成する必要がある場合、次の2つの方法があります。

#### オプション 1: `/users/track` を使用してから送信する

まず、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントでユーザーを作成し、データが伝播するのを待ちます（通常、数分間待つことを推奨します）。その後に APIのみの送信を開始します。Braze は `/users/track` のデータ処理時間を保証しないため、これらの呼び出し間に十分な時間を設けない場合、[競合]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions)が発生する可能性があります。

#### オプション 2: APIトリガー型キャンペーンまたはキャンバスを使用する

[APIトリガー型キャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)または[キャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)ワークフローを使用します。これらを使用すると、受信者がまだ存在しない場合に作成できます。このオプションはバックエンドのプロセスを簡素化しますが、Braze ダッシュボードでキャンペーンまたはキャンバスを設定する必要があります。


## 前提条件

このエンドポイントを使用するには、`messages.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## リクエスト本文

{% alert tip %}
リクエストを完了するために、必ず[メッセージングオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)を本文に含めてください。
{% endalert %}

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
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`broadcast`| オプション | ブール値 | キャンペーンまたはキャンバスが対象とするセグメント全体にメッセージを送信する場合は、`broadcast` を true に設定する必要があります。このパラメーターはデフォルトで false です（2017年8月31日現在）。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定する場合は注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きなオーディエンスにメッセージが送信される可能性があります。 |
|`external_user_ids` | オプション | 文字列の配列 | [外部ユーザー ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) を参照してください。 |
|`user_aliases`| オプション | ユーザー別名オブジェクトの配列 | [ユーザー別名オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。 |
|`segment_id `| オプション | 文字列 | [セグメント識別子]({{site.baseurl}}/api/identifier_types/#segment-identifier)を参照してください。 |
|`audience`| オプション | 接続済みオーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`campaign_id`| オプション* | 文字列 | 詳細は[キャンペーン識別子]({{site.baseurl}}/api/identifier_types/#campaign-identifier/)を参照してください。<br><br>*キャンペーンの指標（_送信数_、_クリック数_、_バウンス_など）を Braze ダッシュボードでトラッキングしたい場合、またはユーザープロファイルの[メッセージ履歴タブ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#messaging-history-tab)でこのメッセージに関連するイベントを確認したい場合は必須です。 |
|`send_id`| オプション | 文字列 | [送信識別子]({{site.baseurl}}/api/identifier_types/#send-identifier)を参照してください。 |
|`override_frequency_capping`| オプション | ブール値 | キャンペーンの `frequency_capping` を無視します。デフォルトは `false` です。 |
|`recipient_subscription_state`| オプション | 文字列 | これを使用して、オプトインしたユーザーのみ（`opted_in`）、配信登録済みかオプトインしているユーザーのみ（`subscribed`）、または配信停止済みのユーザーを含むすべてのユーザー（`all`）にメッセージを送信します。<br><br>`all` ユーザーへの送信は、トランザクションメールメッセージングに便利です。デフォルトは `subscribed` です。 |
|`messages`| オプション | メッセージングオブジェクト | [利用可能なメッセージングオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

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

## 応答の詳細

メッセージ送信エンドポイントの応答には、メッセージのディスパッチを参照するための `dispatch_id` が含まれます。`dispatch_id` はメッセージディスパッチの ID であり、Braze から送信される各「送信」に固有の ID です。詳しくは、[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)を参照してください。

{% endapi %}