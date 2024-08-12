---
nav_title: "GET：アプリのセッションを時間ごとにエクスポート"
article_title: "ゲットだ：アプリのセッションを時間ごとにエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、時間Brazeエンドポイントによるアプリセッション分析のエクスポートについての詳細を概説します。"

---
{% api %}
# アプリのセッションを時間ごとにエクスポート
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> このエンドポイントを使用して、指定した期間におけるアプリの一連のセッション数を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`sessions.data_series` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ|必須|データ型|説明
| -------- | -------- | --------- | ----------- |
|`length` ｜必須｜整数｜返されるシリーズに含める`ending_at` までの最大単位数（日または時間）。1～100の間でなければならない。|
|`unit` ｜オプション｜文字列｜データポイント間の時間の単位。`day` `hour`デフォルトは`day` 。  |
|`ending_at` ｜任意｜日時 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)文字列）｜データシリーズが終了する日付。デフォルトはリクエスト時刻。|
|`app_id` ｜任意｜文字列｜特定のアプリにアナリティクスを制限するために[APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページから取得したアプリAPI識別子。|
|`segment_id` ｜任意｜文字列｜[セグメントAPI識別子を]({{site.baseurl}}/api/identifier_types/)参照。セッションを返す分析可能セグメントを示すセグメントID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIエクスポートに関するヘルプは、[エクスポートのトラブルシューティングを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)ご覧ください。
{% endalert %}

{% endapi %}
