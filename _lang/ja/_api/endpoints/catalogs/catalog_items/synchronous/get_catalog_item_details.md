---
nav_title: "取得:カタログアイテムの詳細を一覧表示する"
article_title: "取得:カタログアイテムの詳細を一覧表示する"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、カタログ アイテムの詳細を一覧表示する Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# カタログアイテムの詳細を一覧表示する
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログ項目とそのコンテンツを返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `catalogs.get_item` 許可。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメータ

| パラメータ | 必須 | データ型 | 説明 |
|---|---|---|---|
| `catalog_name`| 必須 | 文字列 | カタログの名前。 |
| `item_id`| 必須 | 文字列 | カタログ項目の ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

このエンドポイントにはリクエスト本文がありません。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには 2 つのステータス コード応答があります。 `200` そして `404`。

### 成功レスポンスの例

ステータスコード `200` 次の応答本文を返すことができます。

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

### エラー応答の例

ステータスコード `404` 次の応答を返す可能性があります。発生する可能性のあるエラーの詳細については、[「トラブルシューティング」](#troubleshooting) を参照してください。

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

次の表には、返される可能性のあるエラーと、該当する場合は関連するトラブルシューティング手順がリストされています。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found`| カタログ名が有効であることを確認してください。 |
| `item-not-found`| アイテムがカタログにあることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}