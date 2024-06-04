---
nav_title: "ポスト:カタログを作成"
article_title: "ポスト:カタログを作成"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、Create catalog Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログの作成
{% apimethod post %}
カタログ
{% endapimethod %}

> このエンドポイントを使用して、カタログを作成します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.create` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `catalogs` | 必須| 配列| カタログオブジェクトを含む配列。この要求に使用できるカタログオブジェクトは1 つだけです。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### カタログオブジェクトパラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `name` | Required | String | 作成するカタログの名前。|
| `description` | Required | String | 作成するカタログの説明。|
| `fields` | 必須| 配列| オブジェクトがキー`name` と`type`. | を含むオブジェクトの配列。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例
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
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## レスポンス

このエンドポイントには、`201` と`400` の2 つのステータスコード応答があります。

### 成功応答の例

ステータスコード`201` は、以下のレスポンスボディを返す可能性があります。

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

### エラーレスポンス例

ステータスコード`400` は、以下のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します。

| エラー| トラブルシューティング|
| --- | --- |
| `catalog-array-invalid` | `catalogs` はオブジェクトの配列である必要があります。|
| `catalog-name-already-exists` | その名前のカタログが既に存在します。|
| `catalog-name-too-large` | カタログ名の文字制限は250 です。|
| `description-too-long` | 説明の文字制限は250 です。|
| `field-names-not-unique` | 同じフィールド名が2 回参照されます。|
| `field-names-too-large` | フィールド名の文字数制限は250 です。|
| `id-not-first-column` | `id` は配列の最初のフィールドでなければなりません。型が文字列であることを確認します。|
| `invalid-catalog-name` | カタログ名には、文字、数字、ハイフン、およびアンダースコアのみを使用できます。|
| `invalid-field-names` | 文字、数字、ハイフン、アンダースコアのみを含めることができます。|
| `invalid-field-types` | フィールドタイプが有効であることを確認します。|
| `invalid-fields` | `fields` が正しくフォーマットされていません。|
| `too-many-catalog-atoms` | 要求ごとに1つのカタログのみ作成できます。|
| `too-many-fields` | フィールド数の制限は500 です。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
