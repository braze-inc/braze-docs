---
nav_title: "取得:キャンバスリストのエクスポート"
article_title: "取得:キャンバスリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export Canvas list Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# キャンバスリストのエクスポート
{% apimethod get %}
/canvas/list
{% endapimethod %}

> このエンドポイントを使用して、名前、Canvas API識別子、および関連するタグを含むCanvasのリストをエクスポートします。 

キャンバスは作成日時(デフォルトでは古いものから新しいもの)でソートされた100のグループで返されます。

`include_archived`フィールドが指定されていない場合、アーカイブされたキャンバスはAPIレスポンスに含まれません。ただし、停止されていてもアーカイブされていないキャンバスはデフォルトで返されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.list`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

|パラメータ|必須|データ型|説明|
| --------- | -------- | --------- | ----------- |
|`page`|オプション|整数|返すキャンバスのページ。デフォルトは`0`(100個までの最初のセットを返す)|
|`include_archived`|オプション|ブール値|アーカイブされたキャンバスを含めるかどうか。デフォルトは`false`。|
| `sort_direction` | オプション | 文字列 | - 作成時刻を新しいものから古い順にソート: value `desc`を渡す。<br> -作成時刻を古いものから新しいものに並べ替える：値`asc`を渡す。<br><br>`sort_direction`が含まれていない場合、デフォルトの順序は古い順になります。|
| `last_edit.time[gt]` | オプション | 時刻 | 結果をフィルタし、今までに指定した時刻より大きく編集されたキャンバスのみを返します。Format is `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエストの例

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
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブル]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)シューティング」を参照してください。
{% endalert %}

{% endapi %}
