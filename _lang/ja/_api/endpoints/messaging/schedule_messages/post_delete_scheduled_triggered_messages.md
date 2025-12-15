---
nav_title: "POST:スケジュールされた API トリガーキャンペーンを削除"
article_title: "POST:スケジュールされた API トリガーキャンペーンを削除"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされたAPIトリガーキャンペーンの削除Brazeエンドポイントについての詳細を概説する。"

---
{% api %}
# スケジュールされた API トリガーキャンペーンを削除
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> このエンドポイントを使用して、以前にAPIトリガーでスケジューリングしたCanvasメッセージを送信前にキャンセルする。

スケジュールされたメッセージやトリガーが、送信される予定だった時間の間近またはその間に削除された場合、最善の努力で更新されるため、Brazeは、対象となるユーザー全員、一部、または全員に、直前の削除を適用する可能性がある。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.trigger.schedule.delete`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id`| 必須 | 文字列 | [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `schedule_id` | 必須 | 文字列 | 削除する`schedule_id`（スケジュールの作成に対する応答から取得）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
