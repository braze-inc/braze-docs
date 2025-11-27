---
nav_title: "POST: [エンドポイント名］"
article_title: "レイアウト例：POST:ユーザートラック"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
excerpt_separator: ""

description: "この記事では、このPOST [エンドポイント名] Brazeエンドポイントの詳細と使用方法について概説する。"

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# [エンドポイント名

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
このエンドポイントを使用して、Brazeの無効リストから「無効な」電話番号を削除する。これを使用して、電話番号が無効とマークされた後、それらの電話番号を再検証できます。

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## レート制限

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

<!--This is where you can give more information about your endpoint request body. -->

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

### リクエストパラメーター

<!--This is a place for you to describe additional details for the parameters in the request body.-->

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ---------|------ |
| `phone_number` | required | e.164 形式の文字列の配列 | 変更する最大 50 個の電話番号の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

<!--The following example demonstrates a request that will remove specific SMS numbers from Braze's invalid phone number list via the API:-->

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```
{% endapi %}
