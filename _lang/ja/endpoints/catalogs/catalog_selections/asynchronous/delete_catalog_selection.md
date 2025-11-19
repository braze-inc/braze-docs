---
nav_title: "DELETE:カタログ選択を削除する"
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

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.delete_selection`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## パスパラメーター

| パラメータ        | required | データ型 | 説明                    |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name`   | 必須 | 文字列    | カタログ名。           |
| `selection_name` | 必須 | 文字列    | カタログセレクションの名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
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

| エラー                | トラブルシューティング                                          |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found`  | カタログ名が有効であることを確認する。                    |
| `invalid-selection`  | セレクション名が有効であることを確認する。                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
