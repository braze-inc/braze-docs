---
nav_title: "DELETE: Remove Dashboard User Account"
article_title: "DELETE: Remove Dashboard User Account"
permalink: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Remove Existing User Account Endpoint."
hidden: true
---

{% api %}
# Remove a dashboard user account
{% apimethod delete %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

This endpoint allows you to permanently delete an existing dashboard user, similarly to deleting a user in the **Manage Users** section of the Braze dashboard. For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate limit

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Request body

```json
Content-Type: application/json
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
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
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```
## Response
```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```
### Error states
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
