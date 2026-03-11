---
nav_title: "POST:API トリガー配信を使用したCanvas メッセージの送信"
article_title: "POST:API トリガー配信を使用したキャンバスメッセージの送信"
search_tag: エンドポイント
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「API トリガー配信を使用してキャンバスを送信」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# API トリガー配信を使用したCanvas メッセージの送信
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints  %}
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
  "context": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent `context`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## リクエストパラメーター

| パラメーター | 必須かどうか | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 必須かどうか | string | [キャンバス識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`context`| オプション | オブジェクト | これにはキャンバスのエントリプロパティが含まれる。パーソナライゼーションのキーと値のペアは、このリクエストの全ユーザーに適用される。コンテキストオブジェクトは最大50KBまでである。 |
|`broadcast`| オプション | ブール値 | Brazeダッシュボードでキャンバスのターゲットオーディエンスとして設定されたセグメント全体にメッセージを送信する際には、を`broadcast`trueに設定しなければならない。このパラメーターはデフォルトで false です (2017 年 8 月 31 日現在)。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定するときは注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きな視聴者にメッセージが送信される可能性があるためです。 |
|`audience`| オプション| 接続されたオーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。を含めると`audience`、メッセージは定義されたフィルター（カスタム属性やサブスクリプションステータスなど）に一致するユーザーにのみ送信される。 |
|`recipients`| オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>指定されていない場合、かつ`broadcast`が に設定されている場合、メッセージはBrazeダッシュボードでCanvas`true`のターゲットオーディエンスとして設定されたセグメント全体に送信される。<br><br> `recipients` 配列には最大 50 個のオブジェクトを含めることができ、各オブジェクトには 1 つの `external_user_id` 文字列と `canvas_entry_properties` オブジェクトが含まれます。この呼び出しには、`external_user_id`、`user_alias`、または `email` が必要です。リクエストでは 1 つだけ指定する必要があります。<br><br>`email` が識別子の場合、[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) を受信者オブジェクトに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
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

メッセージ送信エンドポイントの応答には、メッセージの送信元を特定`dispatch_id`するための参照情報が含まれる。`dispatch_id` は、メッセージディスパッチの ID です (Braze から送信される「送信」ごとに固有の ID）。詳細については、[ディスパッチIDの動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)を参照してください。

### 成功応答の例

ステータスコード `201` は、次の応答本文を返す可能性があります。キャンバスがアーカイブされたり、停止されたり、一時停止されたりした場合、キャンバスはこのエンドポイントを通過しない。

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

もしあなたのキャンバスがアーカイブされている場合、この`notice`メッセージが表示される："キャンバスがアーカイブされます。キャンバスのアーカイブを解除して、トリガーリクエストが有効になるようにします。"もしあなたのキャンバスがアクティブでない場合、この`notice`メッセージが表示される："キャンバスは一時停止されます。キャンバスを再開して、トリガーリクエストが有効になるようにしてください。」

リクエストで致命的なエラーが発生した場合のエラーコードと説明については、[エラーとレスポンス]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

## 考慮事項

APIトリガーによる配信でキャンバスメッセージを送信するAPI呼び出しを行う際には、以下の点を考慮せよ。

- **既存ユーザーへの送信**：が（デフォルト値である）`true`に設定されている`send_to_existing_only`場合、メッセージはBrazeの既存ユーザーにのみ送信される。
- **新規ユーザーの作成**：が に設定されている`send_to_existing_only``false`場合、オブジェクト`attributes`を含めなければならない。指定されたIDのユーザーが存在しない場合、BrazeはそのIDと属性でユーザーを作成してからメッセージを送信する。
- **ユーザーエイリアスの制限**：フラグ`send_to_existing_only`はユーザーエイリアスでは使用できない。エイリアスのみのユーザーに送信するには、そのユーザーが既にBrazeに存在している必要がある。
- **セグメントターゲティング**：このエンドポイントでは、その`segment_id`パラメータはサポートされていない。セグメントをターゲットにするには、BrazeダッシュボードのBraze キャンバス内にあるターゲットオーディエンス設定でセグメントを設定し、`broadcast: true`を使用するか、[Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)フィルターで`audience`パラメータを使用する。
- **複合標的化**：パラメータ`recipients`を含め、かつダッシュボードでターゲットセグメントを設定した場合、メッセージはAPI呼び出しで指定されたユーザープロファイルのうち、セグメントのフィルターにも一致するものにのみ送信される。
- **サーバー間通信**：サーバー間通信を行う場合、ファイアウォールの内側にあるなら、適切なAPIのURLを許可リストに追加する必要があるかもしれない。

## キャンバスの属性オブジェクト

メッセージングオブジェクト`attributes` を使用して、`canvas/trigger/send` エンドポイントを使用してAPI トリガーキャンバスを送信する前に、ユーザーの属性と値を追加、作成、または更新します。この API 呼び出しを使用すると、キャンバスを処理して送信する前に、ユーザー属性オブジェクトを処理します。これにより、[race conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/)によって発生する問題のリスクを最小限に抑えることができます。ただし、デフォルトでは、サブスクリプショングループをこの方法で更新することはできません。

{% alert note %}
このエンドポイントのキャンペーンバージョンを探していますか?[API トリガー配信を使用したキャンペーンメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) を確認します。
{% endalert %}

{% endapi %}
