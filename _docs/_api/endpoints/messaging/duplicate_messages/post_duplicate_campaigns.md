---
nav_title: "POST: Duplicate campaigns"
article_title: "POST: Duplicate Campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Duplicate campaigns endpoint."

---
{% api %}
# Duplicate campaigns using the API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Use this endpoint to duplicate campaigns. This API endpoint is similar to [duplicating campaigns in the Braze dashboard][1].

{% alert important %}
Duplicating a campaign by using the API is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `campaigns.duplicate` permission.

## Rate limit

This endpoint is limited to 100 API calls per minute.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Required | String | See [campaign identifier]({{site.baseurl}}/api/identifier_types/). |
|`name`| Required | String | The name of the resulting campaign. |
|`description`| Optional | String | The description field for the resulting campaign. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Response

This endpoint will return a `202` status code, and the campaign creation will occur asynchronously. You can use the [security event download][2] to see records of when campaigns were duplicated and by which API key.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}
