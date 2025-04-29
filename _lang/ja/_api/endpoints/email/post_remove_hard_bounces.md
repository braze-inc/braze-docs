---
nav_title: "POST:ハードバウンスメールを削除"
article_title: "POST:ハードバウンスメールを削除"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、「ハードバウンスメールアドレスを削除」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ハードバウンスメールを削除
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> このエンドポイントを使用して、Brazeのバウンスリストとメールプロバイダーが管理するバウンスリストからメールアドレスを削除する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`email.bounce.remove`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| ----------|-----------| ---------|------ |
| `email` | 必須 | 文字列または配列 | 修正するEメールアドレスを文字列で、または最大50個までの配列で指定する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
