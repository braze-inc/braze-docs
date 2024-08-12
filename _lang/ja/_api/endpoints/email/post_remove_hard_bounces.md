---
nav_title: "ポスト:バウンスメールの削除"
article_title: "ポスト:バウンスメールの削除"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、Remove hard bounced email addresses Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ハードバウンスメールの削除
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> このエンドポイントを使用して、Brazeのバウンスリストとメールプロバイダーが管理するバウンスリストからメールアドレスを削除します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`email.bounce.remove` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

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

| パラメータ｜必須｜データ型｜説明
| ----------|-----------| ---------|------ |
|`email` ｜必須｜文字列または配列｜修正するEメールアドレスの文字列、または最大50個までの配列。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
