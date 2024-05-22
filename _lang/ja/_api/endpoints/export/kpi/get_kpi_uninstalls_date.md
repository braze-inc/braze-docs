---
nav_title: "取得:毎日のアプリアンインストールのKPIを日付別にエクスポート"
article_title: "取得:毎日のアプリアンインストールのKPIを日付別にエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、毎日のアプリアンインストール数を日付別にエクスポートする Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 毎日のアプリアンインストールのKPIを日付別にエクスポート
{% apimethod get %}
/kpi/uninstalls/data_series
{% endapimethod %}

> このエンドポイントを使用して、各日付のアンインストール総数の日次系列を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`kpi.uninstalls.data_series`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメータ| 必須 | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `length` | 必須 | 整数 | `ending_at` 返される系列に含めるまでの最大日数。1 ～ 100 (両端を含む) の範囲でなければなりません。|
| `ending_at` | オプション | 日時 <br>([ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)) | データ系列を終了する日付。デフォルトはリクエストの時間です。|
| `app_id` | オプション | 文字列 | API [キーページから取得したアプリ API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 識別子。除外すると、Workspaceのすべてのアプリの結果が返されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/uninstalls/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "uninstalls" : (int) the number of uninstalls
        },
        ...
    ]
}
```

{% alert tip %}
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

{% endapi %}
