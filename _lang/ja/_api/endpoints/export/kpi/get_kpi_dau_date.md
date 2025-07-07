---
nav_title: "取得:デイリーアクティブユーザーを日付別にエクスポートする"
article_title: "取得:デイリーアクティブユーザーを日付別にエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Brazeのエンドポイント「Export daily active users」の詳細について概説する。"

---
{% api %}
# デイリーアクティブユーザーを日付別にエクスポートする
{% apimethod get %}
/kpi/dau/data_series
{% endapimethod %}

> このエンドポイントを使用して、各日付の固有アクティブユーザーの総数の日次情報を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`kpi.dau.data_series`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター| required | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `length` | 必須 | 整数 | 返されるシリーズに `ending_at` が含まれるまでの最大日数。1以上100以下でなければなりません。 |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。リクエストの時刻にデフォルト設定されます。 |
| `app_id` | オプション | 文字列 | [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得したアプリAPI識別子。除外した場合、ワークスペース内のすべてのアプリの結果が返される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/dau/data_series?length=10&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "dau" : (int) the number of daily active users
        },
        ...
    ]
}
```

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
