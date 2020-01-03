---
nav_title: "POST: Delete Scheduled Messages"
page_order: 4

layout: api_page2

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
  "api_key": (required, string) see App Group REST API Key,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

#### Delete Scheduled API Trigger Campaign

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/trigger/schedule/delete`
US-02 | `https://rest.iad-02.braze.com/trigger/schedule/delete`
US-03 | `https://rest.iad-03.braze.com/trigger/schedule/delete`
US-04 | `https://rest.iad-04.braze.com/trigger/schedule/delete`
US-06 | `https://rest.iad-06.braze.com/trigger/schedule/delete`
EU-01 | `https://rest.fra-01.braze.eu/trigger/schedule/delete`

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/schedule/delete
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second deletions could be applied to all, some, or none of your targeted users.



{% endapi %}
