---
nav_title: "ポスト:複数のカタログアイテムの作成"
article_title: "ポスト:複数のカタログアイテムの作成"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、Create multiple catalog items Braze endpointの詳細について説明します。"

---
{% api %}
# 複数のカタログアイテムの作成
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内に複数のアイテムを作成します。 

各リクエストは、最大50 個のアイテムをサポートできます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.add_items` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `catalog_name` | 必須| 文字列| カタログの名前。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `items` | Required | Array | 項目オブジェクトを含む配列。アイテムオブジェクトには、カタログ内のすべてのフィールドが含まれている必要があります。リクエストごとに最大 50 個のアイテムオブジェクトが許可されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

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

## レスポンス

このエンドポイントには、`202`、`400`、`404` の3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード`202` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンス例

ステータスコード`400` は、以下のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します。

| エラー| トラブルシューティング|
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認します。|
| `ids-not-strings` | 項目ID は文字列型である必要があります。|
| `ids-not-unique` | 項目ID は要求内で一意である必要があります。|
| `ids-too-large` | 項目ID は250 文字を超えることはできません。|
| `invalid-ids` | 項目ID には、文字、数字、ハイフン、およびアンダースコアのみを含めることができます。|
| `invalid-fields` | API リクエストで送信するすべてのフィールドがカタログにすでに存在することを確認します。これは、error で指定されたID フィールドとは関係ありません。|
| `invalid-keys-in-value-object` | 項目オブジェクトキーに`.` または`$` を含めることはできません。|
| `item-array-invalid` | `items` はオブジェクトの配列である必要があります。|
| `items-missing-ids` | 項目ID を持たない項目があります。各項目に項目ID があることを確認します。|
| `items-too-large` | 項目値は5000 文字を超えることはできません。|
| `request-includes-too-many-items` | リクエストに含まれる項目が多すぎます。リクエストごとのアイテム制限は50 です。|
| `too-deep-nesting-in-value-object` | アイテムオブジェクトは、50 を超えるレベルのネストを持つことはできません。|
| `unable-to-coerce-value` | 項目タイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
