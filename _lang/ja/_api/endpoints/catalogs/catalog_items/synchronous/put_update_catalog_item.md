---
nav_title: ".PUT(カタログ項目を更新"
article_title: ".PUT(カタログ項目を更新"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "この記事では、カタログ項目の Braze エンドポイントの更新について詳しく説明します。"

---
{% api %}
# カタログ項目を更新
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログ内のアイテムを更新します。 

が `item_id` 見つからない場合、このエンドポイントはカタログにアイテムを作成します。このエンドポイントは同期的です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、アクセス許可を持つ `catalogs.replace_item` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パス パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `catalog_name` |必須項目 |文字列 |カタログの名前。|
| `item_id` |必須項目 |文字列 |カタログ アイテムの ID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `items` |必須項目 |配列 |項目オブジェクトを含む配列。アイテム オブジェクトには、フィールド以外の `id` カタログに存在するフィールドが含まれている必要があります。要求ごとに許可される項目オブジェクトは 1 つだけです。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求の例

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

このエンドポイント`200`には、 `400``404`

### 成功応答の例

状態コード `200` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例

状態コード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、「 [トラブルシューティング](#troubleshooting) 」を参照してください。

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

次の表に、返される可能性のあるエラーと、それに関連するトラブルシューティング手順を示します。

|エラー |トラブルシューティング |
| --- | --- |
| `arbitrary-error` |任意のエラーが発生しました。もう一度お試しいただくか、 [サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。|
| `catalog-not-found` |カタログ名が有効であることを確認してください。|
| `filtered-set-field-too-long` |フィールド値は、項目の文字数制限を超えるフィルター処理されたセットで使用されています。|
| `id-in-body` |要求本文の項目 ID をすべて削除します。|
| `ids-too-large` |各項目 ID の文字数制限は 250 文字です。|
| `invalid-ids` |アイテム ID 名でサポートされている文字は、文字、数字、ハイフン、アンダースコアです。|
| `invalid-fields` |API 要求で送信するすべてのフィールドがカタログに既に存在することを確認します。これは、エラーに記載されている ID フィールドとは関係ありません。|
| `invalid-keys-in-value-object` |項目オブジェクトのキーに `.` または `$`を含めることはできません。 |
| `item-already-exists` |アイテムはカタログに既に存在します。|
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。|
| `items-too-large` |各項目の文字数制限は 5,000 文字です。|
| `request-includes-too-many-items` |要求ごとに作成できるカタログ項目は 1 つだけです。|
| `too-deep-nesting-in-value-object` |項目オブジェクトは、50 レベルを超える入れ子を持つことはできません。|
| `unable-to-coerce-value` |アイテムの種類は変換できません。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}