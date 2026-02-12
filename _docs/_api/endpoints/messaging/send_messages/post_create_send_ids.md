---
nav_title: "POST: Create send IDs"
article_title: "POST: Create Send IDs"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Create send IDs Braze endpoint."

---
{% api %}
# Create send IDs
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> Use this endpoint to create send IDs that can be used to send messages and track message performance programmatically, without campaign creation for each send.

Using the send identifier to track and send messages is useful if you are planning to programmatically generate and send content.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `sends.id.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Required | String | See [campaign identifier]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Optional | String | See [send identifier]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Response

### Example success response

```json
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}
