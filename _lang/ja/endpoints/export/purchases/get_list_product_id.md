---
nav_title: "取得:製品IDをエクスポートする"
article_title: "取得:プロダクトIDをエクスポートする"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「プロダクト ID のエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 製品IDをエクスポートする
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> 製品IDのページ分割されたリストを返すには、このエンドポイントを使用する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}とする。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`purchases.product_list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `page` | オプション | 文字列 | 表示したい商品リストのページ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## 応答

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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}
