---
nav_title: "ポスト:電子メールのブラックリスト"
article_title: "ポスト:電子メールのブラックリスト"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "この記事では、BlacklistメールBrazeエンドポイントの詳細について概説します。"

---
{% api %}
# 電子メールのブラックリスト
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Brazeは、`/email/blacklist` エンドポイントと同じ機能を持つ[`/email/blocklist` エンドポイントを]({{site.baseurl}}/api/endpoints/email/post_blocklist/)リリースしました。代わりに`/email/blocklist` エンドポイントを使用することをお勧めします。
{% endalert %}

> このエンドポイントを使用して、ユーザのメール配信を停止し、ハードバウンスとしてマークします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.blacklist` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
| -----------|----------| --------|------- |
|`email` ｜必須｜文字列または配列｜ブラックリストに入れる電子メールアドレスの文字列、またはブラックリストに入れる最大50個の電子メールアドレスの配列。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}


