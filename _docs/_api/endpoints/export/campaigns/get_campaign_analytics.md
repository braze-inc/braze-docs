---
nav_title: "GET: Export Campaign Analytics"
article_title: "GET: Export Campaign Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export campaign analytics Braze endpoint."

---
{% api %}
# Export campaign analytics
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

> Use this endpoint to retrieve a daily series of various stats for a campaign over time. 

Data returned includes how many messages were sent, opened, clicked, or converted by messaging channel.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Required | String | See [campaign API identifier]({{site.baseurl}}/api/identifier_types/).<br><br> The `campaign_id` for API campaigns can be found at **Developer Console** > **API Settings** and the **Campaign Details** page within your dashboard, or you can use the [List campaigns endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/). |
| `length` | Required | Integer | Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data series should end. Defaults to time of the request. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), **API Settings** is now **API Keys** and can be found at **Settings** > **Setup and Testing** > **API Keys**.
{% endalert %}

## Example request 

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Responses

### Multichannel response

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
                    "delivered": (int)the number of delivered messages,
                    "rejected": (int) the number of rejected messages,
                    "delivery_failed": (int) the number of failied deliveries,
                    "clicks": (int) the number of clicks on shortened links,
                    "opt_out" : (int) the number of opt outs,
                    "help" : (int) the number of help messages recieved
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

### Multivariate response

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

The possible message types are: `email`, `in_app_message`, `webhook`, `android_push`, `ios_push`, `kindle_push`, and `web_push`. All push message types will have the same statistics shown for `android_push`.

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
