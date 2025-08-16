---
nav_title: "PUT:プライマリ SDK 認証キーを設定"
article_title: "PUT:プライマリ SDK 認証キーを設定"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、「プライマリ SDK 認証キーを設定」Braze エンドポイントの詳細について説明します。"
---

{% api %}
# プライマリ SDK 認証キーを設定
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> このエンドポイントを使用して、SDK 認証キーをアプリのプライマリキーとして設定します。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`sdk_authentication.primary`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "key_id": "key id"
}
```

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | string | アプリの API 識別子。 |
| `key_id` | 必須 | string | プライマリとしてマークする SDK 認証キーの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
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
| `keys` | 配列 | すべての SDK 認証キーオブジェクトの配列。 |
| `keys[].id` | string | SDK 認証キーの ID。 |
| `keys[].rsa_public_key` | string | RSA 公開キーの文字列。 |
| `keys[].description` | string | SDK 認証キーの説明。 |
| `keys[].is_primary` | ブール値 | このキーがプライマリ SDK 認証キーであるかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 検証ルール

このエンドポイントには以下の検証ルールがあります。

- `key_id` は有効な SDK 認証キー ID でなければならない。
- `app_id` は有効なアプリ API 識別子でなければならない。
- SDK 認証キーは、指定されたアプリに存在しなければならない。

{% endapi %}
