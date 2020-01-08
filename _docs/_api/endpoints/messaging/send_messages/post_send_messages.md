---
nav_title: "POST: Send Messages Immediately via API Only"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Send Messages Immediately Braze endpoint."
---
{% api %}
# Sending Messages Immediately via API Only
{% apimethod post %}
/messages/send
{% endapimethod %}

This endpoint allows you send your messages using our API. Be sure to include Messaging Objects in your body to complete your requests.

The send endpoint allows you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the <a href="https://dashboard-01.braze.com/app_settings/developer_console/activitylog/">Developer Console</a>.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/SendMessageImmediatelyExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74fc3f0d-11f1-40f6-93f4-2eacb0ed459a {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
   "api_key": (required, string) see App Group REST API Key,
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see External User ID,
   "user_aliases": (optional, array of User Alias Object) see User Alias,
   "segment_id": (optional, string) see Segment Identifier,
   "audience": (optional, Connected Audience Object) see Connected Audience,
   "campaign_id": (optional, string) see Campaign Identifier,
   "send_id": (optional, string) see Send Identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "apple_push": (optional, Apple Push Object),
     "android_push": (optional, Android Push Object),
     "windows_phone8_push": (optional, Windows Phone 8 Push Object),
     "windows_universal_push": (optional, Windows Universal Push Object),
     "kindle_push": (optional, Kindle/FireOS Push Object),
     "web_push": (optional, Web Push Object),
     "email": (optional, Email Object),
     "content_card": (optional, Content Card Object),
     "sms": (optional, SMS Object)
   }
 }
```
For more information on the "broadcast" flag, check out [Broadcast]({{ site.baseurl }}/api/parameters/#broadcast) within our [API Parameters]({{ site.baseurl }}/api/parameters) documentation.

### Available Messaging Objects

You can use these objects in the [request body](#request-body) above.

- [Android Objects]({{ site.baseurl }}/api/objects_filters/android_objects/)
- [Apple Objects]({{ site.baseurl }}/api/objects_filters/apple_objects/)
- [Content Cards Object]({{ site.baseurl }}/api/objects_filters/content_cards_object/)
- [Email Object]({{ site.baseurl }}/api/objects_filters/email_object/)
- [Kindle or FireOS Object]({{ site.baseurl }}/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object]({{ site.baseurl }}/api/objects_filters/sms_object/)
- [Web Objects]({{ site.baseurl }}/api/objects_filters/web_objects/)
- [Webhook Object]({{ site.baseurl }}/api/objects_filters/webhook_objects/)
- [Windows Objects]({{ site.baseurl }}/api/objects_filters/windows_objects/)

{% endapi %}

### Response Details
Message sending endpoint responses will include the message’s dispatch_id for reference back to the dispatch of the message. The dispatch_id is the id of the message dispatch (unique id for each ‘transmission’ sent from the Braze platform).
