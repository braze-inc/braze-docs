---
nav_title: "ポスト:API トリガー配信による Canvas メッセージの送信"
article_title: "ポスト:API トリガー配信による Canvas メッセージの送信"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIトリガー配信によるCanvases送信Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# API トリガー配信による Canvas メッセージの送信
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信で Canvas メッセージを送信します。 

API トリガー配信を使うと、メッセージコンテンツを Braze ダッシュボードに保存しながら、メッセージをいつ送信するか、API 経由で誰に送信するかを指定できます。

このエンドポイントでメッセージを送信するには、[Canvas ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (Canvas の作成時に作成される) が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.trigger.send`権限のある API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [キャンバス識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。|
| `canvas_entry_properties` | オプション| オブジェクト| [Canvasエントリプロパティを参照してください]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)。このリクエストのすべてのユーザーに適用されるパーソナライゼーションキーと値のペア。Canvas エントリプロパティオブジェクトの最大サイズは 50 KB です。|
| `broadcast` | オプション | Boolean | キャンペーンまたはキャンバスのターゲットとなるセグメント全体にメッセージを送信する場合は、true `broadcast` に設定する必要があります。このパラメーターのデフォルトは false です (2017 年 8 月 31 日現在)。<br><br> が true `broadcast` に設定されている場合、`recipients`リストを含めることはできません。ただし、意図せずにこのフラグを設定すると`broadcast: true`、予想よりも多くのユーザーにメッセージが送信される可能性があるため、設定するときは注意してください。|
[| `audience` | オプション| 接続オーディエンスオブジェクト | 接続オーディエンスを参照してください。]({{site.baseurl}}/api/objects_filters/connected_audience/)|
| `recipients` | オプション | 配列 | [受信者オブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/recipient_object/)。指定せずに true に設定すると、`broadcast`メッセージは Canvas の対象となるセグメント全体に送信されます。<br><br> `recipients`配列には最大 50 個のオブジェクトを含めることができ、各オブジェクトには 1 `external_user_id` `canvas_entry_properties` つの文字列とオブジェクトが含まれます。`external_user_id``user_alias`この呼び出しにはまたはが必要です。リクエストは 1 つだけ指定する必要があります。<br><br> の場合`true`、Braze `send_to_existing_only` は既存のユーザーにのみメッセージを送信しますが、このフラグはユーザーエイリアスでは使用できません。`send_to_existing_only``false`がで、`id`指定されたユーザーが存在しない場合、Brazeはメッセージを送信する前にそのIDと属性を持つユーザーを作成します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

サーバー間の呼び出しに API を使用するお客様は、ファイアウォールの内側にいる場合は、適切な API URL をホワイトリストに登録する必要があります。

{% alert note %}
API 呼び出しに特定のユーザーを含め、ダッシュボードにターゲットセグメントを含めると、メッセージは API 呼び出しに含まれていてセグメントフィルターの対象となるユーザープロファイルにのみ送信されます。
{% endalert %}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99},
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
      "external_user_id": "user_identifier",
      "trigger_properties": "",
      "canvas_entry_properties": "",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## 回答詳細

メッセージ送信エンドポイントの応答には、`dispatch_id`メッセージの送信時に参照するためのメッセージが含まれます。`dispatch_id`はメッセージディスパッチのID（Brazeプラットフォームから送信される各「送信」に固有のID）です。詳細については、「[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)」を参照してください。

## 送信エンドポイントの作成

**キャンバスでの属性オブジェクトの使用**

Brazeには、`canvas/trigger/send`エンドポイントを使用してAPIトリガーのCanvasを送信する前に、ユーザーの属性や値を追加、作成、`Attributes`または更新できるというMessaging Objectがあります。このAPI呼び出しは、Canvasを処理して送信する前にUser Attributesオブジェクトを処理するためです。これにより、[競合状態による問題が発生するリスクを最小限に抑えることができます]({{site.baseurl}}/help/best_practices/race_conditions/)。

{% alert important %}
このエンドポイントのキャンペーンバージョンをお探しですか？「[API トリガー配信によるキャンペーンメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)」を参照してください。
{% endalert %}

{% endapi %}

