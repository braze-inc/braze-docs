---
nav_title: "POST: Delete Scheduled Messages"
article_title: "POST: Delete Scheduled Messages"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Delete Scheduled Messages Braze endpoint."

---
{% api %}
# Delete scheduled messages
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/messages/schedule/delete
{% endapimethod %}

The delete scheduled messages endpoint allows you to cancel a message that you previously scheduled _before_ it has been sent.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Required | String | The `schedule_id` to delete (obtained from the response to create schedule). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}
'
```

{% endapi %}
