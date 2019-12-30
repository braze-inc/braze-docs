---
nav_title: "POST: Send Campaign Messages via API Triggered Delivery"
page_order: 4

layout: api_page2

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Email Addresses from the Spam List Braze endpoint."
---

{% api %}

# Sending Campaign Messages via API Triggered Delivery

API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API. Please see this section of [Braze Academy for further details][39].

The send endpoint allows you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the [Developer Console][41].

{% apimethod post %}
/campaigns/trigger/send
{% endapimethod %}

This endpoint allows you to send Campaign messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an [API Triggered Campaign]({{ site.baseurl }}/api/api_campaigns/).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/SendMessageImmediatelyExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74fc3f0d-11f1-40f6-93f4-2eacb0ed459a {% endapiref %}

```
Content-Type: application/json
```

## Request Body

```json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with trigger_properties above)
    },
    ...
  ]
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

{% endapi %}


[41]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
