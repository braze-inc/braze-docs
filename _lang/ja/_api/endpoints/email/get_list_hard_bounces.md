---
nav_title: "取得:ハードバウンドされたメールのクエリ"
article_title: "取得:ハードバウンドされたメールのクエリ"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、Brazeエンドポイントのクエリまたはリストハードバウンスメールアドレスに関する詳細の概要を説明します。"

---
{% api %}
# ハードバウンスされたメールのクエリ
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> このエンドポイントを使用して、一定時間内にメールメッセージを「ハードバウンス」したメールアドレスのリストを取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.hard_bounces`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

|パラメータ|必須|データ型|説明|
| ----------|-----------| ----------|----- |
- `start_date` (省略可能)<br>(注参照)|YYYY-MM-DD形式の文字列|ハードバウンスを取得する範囲の開始日。`end_date`より前である必要があります。APIではUTC時間の午前0時として扱われます。|
-  (省略可能)<br>(注参照) | YYYY-MM-DD形式の文字列 | ハードバウンスを取得する範囲の終了日。APIではUTC時間の午前0時として扱われます。|
|`limit`|オプション|整数|返される結果の数を制限するオプションのフィールド。デフォルトは100。最大値は500。|
| `offset` | オプション | 整数 | 取得元リスト内のオプションの始点。 |
-  (省略可能)<br>(注参照) | String | 提供されていれば、ユーザーがハードバウンスしたかどうかを返します。メールの文字列が適切にフォーマットされているか確認してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`start_date`と`end_date`、または`email`のいずれかを指定する必要があります。`start_date`、`end_date`、`email`の3つをすべて指定した場合、与えられたメールを優先して日付の範囲を無視します。
{% endalert %}

日付範囲にハードバウンス数以上の `limit` ものがある場合は、複数の API 呼び出しを行う必要があります。`offset``limit``offset`と`limit`パラメータを`email`と一緒に含めると、空の応答を返す可能性があります。 

## リクエストの例
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答
エントリは降順に表示されます。

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
