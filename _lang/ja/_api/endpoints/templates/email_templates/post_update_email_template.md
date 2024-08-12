---
nav_title: "ポスト:メールテンプレートの更新"
article_title: "ポスト:メールテンプレートの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、BrazeのエンドポイントであるUpdate email templateの詳細について説明します。"

---
{% api %}
# 既存のEメールテンプレートの更新
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボードのメールテンプレートを更新します。 

メールテンプレートの`email_template_id` 、「**テンプレートとメディア**」ページからアクセスできます。[メールテンプレートの作成エンド]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)ポイントは、`email_template_id` の参照も返します。

`email_template_id` 以外のフィールドはすべて任意ですが、更新するフィールドを少なくとも1つ指定する必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## 前提条件
このエンドポイントを使用するには、`templates.email.update` パーミッションを持つ[API キーが]({{site.baseurl}}/api/api_key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

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

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
| --------- | ---------| --------- | ----------- |
|`email_template_id` ｜必須｜文字列｜[メールテンプレートのAPI識別子]({{site.baseurl}}/api/identifier_types/)。
|`template_name`|オプション|文字列|メールテンプレートの名前。
|`subject`|オプション|文字列|Eメールテンプレートの件名。
|`body`|オプション|文字列|HTMLを含むことができるメールテンプレートの本文。
|`plaintext_body`|オプション|String|メールテンプレート本文のプレーンテキストバージョン。
|`preheader`|オプション|文字列|一部のクライアントでプレビューを生成するために使用されるメールのプレヘッダー。
|`tags`|オプション[|]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)文字列|タグはすでに存在していなければならない。
|`should_inline_css`|Optional|Boolean|テンプレートごとに`inline_css` 機能を有効または無効にする。提供されない場合、BrazeはAppGroupのデフォルト設定を使用します。`true` 、`false` 。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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

次の表は、返される可能性のあるエラーと、該当する場合はそれに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
| テンプレート名は必須です。|
| タグは配列でなければならない｜タグは文字列の配列としてフォーマットされなければならない、例えば`["marketing", "promotional", "transactional"]` 。|
| タグはすべて文字列でなければなりません｜タグが引用符 (`""`) で囲まれていることを確認してください。|
| メールテンプレート作成時にタグを追加するには、そのタグがBrazeに既に存在している必要があります。|
|`should_inline_css` の値が無効です。`true` 、`false` のいずれかが期待されていた｜このパラメータはブーリアン値（trueまたはfalse）のみを受け付ける。`should_inline_css` の値が引用符 (`""`) で囲まれていないことを確認する。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
