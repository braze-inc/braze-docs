---
nav_title: "ポスト:スケジュールされたメッセージの削除"
article_title: "ポスト:スケジュールされたメッセージの削除"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされたメッセージの削除Brazeエンドポイントについて詳しく説明します。"

---
{% api %}
# スケジュールされたメッセージを削除する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/delete
{% endapimethod %}

> このエンドポイントを使用して、送信前に以前にスケジュールしたメッセージをキャンセルします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `messages.schedule.delete` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` |必須項目 |文字列 |to `schedule_id` delete (スケジュールを作成する応答から取得)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
