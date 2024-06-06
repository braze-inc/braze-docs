---
nav_title: "取得:利用可能なメールテンプレートの一覧表示"
article_title: "取得:利用可能なメールテンプレートの一覧表示"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、List available email templates Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 利用可能なメールテンプレートの一覧表示
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> このエンドポイントを使用して、Braze アカウントで使用可能なメールテンプレートのリストを取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## 前提条件
このエンドポイントを使用するには、`templates.email.list` 権限を持つ[API キー]({{site.baseurl}}/api/api_key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `modified_after` | オプション| [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式の文字列| 指定した時刻以降に更新されたテンプレートのみを取得します。|
| `modified_before` | オプション| [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式の文字列| 指定した時刻またはそれ以前に更新されたテンプレートのみを取得します。|
| `limit` | オプション| 正の数| 取得するテンプレートの最大数。指定されていない場合は、デフォルトで100、許容可能な最大値は1000 です。|
| `offset` | オプション| 正の数| 検索条件に一致する残りのテンプレートを返す前にスキップするテンプレートの数|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス 

{% alert important %}
メールのドラッグアンドドロップエディタを使用して作成されたテンプレートは、このレスポンスでは提供されません。
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}



