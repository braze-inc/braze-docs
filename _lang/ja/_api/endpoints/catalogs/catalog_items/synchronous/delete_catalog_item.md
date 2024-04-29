---
nav_title: "削除カタログ項目を削除"
article_title: "削除カタログ項目を削除"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、Delete catalog item Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# カタログ項目を削除する
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> カタログの項目を削除するには、このエンドポイントを使う。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## 前提条件

このエンドポイントを使うには、`catalogs.delete_item` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
|`item_id` | 必須 | String | カタログ項目のID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

このエンドポイントにはリクエストボディがない。

## リクエスト例

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| トラブルシューティング
| --- | --- |
|`arbitrary-error` ｜任意のエラーが発生した。再試行するか、[サポートに]({{site.baseurl}}/support_contact/)連絡する。|
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`item-not-found` ｜削除するアイテムがカタログに存在することを確認する。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}