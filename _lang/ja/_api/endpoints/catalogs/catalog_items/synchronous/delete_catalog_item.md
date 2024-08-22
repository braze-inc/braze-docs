---
nav_title: "DELETE:カタログ項目を削除する"
article_title: "DELETE:カタログ項目を削除する"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「カタログ項目を削除」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログ項目を削除する
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> カタログの項目を削除するには、このエンドポイントを使う。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.delete_item`権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='同期カタログ項目' %}

## パスパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
|  | 必須 | string | カタログ名。 |
|  | 必須 | string | カタログ項目のID。 |


## リクエストパラメーター

このエンドポイントにはリクエストボディがない。

## リクエスト例

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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

| エラー | トラブルシューティング |
| --- | --- |
|  | 任意のエラーが発生した。もう一度試すか、[サポートに]({{site.baseurl}}/support_contact/)連絡する。 |
|  | カタログ名が有効であることを確認する。 |
|  | 削除する項目がカタログに存在することを確認します。 |


{% endapi %}