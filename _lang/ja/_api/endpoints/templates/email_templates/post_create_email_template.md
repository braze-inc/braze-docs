---
nav_title: "ポスト:メールテンプレートを作成"
article_title: "ポスト:メールテンプレートの作成"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Create email templates Braze エンドポイントの詳細について説明します。"
---
{% api %}
# メールテンプレートを作成
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> このエンドポイントを使用して、Braze ダッシュボードにメールテンプレートを作成します。 

これらのテンプレートは、**Templates & Media** ページで使用できます。このエンドポイントからの応答には、`email_template_id` のフィールドが含まれます。このフィールドは、後続のAPI 呼び出しでテンプレートを更新するために使用できます。

ユーザーのメールサブスクリプションステータスは、RESTful API を使用してBraze 経由で更新および取得できます。API を使用して、Braze と他のメールシステムまたは独自のデータベース間で双方向同期を設定できます。すべてのAPI 要求はHTTPS 経由で行われます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## 前提条件
このエンドポイントを使用するには、`templates.email.create` 権限を持つ[API キー]({{site.baseurl}}/api/api_key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

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

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
|`template_name`|必須|文字列|メールテンプレートの名前。|
|`subject`|必須|文字列|メールテンプレートの件名行|
|`body`|必須|文字列|HTML を含む可能性のあるメールテンプレート本文|
|`plaintext_body`|オプション|文字列|メールテンプレート本文のプレーンテキストバージョン。|
|`preheader`|オプション|文字列|一部のクライアントでプレビューを生成するために使用される電子メールのプレヘッダー|
|`tags`|オプション|String|[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)がすでに存在している必要があります。|
||`should_inline_css`|オプション|Boolean|テンプレートごとの`inline_css` 機能を有効または無効にします。指定されていない場合、Braze はアプリグループのデフォルト設定を使用します。`true` または`false` のいずれかが予期されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


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

## 考えられるエラー

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します(該当する場合)。

| エラー| トラブルシューティング|
| --- | --- |
| テンプレート名が必要です|テンプレート名を入力します。|
| タグは配列である必要があります| タグは、`["marketing", "promotional", "transactional"]` のように、文字列の配列としてフォーマットする必要があります。|
| すべてのタグは文字列である必要があります| タグが引用符で囲まれていることを確認します(`""`)。|
| 一部のタグが見つかりませんでした| 電子メールテンプレートの作成時にタグを追加するには、そのタグがBraze にすでに存在している必要があります。|
| 電子メールには有効なコンテンツブロック名が必要です| 電子メールには、この環境に存在しないコンテンツブロックが含まれる場合があります。|
| `should_inline_css` の値が無効です。`true`または`false`のいずれかが予期されました|このパラメータはブール値(trueまたはfalse)のみを受け入れます。`should_inline_css` の値が引用符で囲まれていないことを確認します(`""`)。これにより、値が文字列として送信されます。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
