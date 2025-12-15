---
nav_title: "取得:利用可能なコンテンツブロックをリストアップする"
article_title: "取得:利用可能なコンテンツブロックのリスト"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「利用可能なコンテンツブロックのリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 利用可能なコンテンツブロックのリスト
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> このエンドポイントを使用して、既存の[コンテンツ・ブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)情報をリストアップする。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## 前提条件
このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`content_blocks.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `modified_after`  | オプション | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列 | 指定した時刻以降に更新されたコンテンツブロックのみを取得します。 |
| `modified_before`  |  オプション | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列 | 指定された時刻以前に更新されたコンテンツブロックのみを取得します。 |
| `limit` | オプション | 正の数 | 取得するコンテンツブロックの最大数。指定されない場合、デフォルトの100に設定されます。最大許容値は1000です。 |
| `offset`  |  オプション | 正の数 | 検索条件に合うテンプレートの残りを返す前にスキップするコンテンツブロックの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

```json
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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Modified after time is invalid` | 指定された日付は有効な日付でも解析可能な日付でもない。この値をISO 8601フォーマット（`yyyy-mm-ddThh:mm:ss.ffffff` ）の文字列として再フォーマットする。 |
| `Modified before time is invalid` | 指定された日付は有効な日付でも解析可能な日付でもない。この値をISO 8601フォーマット（`yyyy-mm-ddThh:mm:ss.ffffff` ）の文字列として再フォーマットする。 |
| `Modified after time must be earlier than or the same as modified before time.` | `modified_after` の値を、`modified_before` の時間より早い時間に変更します。 |
| `Content Block number limit is invalid` | `limit` パラメーターは0よりも大きい整数（正の数）でなければなりません。 |
| `Content Block number limit must be greater than 0` | `limit` パラメータを0以上の整数に変更する。 |
| `Content Block number limit exceeds maximum of 1000` | `limit` パラメータを1000未満の整数に変更する。 |
| `Offset is invalid` | `offset` パラメーターは0よりも大きい整数でなければなりません。 |
| オフセットは0より大きくなければなりません | `offset` パラメータを0以上の整数に変更する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
