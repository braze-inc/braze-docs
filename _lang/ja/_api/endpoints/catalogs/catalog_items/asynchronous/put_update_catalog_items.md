---
nav_title: ".PUT(複数のカタログアイテムを更新します"
article_title: ".PUT(複数のカタログアイテムを更新します"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、Brazeエンドポイントの複数カタログアイテムの更新の詳細について説明します。"

---
{% api %}
# カタログ項目を更新
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数のアイテムを更新します。 

カタログアイテムが存在しない場合、このエンドポイントによってカタログにアイテムが作成されます。各リクエストは最大50個のカタログアイテムをサポートできます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.replace_items`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメータ

|パラメータ|必須|データ型|説明|
|---|---|---|---|
|`catalog_name`|必須|文字列|カタログの名前。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

|パラメータ|必須|データ型|説明|
|---|---|---|---|
|`items`|必須|配列|アイテムオブジェクトを含む配列。各オブジェクトにはIDが必要です。項目オブジェクトには、カタログに存在するフィールドを含める必要があります。リクエストごとに最大50個のアイテムオブジェクトが許可されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストの例

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

このエンドポイントには、`202`、`400`、`404`の3つのステータスコード応答があります。

### 成功時の応答の例

ステータスコード`202`は次のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例

ステータスコード`400`は次のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

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

次の表に、返される可能性のあるエラーとそれに関連するトラブルシューティング手順を示します。

|エラー|トラブルシューティング|
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認します。 |
|`ids-not-string`|各項目IDが文字列であることを確認する。|
| `ids-not-unique` | 各項目IDが一意であることを確認します。 |
|`ids-too-large`|各項目IDの文字数制限は250文字です。|
|`item-array-invalid`|`items`はオブジェクトの配列でなければなりません。|
| `items-missing-ids` | 各項目にIDが設定されていることを確認します。 |
|`items-too-large`|アイテム値は5,000文字以内です。|
| `invalid-ids` | 項目ID名に使用できる文字は、英字、数字、ハイフン、アンダースコアです。 |
| `invalid-fields` | APIリクエストで送信しているすべてのフィールドがすでにカタログに存在することを確認します。エラーで述べたIDフィールドとは関係ありません。|
|`invalid-keys-in-value-object`|アイテムオブジェクトキーに`.`や`$`を含めることはできません。|
|`too-deep-nesting-in-value-object`|アイテムオブジェクトのネストレベルは50レベルまでです。|
|`request-includes-too-many-items`|リクエストのアイテム数が多すぎます。リクエストあたりのアイテム数の上限は50です。|
|`unable-to-coerce-value`|アイテムタイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
