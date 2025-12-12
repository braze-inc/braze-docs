---
nav_title: "POST:SDK認証キーを作成する。"
article_title: "POST:SDK 認証キーを作成"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "この記事では、「SDK 認証キーを作成」Braze エンドポイントの詳細について説明します。"
---

{% api %}
# SDK 認証キーを作成
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> このエンドポイントを使用して、アプリ用の新しい SDK 認証キーを作成します。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`sdk_authentication.create`の権限が必要です。

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
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | string | アプリの API 識別子。 |
| `rsa_public_key_str` | 必須 | string | RSA 公開キーの文字列。有効な RSA 公開キーでなければならず、そうでない場合はエラーを返します。 |
| `description` | 必須 | string | SDK 認証キーの説明。 |
| `make_primary` | オプション | ブール値 | `true` に設定すると、作成時にこのキーをプライマリ SDK 認証キーとします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```json
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----", 
  "description": "SDK Authentication Key for iOS App", 
  "make_primary": false
}'
```

## 応答
```json
{
  "id": "key id"
}
```

## 応答パラメーター

| パラメータ | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `id` | string | 新しく作成された SDK 認証キーの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 検証ルール

このエンドポイントには以下の検証ルールがあります。

- 1 つのアプリにつき SDK 認証キーを 3 つまで持つことができる。
- RSA 公開キー文字列は、適切な形式の有効な RSA 公開キーでなければならない。
- `app_id` は有効なアプリ API 識別子でなければならない。
- 説明文を空にすることはできない。

{% endapi %}
