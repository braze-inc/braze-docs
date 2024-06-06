---
nav_title: "ポスト:スケジュールされたメッセージの更新"
article_title: "ポスト:スケジュールされたメッセージの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされたメッセージの更新Brazeエンドポイントについて詳しく説明します。"

---
{% api %}
# スケジュールされたメッセージを更新する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、スケジュールされたメッセージを更新します。 

このエンドポイントは、or `messages` パラメーターのいずれか`schedule`または両方の更新を受け入れます。要求には、これら 2 つのキーのうち少なくとも 1 つが含まれている必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `messages.schedule.update` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` |必須項目 |文字列 |更新する( `schedule_id` スケジュールを作成する応答から取得)。 |
|`schedule` |オプション |オブジェクト | [スケジュール・オブジェクト (schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/)) を参照。|
|`messages` |オプション |オブジェクト | [使用可能なメッセージング・オブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {  
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}
