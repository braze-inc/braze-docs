---
nav_title: "取得:SDK認証キーをリストアップする。"
article_title: "取得:SDK 認証キーを一覧表示"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「SDK 認証キーを一覧表示」Braze エンドポイントの詳細について説明します。"
---

{% api %}
# SDK 認証キーを一覧表示
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> このエンドポイントを使用して、アプリのすべての SDK 認証キーを取得します。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`sdk_authentication.keys`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | string | アプリの API 識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```json
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## 応答パラメーター

| パラメータ | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `keys` | 配列 | SDK 認証キーオブジェクトの配列。 |
| `keys[].id` | string | SDK 認証キーの ID。 |
| `keys[].rsa_public_key` | string | RSA 公開キーの文字列。 |
| `keys[].description` | string | SDK 認証キーの説明。 |
| `keys[].is_primary` | ブール値 | このキーがプライマリ SDK 認証キーであるかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 検証ルール

このエンドポイントには以下の検証ルールがあります。

- `app_id` パラメータは有効なアプリ API 識別子でなければならない。
- アプリはワークスペースに存在していなければならない。

{% endapi %}
