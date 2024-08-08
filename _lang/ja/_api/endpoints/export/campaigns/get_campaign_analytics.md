---
nav_title: "取得:キャンペーン分析をエクスポート"
article_title: "取得:キャンペーン分析をエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、キャンペーン分析をエクスポートする Braze エンドポイントの詳細について説明します。"

---
{% api %}
# キャンペーン分析をエクスポートする
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

> このエンドポイントを使用して、キャンペーンのさまざまな統計情報を時系列で毎日取得できます。 

返されるデータには、メッセージングチャネルによって送信された、開かれた、クリックされた、または変換されたメッセージの数が含まれます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.data_series`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='export campaign analytics' %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | [キャンペーン API 識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。<br><br> `campaign_id`for APIキャンペーンは、[**ダッシュボードのAPIキーページとキャンペーンの詳細ページにあります**]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)。または、[リストキャンペーンエンドポイントを使用することもできます]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)。|
| `length` | 必須 | 整数 | `ending_at` 返される系列に含めるまでの最大日数。1 ～ 100 (両端を含む) の範囲でなければなりません。|
| `ending_at` | オプション | 日時 <br>([ISO-8601文字列](https://en.wikipedia.org/wiki/ISO_8601)) | データ系列を終了する日付。デフォルトはリクエストの時間です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例 

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

### マルチチャネル対応

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "messages" : {
                "ios_push" : [
                    {
                      "variation_name": (string) the name of the message in the dashboard (eg., "iOS_Push"),
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int) the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks,
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
                      "carousel_slide_[NUM]_[TITLE]_click": (optional, int) the number of carousel slide clicks,
                      "notif_button_[NUM]_[TITLE]_click": (optional, int) the number of notification button clicks
                    }
                ],
                "android_push" : [
                    {
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "webhook": [
                    {
                      "sent": (int) the number of sends,
                      "errors": (int) the number of errors
                    }
                ],
                "email" : [
                    {
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
                        "variation_name": (string) the name of the message in the dashboard,
                        "variation_api_id": (string) the variation API identifier,
                        "sent": (int) the number of sends, 
                        "delivered": (int) the number of delivered messages,
                        "failed": (int) the number of failed deliveries,
                        "read": (int) the number of opened messages,
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
                    },
                    {
                        "variation_name": (string) the name of the message in the dashboard,
                        "variation_api_id": (string) the variation API identifier,
                        "enrolled": (optional, int) the number of enrolled users,
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
                    }
                ]
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
            }
         ],
                "content_cards" : [
                  { 
                    "variation_name": (string) the variation name, 
                    "variation_api_id": (string) the variation API identifier, 
                    "sent": (int) the number of sends, 
                    "total_impressions": (int) the number of total impressions, 
                    "unique_impressions": (int) the number of unique impressions,
                    "total_clicks": (int) the number of total clicks, 
                    "unique_clicks": (int) the number of unique clicks, 
                    "total_dismissals": (int) the number of total dismissals, 
                    "unique_dismissals": (int) the number of unique dismissals, 
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
                  }
                ]
              },
           "conversions_by_send_time": (optional, int),
           "conversions1_by_send_time": (optional, int),
           "conversions2_by_send_time": (optional, int),
           "conversions3_by_send_time": (optional, int),
           "conversions": (int),
           "conversions1": (optional, int),
           "conversions2": (optional, int),
           "conversions3": (optional, int),
           "unique_recipients": (int),
           "revenue": (optional, float)
        },
        ...
    ],
    ...
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

指定できるメッセージタイプは`email`、、`in_app_message`、`webhook`、`android_push`、`ios_push`、`kindle_push`、`web_push`です。に表示される統計情報は、`android_push`どのプッシュメッセージタイプでも同じです。

{% alert tip %}
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

{% endapi %}
