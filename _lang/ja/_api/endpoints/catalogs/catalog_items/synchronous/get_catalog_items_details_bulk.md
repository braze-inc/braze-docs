---
nav_title: "取得:複数のカタログ商品詳細をリストする"
article_title: "取得:複数のカタログ商品詳細をリストする"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、List multiple catalog item details Brazeエンドポイントの詳細について概説する。"

---
{% api %}
# 複数のカタログ項目の詳細をリストする
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> 複数のカタログ項目とその内容を返すには、このエンドポイントを使う。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## 前提条件

このエンドポイントを使うには、`catalogs.get_items` パーミッションを持つ[APIキーが]({{site.baseurl}}/api/basics#rest-api-key/)必要だ。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`catalog_name` ｜必須｜文字列｜カタログ名。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## クエリパラメーター

このエンドポイントを呼び出すと、50のアイテムが返される。50以上のアイテムを持つカタログの場合、次のレスポンス例に示すように、`Link` ヘッダーを使用して次のページのデータを取得する。

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`cursor` ｜任意｜文字列｜カタログ項目のページ分割を決定する。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメーター

このエンドポイントにはリクエストボディがない。

## リクエスト例

### カーソルなし

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには3つのステータスコード・レスポンスがある：`200` 、`400` 、`404` 。

### 成功応答例

ステータスコード`200` 、以下のレスポンスヘッダとボディを返すことができる。

{% alert note %}
カタログのアイテム数が50以下の場合、`Link` ヘッダーは存在しない。カーソルのない通話では、`prev` 。アイテムの最後のページを見るとき、`next` は表示されない。
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

### エラー応答例

ステータスコード`400` 、以下のレスポンスボディを返すことができる。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| トラブルシューティング
| --- | --- |
|`catalog-not-found` | カタログ名が有効であることを確認する。|
|`invalid-cursor` ｜`cursor` ｜が有効であることを確認する。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}