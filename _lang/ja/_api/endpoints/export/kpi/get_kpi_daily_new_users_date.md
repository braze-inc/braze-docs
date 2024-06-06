---
nav_title: "取得：日付別の毎日の新規ユーザーのエクスポート"
article_title: "取得：日付別のデイリーニュースユーザーのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export daily new users Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# 日次新規ユーザーを日付別にエクスポート
{% apimethod get %}
/kpi/new_users/data_series
{% endapimethod %}

> このエンドポイントを使用して、各日付の新規ユーザーの合計数の日次系列を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01 {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `kpi.new_users.data_series` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメーター

|パラメータ|必須項目 |データ型 |説明 |
| -------- | -------- | --------- | ----------- |
| `length` |必須項目 |整数型 |返される系列に含めるまでの `ending_at` 最大日数。1 以上 100 以下である必要があります。|
| `ending_at` |オプション |日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) |データ系列が終了する日付。既定値は、要求の時刻です。|
| `app_id` |オプション |文字列 | [[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ] ページから取得したアプリの API 識別子。除外すると、ワークスペース内のすべてのアプリの結果が返されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/new_users/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "new_users" : (int) the number of daily new users
        },
        ...
    ]
}
```

{% alert tip %}
CSV と API のエクスポートに関するヘルプについては、 [エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
