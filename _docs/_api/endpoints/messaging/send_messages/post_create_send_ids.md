---
nav_title: "POST: Create Send IDs"
page_order: 4

layout: api_page2

page_type: reference
platform: API
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Create Send IDs Braze endpoint."
---

{% api %}

# Create Send IDs For Message Send Tracking

{% apimethod post %}
/sends/id/create
{% endapimethod %}

Braze’s Send Identifier adds the ability to send messages and track message performance entirely programmatically, without campaign creation for each send. Using the Send Identifier to track and send messages is useful if you are planning to programmatically generate and send content.

The daily maximum number of custom send identifiers that can be created via this endpoint for a given app group is 100. Each send id - campaign id combination that you create will count towards your daily limit. The response headers for any valid request include the current rate limit status, see [API Limits]({{ site.baseurl }}/api/basics/#api-limits).


{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Messaging/CreateSendIdsForMessageSendTracking {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}


## Request Body

```
Content-Type: application/json
```

```json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (required, string) see Send Identifier
}
```

## Response

```json
{
  "message": "success",
  "send_id" : "example_send_id"
}
```

{% endapi %}
