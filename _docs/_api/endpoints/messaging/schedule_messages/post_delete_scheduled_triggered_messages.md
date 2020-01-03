---
nav_title: "POST: Delete Scheduled API Triggered Campaigns"
page_order: 4

layout: api_page2

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
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

{% endapi %}
