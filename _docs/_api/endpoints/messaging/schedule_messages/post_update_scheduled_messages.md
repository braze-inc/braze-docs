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
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/messages/schedule/update
{% endapimethod %}

The messages update schedule endpoint accepts updates to either the `schedule` or `messages` parameter or both. Your request must contain at least one of those two keys.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/UpdateScheduledMessageExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`schedule_id`|Required|String| The schedule_id to update (obtained from the response to create schedule)|
|`schedule` | Optional | Object | See Schedule Object |
|`messages` | Optional | Object | See Available Message Object |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request Components
- [Schedule Object]({{site.baseurl}}/api/objects_filters/schedule_object/)

### Available Messaging Objects
You can use these objects in the [request body](#request-body) above.

- [Android Objects]({{site.baseurl}}/api/objects_filters/android_objects/)
- [Apple Objects]({{site.baseurl}}/api/objects_filters/apple_objects/)
- [Content Cards Object]({{site.baseurl}}/api/objects_filters/content_cards_object/)
- [Email Object]({{site.baseurl}}/api/objects_filters/email_object/)
- [Kindle or FireOS Object]({{site.baseurl}}/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object]({{site.baseurl}}/api/objects_filters/sms_object/)
- [Web Objects]({{site.baseurl}}/api/objects_filters/web_objects/)
- [Webhook Object]({{site.baseurl}}/api/objects_filters/webhook_object/)
- [Windows Objects]({{site.baseurl}}/api/objects_filters/windows_objects/)

### Request Example
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "schedule_id": "schedule identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
     "apple_push": {
       "alert": "Updated Message!",
       "badge": 1
     },
     "android_push": {
       "title": "Updated title!",
       "alert": "Updated message!"
     },
     "sms": {  
      	"subscription_group_id": "23894012",
      	"message_variation_id": "3728490",
      	"body": "This is my SMS body.",
      	"app_id": "sdj23-234bd-23bdjask"
      }
  }
}'
```

{% endapi %}
