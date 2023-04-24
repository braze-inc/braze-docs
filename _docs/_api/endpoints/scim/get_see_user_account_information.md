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
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

This endpoint allows you to look up an existing dashboard user account by specifying the resource `id` returned by the SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) method. For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Request body
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Required | String | The user's resource ID. This parameter is returned by the  `POST` `/scim/v2/Users/` or `GET` `/scim/v2/Users?filter=userName eq "user@test.com"` methods. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Response
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
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