---
nav_title: "GET：未登録メールアドレスのクエリーリスト"
article_title: "GET：未登録メールアドレスのクエリーリスト"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、Retrieve list of or query email unsubscribes Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 配信停止メールアドレスのクエリーリスト
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> このエンドポイントを使用して、`start_date` から`end_date` までの期間に配信停止された最新のメールを返します。サブスクリプションの完全な状態履歴については、[Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)使用してこのデータを追跡してください。

このエンドポイントを使用して、Brazeと他のメールシステムまたは独自のデータベースとの双方向同期を設定できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.unsubscribe` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
| ----------|-----------| ---------|------ |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列|配信停止を検索する範囲の開始日。これは、APIによってUTC時間の真夜中として扱われる。|
| `end_date` | オプション <br>(注を参照）｜YYYY-MM-DD形式の文字列｜配信停止を検索する範囲の終了日。これは、APIによってUTC時間の真夜中として扱われる。|
|`limit` ｜任意｜整数｜返される結果の数を制限するためのオプション・フィールド。デフォルトは100、最大は500。|
|`offset` ｜任意｜整数｜取得するリストの開始点。|
|`sort_direction` ｜オプション｜文字列｜配信停止を古いものから新しいものへとソートするには、値`asc` を渡す。`desc` 、新しいものから古いものへとソートする。`sort_direction` が含まれていない場合、デフォルトの順序は新しいものから古いものへとなる。|
| `email` | オプション <br>(注を参照) | String | 提供された場合、ユーザーが購読を解除したかどうかを返します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`end_date` のほか、`email` または`start_date` のいずれかを提示しなければならない。
{% endalert %}

日付範囲に`limit` を超える配信停止件数がある場合は、複数回の API 呼び出しを行う必要があります。その都度、`offset` を増やし、`limit` を下回るか、結果がゼロになるまで呼び出します。

## リクエスト例 
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

エントリーは降順で表示される。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
