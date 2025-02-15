---
nav_title: "POST:無効な電話番号を削除する"
article_title: "POST:無効な電話番号を削除する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、無効な電話番号を削除するBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# 無効な電話番号を削除する
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> このエンドポイントを使用して、「無効な」電話番号を無効リストから削除する。

これを使用して、電話番号が無効とマークされた後、それらの電話番号を再検証できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`sms.invalid_phone_numbers.remove`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ---------|------ |
| `phone_number` | required | e.164 形式の文字列の配列 | 変更する最大 50 個の電話番号の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
