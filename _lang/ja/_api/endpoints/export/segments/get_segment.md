---
nav_title: "得る：セグメントリストのエクスポート"
article_title: "得る：セグメントリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Braze エンドポイントのセグメント リストのエクスポートについて詳しく説明します。"

---
{% api %}
# セグメントリストをエクスポート
{% apimethod get %}
/segments/list
{% endapimethod %}

> このエンドポイントを使用してセグメントのリストをエクスポートします。各セグメントには、名前、セグメント API 識別子、分析トラッキングが有効になっているかどうかが含まれます。 

セグメントは、作成時刻順に並べられた 100 個のグループで返されます (デフォルトでは古いものから新しいものへ)。アーカイブされたセグメントは含まれません。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `segments.list` 許可。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ| 必須 | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `page`| オプション | 整数 | 返されるセグメントのページ。デフォルトは 0 (最大 100 の最初のセットを返します)。 |
| `sort_direction`| オプション | 文字列 | - 作成日時を新しいものから古いものの順に並べ替える: 値を渡す `desc`。<br> \- 作成時間を古いものから新しいものの順に並べ替える: 値を渡す `asc`。<br><br>もし `sort_direction` 含まれていない場合、デフォルトの順序は古いものから新しいものになります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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
CSV および API エクスポートに関するヘルプについては、[「エクスポートのトラブルシューティング」]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
