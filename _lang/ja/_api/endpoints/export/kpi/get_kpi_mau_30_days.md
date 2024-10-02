---
nav_title: "取得:過去30 日間の月次アクティブユーザーのエクスポート"
article_title: "取得:過去30 日間の月次アクティブユーザーのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「アクティブユーザーの月次エクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 過去30日間のアクティブユーザーの月次エクスポート
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> このエンドポイントを使用して、30日間にわたるローリング期間における一意のアクティブユーザーの総数を日次で取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`kpi.mau.data_series` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメータ| required | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `length` | required | 整数 | 返される系列に含める`ending_at` の前の最大日数。1以上100以下でなければなりません。 |
| `ending_at` | オプション | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データ系列が終了する日付。デフォルトはリクエストの時刻です。 |
| `app_id` | オプション | string | [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページから取得したアプリケーションAPI 識別子。除外すると、ワークスペース内のすべてのアプリs の結果が返されます。 |
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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
