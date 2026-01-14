---
nav_title: "取得:コンテンツブロックの情報を見る"
article_title: "取得:コンテンツブロックの情報を見る"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、コンテンツブロック情報を見るBrazeエンドポイントの詳細について概説する。"
---

{% api %}
# コンテンツ・ブロックの情報を見る
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> このエンドポイントを使用して、既存の[コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)の情報を呼び出します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## 前提条件
このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`content_blocks.info`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `content_block_id`  | 必須 | 文字列 | コンテンツブロックの識別子。<br><br>これは、API コールでコンテンツブロックの情報をリストアップするか、[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)のページに行き、一番下までスクロールしてコンテンツブロックの API 識別子を検索することで見つけることができます。|
| `include_inclusion_data`  | オプション | ブール値 | `true` に設定された場合、API はこのコンテンツブロックが含まれるキャンペーンとキャンバスのメッセージバリエーション API 識別子を返し、以降の呼び出しで使用できるようにします。 結果は、アーカイブまたは削除されたキャンペーンやキャンバスを除外する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Content Block ID cannot be blank` | コンテンツブロックがリクエストにリストされ、引用符 (`""`) で囲まれていることを確認します。 |
| `Content Block ID is invalid for this workspace` | このコンテンツブロックが存在しないか、別の会社アカウントまたはワークスペースにある。 |
| `Content Block has been deleted—content not available` | このコンテンツブロックは、以前は存在していたかもしれませんが、削除されました。 |
| `Include Inclusion Data—error` | このパラメータはブーリアン値（trueまたはfalse）のみを受け付ける。`include_inclusion_data` の値が引用符（`""` ）で囲まれていないことを確認すること。この場合、値は文字列として送信される。詳細については、[リクエストパラメーター](#request-parameters)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
