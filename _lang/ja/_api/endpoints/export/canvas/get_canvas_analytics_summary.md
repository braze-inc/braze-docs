---
nav_title: "取得:Canvas データ概要分析のエクスポート"
article_title: "取得:Canvas データ概要分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export Canvas データサマリー分析 Braze エンドポイントの詳細について説明します。"

---
{% api %}
# Canvas データ概要分析をエクスポート
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> このエンドポイントを使用すると、Canvasの時系列データのロールアップをエクスポートして、Canvasの結果を簡潔にまとめることができます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.data_summary`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [キャンバス API 識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。|
| `ending_at` | 必須 | 日時 <br>([ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)) | データエクスポートを終了する日付。デフォルトはリクエストの時間です。|
| `starting_at` | オプション* | 日時 <br>([ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)) | データエクスポートを開始する日付。<br><br>* `length` `starting_at` またはのいずれかが必須です。|
| `length` | オプション* | 文字列 | `ending_at` 返されるシリーズに含めるまでの最大日数。1 から 14 (両端を含む) までの数字でなければなりません。<br><br>* `length` `starting_at` またはのいずれかが必須です。|
| `include_variant_breakdown` | オプション | Boolean | バリアント統計を含めるかどうか (デフォルトは) `false`。|
| `include_step_breakdown` | オプション | Boolean | ステップ統計を含めるかどうか (デフォルトは) `false`。|
| `include_deleted_step_data` | オプション | Boolean | 削除されたステップのステップ統計を含めるかどうか (デフォルトは) `false`。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

{% endapi %}
