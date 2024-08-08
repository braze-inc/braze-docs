---
nav_title: "GET：利用可能なコンテンツ・ブロックのリスト"
article_title: "GET：利用可能なコンテンツ・ブロックのリスト"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、List available Content Blocks Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 利用可能なコンテンツ・ブロックのリスト
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> このエンドポイントを使用して、既存の[コンテンツ・ブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)情報を一覧表示します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## 前提条件
このエンドポイントを使用するには、`content_blocks.list` パーミッションを持つ[API キーが]({{site.baseurl}}/api/api_key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`modified_after` ｜任意｜[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列｜指定された時刻以降に更新されたコンテンツブロックのみを取得する。|
|`modified_before` ｜任意｜[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列｜指定された時刻以前に更新されたコンテンツ・ブロックのみを検索する。|
|`limit` ｜任意｜正の数｜取得するコンテンツ・ブロックの最大数。省略時のデフォルトは100、最大許容値は1000。|
|`offset` ｜任意｜正の数｜検索条件に合うテンプレートの残りを返す前にスキップするコンテンツブロックの数。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## トラブルシューティング

次の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
|`Modified after time is invalid` | 指定された日付は有効または解析可能な日付ではありません。この値を ISO 8601 形式 (`yyyy-mm-ddThh:mm:ss.ffffff`) の文字列に変換する。|
|`Modified before time is invalid` | 指定された日付は有効または解析可能な日付ではありません。この値を ISO 8601 形式 (`yyyy-mm-ddThh:mm:ss.ffffff`) の文字列に変換する。|
|`Modified after time must be earlier than or the same as modified before time.` |`modified_after` の値を`modified_before` よりも早い時間に変更する。|
|`Content Block number limit is invalid` ｜`limit` ｜パラメータは0以上の整数（正の数）でなければならない。
|`Content Block number limit must be greater than 0` ｜`limit` ｜パラメータを0以上の整数に変更する。
|`Content Block number limit exceeds maximum of 1000` |`limit` パラメータを1000未満の整数に変更する。|
|`Offset is invalid` ｜`offset` ｜パラメータは0以上の整数でなければならない。
| オフセットは0より大きくなければならない｜`offset` パラメータを0より大きい整数に変更する。
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
