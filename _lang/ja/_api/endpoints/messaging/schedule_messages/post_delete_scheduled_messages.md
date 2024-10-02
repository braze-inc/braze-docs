---
nav_title: "POST:スケジュールされたメッセージを削除する"
article_title: "POST:スケジュールされたメッセージを削除する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Delete scheduled messages Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# スケジュールされたメッセージを削除する
{% apimethod post core_endpoint|{1} %}
/messages/schedule/delete
{% endapimethod %}

> このエンドポイントを使用して、以前にスケジュールしたメッセージを送信前にキャンセルします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`messages.schedule.delete` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | 必須 | string | 削除する`schedule_id` （スケジュール作成のレスポンスから取得）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
