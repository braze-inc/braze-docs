---
nav_title: "POST: Update scheduled API-triggered campaigns"
article_title: "POST: Update Scheduled API-Triggered Campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "This article outlines details about the Update scheduled API-triggered campaigns Braze endpoint."

---
{% api %}
# Update scheduled API-triggered campaigns
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Use this endpoint to update scheduled API-triggered campaigns created in the dashboard, allowing you to decide what action should trigger the message to be sent.

You can pass in `trigger_properties` that will be templated into the message itself.

Note that to send messages with this endpoint, you must have a campaign ID, created when you build an [API-Triggered Campaign]({{site.baseurl}}/api/api_campaigns/).

Any schedule will completely overwrite the one you provided in the create schedule request or previous update schedule requests. For example, if you originally set the schedule to `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then later update it to `"schedule" : {"time" : "2015-02-20T14:14:47"}`, the message will now be sent at the specified time in UTC, not in the user's local time.

Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts so that last-second changes can be applied to all, some, or none of your targeted users. Updates aren't applied if the original schedule used local time and the original time has already passed in any time zone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `campaigns.trigger.schedule.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String| See [campaign identifier]({{site.baseurl}}/api/identifier_types/)|
| `schedule_id` | Required | String | The `schedule_id` to update (obtained from the response to create a schedule). |
|`schedule` | Required | Object | See [schedule object]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
