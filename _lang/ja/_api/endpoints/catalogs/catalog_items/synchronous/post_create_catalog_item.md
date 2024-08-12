---
nav_title: "ポスト:カタログアイテムの作成"
article_title: "ポスト:カタログアイテムの作成"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "この記事では、Create catalog item Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログアイテムの作成
{% apimethod post %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログ内にアイテムを作成します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#820c305b-ea6a-4b71-811a-55003a212a40 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.create_item` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `catalog_name` | 必須| 文字列| カタログの名前。|
| `item_id` | Required | String | カタログアイテムのID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `items` | Required | Array | 項目オブジェクトを含む配列。アイテムオブジェクトには、`id` フィールドを除く、カタログ内のすべてのフィールドが含まれている必要があります。リクエストごとに 1 つの項目オブジェクトのみが許可されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

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
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    }
  ]
}'
```

## レスポンス

このエンドポイントには、`201`、`400`、`404` の3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード`201` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンス例

ステータスコード`400` は、以下のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します。

| エラー| トラブルシューティング|
| --- | --- |
| `arbitrary-error` | 任意のエラーが発生しました。もう一度やり直すか、[Support]({{site.baseurl}}/support_contact/)にお問い合わせください。|
| `catalog-not-found` | カタログ名が有効であることを確認します。|
| `filtered-set-field-too-long` | 項目値が、項目の文字制限を超えるフィルタされたセットで使用されています。|
| `id-in-body` | 要求本文のすべての項目ID を削除します。|
| `ids-too-large` | 各項目ID の文字数制限は250 文字です。|
| `invalid-ids` | 項目ID 名でサポートされる文字は、文字、数字、ハイフン、およびアンダースコアです。|
| `invalid-fields` | API リクエストで送信するすべてのフィールドがカタログにすでに存在することを確認します。これは、error で指定されたID フィールドとは関係ありません。|
| `invalid-keys-in-value-object` | 項目オブジェクトキーに`.` または`$` を含めることはできません。|
| `item-already-exists` | アイテムがカタログにすでに存在します。|
| `item-array-invalid` | `items` はオブジェクトの配列である必要があります。|
| `items-too-large` | 各項目の文字数制限は5000 文字です。|
| `request-includes-too-many-items` | リクエストごとに1つのカタログアイテムのみを作成できます。|
| `too-deep-nesting-in-value-object` | アイテムオブジェクトは、50 を超えるレベルのネストを持つことはできません。|
| `unable-to-coerce-value` | 項目タイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}