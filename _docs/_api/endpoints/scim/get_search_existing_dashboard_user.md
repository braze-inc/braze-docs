---
nav_title: "GET: Search existing dashboard user account by email"
article_title: "GET: Search Existing Dashboard User Account by Email"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Search for an existing dashboard user account by email Braze endpoint."
---

{% api %}
# Search existing dashboard user account by email
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Use this endpoint to look up an existing dashboard user account by specifying their email in the filter query parameter. 

Note that when the query parameter is URL encoded it will read like this:

`/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need a SCIM token. You'll use your service origin as the `X-Request-Origin` header. For more information, refer to [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `userName@example.com` | Required | String | The user's email. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Request parameters

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Example request
```json
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Response
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@test.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
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
                        "appGroupName": "Test Workspace",
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
    ]
}
```

{% endapi %}

