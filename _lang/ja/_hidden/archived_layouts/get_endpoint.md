---
nav_title: "GET: [エンドポイント名]"
article_title: "レイアウト例:GET: [エンドポイント名]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "ここでは、Get [エンドポイントの名前]Braze エンドポイントを使用するための使用方法とパラメータについて説明します。"

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# クエリまたはリスト\[アイテムエンドポイント&クォート;取得&クォート;]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
このエンドポイントを使用して、特定の期間内に"invalid"と見なされた電話番号の一覧を取得します。

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## レートリミット

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md エンドポイント='デフォルト' %}

## 要求パラメータ

<!--This is where you can give more information about your endpoint parameters. -->

| パラメータ | 必須 | データ型 | 説明 |
| ----------|-----------| ----------|----- |
| `start_date` | オプション <br>(注参照) | YYYY-MM-DD 形式の文字列| 無効な電話番号を取得する範囲の開始日は、`end_date` より前である必要があります。これは、API によってUTC 時刻で午前0 時として処理されます。 |
| `end_date` | オプション <br>(注参照) | YYYY-MM-DD 形式の文字列 | 無効な電話番号を取得する範囲の終了日。これは、API によってUTC 時刻で午前0 時として処理されます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するオプションのフィールド。デフォルトは100、最大は500 です。 |
| `offset` | オプション | 整数 | 取得元のリストの任意の開始点。 |
| `phone_numbers` | オプション <br>(注参照) | e.164 形式の文字列の配列 | もし提供されている場合、無効であることが判明した場合は、電話番号を返送します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`start_date` と`end_date` OR `phone_numbers` のいずれかを指定する必要があります。`start_date`、`end_date`、および`phone_numbers` の3 つすべてを指定すると、指定された電話番号が優先され、日付範囲は無視されます。
{% endalert %}

## リクエスト例

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## レスポンス

<!-- An example response that defines the different variables returned-->
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}
