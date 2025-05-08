---
nav_title: "取得:ニュースフィードカード分析のエクスポート"
article_title: "取得:ニュースフィードカード分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ニュースフィードカード分析のエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ニュースフィードカード分析をエクスポートする
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> このエンドポイントを使用して、時間の経過に伴うカードのエンゲージメント統計の日次情報を取得します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`feed.data_series`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター   | required | データ型 | 説明 |
| ----------- | -------- | --------- | ----------- |
| `card_id` | required | 文字列 | [カード API 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br> 指定したカードの `card_id` は、[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページやダッシュボード内のカード詳細ページで確認できるほか、[ニュースフィードカードリストのエクスポート]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)エンドポイントも使用できます。|
| `length` | 必須 | 整数 | 返されるシリーズに `ending_at` が含まれるまでの最大単位数 (日または時間)。1以上100以下でなければなりません。 |
| `unit` | オプション | 文字列 | データポイント間の時間の単位。`day` または `hour` にすることができ、デフォルトは `day` です。  |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。リクエストの時刻にデフォルト設定されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
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
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
