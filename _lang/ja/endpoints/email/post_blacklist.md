---
nav_title: "POST:ブラックリストのメール"
article_title: "POST:ブラックリストのメール"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "この記事では、ブラックリストのメールBrazeエンドポイントに関する詳細を説明します。"

---
{% api %}
# ブラックリストのメール
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}。
/email/blacklist
{% endapimethod %}

{% alert important %}
Brazeは[`/email/blocklist`エンドポイント]({{site.baseurl}}/api/endpoints/email/post_blocklist/)を`/email/blacklist`エンドポイントと同じ機能でリリースしました。代わりに`/email/blocklist`エンドポイントを使用することをお勧めします。
{% endalert %}

> このエンドポイントを使用して、ユーザーのメール配信を停止し、ハードバウンスとしてマークします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`email.blacklist`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| -----------|----------| --------|------- |
| `email` | 必須 | 文字列または配列 | ブラックリストに登録するメールアドレス、または最大50件のメールアドレスの配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}
