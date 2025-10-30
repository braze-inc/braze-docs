---
nav_title: "取得:ハードバウンスメールの照会"
article_title: "取得:ハードバウンスメールの照会"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「ハードバウンスメールアドレスの照会またはリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ハードバウンスメールの照会
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> このエンドポイントを使用して、一定期間内にメールメッセージを「ハードバウンス」したメールアドレスのリストを取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`email.hard_bounces`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ----------|----- |
| `start_date` | オプション* | YYYY-MM-DD形式の文字列| *`start_date` または `email` のいずれかが必要です。これは、ハードバウンスを取得する範囲の開始日であり、`end_date` より前である必要があります。これは、API によって UTC 時間の午前 0 時として扱われます。 |
| `end_date` | required | YYYY-MM-DD形式の文字列 | ハードバウンスを取得する範囲の終了日。これは、API によって UTC 時間の午前 0 時として扱われます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するためのオプション・フィールド。デフォルトは100で、最大は500です。 |
| `offset` | オプション | 整数 | 取得先となるリスト内のオプションの開始点。 |
| `email` | オプション* | string | *`start_date` または `email` のいずれかが必要です。指定されると、ユーザーがハードバウンスしたかどうかを返します。Eメールの文字列が正しくフォーマットされているか確認する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
`end_date` と `email` または `start_date` のいずれかを指定する必要があります。`start_date`、`end_date`、`email` の3つすべてを指定した場合、指定されたメールを優先し、日付の範囲は無視します。
{% endalert %}

日付範囲に `limit` の数を超えるハードバウンスがある場合、複数回の API 呼び出しが必要になります。呼び出しによって返されるのが `limit` を下回るか、結果がゼロになるまで、その都度 `offset` を増やします。`email` とともに `offset` および `limit` パラメーターを含めると、空の応答が返されることがあります。

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答
エントリは降順で表示されます。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
