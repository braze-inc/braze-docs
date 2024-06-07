---
nav_title: "得る：日付別に毎日のアクティブユーザーをエクスポート"
article_title: "得る：日付別に毎日のアクティブユーザーをエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Braze エンドポイントの毎日のアクティブ ユーザーのエクスポートについて詳しく説明します。"

---
{% api %}
# 日付別に毎日のアクティブユーザーをエクスポートする
{% apimethod get %}
/kpi/dau/data_series
{% endapimethod %}

> このエンドポイントを使用して、各日付のユニーク アクティブ ユーザーの合計数の日次系列を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986 {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `kpi.dau.data_series` 許可。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ| 必須 | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `length`| 必須 | 整数 | 最大日数 `ending_at` 返されるシリーズに含めるもの。1 から 100 までの範囲で指定する必要があります。 |
| `ending_at`| オプション | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データ シリーズを終了する日付。デフォルトはリクエストの時刻です。 |
| `app_id`| オプション | 文字列 |[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページから取得されたアプリ API 識別子。除外すると、ワークスペース内のすべてのアプリの結果が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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
CSV および API エクスポートに関するヘルプについては、[「エクスポートのトラブルシューティング」]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
