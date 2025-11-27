---
nav_title: "取得:今後のスケジュールされた キャンペーンとキャンバスを一覧表示する"
article_title: "取得:今後スケジュールされているキャンペーンとキャンバスをリスト"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "この記事では、「今後スケジュールされているキャンペーンとキャンバスをリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 今後のスケジュールされた キャンペーンとキャンバスを一覧表示する
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> このエンドポイントを使用して、現在からリクエストで指定された `end_time` までのスケジュールされたキャンペーンとエントリキャンバスに関する情報の JSON リストを返します。

毎日、繰り返し発生するメッセージは、次回発生時に一度だけ耳元をアプリします。このエンドポイントで返される結果には、Braze ダッシュボードで作成およびスケジュールされたキャンペーンとキャンバスが含まれます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`messages.schedule_broadcasts`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `end_time` | 必須 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列 | 今後予定されているキャンペーンとキャンバスを取得する範囲の終了日。これは、API によって UTC 時間の午前 0 時として扱われます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
