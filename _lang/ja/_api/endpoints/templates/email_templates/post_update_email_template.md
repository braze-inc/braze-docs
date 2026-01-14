---
nav_title: "POST:メールテンプレートの更新"
article_title: "POST:メールテンプレートを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートの更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 既存のEメールテンプレートを更新する
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> このエンドポイントを使用して、BrazeダッシュボードのEメールテンプレートを更新する。

メールテンプレートの`email_template_id` 、**Templates& Media**ページからアクセスできる。[「メールテンプレートを作成」エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)も `email_template_id` 参照を返します。

`email_template_id` 以外のフィールドはすべて任意指定ですが、更新するフィールドを少なくとも1つ指定しなければなりません。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## 前提条件
このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`templates.email.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| 必須 |文字列|[メールテンプレートのAPI識別子]({{site.baseurl}}/api/identifier_types/)|
|`template_name`|オプション|文字列|メールテンプレートの名前|
|`subject`|オプション|文字列|メールテンプレートの件名|
|`body`|オプション|文字列|HTMLを含む可能性のあるメールテンプレート本文。|
|`plaintext_body`|オプション|文字列|メールテンプレート本文のプレーンテキストバージョン。|
|`preheader`|オプション|文字列|一部のクライアントでプレビューを生成するために使用されるメールプレヘッダー。|
|`tags`|オプション|文字列|[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)はすでに存している必要があります。|
|`should_inline_css`|オプション|ブール値|テンプレートごとに`inline_css` 機能を有効または無効にする。提供されない場合、BrazeはAppGroupのデフォルト設定を使用する。`true` か`false` のどちらかが予想される。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、該当する場合、それに関連するトラブルシューティングの手順を示している。

| エラー | トラブルシューティング |
| --- | --- |
| テンプレート名は必須 | テンプレート名を入力する。 |
| タグは配列でなければならない | タグは文字列の配列としてフォーマットされなければならない。例えば、`["marketing", "promotional", "transactional"]` 。 |
| タグはすべて文字列でなければならない | タグが引用符 (`""`) で囲まれていることを確認すること。 |
| いくつかのタグが見つからない | Eメールテンプレート作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要がある。 |
| `should_inline_css` の値が無効である。`true` または`false` のどちらかが予想された | このパラメータはブーリアン値（trueまたはfalse）のみを受け付ける。`should_inline_css` の値が引用符（`""` ）で囲まれていないことを確認すること。この場合、値は文字列として送信される。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
