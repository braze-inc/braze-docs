---
nav_title: "取得:複数のカタログアイテムの詳細の一覧表示"
article_title: "取得:複数のカタログアイテムの詳細の一覧表示"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、List multiple catalog item details Braze endpointの詳細について説明します。"

---
{% api %}
# 複数のカタログアイテムの詳細を一覧表示する
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、複数のカタログアイテムとそのコンテンツを返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.get_items` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `catalog_name` | 必須| 文字列| カタログの名前。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## クエリパラメーター

このエンドポイントへの各呼び出しは、50 個の項目を返すことに注意してください。項目数が50 を超えるカタログの場合は、`Link` ヘッダを使用して、次のページのデータを取得します(応答例を参照)。

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `cursor` | オプション| 文字列| カタログアイテムのページ分割を決定します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求パラメータ

このエンドポイントのリクエストボディはありません。

## リクエスト例

### カーソルなし

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソルあり

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

このエンドポイントには、`200`、`400`、`404` の3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード`200` は、以下のレスポンスヘッダと本文を返す可能性があります。

{% alert note %}
カタログのアイテム数が50 以下の場合、`Link` ヘッダは存在しません。カーソルがないコールの場合、`prev` は表示されません。項目の最後のページを見ると、`next` は表示されません。
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### エラーレスポンス例

ステータスコード`400` は、以下のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
  "errors": [
    {
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
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
| `catalog-not-found` | カタログ名が有効であることを確認します。|
| `invalid-cursor` | `cursor` が有効であることを確認します。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}