---
nav_title: "取得：ニュースフィードカード分析のエクスポート"
article_title: "取得：ニュースフィードカード分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ニュースフィードカード分析のエクスポートBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# ニュースフィードカード分析のエクスポート
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> このエンドポイントを使用して、時間の経過に伴うカードの日次エンゲージメント統計を取得します。

{% alert note %}
ニュースフィードは非推奨になります。Brazeでは、ニュースフィードツールをご利用のお客様には、柔軟性、カスタマイズ性、信頼性に優れたコンテンツカードメッセージングチャネルへの移行を推奨しています。詳しくは、 [移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) をご覧ください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `feed.data_series` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| ----------- | -------- | --------- | ----------- |
| `card_id` |必須項目 |文字列 | [「カード API 識別子]({{site.baseurl}}/api/identifier_types/)」を参照してください。<br><br> 特定のカードの API `card_id` [キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページとダッシュボード内のカードの詳細ページ、または [ニュースフィード カード リストのエクスポート エンドポイント]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)を使用できます。|
| `length` |必須項目 |整数型 |返される系列に含める前の `ending_at` 最大単位数 (日数または時間数)。1 以上 100 以下である必要があります。|
| `unit` |オプション |文字列 |データポイント間の時間の単位。`day`または は で`hour`、既定値は `day`です。 |
| `ending_at` |オプション |日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) |データ系列が終了する日付。既定値は、要求の時刻です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
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
CSV と API のエクスポートに関するヘルプについては、 [エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
