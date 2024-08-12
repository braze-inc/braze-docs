---
nav_title: "取得:Canvas Data Series 分析のエクスポート"
article_title: "取得:Canvas Data Series 分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Canvas データシリーズのエクスポート分析Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# Canvas データシリーズアナリティックのエクスポート
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

> このエンドポイントを使用して、キャンバスの時系列データをエクスポートします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.data_series` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 必須| 文字列| [Canvas API 識別子]({{site.baseurl}}/api/identifier_types/) を参照してください。|
| `ending_at` | 必須| 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string)| データエクスポートを終了する日付。デフォルトは要求の時刻です。|
| `starting_at` | オプション* | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string)| データエクスポートを開始する日付。<br><br>* `length`または`starting_at`のいずれかが必要です。|
| `length` | オプション* | String | `ending_at` が返された系列に含まれるまでの最大日数。1 ～14 (両端を含む) である必要があります。<br><br>* `length`または`starting_at`のいずれかが必要です。|
| `include_variant_breakdown` | オプション| ブール| バリアント統計を含めるかどうか(デフォルトは`false`) |
| `include_step_breakdown` | オプション| ブール| ステップ統計を含めるかどうか(デフォルトは`false`) |
| `include_deleted_step_data` | オプション| ブール| 削除されたステップのステップ統計を含めるかどうか(デフォルトは`false`) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## レスポンス

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
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}

{% endapi %}
