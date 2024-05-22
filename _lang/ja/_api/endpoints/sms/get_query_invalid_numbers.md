---
nav_title: "GET：無効な電話番号の照会"
article_title: "GET：無効な電話番号の照会"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、Query invalid phone numbers Brazeエンドポイントの詳細について説明します。"
---
{% api %}
# 無効な電話番号の照会
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> このエンドポイントを使用して、一定期間内に「無効」とされた電話番号のリストを取り出します。詳しくは「[無効な電話番号の処理]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers)」のドキュメントをご覧ください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`sms.invalid_phone_numbers` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
| ----------|-----------| ----------|----- |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列|無効な電話番号を検索する範囲の開始日、`end_date` より前でなければならない。これは、APIによってUTC時間の真夜中として扱われる。|
| `end_date` | オプション <br>(注を参照）｜YYYY-MM-DD形式の文字列｜無効な電話番号を検索する範囲の終了日。これは、APIによってUTC時間の真夜中として扱われる。|
|`limit` ｜任意｜整数｜返される結果の数を制限するためのオプション・フィールド。デフォルトは100、最大は500。|
|`offset` ｜任意｜整数｜取得するリストの開始点。|
|`phone_numbers` | オプション <br>(注を参照）｜e.164形式の文字列の配列｜提供された場合、それが無効であることが判明した場合、電話番号を返します。|
|`reason` | オプション <br>(注を参照) | String | 利用可能な値は、"provider\_error"(プロバイダーエラーで電話がSMSを受信できないことを示す)または "deactivated"(電話番号が無効化された)。省略された場合は、すべての理由が返される。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`start_date` と`end_date` または`phone_numbers` のいずれかを提示しなければならない。`start_date` 、`end_date` 、`phone_numbers` の3つすべてを入力された場合、入力された電話番号を優先し、日付の範囲は無視します。
{% endalert %}

日付範囲に`limit` を超える無効な電話番号がある場合は、`limit` より少ないかゼロの結果が返されるまで、毎回`offset` を増やしながら複数のAPIコールを行う必要があります。

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答
エントリーは降順で表示される。

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
