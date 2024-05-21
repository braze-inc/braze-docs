---
nav_title: "設置:カタログ項目を更新"
article_title: "設置:カタログ項目を更新"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "この記事では、カタログアイテムのBrazeエンドポイントの更新についての詳細を説明します。"

---
{% api %}
# カタログ項目を更新
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> カタログのアイテムを更新するには、このエンドポイントを使用します。 

`item_id` が見つからない場合は、このエンドポイントがカタログにアイテムを作成します。このエンドポイントは同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.replace_item` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

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
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
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
|`id-in-body` | リクエストボディのアイテムIDを削除する。|
|`ids-too-large` ｜各アイテムIDの文字数制限は250文字です。|
|`invalid-ids` ｜アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアです。|
|`invalid-fields` ｜APIリクエストで送信するすべてのフィールドがカタログにすでに存在することを確認する。これはエラーにあるIDフィールドとは関係ない。|
|`invalid-keys-in-value-object` | アイテム・オブジェクト・キーに`.` または`$` を含めることはできない。|
|`item-already-exists` | そのアイテムはすでにカタログに存在します。|
|`item-array-invalid` |`items` はオブジェクトの配列でなければならない。|
|`items-too-large` ｜各項目の文字数制限は5,000文字です。|
|`request-includes-too-many-items` ｜1つのリクエストにつき1つのカタログ項目しか作成できません。|
|`too-deep-nesting-in-value-object` | アイテムオブジェクトは50レベル以上の入れ子を持つことができない。|
|`unable-to-coerce-value` ｜アイテムタイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}