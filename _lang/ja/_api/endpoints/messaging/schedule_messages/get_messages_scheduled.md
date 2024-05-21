---
nav_title: "取得:予定されているキャンペーンとキャンバスを一覧表示する"
article_title: "取得:予定されているキャンペーンとキャンバスを一覧表示する"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "この記事では、予定されているキャンペーンとキャンバスBrazeエンドポイントのリストに関する詳細について説明します。"

---
{% api %}
# 予定されているキャンペーンとキャンバスを一覧表示する
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> このエンドポイントを使用して、現在と、リクエストで指定された`end_time` の間にスケジュールされたキャンペーンとエントリキャンバスに関する情報のJSON リストを返します。

毎日、定期的なメッセージは、次回の発生時に一度だけ表示されます。このエンドポイントで返される結果は、Braze で作成およびスケジュールされたキャンペーンおよびキャンバスの場合のみです。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`messages.schedule_broadcasts` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | -------- | --------- | ----------- |
| `end_time` | 必須| [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式の文字列| 次のスケジュールされたキャンペーンおよびキャンバスを取得する範囲の終了日。これは、API によってUTC 時刻の午前0 時として処理されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "scheduled_broadcasts": [
    {
      "name" (string) the name of the scheduled boradcast,
      "id" (stings) the Canvas or campaign identifier,
      "type" (string) the broadcast type either Canvas or Campaign,
      "tags" (array) an array of tag names formatted as strings,
      "next_send_time" (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type" (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
