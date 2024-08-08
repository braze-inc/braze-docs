---
nav_title: "ポスト:スケジュールされた API トリガーキャンバスの削除"
article_title: "ポスト:スケジュールされた API トリガーキャンバスの削除"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされた API トリガーの削除 Canvases Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# スケジュールされた API トリガー キャンバスの削除
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> 削除スケジュールエンドポイントを使用すると、API によってトリガーされた Canvases を以前にスケジュールしたメッセージを、送信前にキャンセルできます。

送信予定時刻のすぐ近くまたは送信中に削除されたスケジュールされたメッセージまたはトリガーは、ベストエフォートで更新されるため、直前の削除は、対象ユーザーのすべてまたは一部に適用されるか、まったく適用されない可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `canvas.trigger.schedule.delete` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id`|必須項目 |文字列 |「 [キャンバス識別子]({{site.baseurl}}/api/identifier_types/)」を参照してください。|
| `schedule_id` |必須項目 |文字列 |to `schedule_id` delete (スケジュールを作成する応答から取得)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 要求の例
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
