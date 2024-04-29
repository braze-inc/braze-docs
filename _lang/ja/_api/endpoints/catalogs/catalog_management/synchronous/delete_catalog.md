---
nav_title: "削除カタログを削除する"
article_title: "削除カタログを削除する"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、Delete catalog Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# カタログを削除する
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> カタログを削除するには、このエンドポイントを使用する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## 前提条件

このエンドポイントを使うには、`catalogs.delete` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## パスパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 応答

このエンドポイントには2つのステータスコード・レスポンスがある：`200` と`404` 。

### 成功応答例

ステータスコード`200` 、以下のレスポンスボディを返すことができる：

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード`404` 、以下のレスポンスボディを返すことができる。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| トラブルシューティング
| --- | --- |
|`catalog-not-found` | カタログ名が有効であることを確認する。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}