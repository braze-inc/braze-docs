---
nav_title: "取得:輸出セグメント分析"
article_title: "取得:セグメント分析のエクスポート"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、エクスポートセグメント分析Brazeエンドポイントについての詳細を概説する。"

---
{% api %}
# 輸出セグメント分析
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> このエンドポイントを使用して、時間の経過に伴うセグメントの推定サイズの日次情報を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`segments.data_series`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `segment_id` | 必須 | 文字列 | [セグメントAPI 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br> 特定のSegmentの`segment_id` は、Braze アカウントの[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページにあります。または、[エクスポートSegment一覧エンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) を使用できます。  |
| `length` | 必須 | 整数 | 返されるシリーズに `ending_at` が含まれるまでの最大日数。1以上100以下でなければなりません。 |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。リクエストの時刻にデフォルト設定されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
