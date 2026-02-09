---
nav_title: "POST:カタログ・フィールドを作成する"
article_title: "POST:カタログフィールドの作成"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログフィールドの作成」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログ・フィールドを作成する
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> このエンドポイントを使用して、カタログに複数のフィールドを作成する。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.create_fields`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## パスパラメーター

| パラメータ      | required | データ型 | 説明          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | 必須 | 文字列    | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエストパラメーター

| パラメーター | required | データ型 | 説明                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | required | 配列     | フィールドオブジェクトを含む配列。フィールドオブジェクトは、新しいフィールドの名前とタイプを含んでいなければなりません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエスト例

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
    }
  ]
}'
```

## 応答

このエンドポイントには、`202`、`400`、`404` という 3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー                                | トラブルシューティング                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | 任意のエラーが発生した。もう一度試すか、[サポートに]({{site.baseurl}}/support_contact/)連絡する。 |
| `catalog-not-found`                  | カタログ名が有効であることを確認する。                                                                  |
| `company-size-limit-already-reached` | カタログのストレージサイズの上限に達しています。                                                             |
| `request-includes-too-many-fields`   | 各リクエストは最大50の新規フィールドをサポートできる。                                                          |
| `catalog-exceeds-fields-limit`       | カタログは500以上のフィールドを持つことはできない。                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
