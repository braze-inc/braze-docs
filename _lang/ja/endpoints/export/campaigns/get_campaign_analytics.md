---
nav_title: "取得:キャンペーン分析をエクスポートする"
article_title: "取得:キャンペーン分析をエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、キャンペーン分析のエクスポートBrazeエンドポイントの詳細について概説する。"

---
{% api %}
# キャンペーン分析をエクスポートする
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

> このエンドポイントを使用して、一定期間にわたるキャンペーンのさまざまな統計の日次情報を取得します。 

返されるデータには、メッセージング・チャネル別に、送信、開封、クリック、変換されたメッセージの数が含まれる。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.data_series`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='export campaign analytics' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | 必須 | string | [キャンペーン API 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br> API キャンペーンの `campaign_id` は、[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページ、またはダッシュボードの**キャンペーンの詳細**ページで確認できます。または、[「キャンペーンをリスト」エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)を使用することもできます。 |
| `length` | 必須 | 整数 | 返されるシリーズに `ending_at` が含まれるまでの最大日数。1以上100以下でなければなりません。 |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。リクエストの時刻にデフォルト設定されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト 

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 回答

### マルチチャンネル対応

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time": (string) the date as ISO 8601 date,
            "conversions_by_send_time": (optional, int),
            "conversions1_by_send_time": (optional, int),
            "conversions2_by_send_time": (optional, int),
            "conversions3_by_send_time": (optional, int),
            "conversions": (optional, int),
            "conversions1": (optional, int),
            "conversions2": (optional, int),
            "conversions3": (optional, int),
            "unique_recipients": (int),
            "revenue": (optional, float)
            "messages" : {
                "ios_push" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "android_push" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "webhook": [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "errors": (int) the number of errors
                    }
                ],
                "email" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "opens": (int) the number of opens,
                      "unique_opens": (int) the number of unique opens,
                      "clicks": (int) the number of clicks,
                      "unique_clicks": (int) the number of unique clicks,
                      "unsubscribes": (int) the number of unsubscribes,
                      "bounces": (int) the number of bounces,
                      "delivered": (int) the number of messages delivered,
                      "reported_spam": (int) the number of messages reported as spam
                    }
                ],
                "sms" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "sent_to_carrier" : (int) the number of messages sent to the carrier,
                      "delivered": (int) the number of delivered messages,
                      "rejected": (int) the number of rejected messages,
                      "delivery_failed": (int) the number of failed deliveries,
                      "clicks": (int) the number of clicks on shortened links,
                      "opt_out" : (int) the number of opt outs,
                      "help" : (int) the number of help messages received
                  }
                ],
                "whats_app": [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends, 
                      "delivered": (int) the number of delivered messages,
                      "failed": (int) the number of failed deliveries,
                      "read": (int) the number of opened messages
                    },
                ],
                "content_cards" : [
                  { 
                    "variation_api_id": (string) the variation API identifier, 
                    "sent": (int) the number of sends, 
                    "total_clicks": (int) the number of total clicks, 
                    "total_dismissals": (int) the number of total dismissals, 
                    "total_impressions": (int) the number of total impressions, 
                    "unique_clicks": (int) the number of unique clicks, 
                    "unique_dismissals": (int) the number of unique dismissals, 
                    "unique_impressions": (int) the number of unique impressions
                  }
                ],
                ...
            }
        }
    ],
}
```

### 多変量応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "conversions" : (int) the number of conversions,
            "revenue": (float) the number of dollars of revenue (USD),
            "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
            "messages" : {
               "trigger_in_app_message": [{
                    "variation_name": (optional, string) the variation name,
                    "impressions": (int) the number of impressions,
                    "clicks": (int) the number of clicks,
                    "first_button_clicks": (int) the number of first button clicks,
                    "second_button_clicks": (int) the number of second button clicks,
                    "revenue": (float) the number of dollars of revenue (USD),
                    "unique_recipients": (int) the number of unique recipients,
                    "conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      			}, {
      				"variation_name": (optional, string) the variation name,
      				"impressions": (int) the number of impressions,
      				"clicks": (int) the number of clicks,
      				"first_button_clicks": (int) the number of first button clicks,
      				"second_button_clicks": (int) the number of second button clicks,
                    "revenue": (float) the number of dollars of revenue (USD),
                    "unique_recipients": (int) the number of unique recipients,
                    "conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      			}, {
      				"variation_name": (optional, string) the variation name,
      				"revenue": (float) the number of dollars of revenue (USD),
      				"unique_recipients": (int) the number of unique recipients,
      				"conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      				"enrolled": (optional, int) the number of enrolled users
      			}]
      		},
      		"conversions_by_send_time": (optional, int),
      		"conversions1_by_send_time": (optional, int),
      		"conversions2_by_send_time": (optional, int),
      		"conversions3_by_send_time": (optional, int),
      		"conversions": (optional, int),
      		"conversions1": (optional, int),
      		"conversions2": (optional, int),
      		"conversions3": (optional, int),
      		"unique_recipients": (int),
      		"revenue": (optional, float)
         }],
         ...
}
```

可能なメッセージタイプは、`email`、`in_app_message`、`webhook`、`android_push`、`ios_push`、`kindle_push`、`web_push` です。すべてのプッシュメッセージタイプは、`android_push` に同じ統計が表示されます。

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
