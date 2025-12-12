---
nav_title: "取得:無効な電話番号を照会する"
article_title: "取得:無効な電話番号を照会する"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「無効な電話番号を照会する」Braze エンドポイントの詳細について説明します。"
---
{% api %}
# 無効な電話番号を照会する
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> このエンドポイントを使用して、一定期間内に「無効」とされた電話番号のリストを引き出す。詳細については、「[無効な電話番号の処理」]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers)のドキュメントを参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`sms.invalid_phone_numbers`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ----------|----- |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列| 無効な電話番号を取得する範囲の開始日であり、`end_date` より前である必要があります。これは API によって UTC 時間の真夜中として扱われます。 |
| `end_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列 | 無効な電話番号を取得する範囲の終了日。これは API によって UTC 時間の真夜中として扱われます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するためのオプション・フィールド。デフォルトは100で、最大は500です。 |
| `offset` | オプション | 整数 | 取得先となるリスト内のオプションの開始点。 |
| `phone_numbers` | オプション <br>(注を参照) | e.164 形式の文字列の配列 | 提供された場合、電話番号が無効であることが判明した場合は返却する。 |
| `reason` | オプション <br>（注を参照） | string | 利用可能な値は、"provider_error" （プロバイダーエラーにより、電話がSMSを受信できないことを示す）または "deactivated"（電話番号が無効化されている）である。省略された場合は、すべての理由が返される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`start_date` と `end_date`、または `phone_numbers` のいずれかを指定する必要があります。`start_date`、`end_date`、`phone_numbers` の3つすべてを指定した場合、指定された電話番号を優先し、日付の範囲は無視します。
{% endalert %}

日付範囲に `limit` の数を超える無効な電話番号がある場合、複数回の API 呼び出しが必要になります。呼び出しによって返されるのが `limit` を下回るか、結果がゼロになるまで、その都度 `offset` を増やします。

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答
エントリは降順で表示されます。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}
