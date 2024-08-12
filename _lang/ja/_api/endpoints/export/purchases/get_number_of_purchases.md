---
nav_title: "取得:輸出仕入数"
article_title: "取得:輸出仕入数"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、Export number of purchases Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 輸出仕入数
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> このエンドポイントを使用して、時間範囲内でのアプリ内の購入の合計数を返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## 前提条件

このエンドポイントを使用するには、`purchases.quantity_series` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `ending_at` | オプション| 日時([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string)| データエクスポートを終了する日付。デフォルトは要求の時刻です。|
| `length` | Required | Integer | `ending_at` が返される系列に含まれるまでの最大日数。1 ～100 (両端を含む) である必要があります。|
| `unit` | オプション| 文字列| データポイント間の時間の単位。day またはhour にすることができます。デフォルトはday です。|
| `app_id` | オプション| 文字列| [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページから取得されたアプリケーションAPI 識別子。除外すると、ワークスペース内のすべてのアプリの結果が返されます。|
| `product` | オプション| 文字列| 応答をフィルタする製品の名前。除外すると、すべてのアプリの結果が返されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}
