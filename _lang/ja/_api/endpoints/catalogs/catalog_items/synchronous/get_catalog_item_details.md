---
nav_title: "取得:カタログ項目の詳細をリストアップする"
article_title: "取得:カタログ項目の詳細をリスト"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログ項目の詳細をリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログ項目の詳細をリストアップする
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> カタログ項目とその内容を返すには、このエンドポイントを使う。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.get_item`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
| `item_id` | 必須 | 文字列 | カタログ項目のID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエストパラメーター

このエンドポイントにはリクエストボディがない。

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには2つのステータスコード応答があります: `200` と `404`。

### 成功応答の例

ステータスコード `200` は、次の応答本文を返す可能性があります。

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### エラー応答例

ステータスコード `404` は、次の応答を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、該当する場合、それに関連するトラブルシューティングの手順を示している。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認する。 |
| `item-not-found` | その商品がカタログに掲載されているか確認する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
