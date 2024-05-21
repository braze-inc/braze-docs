---
nav_title: "取得:キャンバスリストの書き出し"
article_title: "取得:キャンバスリストの書き出し"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「キャンバスを書き出し」リストの「Braze」エンドポイントについて説明します。"

---
{% api %}
# キャンバスリストの書き出し
{% apimethod get %}
/canvas/list
{% endapimethod %}

> このエンドポイントを使用して、名前、Canvas API ID、および関連するタグを含むCanvase のリストをエクスポートします。 

キャンバスは、作成時にソートされた100 個のグループで返されます(デフォルトでは最も古いものから最新のもの)。

アーカイブされたキャンバスは、`include_archived` フィールドが指定されていない限り、API 応答に含まれません。ただし、停止しているがアーカイブされていないキャンバスは、デフォルトで返されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.list` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | -------- | --------- | ----------- |
| `page` | オプション| 整数| 返されるキャンバスのページ。デフォルトは`0` (100 までの最初のセットを返します) |
| `include_archived` | オプション| ブール| アーカイブされたキャンバスを含めるかどうかに関係なく、デフォルトは`false` | です。
| `sort_direction` | オプション| String | - 作成時刻を最新から最も古い順に並べ替えます。値`desc` を渡します。<br> \- 作成時刻を最も古いものから最新のものにソートするには、`asc` の値を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は最も古い順から最新の順になります。|
| `last_edit.time[gt]` | Optional | Time | 結果をフィルタリングし、これまでに指定された時間よりも大きい時間に編集されたキャンバスのみを返します。フォーマットは`yyyy-MM-DDTHH:mm:ss`です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}

{% endapi %}
