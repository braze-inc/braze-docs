---
nav_title: "取得:収益データのエクスポート"
article_title: "取得:収益データのエクスポート"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "本稿では、輸出売上データBraze エンドポイントについて詳しく説明します。"

---
{% api %}
# 時間別売上データのエクスポート
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> このエンドポイントを使用して、ある期間にわたってアプリに費やされた総金額を返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## 前提条件

このエンドポイントを使用するには、`purchases.revenue_series` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md エンドポイント='purchases product list' %}

## リクエストパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `ending_at` | オプション | 日時([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートを終了する日付。デフォルトはリクエストの時刻です。 |
| `length` | required | 整数 | 返される系列に含める`ending_at` の前の最大日数。1以上100以下でなければなりません。 |
| `unit` | オプション | string | データポイント間の時刻の単位。日、または時間を指定できます。デフォルトは日です。 |
| `app_id` | オプション | string | [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページから取得したアプリケーションAPI 識別子。除外すると、ワークスペース内のすべてのアプリs の結果が返されます。 |
| `product` | オプション | string | 応答をフィルタリングする商品の名称。除外すると、すべてのアプリs の結果が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "revenue" : (int) amount of revenue for the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}
