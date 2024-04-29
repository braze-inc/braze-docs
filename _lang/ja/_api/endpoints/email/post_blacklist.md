---
nav_title: "ポストメールをブラックリストに登録する"
article_title: "ポストメールをブラックリストに登録する"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "この記事では、ブラックリスト メール Braze エンドポイントの詳細について説明します。"

---
{% api %}
# メールをブラックリストに登録する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Brazeは、 [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/) 同じ機能を持つエンドポイント `/email/blacklist` 終点。ご利用をお勧めします `/email/blocklist` 代わりにエンドポイントを使用します。
{% endalert %}

> このエンドポイントを使用して、ユーザーの電子メールの登録を解除し、ハードバウンスとしてマークします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `email.blacklist` 許可。

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

| パラメータ | 必須 | データ型 | 説明 |
| -----------|----------| --------|------- |
| `email`| 必須 | 文字列または配列 | ブラックリストに登録する文字列の電子メール アドレス、またはブラックリストに登録する最大 50 個の電子メール アドレスの配列。 |
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


