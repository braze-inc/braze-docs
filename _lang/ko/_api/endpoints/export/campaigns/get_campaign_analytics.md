---
nav_title: "GET: 내보내기 캠페인 분석"
article_title: "GET: 내보내기 캠페인 분석"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 내보내기 캠페인 분석 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 캠페인 분석 내보내기
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인에 대한 다양한 통계의 일별 시리즈를 시간별로 검색할 수 있습니다. 

반환된 데이터에는 메시징 채널별로 전송, 열기, 클릭 또는 변환된 메시지 수가 포함됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `campaigns.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='export campaign analytics' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | -------- | --------- | ----------- |
| `campaign_id` | 필수 | 문자열 | [캠페인 API 식별자]({{site.baseurl}}/api/identifier_types/) 참조.<br><br> API 캠페인용 `campaign_id`는 대시보드 내의 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지와 **캠페인 세부정보** 페이지에서 찾을 수 있으며, [캠페인 목록 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)를 사용할 수도 있습니다. |
| `length` | 필수 | 정수 | 반환된 시리즈에 포함할 `ending_at` 이전 최대 일 수입니다. 1에서 100 사이여야 합니다(포함). |
| `ending_at` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 계열이 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시 

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

### 멀티채널 응답

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

### 다변량 응답

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

가능한 메시지 유형은 `email`, `in_app_message`, `webhook`, `android_push`, `ios_push`, `kindle_push`, `web_push`입니다. 모든 푸시 메시지 유형에는 `android_push`에 대해 동일한 통계가 표시됩니다.

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
