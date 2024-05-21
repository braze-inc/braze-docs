---
nav_title: "取得:コンテンツブロック情報を参照"
article_title: "取得:コンテンツブロック情報を参照"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、See Content Blocks 情報Braze エンドポイントの詳細について説明します。"
---

{% api %}
# コンテンツブロック情報を参照
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> このエンドポイントを使用して、既存の[Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) の情報を呼び出します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## 前提条件
このエンドポイントを使用するには、`content_blocks.info` 権限を持つ[API キー]({{site.baseurl}}/api/api_key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `content_block_id`  | Required | String | The Content Block identifier.<br><br>これは、API コールでコンテンツブロック情報を一覧表示するか、[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページに移動し、一番下までスクロールしてコンテンツブロックAPI 識別子を検索することで確認できます。|
| `include_inclusion_data` | Optional | Boolean | `true` に設定すると、API は、このコンテンツブロックが含まれているキャンペーンおよびキャンバスのメッセージバリエーションAPI 識別子を返し、後続のコールで使用します。 アーカイブまたは削除されたキャンペーンまたはキャンバスは除外されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## トラブルシューティング

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します。

| エラー| トラブルシューティング|
| --- | --- |
| `Content Block ID cannot be blank` | コンテンツブロックがリクエストにリストされ、引用符で囲まれていることを確認します(`""`)。|
| `Content Block ID is invalid for this workspace` | このコンテンツブロックは存在しないか、別の会社アカウントまたはワークスペースにあります。|
| `Content Block has been deleted—content not available` | このコンテンツブロックは以前に存在していたかもしれませんが、削除されました。|
| `Include Inclusion Data—error` | このパラメータはブール値(true またはfalse) のみを受け入れます。`include_inclusion_data` の値が引用符で囲まれていないことを確認します(`""`)。この値は文字列として送信されます。詳細については、[リクエストパラメータ](#request-parameters)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
