---
nav_title: "POST:カタログアイテムを作成"
article_title: "POST:カタログアイテムの作成"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "この記事では、Create catalog item Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# カタログ項目を作成する
{% apimethod post %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログにアイテムを作成する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#820c305b-ea6a-4b71-811a-55003a212a40 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.create_item`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
| `item_id` | 必須 | 文字列 | カタログ項目のID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `items` | required | 配列 | アイテム・オブジェクトを含む配列。アイテムオブジェクトは、`id` フィールドを除く、カタログのすべてのフィールドを含むべきである。1つのリクエストにつき、1つのアイテムオブジェクトのみが許可される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
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
    }
  ]
}'
```

## 応答

このエンドポイントには、`201`、`400`、`404` という 3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード `201` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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
| `arbitrary-error` | 任意のエラーが発生した。もう一度試すか、[サポートに]({{site.baseurl}}/support_contact/)連絡する。 |
| `catalog-not-found` | カタログ名が有効であることを確認する。 |
| `filtered-set-field-too-long` | フィールド値は、項目の文字数制限を超えるフィルターセットで使用されている。 |
| `id-in-body` | リクエスト本文の項目 ID を削除します。 |
| `ids-too-large` | 各アイテムIDの文字数制限は250文字である。 |
| `invalid-ids` | アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアである。 |
| `invalid-fields` | APIリクエストで送信するすべてのフィールドが、すでにカタログに存在していることを確認する。これは、エラーに記載されている ID フィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | 項目オブジェクトのキーに `.` または `$` を含めることはできません。 |
| `item-already-exists` | そのアイテムはすでにカタログに存在する。 |
| `item-array-invalid` | `items` はオブジェクト配列でなければなりません。 |
| `items-too-large` | 各項目の文字数制限は5,000文字である。 |
| `request-includes-too-many-items` | 1つのリクエストにつき1つのカタログ項目しか作成できない。 |
| `too-deep-nesting-in-value-object` | アイテム・オブジェクトは50レベル以上の入れ子を持つことはできない。 |
| `unable-to-coerce-value` | 項目タイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
