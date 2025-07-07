---
nav_title: "取得:キャンバスリストをエクスポートする"
article_title: "取得:キャンバスリストをエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「キャンバスリストのエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# キャンバスリストをエクスポートする
{% apimethod get %}
/canvas/list
{% endapimethod %}

> このエンドポイントを使用して、名前、キャンバスAPI識別子、関連タグを含むキャンバスのリストをエクスポートする。

キャンバスは、作成時刻順 (デフォルトでは古い順) で並べられた 100 個のグループで返されます。

`include_archived` フィールドが指定されていない限り、アーカイブされたキャンバスは API 応答に含まれません。ただし、停止しているがアーカイブされていないキャンバスは、デフォルトで返却される。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返すキャンバスのページ、デフォルトは`0` （最大100枚までの最初のセットを返す） |
| `include_archived` | オプション | ブール値 | アーカイブされたキャンバスを含めるかどうか。デフォルトは`false` 。 |
| `sort_direction` | オプション | 文字列 | \- 作成時刻を新しいものから古いものへと並べ替える: 値 `desc` を渡します。<br> \- 作成時刻を古いものから新しいものへと並べ替える: 値 `asc` を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は古いものから新しいものとなる。 |
| `last_edit.time[gt]` | オプション | 時刻 | 結果をフィルターし、現在までに指定された時間より長く編集されたキャンバスのみを返します。形式は `yyyy-MM-DDTHH:mm:ss` です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
