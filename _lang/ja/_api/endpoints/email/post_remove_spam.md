---
nav_title: "ポスト迷惑メールリストからメールアドレスを削除する"
article_title: "ポスト迷惑メールリストからメールアドレスを削除する"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "この記事では、迷惑メールリストからメールアドレスを削除するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 迷惑メールリストからメールアドレスを削除する
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> このエンドポイントを使用して、BrazeのスパムリストおよびEメールプロバイダーが管理するスパムリストからEメールアドレスを削除します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.spam.remove`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## リクエストパラメータ

|パラメータ|必須|データ型|説明|
| ----------|-----------| --------|------- |
|`email`|必須|文字列または配列|変更する文字列のメールアドレス、または50個までのメールアドレスの配列。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエストの例
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
