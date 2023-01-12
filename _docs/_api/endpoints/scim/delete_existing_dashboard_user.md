---
nav_title: "DELETE: Remove Dashboard User Account"
article_title: "DELETE: Remove Dashboard User Account"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Remove Existing User Account endpoint."
---

{% api %}
# Remove a dashboard user account
{% apimethod delete %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

This endpoint allows you to permanently delete an existing dashboard user by specifying the resource `id` returned by the SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) method. This is similar to deleting a user in the **Manage Users** section of the Braze dashboard. For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Request body

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Required | String | The user’s resource ID. This parameter is returned by the  `POST` `/scim/v2/Users/` or `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` methods. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
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
If a developer with this ID doesn’t exist in Braze, the endpoint will respond with:
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
