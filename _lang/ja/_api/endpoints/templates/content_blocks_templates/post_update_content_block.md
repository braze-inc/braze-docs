---
nav_title: "POST:コンテンツ・ブロックを更新する"
article_title: "POST:コンテンツ・ブロックを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「コンテンツブロックを更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# コンテンツ・ブロックを更新する
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> このエンドポイントを使用して、[コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)を更新します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## 前提条件
このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`content_blocks.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `content_block_id`|	必須 |	文字列 | コンテンツブロックの API 識別子。|
| `name` | オプション | 文字列 | コンテンツブロックの名前。100 文字未満でなければなりません。 |
| `description` | オプション | 文字列 | コンテンツブロックの説明。250 文字未満でなければなりません。 |
| `content` | オプション | 文字列 | コンテンツブロック内のHTMLまたはテキストコンテンツ。
| `state` | オプション | 文字列 | `active` または`draft` を選択する。指定がない場合のデフォルトは`active` である。 |
| `tags` | オプション | 文字列の配列 | [タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)はすでに存している必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## トラブルシューティング

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Content cannot be blank` |
| `Content must be a string` | コンテンツが引用符 (`""`) で囲まれていることを確認する。 |
| `Content must be smaller than 50kb` | コンテンツブロック内のコンテンツは、合計 50kb 未満でなければなりません。 |
| `Content contains malformed liquid` | 指定されたリキッドは有効でも解析可能でもない。有効な Liquid を使用してもう一度やり直すか、サポートにお問い合わせください。 |
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
| `Content Block description must be a string` | コンテンツ・ブロックの説明が引用符 (`""`) で囲まれていることを確認する。 |
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
| `Content Block name can only contain alphanumeric characters` | コンテンツブロック名には、文字 (大文字または小文字) `A` ～ `Z`、数字 `0` ～ `9`、ダッシュ `-`、アンダースコア `_` のいずれかを含められます。絵文字、`!` 、`@` 、`~` 、`&` 、その他の「特殊」文字など、英数字以外の文字を含むことはできない。 |
| `Content Block with this name already exists` | 別の名前を試してみよう。 |
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
| `Tags must be an array` | タグは文字列の配列としてフォーマットされなければならない。例えば、`["marketing", "promotional", "transactional"]` 。 |
| `All tags must be strings` | タグが引用符 (`""`) で囲まれていることを確認すること。 |
| `Some tags could not be found` | コンテンツブロックの作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
