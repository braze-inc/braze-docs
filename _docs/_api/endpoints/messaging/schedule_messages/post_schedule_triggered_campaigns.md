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

# Schedule API Triggered Campaigns

{% apimethod post %}
/campaigns/trigger/schedule/create
{% endapimethod %}

Use this endpoint to trigger API Triggered Campaigns, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

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
  "send_id": (optional, string) see Send Identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, Array of Recipient Object),
  // for any keys that conflict between these trigger properties and those in a Recipient Object, the value from the
  // Recipient Object will be used
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see Trigger Properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

This endpoint uses the [Schedule Object]({{ site.baseurl }}/api/objects_filters/schedule_object/).


{% endapi %}
