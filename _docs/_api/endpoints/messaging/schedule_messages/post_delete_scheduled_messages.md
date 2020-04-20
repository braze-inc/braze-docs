---
nav_title: "POST: Delete Scheduled Messages"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Delete Scheduled Messages Braze endpoint."
---
{% api %}
# Delete Scheduled Messages
{% apimethod post %}
/messages/schedule/delete
{% endapimethod %}

The delete scheduled messages endpoint allows you to cancel a message that you previously scheduled _before_ it has been sent.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## Request Body

```
Content-Type: application/json
```

```json
{
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete?schedule_id=248762133332' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "schedule_id": "248762133332"
}
'
```

{% endapi %}
