---
nav_title: "取得:キャンバスデータのサマリー分析をエクスポート"
article_title: "取得:エクスポートキャンバスデータサマリー分析"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "ここでは、キャンバスデータサマリーのエクスポート分析 Braze エンドポイントについて説明します。"

---
{% api %}
# キャンバスデータのサマリー分析をエクスポート
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> このエンドポイントを使用して、キャンバスの時系列データのロールアップをエクスポートし、キャンバスの結果の簡潔な概要を提供します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.data_summary`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [キャンバス API 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `ending_at` | 必須 | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データエクスポートの終了日。デフォルトは要求の時刻です。 |
| `starting_at` | オプション* | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データエクスポートの開始日。<br><br>* `length` または `starting_at` のいずれかが必要です。 |
| `length` | オプション* | 文字列 | 返される系列に含まれる`ending_at` の前の最大日数。1以上14以下でなければなりません。<br><br>* `length` または `starting_at` のいずれかが必要です。 |
| `include_variant_breakdown` | オプション | ブール値 | バリアント統計を含めるかどうか(デフォルトs to `false`)。  |
| `include_step_breakdown` | オプション | ブール値 | ステップ統計を含めるかどうか(デフォルトs to `false`)。 |
| `include_deleted_step_data` | オプション | ブール値 | 削除されたステップs (デフォルトs から`false`) のステップを含めるかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
**タイムゾーンアライメント:**Braze ダッシュボード 分析は、ダッシュボード内の企業の設定されたタイムゾーンに毎日集計されます。統計がダッシュボードに合うように、タイムスタンプが企業のタイムゾーンと一致していることを確認します。たとえば、会社の時刻がUTC+2の場合、タイムスタンプは12AM UTC+2になります。
{% endalert %}

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
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
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
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
  "message": (required, string) the status of the export, returns 'success' on successful completion
}
```

{% alert important %}
**`influenced_opens` フィールド:**API レスポンスでは、`influenced_opens` フィールドは、開封s の総数を表します(直接および影響を受ける開封s の両方を組み合わせたもの)。Braze ダッシュボードでは、「被影響開封s」は、直接開封sを除いた、被影響開封sのみを指す。これは、API のレガシー命名規則によるものです。
{% endalert %}

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
