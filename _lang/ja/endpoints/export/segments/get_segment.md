---
nav_title: "取得:セグメントリストをエクスポートする"
article_title: "取得:セグメントリストをエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、セグメントリストBrazeエンドポイントのエクスポートについての詳細を概説する。"

---
{% api %}
# セグメントリストをエクスポートする
{% apimethod get %}
/segments/list
{% endapimethod %}

> このエンドポイントを使用して、名前、セグメント API 識別子、分析の追跡が有効かどうかがそれぞれに含まれているセグメントのリストをエクスポートします。

セグメントは100のグループに分けられ、作成日順にソートされて返される（デフォルトでは古いものから新しいものへ）。アーカイブされたセグメントは含まれません。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`segments.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター| required | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返すセグメントのページ。デフォルトは0（最大100の最初のセットを返す）。 |
| `sort_direction` | オプション | 文字列 | \- 作成時刻を新しいものから古いものへと並べ替える: 値 `desc` を渡します。<br> \- 作成時刻を古いものから新しいものへと並べ替える: 値 `asc` を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は古いものから新しいものとなる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
