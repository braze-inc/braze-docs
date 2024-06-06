---
nav_title: "ポスト:メールのブロックリスト"
article_title: "ポスト:メールのブロックリスト"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "この記事では、Braze エンドポイントのブロックリストメールの詳細について説明します。"

---
{% api %}
# メールのブロックリスト
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> このエンドポイントを使用して、メールからユーザの登録を解除し、ハードバウンスとしてマークします。
 
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.blacklist` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| -----------|----------| --------|------- |
| `email` | Required | String or array | string email address to blocklist、またはblocklist に50 個までのメールアドレスの配列。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
