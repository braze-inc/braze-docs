---
nav_title: "取得:製品ID のエクスポート"
article_title: "取得:製品ID のエクスポート"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、Export 製品ID Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 製品ID のエクスポート
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> このエンドポイントを使用して、ページ分割された製品ID のリストを返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## 前提条件

このエンドポイントを使用するには、`purchases.product_list` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `page` | オプション| 文字列| 表示する製品リストのページ。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}
