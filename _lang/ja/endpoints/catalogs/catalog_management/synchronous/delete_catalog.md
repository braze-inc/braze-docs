---
nav_title: "DELETE:カタログを削除する"
article_title: "DELETE:カタログの削除"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「カタログの削除」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログを削除する
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> カタログを削除するには、このエンドポイントを使用する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.delete`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 応答

このエンドポイントには2つのステータスコード応答があります: `200` と `404`。

### 成功応答の例

ステータスコード `200` は、次の応答本文を返す可能性があります。

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

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
