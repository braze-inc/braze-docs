---
nav_title: "パッチ:複数のカタログアイテムを編集します"
article_title: "パッチ:複数のカタログアイテムを編集します"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を編集するBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# 複数のカタログアイテムを編集します
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数の既存アイテムを編集する。

各リクエストは最大50アイテムまで対応できる。このエンドポイントは非同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## 前提条件

このエンドポイントを使うには、`catalogs.update_items` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`items` ｜必須｜配列｜アイテム・オブジェクトを含む配列。アイテム・オブジェクトは、カタログに存在するフィールドを含んでいなければならない。リクエスト1件につきアイテムオブジェクトは50個まで許可される。|
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

このエンドポイントには3つのステータスコード・レスポンスがある：`202` 、`400` 、`404` 。

### 成功応答例

ステータスコード`202` 、以下のレスポンスボディを返すことができる。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード`400` 、以下のレスポンスボディを返すことができる。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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

| トラブルシューティング
| --- | --- |
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`ids-too-large` | アイテムIDは250文字以内である。|
|`ids-not-strings` | アイテムIDは文字列型でなければならない。|
|`ids-not-unique` | アイテムIDはリクエスト内でユニークでなければならない。|
アイテム ID には、英字、数字、ハイフン、アンダースコアのみを使用できます。
|`invalid-fields` ｜APIリクエストで送信するすべてのフィールドがすでにカタログに存在することを確認する。これはエラーにあるIDフィールドとは関係ない。|
|`invalid-keys-in-value-object` | アイテム・オブジェクト・キーに`.` または`$` を含めることはできない。|
|`items-missing-ids` | アイテムIDを持たないアイテムがある。各アイテムがアイテムIDを持っていることを確認する。|
|`item-array-invalid` |`items` はオブジェクトの配列でなければならない。|
|`items-too-large` ｜項目値は5,000文字を超えることはできない。|
|`request-includes-too-many-items` | リクエストの項目が多すぎる。1回のリクエストにつき、アイテム数の上限は50である。|
|`too-deep-nesting-in-value-object` | アイテム・オブジェクトは50レベル以上の入れ子を持つことができない。|
|`unable-to-coerce-value` | アイテムタイプは変換できない。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}