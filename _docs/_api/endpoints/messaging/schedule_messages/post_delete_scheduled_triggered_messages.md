---
nav_title: "POST: Delete Scheduled API Triggered Campaigns"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Delete Scheduled API Triggered Messages Braze endpoint."
---
{% api %}
# Delete Scheduled API Triggered Campaigns
{% apimethod post %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

The delete schedule endpoint allows you to cancel a message that you previously scheduled API Triggered Campaigns before it has been sent.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}


## Request Body

```
Content-Type: application/json
```

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second deletions could be applied to all, some, or none of your targeted users.

```json
{
  "campaign_id": (required, string) the Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

## Request Components
- [Campaign Identifier](({{site.baseurl}}/api/identifier_types/)

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete?campaign_id=123456789&schedule_id=123456789' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "campaign_id": "123456789",
  "schedule_id": "123456789"
}
'
```

{% endapi %}
