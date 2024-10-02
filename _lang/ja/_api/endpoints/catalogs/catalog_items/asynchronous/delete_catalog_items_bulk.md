---
nav_title: "削除:複数のカタログ項目を削除する"
article_title: "削除:複数のカタログ項目を削除する"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を削除するBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# 複数のカタログ項目を削除する
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> カタログの複数の項目を削除するには、このエンドポイントを使用する。 

各リクエストは最大50個の項目まで対応できます。このエンドポイントは非同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.delete_items` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | string | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `items` | required | 配列 | アイテム・オブジェクトを含む配列。項目オブジェクトには、Braze が削除すべき項目を参照する `id` が含まれている必要があります。1回のリクエストにつき、アイテムオブジェクトは50個まで認められる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## 応答

このエンドポイントには、`202`、`400`、`404` という3つのステータスコード応答があります。

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
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request",
}
```

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認する。 |
| `ids-too-large` | 項目 ID は250文字以内にする必要があります。 |
| `ids-not-unique` | 項目 ID がリクエスト内で一意であることを確認します。 |
| `ids-not-strings` | 項目 ID は文字列型でなければなりません。 |
| `items-missing-ids` | アイテムIDを持たないアイテムがある。各項目に項目 ID があることを確認します。 |
| `invalid-ids` | 項目 ID には、英字、数字、ハイフン、アンダースコアのみを使用できます。 |
| `request-includes-too-many-items` | リクエスト内の項目が多すぎますリクエストごとの項目の上限は50個です。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}