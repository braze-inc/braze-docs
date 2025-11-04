---
nav_title: "POST: Update scheduled messages"
article_title: "POST: Update Scheduled Messages"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update scheduled messages Braze endpoint."

---
{% api %}
# Update scheduled messages
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/update
{% endapimethod %}

> Use this endpoint to update scheduled messages.

This endpoint accepts updates to either the `schedule` or `messages` parameter or both. Your request must contain at least one of those two keys.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `messages.schedule.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Required | String | The `schedule_id` to update (obtained from the response to create schedule). |
|`schedule` | Optional | Object | See [schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/). |
|`messages` | Optional | Object | See [available messaging objects]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
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
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}
