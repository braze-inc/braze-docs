---
nav_title: "GET：輸出収入データ"
article_title: "GET：輸出収入データ"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、収益データのエクスポートBrazeエンドポイントの詳細について概説します。"

---
{% api %}
# 時間ごとの収益データのエクスポート
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> このエンドポイントを使用して、時間範囲にわたってアプリで使用された合計金額を返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## 前提条件

このエンドポイントを使用するには、`purchases.revenue_series` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`ending_at` ｜任意｜日時[（ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)文字列）｜データ・エクスポートを終了する日付。デフォルトはリクエスト時刻。|
|`length` ｜必須｜整数｜返されるシリーズに含める`ending_at` までの最大日数。1～100の間でなければならない。|
|`unit` ｜オプション｜文字列｜データポイント間の時間の単位。デフォルトは日。|
|`app_id` ｜任意｜文字列｜[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得したアプリAPI識別子。除外すると、ワークスペース内のすべてのアプリの結果が返されます。|
|`product` ｜任意｜文字列｜応答をフィルタリングする製品名。除外した場合は、すべてのアプリの結果が返されます。|
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
CSVおよびAPIエクスポートに関するヘルプは、[エクスポートのトラブルシューティングを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)ご覧ください。
{% endalert %}
