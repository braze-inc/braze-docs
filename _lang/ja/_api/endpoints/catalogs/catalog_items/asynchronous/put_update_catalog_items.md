---
nav_title: "設置:複数のカタログアイテムを更新します"
article_title: "設置:複数のカタログアイテムを更新します"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を更新するBrazeエンドポイントの詳細について概説します。"

---
{% api %}
# カタログ項目を更新
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数のアイテムを更新します。 

カタログ項目が存在しない場合、このエンドポイントはカタログに項目を作成します。各リクエストは最大50のカタログ項目をサポートすることができます。このエンドポイントは非同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.replace_items` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## 経路パラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`items` ｜必須｜配列｜アイテム・オブジェクトを含む配列。各オブジェクトはIDを持たなければならない。アイテム・オブジェクトは、カタログに存在するフィールドを含んでいなければならない。1回のリクエストにつき、アイテムオブジェクトは50個まで許可される。|
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
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2
    }
  ]
}'
```

## 応答

このエンドポイントには、`202` 、`400` 、`404` の3つのステータスコード・レスポンスがある。

### 成功応答例

ステータスコード`202` 、以下のレスポンスボディを返すことができる。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード`400` 、以下のレスポンスボディを返すことができる。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

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

次の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`ids-not-string` ｜各アイテムIDが文字列であることを確認する。|
|`ids-not-unique` ｜各アイテムIDが一意であることを確認する。|
|`ids-too-large` ｜各アイテムIDの文字数制限は250文字です。|
|`item-array-invalid` |`items` はオブジェクトの配列でなければならない。|
|`items-missing-ids` ｜各アイテムがIDを持っていることを確認する。|
|`items-too-large` ｜項目値は5,000文字を超えることはできません。|
|`invalid-ids` ｜アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアです。|
|`invalid-fields` ｜APIリクエストで送信するすべてのフィールドが、すでにカタログに存在していることを確認する。これはエラーにあるIDフィールドとは関係ない。|
|`invalid-keys-in-value-object` | アイテム・オブジェクト・キーに`.` または`$` を含めることはできない。|
|`too-deep-nesting-in-value-object` | アイテムオブジェクトは50レベル以上の入れ子を持つことができない。|
|`request-includes-too-many-items` | リクエストの項目数が多すぎます。1回のリクエストの上限は50個です。|
|`unable-to-coerce-value` ｜アイテムタイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
