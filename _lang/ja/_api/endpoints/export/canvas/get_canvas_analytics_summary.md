---
nav_title: "取得:Canvas Data Summary Analyticsのエクスポート"
article_title: "取得:Canvas Data Summary Analyticsのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export Canvas data summary analytics Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# Canvasデータ要約分析のエクスポート
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> このエンドポイントを使用すると、キャンバスの時系列データのロールアップをエクスポートでき、キャンバスの結果を簡潔に要約できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.data_summary`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

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
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
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
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the number of influenced opens,
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブル]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)シューティング」を参照してください。
{% endalert %}

{% endapi %}
