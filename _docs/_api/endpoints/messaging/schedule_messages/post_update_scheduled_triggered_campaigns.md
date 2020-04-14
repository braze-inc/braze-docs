---
nav_title: "POST: Update Scheduled API Triggered Campaign Messages"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Campaigns

description: "This article outlines details about the Update Scheduled API Triggered Campaigns Braze endpoint."
---
{% api %}
# Update Scheduled API Triggered Campaigns
{% apimethod post %}
/campaigns/trigger/schedule/update
{% endapimethod %}

Use this endpoint to update scheduled API Triggered Campaigns, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

This endpoint allows you to send Campaign messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an [API Triggered Campaign]({{site.baseurl}}/api/api_campaigns/).

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests. For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time. Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second changes could be applied to all, some, or none of your targeted users.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateScheduledMessageExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}


## Request Body

```
Content-Type: application/json
```

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

This endpoint uses the [Schedule Object]({{site.baseurl}}/api/objects_filters/schedule_object/).

{% endapi %}
