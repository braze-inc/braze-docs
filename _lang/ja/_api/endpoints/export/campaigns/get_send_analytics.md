---
nav_title: "取得:分析結果をエクスポートする"
article_title: "取得:分析結果をエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export send analytics Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# 送信分析をエクスポートする
{% apimethod get %}
/sends/data_series
{% endapimethod %}

> このエンドポイントを使用して、APIキャンペーンで追跡された`send_id` の様々な統計情報を毎日取得する。

Brazeは送信後14日間、送信分析を保存する。キャンペーンのコンバージョンは、特定のユーザーがキャンペーンから受け取った直近の`send_id` 。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## 前提条件

このエンドポイントはAPIキャンペーン専用である。このエンドポイントを使うには、`sends.data_series` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメータ｜必須｜データ型｜説明
| --------- | -------- | --------- |------------ |
|`campaign_id` ｜必須｜文字列｜[キャンペーンAPI識別子を]({{site.baseurl}}/api/identifier_types/)参照。|
|`send_id` | 必須｜文字列｜[送信API識別子を]({{site.baseurl}}/api/identifier_types/)参照のこと。|
|`length` ｜必須｜整数｜返されるシリーズに含める`ending_at` までの最大日数。1～100の間でなければならない。|
|`ending_at` ｜任意｜日時 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)文字列）｜データシリーズが終了する日付。デフォルトはリクエスト時刻である。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例 

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
CSVおよびAPIエクスポートに関するヘルプは、[エクスポートのトラブルシューティングを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)参照のこと。
{% endalert %}

{% endapi %}
