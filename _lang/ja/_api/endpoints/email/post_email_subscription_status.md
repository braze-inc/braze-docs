---
nav_title: "ポスト:メール購読ステータスの変更"
article_title: "ポスト:メール購読ステータスの変更"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、ユーザーのメール購読ステータスを変更するBrazeエンドポイントの詳細について概説します。"

---
{% api %}
# メール購読ステータスの変更
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのメール購読状態を設定します。 

ユーザーは、`opted_in` 、`unsubscribed` 、または`subscribed` （特にオプトインまたはオプトアウトされていない）。

Braze内のどのユーザーにもまだ関連付けられていないメールアドレスのメール購読状態を設定することができます。そのEメールアドレスがその後ユーザーに関連付けられると、アップロードしたEメール購読状態が自動的に設定されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.status` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
| --------- | ---------| --------- | ----------- |
|`email` ｜必須｜文字列または配列｜修正するEメールアドレスの文字列、または最大50個までの配列。|
|`subscription_state` ｜必須｜文字列｜"subscribe"、"unsubscribed"、または "opted_in "のいずれか。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
