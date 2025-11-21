---
nav_title: "GET: Generate preference center URL"
article_title: "GET: Generate Preference Center URL"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the Generate preference center URL Braze endpoint."

---
{% api %}
# Generate preference center URL
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Use this endpoint to generate a URL for a preference center.

Each preference center URL is unique to each user.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `preference_center.user.get` permission.

## Rate limit

This endpoint has a rate limit of 1,000 requests per minute, per workspace.

## Path parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Required | String | The ID for your preference center. |
|`userID`| Required | String | The user ID. |
{:  role="presentation" }

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| Required | String | The ID for your preference center. |
|`external_id`| Required | String | The external ID for a user. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
This endpoint only generates URLs for the new preference center (such as preference centers created using our API or the drag-and-drop editor).
{% endalert %}
