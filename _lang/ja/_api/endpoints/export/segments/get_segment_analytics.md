---
nav_title: "取得:セグメント分析をエクスポート"
article_title: "取得:セグメント分析をエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、エクスポートセグメント分析 Braze エンドポイントの詳細について説明します。"

---
{% api %}
# セグメント分析をエクスポート
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> このエンドポイントを使用して、セグメントの推定サイズの日次系列を経時的に取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`segments.data_series`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `segment_id` | 必須 | 文字列 | [セグメント API 識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。<br><br> `segment_id`特定のセグメントのは、Braze アカウントの [API キーページにあります]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)。また、[セグメントリストのエクスポートエンドポイントを使用することもできます]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)。|
| `length` | 必須 | 整数 | `ending_at` 返される系列に含めるまでの最大日数。1 ～ 100 (両端を含む) の範囲でなければなりません。|
| `ending_at` | オプション | 日時 <br>([ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)) | データ系列を終了する日付。デフォルトはリクエストの時間です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
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
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

{% endapi %}
