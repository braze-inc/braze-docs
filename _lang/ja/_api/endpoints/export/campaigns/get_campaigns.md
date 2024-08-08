---
nav_title: "得る：キャンペーンリストのエクスポート"
article_title: "得る：キャンペーンリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、キャンペーン リストのエクスポート Braze エンドポイントの詳細について説明します。"

---
{% api %}
# キャンペーンリストをエクスポート
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> このエンドポイントを使用してキャンペーンのリストをエクスポートします。各リストには、キャンペーンの名前、キャンペーン API 識別子、API キャンペーンであるかどうか、キャンペーンに関連付けられたタグが含まれます。 

キャンペーンは、作成日時順に並べられた 100 個のグループで返されます (デフォルトでは古いものから新しいものへ)。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `campaigns.list` 許可。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ | 必須 | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `page`| オプション | 整数 | 返されるキャンペーンのページ。デフォルトは 0 (最大 100 の最初のセットを返します)。 |
| `include_archived`| オプション | ブール値 | アーカイブされたキャンペーンを含めるかどうか。デフォルトは false です。 |
| `sort_direction`| オプション | 文字列 | - 作成日時を新しいものから古いものの順に並べ替える: 値を渡す `desc`。<br> \- 作成時間を古いものから新しいものの順に並べ替える: 値を渡す `asc`。<br><br>もし `sort_direction` 含まれていない場合、デフォルトの順序は古いものから新しいものになります。 |
| `last_edit.time[gt]`| オプション | 時間 | 結果をフィルタリングし、現在までに指定された時間より後に編集されたキャンペーンのみを返します。フォーマットは `yyyy-MM-DDTHH:mm:ss`。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
 
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
CSV および API エクスポートに関するヘルプについては、[「エクスポートのトラブルシューティング」]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
