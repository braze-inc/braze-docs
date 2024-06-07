---
nav_title: "取得:カタログを一覧表示"
article_title: "取得:カタログを一覧表示"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、リストカタログBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログを一覧表示する
{% apimethod get %}
カタログ
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のカタログのリストを返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d65fb86-ccf7-423f-9eb2-f68ab36df824 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`catalogs.get`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## パスとリクエストのパラメーター

このエンドポイントにはパスまたはリクエストパラメータはありません。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功レスポンスの例

`200`ステータスコードは次のレスポンスボディを返す可能性があります。

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 10,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    },
    {
      "description": "My Catalog",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "string_field",
          "type": "string"
        },
        {
          "name": "number_field",
          "type": "number"
        },
        {
          "name": "boolean_field",
          "type": "boolean"
        },
        {
          "name": "time_field",
          "type": "time"
        },
      ],
      "name": "my_catalog",
      "num_items": 3,
      "updated_at": "2022-11-02T09:03:19.967+00:00"
    },
  ],
  "message": "success"
}
```

{% endapi %}
