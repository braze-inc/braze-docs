---
nav_title: "GET：過去30日間の月間アクティブユーザー数をエクスポート"
article_title: "GET：過去30日間の月間アクティブユーザー数をエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Brazeの月間アクティブユーザー数輸出エンドポイントの詳細について説明します。"

---
{% api %}
# 過去30日間の月間アクティブユーザーをエクスポート
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> このエンドポイントを使用して、30日間にわたるユニーク・アクティブ・ユーザーの総数の日次シリーズを取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`kpi.mau.data_series` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ|必須|データ型|説明
| -------- | -------- | --------- | ----------- |
|`length` ｜必須｜整数｜返されるシリーズに含める`ending_at` までの最大日数。1～100の間でなければならない。|
|`ending_at` ｜任意｜日時 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)文字列）｜データシリーズが終了する日付。デフォルトはリクエスト時刻。|
|`app_id` ｜任意｜文字列｜[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得したアプリAPI識別子。除外すると、ワークスペース内のすべてのアプリの結果が返されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
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
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIエクスポートに関するヘルプは、[エクスポートのトラブルシューティングを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)ご覧ください。
{% endalert %}

{% endapi %}
