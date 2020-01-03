---
nav_title: "GET: Send Analytics"
page_order: 4

layout: api_page2

page_type: reference
platform:
  - API

tool:
  - Campaign


description: "This article outlines details about Braze's Campaign Daily Stats by Send ID endpoint."
---

{% api %}

# Send Analytics Endpoint

{% apimethod get %}
/sends/data_series
{% endapimethod %}

This endpoint allows you to retrieve a daily series of various stats for a tracked `send_id`. Braze stores send analytics for 14 days after the send.

Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.

The `send_id` is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the `send_id` is included in response for the `messages/send`, `messages/schedule`, `campaign/trigger/send` and `campaign/trigger/schedule` endpoints.


{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Request Parameter Details

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- |------------ |
| `api_key` | Yes | String | App Group REST API Key. |
| `campaign_id` | Yes | String | Campaign API Identifier. |
| `send_id` | Yes | String | Send API Identifier. |
| `length` | Yes | Integer | Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive. |
| `ending_at` | No | DateTime (ISO 8601 string) | Date on which the data series should end - defaults to time of the request. |

{% alert important %}
The `send_id` is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the `send_id` is included in response for the `messages/send`, `messages/schedule`, `campaign/trigger/send` and campaign/trigger/schedule endpoints.
{% endalert %}

### Example URL
`https://rest.iad-01.braze.com/sends/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&campaign_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&send_id=3456789&length=7&ending_at=2014-12-10T23:59:59-05:00`

### Send Analytics Endpoint API Response

```json
Content-Type: application/json
{
            "variation_name": (string) variation name,
            "sent": (int) the number of sends,
            "delivered": (int) the number of messages successfully delivered,
            "undelivered": (int) the number of undelivered,
            "delivery_failed": (int) the number of rejected,
            "direct_opens": (int) the number of direct opens,
            "total_opens": (int) the number of total opens,
            "bounces": (int) the number of bounces,
            "body_clicks": (int) the number of body clicks,
            "revenue": (float) the number of dollars of revenue (USD),
            "unique_recipients": (int) the number of unique recipients,
            "conversions": (int) the number of conversions,
            "conversions_by_send_time": (int) the number of conversions,
            "conversions1": (int, optional) the number of conversions for the second conversion event,
            "conversions1_by_send_time": (int, optional) the number of conversions for the second conversion event by send time,
            "conversions2": (int, optional) the number of conversions for the third conversion event,
            "conversions2_by_send_time": (int, optional) the number of conversions for the third conversion event by send time,
            "conversions3": (int, optional) the number of conversions for the fourth conversion event,
            "conversions3_by_send_time": (int, optional) the number of conversions for the fourth conversion event by send time
          }
        ]
      },
      "conversions_by_send_time": 0,
      "conversions1_by_send_time": 0,
      "conversions2_by_send_time": 0,
      "conversions3_by_send_time": 0,
      "conversions": 0,
      "conversions1": 0,
      "conversions2": 0,
      "conversions3": 0,
      "unique_recipients": 1,
      "revenue": 0
    }
  ],
  "message": "success"
}
```

{% endapi %}
