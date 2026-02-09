---
nav_title: "DELETE:カタログ・フィールドを削除する"
article_title: "DELETE:カタログフィールドの削除"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「カタログフィールドの削除」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログ・フィールドを削除する
{% apimethod delete %}
/catalogs/{catalog_name}/fields/{field_name}
{% endapimethod %}

> カタログ・フィールドを削除するには、このエンドポイントを使用する。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.delete_fields`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## パスパラメーター

| パラメータ      | required | データ型 | 説明                |
| -------------- | -------- | --------- | -------------------------- |
| `catalog_name` | 必須 | 文字列    | カタログ名。       |
| `field_name`   | 必須 | 文字列    | カタログ・フィールドの名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/fields/ratings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 応答

このエンドポイントには2つのステータスコード応答があります: `202` と `404`。

### 成功応答の例

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード `404` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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

| エラー                           | トラブルシューティング                                                  |
| ------------------------------- | ---------------------------------------------------------------- |
| `catalog-not-found`             | カタログ名が有効であることを確認する。                            |
| `field-referenced-by-selection` | カタログフィールドが現在選択によって使用されていることを確認する。 |
| `field-is-inventory`            | カタログ・フィールドがインベントリ・フィールドとして使用されていることを確認する。      |
| `invalid-field-name`            | カタログフィールド名が有効であることを確認する。                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
