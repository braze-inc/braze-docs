---
nav_title: "GET: [Endpoint Name]"
article_title: "レイアウト例：GET: [Endpoint Name]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "この記事では、Get [エンドポイント名] Braze エンドポイントを使用するための使用方法とパラメーターについて説明します。"

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# クエリまたは List [項目エンドポイント "Gets"

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
このエンドポイントを使用して、一定期間内に「無効」と判断された電話番号のリストを引き出す。

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## レート制限

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

<!--This is where you can give more information about your endpoint parameters. -->

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ----------|----- |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列| 無効な電話番号を取得する範囲の開始日であり、`end_date` より前である必要があります。これは API によって UTC 時間の真夜中として扱われます。 |
| `end_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列 | 無効な電話番号を取得する範囲の終了日。これは API によって UTC 時間の真夜中として扱われます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するためのオプション・フィールド。デフォルトは100で、最大は500です。 |
| `offset` | オプション | 整数 | 取得先となるリスト内のオプションの開始点。 |
| `phone_numbers` | オプション <br>(注を参照) | e.164 形式の文字列の配列 | 提供された場合、電話番号が無効であることが判明した場合は返却する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`start_date` と `end_date`、または `phone_numbers` のいずれかを指定する必要があります。`start_date`、`end_date`、`phone_numbers` の3つすべてを指定した場合、指定された電話番号を優先し、日付の範囲は無視します。
{% endalert %}

## 例のリクエスト

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

<!-- An example response that defines the different variables returned-->
```json
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
