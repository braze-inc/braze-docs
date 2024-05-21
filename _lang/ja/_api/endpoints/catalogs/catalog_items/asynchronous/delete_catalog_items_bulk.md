---
nav_title: "削除：複数のカタログアイテムを削除します"
article_title: "削除：複数のカタログアイテムを削除します"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、複数のカタログアイテムの削除Brazeエンドポイントについて詳しく説明します。"

---
{% api %}
# 複数のカタログアイテムを削除します
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数のアイテムを削除します。 

各要求は、最大 50 個の項目をサポートできます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `catalogs.delete_items` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パス パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `catalog_name` |必須項目 |文字列 |カタログの名前。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `items` |必須項目 |配列 |項目オブジェクトを含む配列。アイテムオブジェクトには、 `id` Brazeが削除すべきアイテムの参照が含まれている必要があります。要求ごとに最大 50 個の項目オブジェクトが許可されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求の例

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

このエンドポイント`202`には、 `400``404`

### 成功応答の例

状態コード `202` は、次の応答本文を返す可能性があります。

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

次の表に、返される可能性のあるエラーと、それに関連するトラブルシューティング手順を示します。

|エラー |トラブルシューティング |
| --- | --- |
| `catalog-not-found` |カタログ名が有効であることを確認してください。|
| `ids-too-large` |アイテム ID は 250 文字以下にする必要があります。|
| `ids-not-unique` |要求内で項目 ID が一意であることを確認します。|
| `ids-not-strings` |アイテム ID は文字列型である必要があります。|
| `items-missing-ids` |アイテム ID を持たないアイテムがあります。各アイテムにアイテム ID があることを確認します。 |
アイテム ID には、英字、数字、ハイフン、アンダースコアのみを使用できます。
| `request-includes-too-many-items` |リクエストのアイテムが多すぎます。要求ごとの項目数の制限は 50 です。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}