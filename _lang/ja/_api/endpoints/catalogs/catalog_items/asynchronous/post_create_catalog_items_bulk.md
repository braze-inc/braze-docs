---
nav_title: "POST:複数のカタログアイテムを作成"
article_title: "POST:複数のカタログアイテムを作成"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、複数のカタログアイテムを作成するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 複数のカタログアイテムを作成する
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログに複数のアイテムを作成します。 

各リクエストは最大50個の項目まで対応できます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.add_items`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメータ

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | string | カタログの名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `items` | required | 配列 | アイテムオブジェクトを含む配列。アイテムオブジェクトには、カタログのすべてのフィールドが含まれている必要があります。リクエストごとに最大50個の項目オブジェクトが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 例のリクエスト

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 40.7413,
        "Longitude": -73.9764
      },
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ],
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 40.7489,
        "Longitude": -73.9972
      },
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ],
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

## 応答

このエンドポイントには、`202`、`400`、`404` という3つのステータスコード応答があります。

### 成功応答の例

ステータスコード `202` は次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### 例外エラー応答

ステータスコード `400` は次の応答本文を返す可能性があります。エラーに関する詳細は[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `ids-not-strings` | アイテムIDは文字列でなければなりません。 |
| `ids-not-unique` | リクエスト内のアイテムIDは一意でなければなりません。 |
| `ids-too-large` | 項目 ID は250文字以内にする必要があります。 |
| `invalid-ids` | アイテムIDには、文字、数字、ハイフン、アンダースコアのみを含めることができます。 |
| `invalid-fields` | APIリクエストで送信しているすべてのフィールドがカタログに既に存在することを確認してください。これはエラーで言及されているIDフィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | アイテムオブジェクトのキーには`.`または`$`を含めることはできません。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。 |
| `items-missing-ids` | アイテムIDがないアイテムがあります。各項目が項目 ID を持っていることを確認します。 |
| `items-too-large` | アイテムの値は5,000文字を超えることはできません。 |
| `request-includes-too-many-items` | リクエストの項目が多すぎます。リクエストごとの項目の上限は50個です。 |
| `too-deep-nesting-in-value-object` | アイテムオブジェクトは50レベル以上のネストを持つことはできません。 |
| `unable-to-coerce-value` | アイテムタイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
