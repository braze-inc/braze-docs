---
nav_title: "POST:API トリガー配信でキャンペーンを送信する"
article_title: "POST:API トリガー配信でキャンペーンを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIトリガー配信Brazeエンドポイントを経由してキャンペーンを送信についての詳細を概説する。"

---
{% api %}
# APIトリガー配信でキャンペーンメッセージを送る
{% apimethod post core_endpoint|{1} %}
/campaigns/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信を介して、指定したユーザーに即時の1回限りのメッセージを送信します。 

APIトリガー配信により、Brazeダッシュボード内にメッセージコンテンツを収容しながら、APIを介してメッセージの送信タイミングと送信先を指定できる。

セグメントをターゲットにしている場合、リクエストの記録は[開発者コンソール](https://dashboard.braze.com/app_settings/developer_console/activitylog/)に保存されます。このエンドポイントを使用してメッセージを送信するには、[API トリガーキャンペーン]({{site.baseurl}}/api/api_campaigns/)を構築する際に[キャンペーン ID](https://www.braze.com/docs/api/identifier_types/) を作成しておく必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Request body

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
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {  
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|string|[キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`send_id`| オプション | string | [送信識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`trigger_properties`| オプション | オブジェクト | [トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。このリクエストのすべてのユーザーに適用されるパーソナライゼーションキーバリューペア。 |
|`broadcast`| オプション | ブール値 | キャンペーンやキャンバスがターゲットとするセグメント全体にメッセージを送信する場合は、`broadcast` を true に設定する必要がある。このパラメータはデフォルトで false です (2017年8月31日現在)。<br><br> `broadcast` をtrueに設定すると、`recipients` リストを含めることはできない。ただし、`broadcast: true` 、意図せずこのフラグを設定してしまうと、予想以上に多くの読者にメッセージを送ってしまう可能性があるため、設定には注意が必要である。 |
|`audience`| オプション | 接続された観客オブジェクト| [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。 |
|`recipients`| オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>`send_to_existing_only` が `false` の場合、属性オブジェクトが含まれていなければなりません。<br><br>`recipients` が提供されず、`broadcast` がtrueに設定されている場合、メッセージはキャンペーンがターゲットとしているセグメント全体に送信される。 |
|`attachments`| オプション | 配列 | `broadcast` が true に設定されている場合、`attachments` リストを含めることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- 受信者配列には最大50個のオブジェクトを含めることができ、各オブジェクトには1つの `external_user_id` 文字列と `trigger_properties` オブジェクトが含まれます。
- `send_to_existing_only` が`true` の場合、Braze は既存ユーザーにのみメッセージを送信します。ただし、このフラグは、ユーザーのエイリアスでは使えません。 
- `send_to_existing_only` が`false` の場合、属性が含まれていなければなりません。Brazeは、メッセージを送信する前に、`id` と属性を持つユーザーを作成する。

ユーザーのサブスクリプショングループのステータスは、`attributes` オブジェクト内に`subscription_groups` パラメータを含めることで更新できる。詳細については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)を参照してください。

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
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ] 
}'
```

## 応答の詳細

メッセージ送信エンドポイントのレスポンスには、メッセージのディスパッチに参照できるように、メッセージの`dispatch_id` が含まれる。`dispatch_id` はメッセージディスパッチの ID で、Braze から送信される各送信に固有の ID です。このエンドポイントを使用すると、バッチ処理されたユーザーセット全体に対して1つの `dispatch_id` を受け取ります。`dispatch_id` の詳細については、[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)に関するドキュメントを参照してください。

## 送信エンドポイントを作成する

**キャンペーンで属性オブジェクトを使う**

Brazeには、`attributes` というメッセージングオブジェクトがあり、APIトリガーのキャンペーンを送る前に、ユーザーの属性や値を追加、作成、更新することができる。この API 呼び出しとして `campaign/trigger/send` エンドポイントを使用すると、キャンペーンを処理して送信する前に、ユーザー属性オブジェクトが処理されます。これにより、[レースコンディションに]({{site.baseurl}}/help/best_practices/race_conditions/)起因する問題が発生するリスクを最小限に抑えることができる。 

{% alert important %}
このエンドポイントのキャンバスバージョンをお探し？[API トリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint)を確認してください。
{% endalert %}

{% endapi %}
