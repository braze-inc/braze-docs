---
nav_title: "取得:利用可能なEメールテンプレートの一覧"
article_title: "取得:利用可能なメールテンプレートの一覧表示"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートで使用可能なリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 利用可能なEメールテンプレートの一覧
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> このエンドポイントを使用して、Brazeアカウントで利用可能なEメールテンプレートのリストを取得する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## 前提条件
このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`templates.email.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `modified_after`  | オプション | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列 | 指定された時刻以降に更新されたテンプレートだけを取得する。 |
| `modified_before`  |  オプション | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列 | 指定された時刻以前に更新されたテンプレートのみを取得します。 |
| `limit` | オプション | 正の数 | 取得するテンプレートの最大数。指定されない場合、デフォルトの100に設定されます。最大許容値は1000です。 |
| `offset`  |  オプション | 正の数 | 検索条件に合う残りのテンプレートを返す前にスキップするテンプレートの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 応答 

{% alert important %}
電子メール用のドラッグアンドドロップエディタを使用して作成されたテンプレートは、この回答では提供されない。
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



