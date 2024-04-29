---
nav_title: "削除複数のカタログアイテムを削除します"
article_title: "削除複数のカタログアイテムを削除します"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を削除するBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# 複数のカタログアイテムを削除します
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> カタログの複数の項目を削除するには、このエンドポイントを使用する。 

各リクエストは最大50アイテムまで対応できる。このエンドポイントは非同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## 前提条件

このエンドポイントを使うには、`catalogs.delete_items` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`items` ｜必須｜配列｜アイテム・オブジェクトを含む配列。アイテムオブジェクトには、Brazeが削除すべきアイテムを参照する`id` 。リクエスト1件につきアイテムオブジェクトは50個まで許可される。|
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

このエンドポイントには3つのステータスコード・レスポンスがある：`202` 、`400` 、`404` 。

### 成功応答例

ステータスコード`202` 、以下のレスポンスボディを返すことができる。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード`400` 、以下のレスポンスボディを返すことができる。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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

| トラブルシューティング
| --- | --- |
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`ids-too-large` | アイテムIDは250文字以内である。|
|`ids-not-unique` | アイテムIDがリクエスト内でユニークであることをチェックする。|
|`ids-not-strings` | アイテムIDは文字列型でなければならない。|
|`items-missing-ids` | アイテムIDを持たないアイテムがある。各アイテムがアイテムIDを持っていることを確認する。|
アイテム ID には、英字、数字、ハイフン、アンダースコアのみを使用できます。
|`request-includes-too-many-items` | リクエストの項目が多すぎる。1回のリクエストにつき、アイテム数の上限は50である。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}