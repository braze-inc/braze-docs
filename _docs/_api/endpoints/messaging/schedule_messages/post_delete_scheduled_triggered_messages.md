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
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/campaigns/trigger/schedule/delete
{% endapimethod %}

The delete schedule endpoint allows you to cancel a message that you previously scheduled API Triggered Campaigns before it has been sent.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}


## Request Body

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second deletions could be applied to all, some, or none of your targeted users.

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": (required, string) the Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id`|Required|String| See Campaign Identifier|
| `schedule_id` | Required | String | The schedule_id to delete (obtained from the response to create schedule) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Request Components
- [Campaign Identifier]({{site.baseurl}}/api/identifier_types/)

### Example Request
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "campaign_id": "123456789",
  "schedule_id": "123456789"
}
'
```

{% endapi %}
