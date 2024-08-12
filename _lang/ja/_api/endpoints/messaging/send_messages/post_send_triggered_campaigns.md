---
nav_title: "ポスト:API トリガ配信を使用したキャンペーンの送信"
article_title: "ポスト:API トリガ配信を使用したキャンペーンの送信"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、API トリガー配信Braze エンドポイントを使用した送信キャンペーンの詳細について説明します。"

---
{% api %}
# API トリガー配信を使用したキャンペーンメッセージの送信
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信を介して、指定されたユーザに即時のワンオフメッセージを送信します。 

API トリガー配信では、メッセージが送信されたとき、およびAPI 経由で誰に送信されるかを指示しながら、Braze ダッシュボード内にメッセージコンテンツを保存できます。

セグメントをターゲットとしている場合、リクエストのレコードは[Developer Console](https://dashboard.braze.com/app_settings/developer_console/activitylog/) に保存されます。このエンドポイントでメッセージを送信するには、[キャンペーンID](https://www.braze.com/docs/api/identifier_types/) を作成し、[API トリガキャンペーン]({{site.baseurl}}/api/api_campaigns/) を作成する必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.send` 権限を持つAPI キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message will send to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
  ]
}
```

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|文字列|参照[キャンペーン識別子]({{site.baseurl}}/api/identifier_types/).|
|`send_id`| オプション| 文字列| [送信識別子]({{site.baseurl}}/api/identifier_types/)を参照|
|`trigger_properties`| オプション| オブジェクト| [トリガプロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。この要求のすべてのユーザーに適用されるカスタマイズキーと値のペア。|
||`broadcast`| オプション| ブール| キャンペーンまたはキャンバスがターゲットとするセグメント全体にメッセージを送信するときは、`broadcast` をtrue に設定する必要があります。このパラメーターのデフォルトはfalse です(2017年8 月31 日現在)。<br><br> `broadcast` がtrue に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定するときは注意が必要です。意図せずにこのフラグを設定すると、期待した視聴者よりも大きな視聴者にメッセージが送信される可能性があります。|
|`audience`| オプション| 接続されたオーディエンスオブジェクト| [接続されたオーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照|
|`recipients`| オプション| 配列| [recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>`send_to_existing_only` が`false` の場合、属性オブジェクトを含める必要があります。<br><br>`recipients` が指定されず、`broadcast` がtrue に設定されている場合、メッセージはキャンペーンの対象となるセグメント全体に送信されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- recipients 配列には、最大50 個のオブジェクトを含めることができます。各オブジェクトには、単一の`external_user_id` 文字列と`trigger_properties` オブジェクトが含まれます。
- `send_to_existing_only` が`true` の場合、Braze はメッセージを既存のユーザにのみ送信します。ただし、このフラグはユーザーエイリアスでは使用できません。 
- `send_to_existing_only` が`false` の場合、属性を含める必要があります。Braze は、`id` と属性を持つユーザを作成してからメッセージを送信します。

ユーザのサブスクリプショングループのステータスは、`subscription_groups` パラメータを`attributes` オブジェクトに含めることで更新できます。詳細については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)を参照してください。

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ]
}'
```

## 対応内容

メッセージ送信エンドポイント応答には、メッセージのディスパッチへの参照のためのメッセージの`dispatch_id` が含まれます。`dispatch_id` はメッセージディスパッチのID で、Braze から送信される各送信の一意のID です。このエンドポイントを使用すると、バッチ処理されたユーザーのセット全体に対して単一の`dispatch_id` を受け取ります。`dispatch_id` の詳細については、[ Dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) のドキュメントを参照してください。

## 送信エンドポイントの作成

**キャンペーンでの属性オブジェクトの使用**

Braze には、`attributes` というメッセージングオブジェクトがあり、API トリガキャンペーンを送信する前に、ユーザの属性と値を追加、作成、または更新できます。このAPI コールとして`campaign/trigger/send` エンドポイントを使用すると、ユーザー属性オブジェクトが処理され、キャンペーンが送信される前に処理されます。これにより、[race conditions]({{site.baseurl}}/help/best_practices/race_conditions/)に起因する問題が発生するリスクを最小限に抑えることができます。 

{% alert important %}
このエンドポイントのキャンバスバージョンを探していますか?[APIトリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint)を確認してください。
{% endalert %}

{% endapi %}
