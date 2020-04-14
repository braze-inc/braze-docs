---
nav_title: "POST: Update Scheduled Messages"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Update Scheduled Messages Braze endpoint."
---
{% api %}
# Update Scheduled Messages
{% apimethod post %}
/messages/schedule/update
{% endapimethod %}

The messages update schedule endpoint accepts updates to either the `schedule` or `messages` parameter or both. Your request must contain at least one of those two keys.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/UpdateScheduledMessageExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}


## Request Body

```
Content-Type: application/json
```

```json
{
  "api_key": (required, string) see App Group REST API Key,
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see create schedule documentation
  }
}
```
This endpoint uses the [Schedule Object]({{site.baseurl}}/api/objects_filters/schedule_object/).

### Available Messaging Objects

You can use these objects in the [request body](#request-body) above.

- [Android Objects]({{site.baseurl}}/api/objects_filters/android_objects/)
- [Apple Objects]({{site.baseurl}}/api/objects_filters/apple_objects/)
- [Content Cards Object]({{site.baseurl}}/api/objects_filters/content_cards_object/)
- [Email Object]({{site.baseurl}}/api/objects_filters/email_object/)
- [Kindle or FireOS Object]({{site.baseurl}}/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object]({{site.baseurl}}/api/objects_filters/sms_object/)
- [Web Objects]({{site.baseurl}}/api/objects_filters/web_objects/)
- [Webhook Object]({{site.baseurl}}/api/objects_filters/webhook_objects/)
- [Windows Objects]({{site.baseurl}}/api/objects_filters/windows_objects/)

{% endapi %}
