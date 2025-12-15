---
nav_title: "POST:カタログを作成"
article_title: "POST:カタログを作成する"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、「カタログを作成」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログを作成する
{% apimethod post %}
/catalogs
{% endapimethod %}

> このエンドポイントを使用してカタログを作成する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.create`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `catalogs` | required | 配列 | カタログ・オブジェクトを含む配列。このリクエストでは、カタログオブジェクトは 1 つのみ許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### カタログ・オブジェクトのパラメータ

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `name` | 必須 | 文字列 | 作成したいカタログの名前。 |
| `description` | 必須 | 文字列 | 作成したいカタログの説明。 |
| `fields` | required | 配列 | オブジェクトにキー `name` と `type` が含まれるオブジェクト配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## 応答

このエンドポイントには2つのステータスコード応答があります: `201` と `400`。

### 成功応答の例

ステータスコード `201` は、次の応答本文を返す可能性があります。

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
      ],
      "parameter_values": [
        "restaurants"
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
| `catalog-array-invalid` | `catalogs` はオブジェクト配列でなければなりません。 |
| `catalog-name-already-exists` | その名前のカタログはすでに存在する。 |
| `catalog-name-too-large`  | カタログ名の文字数制限は250文字である。 |
| `description-too-long` | 説明文の文字数制限は250文字である。 |
| `field-names-not-unique` | 同じフィールド名が2回参照されている。 |
| `field-names-too-large` | フィールド名の文字数制限は250文字である。 |
| `id-not-first-column` | `id` は、配列の最初のフィールドである必要があります。型が文字列であることを確認する。 |
| `invalid-catalog-name` | カタログ名にはアルファベット、数字、ハイフン、アンダースコアのみを含めることができる。 |
| `invalid-field-names` | フィールドに含めることができるのは、アルファベット、数字、ハイフン、アンダースコアのみである。 |
| `invalid-field-types` | フィールドタイプが有効であることを確認する。 |
| `invalid-fields` | `fields` が正しくフォーマットされていない。 |
| `too-many-catalog-atoms` | 1つのリクエストにつき1つのカタログしか作成できない。 |
| `too-many-fields` | フィールド数の上限は500である。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
