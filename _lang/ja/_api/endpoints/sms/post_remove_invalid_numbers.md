---
nav_title: "ポスト:無効な電話番号の削除"
article_title: "ポスト:無効な電話番号の削除"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、Remove invalid phone numbers Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 無効な電話番号を削除する
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> このエンドポイントを使用して、無効なリストから"invalid"電話番号を削除します。 

これを使用して、電話番号が無効としてマークされた後、電話番号を再検証できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`sms.invalid_phone_numbers.remove` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| ----------|-----------| ---------|------ |
| `phone_number` | 必須| e.164 形式の文字列の配列| 変更する電話番号が最大50 個の配列。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
