---
nav_title: "ポスト複数のカタログ アイテムを作成する"
article_title: "ポスト複数のカタログ アイテムを作成する"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を作成するBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# 複数のカタログ アイテムを作成する
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログに複数のアイテムを作成します。 

各要求は、最大 50 個の項目をサポートできます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、アクセス許可を持つ `catalogs.add_items` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パス パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `catalog_name` |必須項目 |文字列 |カタログの名前。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `items` |必須項目 |配列 |項目オブジェクトを含む配列。アイテム オブジェクトには、カタログ内のすべてのフィールドが含まれている必要があります。要求ごとに最大 50 個の項目オブジェクトが許可されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求の例

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
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

## 応答

このエンドポイント`202`には、 `400``404`

### 成功応答の例

状態コード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例

状態コード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、「 [トラブルシューティング](#troubleshooting) 」を参照してください。

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

次の表に、返される可能性のあるエラーと、それに関連するトラブルシューティング手順を示します。

|エラー |トラブルシューティング |
| --- | --- |
| `catalog-not-found` |カタログ名が有効であることを確認してください。|
| `ids-not-strings` |アイテム ID は文字列型である必要があります。|
| `ids-not-unique` |アイテム ID は、要求内で一意である必要があります。|
| `ids-too-large` |アイテム ID は 250 文字以下にする必要があります。|
アイテム ID には、英字、数字、ハイフン、アンダースコアのみを使用できます。
| `invalid-fields` |API 要求で送信するすべてのフィールドがカタログに既に存在することを確認します。これは、エラーに記載されている ID フィールドとは関係ありません。|
| `invalid-keys-in-value-object` |項目オブジェクトのキーに `.` または `$`を含めることはできません。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。|
| `items-missing-ids` |アイテム ID を持たないアイテムがあります。各アイテムにアイテム ID があることを確認します。 |
| `items-too-large` |項目の値は 5,000 文字を超えることはできません。|
| `request-includes-too-many-items` |リクエストのアイテムが多すぎます。要求ごとの項目数の制限は 50 です。|
| `too-deep-nesting-in-value-object` |項目オブジェクトは、50 レベルを超える入れ子を持つことはできません。|
| `unable-to-coerce-value` |アイテムの種類は変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
