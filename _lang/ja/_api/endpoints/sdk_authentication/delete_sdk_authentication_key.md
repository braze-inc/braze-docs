---
nav_title: "DELETE:SDK 認証キーを削除"
article_title: "DELETE:SDK 認証キーを削除"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、「SDK 認証キーを削除」Braze エンドポイントの詳細について説明します。"
---

{% api %}
# SDK 認証キーを削除
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> このエンドポイントを使用して、アプリの SDK 認証キーを削除します。

{% alert important %}
プライマリキーは削除できません。プライマリキーを削除しようとすると、このエンドポイントはエラーを返します。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`sdk_authentication.delete`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 必須 | string | アプリの API 識別子。 |
| `key_id` | 必須 | string | 削除する SDK 認証キーの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
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
    }
  ]
}
```

## 応答パラメーター

| パラメータ | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `keys` | 配列 | 残りの SDK 認証キーオブジェクトの配列。 |
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
- プライマリ SDK 認証キーは削除できない。

{% endapi %}
