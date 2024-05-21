---
nav_title: "ポスト:スケジュールされたAPI トリガキャンペーンの削除"
article_title: "ポスト:スケジュールされたAPI トリガキャンペーンの削除"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、スケジュールされたAPI トリガキャンペーンBraze エンドポイントの削除の詳細について説明します。"

---
{% api %}
# スケジュールされたAPI トリガキャンペーンの削除
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> このエンドポイントを使用して、送信前にAPI トリガーでスケジュールしたCanvas メッセージをキャンセルします。

スケジュールされたメッセージまたはトリガーが送信される予定の間に非常に近くまたは削除された場合は、最善の努力で更新されるため、最後の2 回目の削除はターゲットユーザーのすべて、一部、またはすべてに適用される可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.schedule.delete` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

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

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
| `campaign_id`| 必須| 文字列| [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照|
| `schedule_id` | Required | String | 削除する`schedule_id` (スケジュール作成のレスポンスから取得)。|
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
