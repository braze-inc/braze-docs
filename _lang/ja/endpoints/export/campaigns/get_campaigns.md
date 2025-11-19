---
nav_title: "取得:キャンペーンリストをエクスポートする"
article_title: "取得:キャンペーンリストをエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「キャンペーンリストのエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# キャンペーンリストをエクスポートする
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> このエンドポイントを使用して、それぞれに名前、キャンペーン API 識別子、それが API キャンペーンであるかどうか、キャンペーンに関連付けられたタグが含まれたキャンペーンのリストをエクスポートします。

キャンペーンは、作成された時間（デフォルトでは古いものから新しいもの）順にソートされた100のグループで返される。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返すキャンペーンのページ、デフォルトは0（最大100の最初のセットを返す）。 |
| `include_archived` | オプション | ブール値 | アーカイブされたキャンペーンを含めるかどうか。デフォルトはfalse。 |
| `sort_direction` | オプション | 文字列 | \- 作成時刻を新しいものから古いものへと並べ替える: 値 `desc` を渡します。<br> \- 作成時刻を古いものから新しいものへと並べ替える: 値 `asc` を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は古いものから新しいものとなる。 |
| `last_edit.time[gt]` | オプション | 時刻 | 結果をフィルタリングし、現在までに指定された時間以上編集されたキャンペーンのみを返す。形式は `yyyy-MM-DDTHH:mm:ss` です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
