---
nav_title: "ポスト:コンテンツブロックを更新"
article_title: "ポスト:コンテンツブロックを更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Update Content Blocks Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# コンテンツブロックを更新
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> [コンテンツ・ブロックを]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)更新するには、このエンドポイントを使用します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## 前提条件
このエンドポイントを使用するには、`content_blocks.update` パーミッションを持つ[API キーが]({{site.baseurl}}/api/api_key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

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

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
| `content_block_id`|	必須	文字列｜コンテンツ・ブロックのAPI識別子。
|`name` ｜任意｜文字列｜コンテンツブロックの名前。100文字以下でなければならない。|
|`description` ｜任意｜文字列｜コンテンツブロックの説明。250文字以内であること。|
|`content` ｜任意｜文字列｜コンテンツブロック内のHTMLまたはテキストコンテンツ。
|`state` ｜任意｜文字列｜`active` または`draft` 。指定がない場合のデフォルトは`active` である。|
|`tags` ｜任意｜文字列の配列｜[タグは]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)すでに存在していなければならない。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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

次の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
| `Content cannot be blank` |
|`Content must be a string` | コンテンツが引用符(`""`)で囲まれていることを確認してください。|
|`Content must be smaller than 50kb` | コンテンツブロック内のコンテンツは、合計50kb以下でなければなりません。|
|`Content contains malformed liquid` | 指定されたリキッドは有効でないか、解析できません。有効なリキッドで再試行するか、サポートまでご連絡ください。|
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
|`Content Block description must be a string` | コンテンツブロックの説明が引用符 (`""`) で囲まれていることを確認してください。|
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
|`Content Block name can only contain alphanumeric characters` ｜コンテンツブロック名には、次のいずれかの文字を含めることができます：文字（大文字または小文字）`A` ～`Z` 、数字`0` ～`9` 、ダッシュ`-` 、アンダースコア`_` 。絵文字、`!` 、`@` 、`~` 、`&` 、その他の「特殊」文字など、英数字以外の文字を含めることはできません。|
|`Content Block with this name already exists` | 別の名前を試してみてください。|
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
`Tags must be an array` | タグは文字列の配列としてフォーマットされなければならない。例えば、`["marketing", "promotional", "transactional"]` 。|
｜`All tags must be strings` ｜タグが引用符で囲まれていることを確認してください（`""` ）。|
|`Some tags could not be found` ｜コンテンツブロックの作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要があります。|
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
