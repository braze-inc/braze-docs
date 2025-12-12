---
nav_title: "パッチ:カタログアイテムを編集"
article_title: "パッチ:カタログアイテムの編集"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、カタログ項目の編集Brazeエンドポイントについての詳細を概説する。"

---
{% api %}
# カタログ項目を編集する
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログの既存のアイテムを編集する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.update_item`の権限が必要です。

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
| `items` | required | 配列 | アイテム・オブジェクトを含む配列。項目オブジェクトには、`id` フィールドを除き、カタログに存在するフィールドを含める必要があります。1つのリクエストにつき、1つのアイテムオブジェクトのみが許可される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
`$add` および `$remove` 演算子は配列型フィールドにのみ適用可能であり、PATCH エンドポイントでのみサポートされます。
{% endalert %}

## 応答

このエンドポイントには、`200`、`400`、`404` という 3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード `200` は、次の応答本文を返す可能性があります。

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
| `id-in-body` | アイテムIDがすでにカタログに存在する。 |
| `ids-too-large` | 各アイテムIDの文字数制限は250文字である。 |
| `invalid-ids` | アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアである。 |
| `invalid-fields` | リクエストのフィールドがカタログに存在することを確認する。 |
| `invalid-keys-in-value-object` | 項目オブジェクトのキーに `.` または `$` を含めることはできません。 |
| `item-not-found` | その商品がカタログに掲載されているか確認する。 |
| `item-array-invalid` | `items` はオブジェクト配列でなければなりません。 |
| `items-too-large` | 各項目の文字数制限は5,000文字である。 |
| `request-includes-too-many-items` | 1つのリクエストにつき1つのカタログ項目しか編集できない。 |
| `too-deep-nesting-in-value-object` | アイテム・オブジェクトは50レベル以上の入れ子を持つことはできない。 |
| `unable-to-coerce-value` | 項目タイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
