---
nav_title: "ポストカタログを作成"
article_title: "ポストカタログを作成"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、Create catalog Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# カタログを作成する
{% apimethod post %}
カタログ
{% endapimethod %}

> このエンドポイントを使用してカタログを作成する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## 前提条件

このエンドポイントを使うには、`catalogs.create` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## リクエストパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalogs` ｜必須｜配列｜カタログオブジェクトを含む配列。このリクエストでは1つのカタログオブジェクトのみが許可される。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### カタログ・オブジェクトのパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`name` ｜必須｜文字列｜作成したいカタログの名前。|
|`description` | 必須 | 文字列 | 作成したいカタログの説明。|
|`fields` ｜必須｜配列｜オブジェクトの配列で、オブジェクトはキー`name` と`type` を含む。|
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

## 応答

このエンドポイントには2つのステータスコード・レスポンスがある：`201` と`400` 。

### 成功応答例

ステータスコード`201` 、以下のレスポンスボディを返すことができる。

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

### エラー応答例

ステータスコード`400` 、以下のレスポンスボディを返すことができる。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| トラブルシューティング
| --- | --- |
|`catalog-array-invalid` |`catalogs` はオブジェクトの配列でなければならない。|
その名前のカタログはすでに存在します
|`catalog-name-too-large` ｜カタログ名の文字数制限は250である。|
|`description-too-long` ｜説明文の文字数制限は250文字である。|
|`field-names-not-unique` | 同じフィールド名が2回参照されている。|
|`field-names-too-large` ｜フィールド名の文字数制限は250である。|
|`id-not-first-column` ｜`id` ｜は配列の最初のフィールドでなければならない。型が文字列であることを確認する。|
|`invalid-catalog-name` | カタログ名にはアルファベット、数字、ハイフン、アンダースコアのみを含めることができる。|
|`invalid-field-names` ｜フィールドにはアルファベット、数字、ハイフン、アンダースコアのみを含めることができる。|
|`invalid-field-types` ｜フィールドタイプが有効であることを確認する。|
|`invalid-fields` |`fields` の書式が正しくない。|
|`too-many-catalog-atoms` ｜1つのリクエストにつき1つのカタログしか作成できない。|
|`too-many-fields` | フィールド数の上限は500である。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
