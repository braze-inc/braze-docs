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
{% apimethod post core_endpoint|{1} %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> このエンドポイントを使用して、以前にAPIトリガーでスケジューリングしたCanvasメッセージを送信前にキャンセルする。

送信予定時刻に非常に近いか、送信予定時刻に削除されたスケジュール済みのメッセージまたはトリガーは、ベストエフォートで更新されます。このため、直前の削除は、ターゲットユーザーの全員または一部に適用されるか、あるいはまったく適用されない可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.schedule.delete` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

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
| `campaign_id`| 必須 | string | [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `schedule_id` | 必須 | string | 削除する`schedule_id` （スケジュール作成のレスポンスから取得）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## リクエスト例
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
