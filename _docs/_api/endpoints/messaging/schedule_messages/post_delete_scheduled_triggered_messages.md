---
nav_title: "POST: Delete Scheduled API-Triggered Campaigns"
article_title: "POST: Delete Scheduled API-Triggered Campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Delete Scheduled API-Triggered Messages Braze endpoint."

---
{% api %}
# Delete scheduled API-triggered campaigns
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/campaigns/trigger/schedule/delete
{% endapimethod %}

The delete schedule endpoint allows you to cancel a message that you previously scheduled API-triggered campaigns before it has been sent.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Request body

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second deletions could be applied to all, some, or none of your targeted users.

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id`| Required | String | See [campaign identifier]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Required | String | The `schedule_id` to delete (obtained from the response to create schedule). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}
'
```

{% endapi %}
