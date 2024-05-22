---
nav_title: "GET：リスト カタログ項目詳細"
article_title: "GET：リスト カタログ項目詳細"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、List catalog item details Brazeエンドポイントの詳細について概説します。"

---
{% api %}
# カタログ項目の詳細を一覧表示
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> カタログ項目とその内容を返すには、このエンドポイントを使用します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.get_item` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## 経路パラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
|`item_id` | 必須 | String | カタログ項目のID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

このエンドポイントにはリクエストボディがない。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには、`200` と`404` の2つのステータスコード・レスポンスがある。

### 成功応答例

ステータスコード`200` 、以下のレスポンスボディを返すことができる。

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

ステータスコード`404` 。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

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

次の表は、返される可能性のあるエラーと、該当する場合はそれに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`item-not-found` ｜アイテムがカタログに掲載されているか確認する。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}