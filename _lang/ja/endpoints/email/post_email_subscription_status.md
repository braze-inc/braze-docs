---
nav_title: "POST:メールサブスクリプションステータスの変更"
article_title: "POST:メールサブスクリプションステータスの変更"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、「ユーザーのメールサブスクリプションステータスの変更」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# メールサブスクリプションステータスの変更
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}。
/email/status
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのメール購読状態を設定する。

ユーザーは、`opted_in`、`unsubscribed`、または `subscribed` （特にオプトインまたはオプトアウトされていない） になる可能性があります。

Braze内のどのユーザーにもまだ関連付けられていないEメールアドレスのEメール購読状態を設定できる。その後、そのEメールアドレスがユーザーに関連付けられると、アップロードしたEメール購読状態が自動的に設定される。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`email.status`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

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

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `email` | 必須 | 文字列または配列 | 修正するEメールアドレスを文字列で、または最大50個までの配列で指定する。 |
| `subscription_state` | 必須 | string | サブスクライバー」、「配信停止」のいずれか、または "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
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
