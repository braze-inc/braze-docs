---
nav_title: "POST:API トリガー配信を使用したCanvas メッセージの送信"
article_title: "POST:API トリガー配信を使用したキャンバスメッセージの送信"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「API トリガー配信を使用してキャンバスを送信」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# API トリガー配信を使用したCanvas メッセージの送信
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}。
/canvas/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、API によってトリガーされる配信でキャンバスメッセージを送信します。

API トリガー配信を使用すると、API を使用してメッセージの宛先と送信のタイミングを指定すると同時に、メッセージの内容を Braze ダッシュボードに保存できます。

このエンドポイントでメッセージを送信するには、[キャンバスID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)(キャンバスの構築時に作成されます)が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.trigger.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## 要求本文:

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
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 必須 | string | [キャンバス識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`canvas_entry_properties`| オプション | オブジェクト | これには、[Canvas エントリプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)が含まれます。カスタマイズキーと値のペアは、このリクエストのすべてのユーザーに適用されます。キャンバスエントリのプロパティオブジェクトの最大サイズは 50 KB に制限されています。<br><br>**注:**[キャンバスコンテキスト早期アクセス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)に参加している場合、このパラメーターは `context` で、キャンバスエントリプロパティが含まれます。 |
|`broadcast`| オプション | ブール値 | キャンペーンまたはキャンバスが対象とするSegment全体にメッセージを送信する場合は、`broadcast` をtrue に設定する必要があります。このパラメーターはデフォルトで false です (2017 年 8 月 31 日現在)。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定するときは注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きな視聴者にメッセージが送信される可能性があるためです。 |
|`audience`| オプション| 接続されたオーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`recipients`| オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>指定されておらず、`broadcast` がtrue に設定されている場合、メッセージはキャンバスがターゲットとするセグメント全体に送信されます。<br><br> `recipients` 配列には最大 50 個のオブジェクトを含めることができ、各オブジェクトには 1 つの `external_user_id` 文字列と `canvas_entry_properties` オブジェクトが含まれます。この呼び出しには、`external_user_id`、`user_alias`、または `email` が必要です。リクエストでは 1 つだけ指定する必要があります。<br><br>`email` が識別子の場合、[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) を受信者オブジェクトに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
`recipients` パラメータの場合、`send_to_existing_only` が `true` のとき、Braze は既存のユーザにのみメッセージを送信します。ただし、このフラグは、ユーザーのエイリアスでは使えません。<br><br>`send_to_existing_only` が `false` の場合、属性オブジェクトが含まれていなければなりません。`send_to_existing_only` が `false`** で**、指定された `id` を持つユーザーが存在しない場合、Braze はそのID と属性 を持つユーザーを作成してからメッセージを送信します。
{% endalert %}

サーバー間の呼び出しに API を使用する顧客には、ファイアウォールの内側にある場合は、適切な API URL を許可リストに追加する必要が生じることがあります。

{% alert note %}
API 呼び出しに特定のユーザーとダッシュボードのターゲットセグメントの両方を含めると、メッセージは、API 呼び出しに含まれ、セグメントフィルターの条件を満たすユーザープロファイルにのみ送信されます。
{% endalert %}

## 例のリクエスト
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
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## 対応内容

メッセージ送信エンドポイントの応答には、メッセージのディスパッチを参照できるように、メッセージの `dispatch_id` が含まれます。`dispatch_id` は、メッセージディスパッチの ID です (Braze から送信される「送信」ごとに固有の ID）。詳細については、[ディスパッチIDの動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)を参照してください。

### 成功応答の例

ステータスコード `201` は、次の応答本文を返す可能性があります。キャンバスがアーカイブ、停止、または一時停止されている場合、キャンバスはこのエンドポイントを介して送信されません。

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

キャンバスがアーカイブされている場合は、次の`notice` メッセージが表示されます。"キャンバスがアーカイブされます。キャンバスのアーカイブを解除して、トリガーリクエストが有効になるようにします。"キャンバスがアクティブでない場合は、次の`notice` メッセージが表示されます。"キャンバスは一時停止されます。キャンバスを再開して、トリガーリクエストが有効になるようにしてください。」

リクエストで致命的なエラーが発生した場合のエラーコードと説明については、[エラーとレスポンス]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

## キャンバスの属性オブジェクト

メッセージングオブジェクト`attributes` を使用して、`canvas/trigger/send` エンドポイントを使用してAPI トリガーキャンバスを送信する前に、ユーザーの属性と値を追加、作成、または更新します。この API 呼び出しを使用すると、キャンバスを処理して送信する前に、ユーザー属性オブジェクトを処理します。これにより、[race conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/)によって発生する問題のリスクを最小限に抑えることができます。ただし、デフォルトでは、サブスクリプショングループをこの方法で更新することはできません。

{% alert note %}
このエンドポイントのキャンペーンバージョンを探していますか?[API トリガー配信を使用したキャンペーンメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) を確認します。
{% endalert %}

{% endapi %}
