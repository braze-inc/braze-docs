---
nav_title: "POST: Schedule API Triggered Campaign Messages"
page_order: 4

layout: api_page2

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Email Addresses from the Spam List Braze endpoint."
---

{% api %}

# Update Scheduled API Triggered Campaigns

{% apimethod post %}
/campaigns/trigger/schedule/update
{% endapimethod %}

Use this endpoint to update scheduled API Triggered Campaigns, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

This endpoint allows you to send Campaign messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an [API Triggered Campaign]({{ site.baseurl }}/api/api_campaigns/).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateScheduledMessageExample {% endapiref %}
{% apiref postman %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateScheduledApiTriggeredCampaignExample {% endapiref %}

```
Content-Type: application/json
```

## Request Body

```json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

This endpoint uses the [Schedule Object]({{ site.baseurl }}/api/objects_filters/schedule_object/).

{% endapi %}
