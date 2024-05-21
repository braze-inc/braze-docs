---
nav_title: "パッチ:カタログ項目を編集"
article_title: "パッチ:カタログ項目を編集"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、カタログアイテムの編集Brazeエンドポイントの詳細について概説します。"

---
{% api %}
# カタログ項目を編集
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> カタログの既存のアイテムを編集するには、このエンドポイントを使用します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.update_item` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## 経路パラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
|`item_id` | 必須 | String | カタログ項目のID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`items` ｜必須｜配列｜アイテム・オブジェクトを含む配列。アイテム・オブジェクトは、`id` フィールドを除き、カタログに存在するフィールドを含むべきである。1つのリクエストにつき1つのアイテムオブジェクトのみが許可される。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

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
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## 応答

このエンドポイントには、`200` 、`400` 、`404` の3つのステータスコード・レスポンスがある。

### 成功応答例

ステータスコード`200` 、以下のレスポンスボディを返すことができる。

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
|`arbitrary-error` ｜任意のエラーが発生しました。再度お試しいただくか、[サポートまで]({{site.baseurl}}/support_contact/)お問い合わせください。|
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`filtered-set-field-too-long` ｜項目の文字数制限を超えるフィルタリングセットでフィールド値が使用されています。|
|`id-in-body` ｜アイテムIDがすでにカタログに存在します。|
|`ids-too-large` ｜各アイテムIDの文字数制限は250文字です。|
|`invalid-ids` ｜アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアです。|
|`invalid-fields` ｜リクエストのフィールドがカタログに存在することを確認する。|
|`invalid-keys-in-value-object` | アイテム・オブジェクト・キーに`.` または`$` を含めることはできない。|
|`item-not-found` ｜アイテムがカタログに掲載されているか確認する。|
|`item-array-invalid` |`items` はオブジェクトの配列でなければならない。|
|`items-too-large` ｜各項目の文字数制限は5,000文字です。|
|`request-includes-too-many-items` ｜1つのリクエストにつき1つのカタログ項目しか編集できません。|
|`too-deep-nesting-in-value-object` | アイテムオブジェクトは50レベル以上の入れ子を持つことができない。|
|`unable-to-coerce-value` ｜アイテムタイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}