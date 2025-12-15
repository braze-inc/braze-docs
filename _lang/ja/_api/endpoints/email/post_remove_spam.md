---
nav_title: "POST:スパムリストからメールアドレスを削除する"
article_title: "POST:スパムリストからメールアドレスを削除"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "この記事では、スパムリストBrazeエンドポイントからメールアドレスを削除する方法について詳しく説明します。"

---
{% api %}
# スパムリストからメールアドレスを削除する
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> このエンドポイントを使用して、メールアドレスをBrazeのスパムリストおよびメールプロバイダーが管理するスパムリストから削除します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`email.spam.remove`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| --------|------- |
| `email` | 必須 | 文字列または配列 | 修正するEメールアドレスを文字列で、または最大50個までの配列で指定する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
