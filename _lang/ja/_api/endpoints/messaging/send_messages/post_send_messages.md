---
nav_title: "POST:APIのみを使用してメッセージを即座に送信する"
article_title: "POST:APIのみを使用してメッセージを即座に送信する"
search_tag: エンドポイント
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIのみを使用したBrazeエンドポイントによるメッセージの即時送信についての詳細を概説する。"

---
{% api %}
# APIのみを使用してメッセージを即座に送信する
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints  %}
/messages/send
{% endapimethod %}

> このエンドポイントを使用して、Braze APIを使用して指定したユーザーに即時メッセージを送信する。

セグメントをターゲットにしている場合、リクエストの記録は[開発者コンソール](https://dashboard.braze.com/app_settings/developer_console/activitylog/)に保存されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
このエンドポイントをAPIキャンペーンで使用する場合、リクエストが成功するためには、受信者が既にBrazeに存在している必要がある。これは、\`\` または \`\``user_aliases` `external_user_ids`パラメータでユーザーを指定する際に適用される。
{% endalert %}

### API送信で新規ユーザーを作成する

APIを使用して送信の一部としてユーザーを作成する必要がある場合、次の2つの方法がある：

#### オプション 1: 使え`/users/track`　それから送れ

まず、エンド[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)ポイントでユーザーを作成する。その後、データが伝播するのを待つ（通常、数分間待つことを推奨する）。その後にAPIのみの送信を開始する。Brazeはデータ処理時間を保証しないことに注意せよ。したがって、これらの`/users/track`呼び出し間に十分な時間を設けない場合、[競合]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions)が発生する可能性がある。

#### オプション 2: APIトリガー型キャンペーンまたはキャンバスを使用する

[APIトリガー型キャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)または[キャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)ワークフローを使用する。これらは、受信者がまだ存在しない場合に作成することを可能にする。このオプションはバックエンドのプロセスを簡素化するが、Brazeダッシュボードでキャンペーンまたはキャンバスを設定する必要がある。


## 前提条件

このエンドポイントを使用するには、`messages.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Request body

{% alert tip %}
リクエストを完了させるために、必ず[メッセージングオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)を本文に含めてください。
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

| パラメーター | 必須かどうか | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`broadcast`| オプション | ブール値 | キャンペーンまたはキャンバスが対象とするSegment全体にメッセージを送信する場合は、`broadcast` をtrue に設定する必要があります。このパラメーターはデフォルトで false です (2017 年 8 月 31 日現在)。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、設定 `broadcast: true` の場合は注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きなオーディエンスにメッセージが送信される可能性があるためです。 |
|`external_user_ids` | オプション | 文字列の配列 | [外部ユーザーID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)を参照してください。 |
|`user_aliases`| オプション | ユーザー別名オブジェクトの配列| [ユーザー別名オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。 |
|`segment_id `| オプション | 文字列 | [セグメント識別子]({{site.baseurl}}/api/identifier_types/#segment-identifier)を参照してください。 |
|`audience`| オプション | 接続されたオーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`campaign_id`| オプション* | 文字列 | 詳細は[キャンペーン識別子を]({{site.baseurl}}/api/identifier_types/#campaign-identifier/)参照のこと。<br><br>キャンペーンの指標（_送信数_、_クリック数_、_バウンス_など）をBrazeダッシュボードでトラッキングしたい場合、必須である。 |
|`send_id`| オプション | 文字列 | [送信識別子]({{site.baseurl}}/api/identifier_types/#send-identifier)を参照してください。 |
|`override_frequency_capping`| オプション | ブール値 | キャンペーンでは`frequency_capping` を無視する。デフォルトは`false` 。 |
|`recipient_subscription_state`| オプション | 文字列 | これを使用して、オプトインしたユーザーのみ (`opted_in`)、配信登録済みかオプトインしているユーザーのみ (`subscribed`)、または配信停止済みのユーザーを含むすべてのユーザー (`all`) にメッセージを送信します。<br><br>`all` ユーザーは、トランザクションメールメッセージングに使用すると便利です。デフォルトは `subscribed` です。 |
|`messages`| オプション | メッセージングオブジェクト | [利用可能なメッセージングオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
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

## 対応内容

メッセージ送信エンドポイントの応答には、メッセージのディスパッチを参照できるように、メッセージの `dispatch_id` が含まれます。`dispatch_id` は、メッセージディスパッチの ID です。つまり、Braze から送信される「送信」ごとに固有の ID です。詳しくは、[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)を参照してください。

{% endapi %}
