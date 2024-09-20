---
nav_title: "DELETE:カタログ選択を削除"
article_title: "DELETE:カタログ選択を削除"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「カタログ選択を削除」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログ選択を削除する
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> カタログの選択を削除するには、このエンドポイントを使用する。
{% alert important %}
このエンドポイントは現在早期アクセス中である。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、`catalogs.delete_selection`権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## パスパラメーター

| パラメーター        | required | データ型 | 説明                    |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name`   | 必須 | string    | カタログ名。           |
| `selection_name` | 必須 | string    | カタログセレクションの名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 応答

このエンドポイントには、`202` と `404` の 2 つのステータスコード応答があります。

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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラー                | トラブルシューティング                                          |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found`  | カタログ名が有効であることを確認する。                    |
| `invalid-selection`  | セレクション名が有効であることを確認する。                  |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}