---
nav_title: "DELETE: Remove Dashboard Developer Account"
article_title: "DELETE: Remove Dashboard Developer Account"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Remove Existing Developer Account Endpoint."
permalink: /scim/delete
hidden: true
---

{% api %}
# Remove a dashboard developer account
{% apimethod delete %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

This endpoint allows you to permanently delete an existing dashboard developer, similarly to deleting a user in the Manage Users section of the Braze dashboard.

## Rate limit

{% include rate_limits.md endpoint='delete dashboard developer' %}

## Request body

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
```

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Required | String | The developer's email address |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```
## Response
```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```
## Error states
If a developer with this email address doesn’t exist in Braze, the endpoint will respond with:
```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User not found",
  "status": 404
}
```
{% endapi %}
