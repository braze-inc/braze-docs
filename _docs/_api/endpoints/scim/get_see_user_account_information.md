---
nav_title: "GET: Look Up an Existing Dashboard User Account"
article_title: "GET: Look Up an Existing Dashboard User Account"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Look Up an Existing Dashboard User Account Endpoint."
---

{% api %}
# Look up an existing dashboard user account
{% apimethod get %}
/scim/v2/users/YOUR_ID_HERE
{% endapimethod %}

This endpoint allows you to look up an existing dashboard user account by specifying their email. For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate limit

{% include rate_limits.md endpoint='look up dashboard user' %}

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Required | String | The users's email address |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Response
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "user@test.com",
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test App Group",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "241adcd25789fabcded",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

{% endapi %}

