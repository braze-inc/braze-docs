---
nav_title: "取得：送信分析のエクスポート"
article_title: "取得：送信分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、エクスポート送信分析の Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# 送信分析のエクスポート
{% apimethod get %}
/sends/data_series
{% endapimethod %}

> このエンドポイントを使用して、追跡対象 `send_id` の API キャンペーンのさまざまな統計を毎日取得します。

Brazeストアは、送信後14日間アナリティクスを送信します。キャンペーンのコンバージョンは、特定のユーザーがキャンペーンから獲得した最新の `send_id` コンバージョンに関連付けられます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## 前提 条件

このエンドポイントは API キャンペーン専用です。このエンドポイントを使用するには、アクセス許可を持つ `sends.data_series` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | -------- | --------- |------------ |
| `campaign_id` |必須項目 |文字列 | [詳しくは、キャンペーン API 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。|
| `send_id` |必須項目 |文字列 |「 [API 識別子の送信]({{site.baseurl}}/api/identifier_types/)」を参照してください。|
| `length` |必須項目 |整数型 |返される系列に含めるまでの `ending_at` 最大日数。1 以上 100 以下である必要があります。|
| `ending_at` |オプション |日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) |データ系列が終了する日付。既定値は、要求の時刻です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例 

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time": (string) the date as ISO 8601 date,
            "messages": {
                "ios_push" : [
                    {
                      "variation_name": (string) variation name,
                      "sent": (int) the number of sends,
                      "delivered": (int) the number of messages successfully delivered,
                      "undelivered": (int) the number of undelivered,
                      "delivery_failed": (int) the number of rejected,
                      "direct_opens": (int) the number of direct opens,
                      "total_opens": (int) the number of total opens,
                      "bounces": (int) the number of bounces,
                      "body_clicks": (int) the number of body clicks,
                      "revenue": (float) the number of dollars of revenue (USD),
                      "unique_recipients": (int) the number of unique recipients at the campaign-level,
                      "conversions": (int) the number of conversions,
                      "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                      "conversions1": (optional, int) the number of conversions for the second conversion event,
                      "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                      "conversions2": (optional, int) the number of conversions for the third conversion event,
                      "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                      "conversions3_by_send_time": (optional, int) the number of conversions for the fourth, conversion event attributed to the date the campaign was sent
                      }
                  ]
            },
        "conversions_by_send_time": (optional, int),
        "conversions1_by_send_time": (optional, int),
        "conversions2_by_send_time": (optional, int),
        "conversions3_by_send_time": (optional, int),
        "conversions": (int),
        "conversions1": (optional, int),
        "conversions2": (optional, int),
        "conversions3": (optional, int),
        "unique_recipients": (int),
        "revenue": (optional, float)
      }
    ],
  "message": "success"
}
```

{% alert tip %}
CSV と API のエクスポートに関するヘルプについては、 [エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
