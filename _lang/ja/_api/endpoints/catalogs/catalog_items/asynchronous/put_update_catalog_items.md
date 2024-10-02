---
nav_title: "PUT:複数のカタログアイテムを更新"
article_title: "PUT:複数のカタログアイテムを更新"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、「複数のカタログ項目を更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログ項目のアップデート
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数の項目を更新します。 

カタログアイテムが存在しない場合、このエンドポイントはカタログ内にアイテムを作成します。1つのリクエストにつき、最大50個のカタログアイテムに対応できます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.replace_items` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

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
| `items` | required | 配列 | 項目オブジェクトを含む配列。各オブジェクトにはID が必要です。アイテムオブジェクトには、カタログに存在するフィールドs が含まれている必要があります。リクエストごとに最大 50 個のアイテムオブジェクトが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

## 応答

このエンドポイントには、`202`、`400`、`404` という3つのステータスコード応答があります。

### 成功応答の例

ステータス コード`202`は、以下のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンス例

ステータス コード`400`は、以下のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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
| `catalog-not-found` | カタログの名前が有効であることを確認します。 | 
| `ids-not-string` | 各項目ID が文字列であることを確認します。 |
| `ids-not-unique` | 各項目の ID が一意であることを確認します。 |
| `ids-too-large` | 各項目ID の文字数の制限は250 文字です。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。 |
| `items-missing-ids` | 各項目にIDがあることを確認します。 |
| `items-too-large` | 項目値は5000 文字を超えることはできません。 |
| `invalid-ids` | アイテムID 名でサポートされている文字は、文字、数字、ハイフン、およびアンダースコアです。 |
| `invalid-fields` | API リクエストで送信するすべてのフィールドがカタログにすでに存在することを確認します。これは、エラーに記載されている ID フィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | 項目オブジェクトキーに`.` または`$` を含めることはできません。 |
| `too-deep-nesting-in-value-object` | アイテムオブジェクトには、50 を超えるレベルのネストを含めることはできません。 |
| `request-includes-too-many-items` | あなたのリクエストは項目が多すぎます。リクエストごとの項目の上限は50個です。 |
| `unable-to-coerce-value` | 項目タイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
