---
nav_title: "パッチ:複数のカタログ項目を編集する"
article_title: "パッチ:複数のカタログ項目を編集する"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を編集するBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# 複数のカタログ項目を編集する
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数の既存アイテムを編集する。

各リクエストは最大50個の項目まで対応できます。このエンドポイントは非同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.update_items` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='非同期カタログ項目' %}

## パスパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | string | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `items` | required | 配列 | アイテム・オブジェクトを含む配列。項目オブジェクトには、カタログに存在するフィールドを含める必要があります。1回のリクエストにつき、アイテムオブジェクトは50個まで認められる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
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
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
`$add` および `$remove` 演算子は配列型フィールドにのみ適用可能であり、PATCH エンドポイントでのみサポートされます。
{% endalert %}

## 応答

このエンドポイントには、`202`、`400`、`404` という3つのステータスコード応答があります。

### 成功応答の例

ステータスコード `202` は、次の応答本文を返す可能性があります。

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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認する。 |
| `ids-too-large` | 項目 ID は250文字以内にする必要があります。 |
| `ids-not-strings` | 項目 ID は文字列型でなければなりません。 |
| `ids-not-unique` | 項目 ID はリクエスト内で一意でなければなりません。 |
| `invalid-ids` | 項目 ID には、英字、数字、ハイフン、アンダースコアのみを使用できます。 |
| `invalid-fields` | APIリクエストで送信するすべてのフィールドが、すでにカタログに存在していることを確認する。これは、エラーに記載されている ID フィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | 項目オブジェクトのキーに `.` または `$` を含めることはできません。 |
| `items-missing-ids` | アイテムIDを持たないアイテムがある。各項目が項目 ID を持っていることを確認します。 |
| `item-array-invalid` | `items` はオブジェクト配列でなければなりません。 |
| `items-too-large` | 項目値は5,000文字を超えることはできない。 |
| `request-includes-too-many-items` | リクエスト内に項目が多すぎますリクエストごとの項目の上限は50個です。 |
| `too-deep-nesting-in-value-object` | アイテム・オブジェクトは50レベル以上の入れ子を持つことはできない。 |
| `unable-to-coerce-value` | 項目タイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}