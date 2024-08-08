---
nav_title: "削除:カタログ項目を削除"
article_title: "削除:カタログ項目を削除"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、Delete カタログアイテムBraze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログアイテムの削除
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の項目を削除します。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.delete_item` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `catalog_name` | 必須| 文字列| カタログの名前。|
| `item_id` | Required | String | カタログアイテムのID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメータ

このエンドポイントのリクエストボディはありません。

## リクエスト例

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

このエンドポイントには、`202`、`400`、`404` の3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード`202` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンス例

ステータスコード`400` は、以下のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します。

| エラー| トラブルシューティング|
| --- | --- |
| `arbitrary-error` | 任意のエラーが発生しました。もう一度やり直すか、[Support]({{site.baseurl}}/support_contact/)にお問い合わせください。|
| `catalog-not-found` | カタログ名が有効であることを確認します。|
| `item-not-found` | 削除するアイテムがカタログに存在することを確認します。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}