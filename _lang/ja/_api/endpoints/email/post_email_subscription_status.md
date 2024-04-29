---
nav_title: "ポストメールサブスクリプションステータスの変更"
article_title: "ポストメールサブスクリプションステータスの変更"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、Change user のメールサブスクリプションステータスBraze エンドポイントの詳細について説明します。"

---
{% api %}
# メールサブスクリプションステータスの変更
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのメールサブスクリプションの状態を設定します。 

ユーザーは、`opted_in`、`unsubscribed`、または`subscribed` (特にオプトインまたはオプトアウトしない) のいずれかです。

Braze 内のユーザにまだ関連付けられていないメールアドレスのメールサブスクリプションの状態を設定できます。その後、そのメールアドレスがユーザに関連付けられると、アップロードしたメールサブスクリプションステートが自動的に設定されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.status` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

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

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
| `email` | 必須| 文字列または配列| 変更する文字列の電子メールアドレス、または変更する最大50 個の電子メールアドレスの配列。|
| `subscription_state` | 必須| 文字列| "subscribed" " unsubscribed" または"opted_in" |
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
