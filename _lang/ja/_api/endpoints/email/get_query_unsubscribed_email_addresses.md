---
nav_title: "取得:配信停止になっているメールアドレスのリストの照会"
article_title: "取得:配信停止になっているメールアドレスのリストを照会"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、配信停止になっているメールの照会のリストを取得する Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 配信停止になっているメールアドレスのリストの照会
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> このエンドポイントを使用して、`start_date` から `end_date` までの期間に配信停止された最新のメールを返します。完全なサブスクリプション状態の履歴については、このデータを追跡するために[Currents]({{site.baseurl}}/user_guide/data/braze_currents/)を使用してください。

このエンドポイントを使用して、Brazeと他のメールシステムまたは独自のデータベースとの間で双方向同期を設定できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`email.unsubscribe`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ---------|------ |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列| 配信停止を取得する範囲の開始日。end_date. より前でなければならない。API では UTC 時間の午前 0 時として扱われる。 |
| `end_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列 | 配信停止を取得する範囲の終了日。これは、API によって UTC 時間の午前 0 時として扱われます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するためのオプション・フィールド。デフォルトは100で、最大は500です。 |
| `offset` | オプション | 整数 | 取得先となるリスト内のオプションの開始点。 |
| `sort_direction` | オプション | 文字列 | 値 `asc` を渡して、配信停止を最も古いものから最も新しいものへと並べ替えます。`desc`を渡して、最新のものから古いものへ並べ替えます。`sort_direction` が含まれていない場合、デフォルトの順序は新しいものから古いものです。 |
| `email` | オプション <br>（注を参照） | 文字列 | 指定されると、ユーザーが配信停止したかどうかを返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`end_date` を指定する必要があり、さらに `email` または `start_date` のいずれかを指定する必要があります。
{% endalert %}

日付範囲に`limit`以上の退会者がいる場合、複数のAPI呼び出しを行う必要があります。そのたびに`offset`を増やして、呼び出しが`limit`未満またはゼロの結果を返すまで繰り返します。

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

エントリは降順で表示されます。

```json
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
