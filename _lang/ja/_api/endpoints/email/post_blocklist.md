---
nav_title: "ポストメールをブロックリストに登録する"
article_title: "ポストメールをブロックリストに登録する"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "この記事では、ブロックリストメールのBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# メールをブロックリストに登録する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのメール登録を解除し、ハードバウンスとしてマークします。
 
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、アクセス許可を持つ `email.blacklist` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

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

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| -----------|----------| --------|------- |
| `email` |必須項目 |文字列または配列 |ブロックリストに登録する文字列メールアドレス、またはブロックリストに登録する最大 50 個のメールアドレスの配列。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
