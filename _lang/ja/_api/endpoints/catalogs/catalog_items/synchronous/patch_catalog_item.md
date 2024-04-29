---
nav_title: "パッチ:カタログ項目を編集"
article_title: "パッチ:カタログ項目を編集"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、編集カタログアイテムBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログ項目を編集
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の既存のアイテムを編集します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.update_item`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメータ

|パラメータ|必須|データ型|説明|
|---|---|---|---|
|`catalog_name`|必須|文字列|カタログの名前。|
|`item_id`|必須|文字列|カタログアイテムのID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

|パラメータ|必須|データ型|説明|
|---|---|---|---|
|`items`|必須|配列|アイテムオブジェクトを含む配列。項目オブジェクトには、`id`フィールドを除くカタログに存在するフィールドを含める必要があります。リクエストごとに許可されるアイテムオブジェクトは1つだけです。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストの例

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

このエンドポイントには、`200`、`400`、`404`の3つのステータスコード応答があります。

### 成功時の応答の例

ステータスコード`200`は次のレスポンスボディを返す可能性があります。

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
|`arbitrary-error`|任意のエラーが発生しました。後でもう一度やり直すか、[サポートに]({{site.baseurl}}/support_contact/)お問い合わせください。|
| `catalog-not-found` | カタログ名が有効であることを確認します。 |
| `filtered-set-field-too-long` | 項目の文字数制限を超えたフィルタされたセットでフィールド値が使用されています。 |
| `id-in-body` | カタログにアイテムIDがすでに存在します。 |
|`ids-too-large`|各項目IDの文字数制限は250文字です。|
| `invalid-ids` | 項目ID名に使用できる文字は、英字、数字、ハイフン、アンダースコアです。 |
| `invalid-fields` | リクエストのフィールドがカタログに存在することを確認します。 |
|`invalid-keys-in-value-object`|アイテムオブジェクトキーに`.`や`$`を含めることはできません。|
| `item-not-found` | カタログに商品が入っていることを確認します。 |
|`item-array-invalid`|`items`はオブジェクトの配列でなければなりません。|
|`items-too-large`|各項目の文字数制限は5,000文字です。|
| `request-includes-too-many-items` | 1リクエストにつき編集できるカタログアイテムは1つだけです。 |
|`too-deep-nesting-in-value-object`|アイテムオブジェクトのネストレベルは50レベルまでです。|
|`unable-to-coerce-value`|アイテムタイプは変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}