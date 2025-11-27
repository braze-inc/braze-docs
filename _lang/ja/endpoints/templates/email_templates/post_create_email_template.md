---
nav_title: "POST:Eメールテンプレートを作成する"
article_title: "POST:メールテンプレートを作成する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、BrazeのEメールテンプレート作成エンドポイントの詳細について概説する。"
---
{% api %}
# Eメールテンプレートを作成する
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> BrazeダッシュボードでEメールテンプレートを作成するには、このエンドポイントを使用する。

これらのテンプレートは、**「テンプレート＆メディア**」ページで利用できるようになる。このエンドポイントからの応答には`email_template_id`のフィールドが含まれており、後続のAPI呼び出しでテンプレートを更新するために使用できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## 前提条件
このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`templates.email.create`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`template_name`|必須|文字列|メールテンプレートの名前|
|`subject`|必須|文字列|メールテンプレートの件名|
|`body`|必須|文字列|HTMLを含む可能性のあるメールテンプレート本文。|
|`plaintext_body`|オプション|文字列|メールテンプレート本文のプレーンテキストバージョン。|
|`preheader`|オプション|文字列|一部のクライアントでプレビューを生成するために使用されるメールプレヘッダー。|
|`tags`|オプション|文字列|[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)はすでに存している必要があります。|
|`should_inline_css`|オプション|ブール値|テンプレートごとに`inline_css` 機能を有効または無効にする。提供されない場合、Brazeはアプリグループのデフォルト設定を使用する。`true` か`false` のどちらかが予想される。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## 回答例

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、該当する場合、それに関連するトラブルシューティングの手順を示している。

| エラー | トラブルシューティング |
| --- | --- |
| テンプレート名は必須 | テンプレート名を入力する。 |
| タグは配列でなければならない | タグは文字列の配列としてフォーマットされなければならない。例えば、`["marketing", "promotional", "transactional"]` 。 |
| タグはすべて文字列でなければならない | タグが引用符 (`""`) で囲まれていることを確認すること。 |
| いくつかのタグが見つからない | Eメールテンプレート作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要がある。 |
| Eメールには有効なコンテンツ・ブロック名が必要である | メールには、この環境には存在しないコンテンツ・ブロックが含まれている可能性がある。 |
| `should_inline_css` の値が無効である。`true` または`false` のどちらかが予想された | このパラメータはブーリアン値（trueまたはfalse）のみを受け付ける。`should_inline_css` の値が引用符（`""` ）で囲まれていないことを確認すること。この場合、値は文字列として送信される。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
