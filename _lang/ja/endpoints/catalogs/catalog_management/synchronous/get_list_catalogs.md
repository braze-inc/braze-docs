---
nav_title: "取得:カタログをリストアップする"
article_title: "取得:リストカタログ"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログのリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログをリストアップする
{% apimethod get %}
/catalogs
{% endapimethod %}

> ワークスペース内のカタログのリストを返すには、このエンドポイントを使用する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d65fb86-ccf7-423f-9eb2-f68ab36df824 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## パスとリクエストのパラメータ

このエンドポイントには、パスまたはリクエストパラメータはありません。

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功応答の例

ステータスコード `200` は、次の応答本文を返す可能性があります。

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
