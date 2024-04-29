---
nav_title: "取得:Canvas Data Series Analyticsのエクスポート"
article_title: "取得:Canvas Data Series Analyticsのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export Canvas data series analytics Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# Canvasデータ系列の分析をエクスポート
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

> Canvasの時系列データをエクスポートするには、このエンドポイントを使用します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.data_series`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

|パラメータ|必須|データ型|説明|
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [Canvas API識別子]({{site.baseurl}}/api/identifier_types/)を参照。 |
|`ending_at`|必須|日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)文字列）|データエクスポートを終了する日付。リクエストの時刻がデフォルト。|
|`starting_at`|オプション*|日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)文字列） | データのエクスポートを開始する日付。<br><br>※`length`または`starting_at`のいずれかが必要です。|
|`length`|オプション*|文字列|返される系列に含める`ending_at`前の最大日数。1から14の間でなければなりません。<br><br>※`length`または`starting_at`のいずれかが必要です。|
|`include_variant_breakdown`|オプション|ブール値|バリアント統計を含めるかどうか(デフォルトは`false`)。|
|`include_step_breakdown`|オプション|ブール値|ステップ統計を含めるかどうか(デフォルトは`false`)。|
|`include_deleted_step_data`|オプション|ブール値|削除されたステップのステップ統計を含めるかどうか(デフォルトは`false`)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエストの例

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) the Canvas name,
    "stats": [
      {
        "time": (string) the date as ISO 8601 date,
        "total_stats": {
          "revenue": (float) the number of dollars of revenue (USD),
          "conversions": (int) the number of conversions,
          "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
          "entries": (int) the number of entries
        },
        "variant_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
            "name": (string) the name of variant,
            "revenue": (float) the number of dollars of revenue (USD),
            "conversions": (int) the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "entries": (int) the number of entries
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
            "name": (string) the name of step,
            "revenue": (float) the the number of dollars of revenue (USD),
            "conversions": (int) the the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "messages": {
              "email": [
                {
                  "sent": (int) the number of sends,
                  "opens": (int) the number of opens,
                  "unique_opens": (int) the number of unique opens,
                  "clicks": (int) the number of clicks
                  ... (more stats)
                }
              ],
              "sms" : [
                {
                  "sent": (int) the number of sends,
                  "sent_to_carrier" : (int) the number of messages sent to the carrier,
                  "delivered": (int)the number of delivered messages,
                  "rejected": (int) the number of rejected messages,
                  "delivery_failed": (int) the number of failed deliveries,
                  "clicks": (int) the number of clicks on shortened links,
                  "opt_out" : (int) the number of opt outs,
                  "help" : (int) the number of help messages received
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブル]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)シューティング」を参照してください。
{% endalert %}

{% endapi %}
