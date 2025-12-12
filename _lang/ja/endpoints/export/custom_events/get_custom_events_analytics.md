---
nav_title: "取得:カスタムイベント分析をエクスポートする"
article_title: "取得:カスタムイベント分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「カスタムイベント分析のエクスポート」Braze エンドポイントの詳細について概説します。"

---
{% api %}
# カスタムイベント分析をエクスポートする
{% apimethod get %}
/events/data_series
{% endapimethod %}

> このエンドポイントを使用して、指定された期間にわたり、アプリ内でカスタムイベントが発生した回数を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`events.data_series`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター| required | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `event` | 必須 | 文字列 | アナリティクスを返すカスタムイベントの名前。 |
| `length` | 必須 | 整数 | 返されるシリーズに `ending_at` が含まれるまでの最大単位数 (日または時間)。1以上100以下でなければなりません。 |
| `unit` | オプション | 文字列 | データポイント間の時間の単位。`day` または `hour` にすることができ、デフォルトは `day` です。  |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。リクエストの時刻にデフォルト設定されます。 |
| `app_id` | オプション | 文字列 | 特定のアプリに分析を限定するために、[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得したアプリAPI識別子。 |
| `segment_id` | オプション | 文字列 | [セグメントAPI 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。イベント分析が返されるべき、分析可能なセグメントを示すセグメント ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### 致命的なエラーの応答コード {#fatal-export}

リクエストが致命的なエラーに遭遇した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラー& レスポンスを]({{site.baseurl}}/api/errors/#fatal-errors)参照のこと。

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
