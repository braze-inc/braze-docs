---
nav_title: "削除:ダッシュボードのユーザーアカウントを削除する"
article_title: "削除:ダッシュボードのユーザーアカウントを削除する"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ダッシュボードのユーザーアカウントを削除するBrazeエンドポイントの詳細について概説する。"
---

{% api %}
# ダッシュボードのユーザーアカウントを削除する
{% apimethod delete %}
/scim/v2/Users/{id}
{% endapimethod %}

> このエンドポイントを使用して、SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) メソッドによって返されるリソース `id` を指定することによって、既存のダッシュボードユーザーを永続的に削除します。 

これは、Brazeダッシュボードの**Company Users**セクションでユーザーを削除するのと同様である。SCIM トークンの取得方法については、[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## 前提条件

このエンドポイントを使うには、SCIMトークンが必要だ。詳細については、「[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)」を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='ダッシュボードユーザーを削除する' %}

## パスパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `id` | 必須 | string | ユーザーのリソースID。このパラメータは、`POST` `/scim/v2/Users/` または`GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` メソッドによって返される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request body

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## リクエスト例
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## 応答

### エラー応答例

```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```

このIDを持つ開発者がBrazeに存在しない場合、エンドポイントは次のように応答する：
```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```
{% endapi %}
