---
nav_title: "取得:カスタムイベント分析のエクスポート"
article_title: "取得:カスタムイベント分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、カスタムイベントのエクスポート分析Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カスタムイベント分析のエクスポート
{% apimethod get %}
/events/data_series
{% endapimethod %}

> このエンドポイントを使用して、指定した期間にアプリ内で発生したカスタムイベントの数の連続を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`events.data_series` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| -------- | -------- | --------- | ----------- |
| `event` | Required | String | 分析を返すカスタムイベントの名前。|
| `length` | Required | Integer | `ending_at` より前の最大単位数(日数または時間数) が返された系列に含まれます。1 ～100 (両端を含む) である必要があります。|
| `unit` | オプション| 文字列| データポイント間の時間の単位。`day`または`hour`にすることができます。デフォルトは`day`です。|
| `ending_at` | オプション| 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string)| データ系列が終了する日付。デフォルトは要求の時刻です。|
| `app_id` | オプション| 文字列| [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページから取得されたアプリケーションAPI 識別子。分析を特定のアプリに制限します。|
| `segment_id` | オプション| String | [セグメントAPI 識別子]({{site.baseurl}}/api/identifier_types/) を参照してください。イベント分析を返す分析が有効なセグメントを示すセグメントID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %} 

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### 致命的なエラー応答コード {#fatal-export}

リクエストで致命的なエラーが発生した場合に返されるステータスコードと関連するエラーメッセージについては、[Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors) を参照してください。

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}

{% endapi %}
