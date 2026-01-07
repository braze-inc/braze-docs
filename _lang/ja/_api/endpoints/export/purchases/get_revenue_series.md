---
nav_title: "取得:輸出収入データ"
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

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}とする。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`purchases.revenue_series`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `ending_at` | オプション | 日時 ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートを終了する日付。リクエストの時刻にデフォルト設定されます。 |
| `length` | 必須 | 整数 | 返されるシリーズに `ending_at` が含まれるまでの最大日数。1以上100以下でなければなりません。 |
| `unit` | オプション | 文字列 | データポイント間の時間の単位。日または時間にすることができ、デフォルトは日です。 |
| `app_id` | オプション | 文字列 | [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得したアプリAPI識別子。除外された場合、ワークスペース内のすべてのアプリの結果が返されます。 |
| `product` | オプション | 文字列 | 応答をフィルターする製品の名前。除外された場合、すべてのアプリの結果が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}
