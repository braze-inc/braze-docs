---
nav_title: "取得:ハードバウンスされたメールのクエリ"
article_title: "取得:ハードバウンスされたメールのクエリ"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、Query またはList hard bounced email addresses Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ハードバウンスされたメールのクエリ
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> このエンドポイントを使用して、"hard bounced"を持つメールアドレスのリストをプルします。特定の時間内にメールメッセージをプルします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.hard_bounces` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| ----------|-----------| ----------|----- |
| `start_date` | オプション<br>(注を参照)| YYYY-MM-DD 形式の文字列| ハードバウンスを取得する範囲の開始日は、`end_date` より前である必要があります。これは、API によってUTC 時刻の午前0 時として処理されます。|
| `end_date` | オプション<br>(注を参照)| YYY-MM-DD 形式の文字列| ハードバウンスを取得する範囲の終了日。これは、API によってUTC 時刻の午前0 時として処理されます。|
| `limit` | オプション| 整数| 返される結果の数を制限するオプションフィールド。デフォルトは100、最大は500 です。|
| `offset` | オプション| 整数| リスト内のオプションの開始点から取得する。|
| `email` | オプション<br>(note を参照) | String | 指定した場合、ユーザがハードバウンスしたかどうかを返します。電子メール文字列が正しくフォーマットされていることを確認します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`start_date` と`end_date` を指定するか、または`email` を指定する必要があります。3 つ、`start_date`、`end_date`、および`email` すべてを指定すると、指定されたE メールが優先され、日付範囲は無視されます。
{% endalert %}

日付範囲に`limit` 個以上のハードバウンスがある場合は、`offset` を増やすたびに`limit` またはゼロのいずれかの結果が返されるまで、複数のAPI 呼び出しを実行する必要があります。`offset` および`limit` パラメータを`email` とともに含めると、空の応答を返すことができます。 

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## レスポンス
エントリは降順で表示されます。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
