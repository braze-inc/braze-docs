---
nav_title: "PUT: Update Dashboard User Account"
article_title: "PUT: Update Dashboard User Account"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update existing dashboard user account Braze endpoint."
---

{% api %}
# Update dashboard user account
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> This endpoint allows you to update an existing dashboard user account by specifying the resource `id` returned by the SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) method. 

It allows you to update of given and family names, permissions (for setting permissions at the company, workspace, and team level) and department. For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

For security reasons, `userName` (email address) cannot be updated through this endpoint. If you would like to change the `userName` (email address) for a user, contact [Support]({{site.baseurl}}/support_contact/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `id` | Required | String | The user's resource ID. This parameter is returned by the  `POST` `/scim/v2/Users/` or `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` methods. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Request body
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
                    } 
                ]
            } 
        ]
   }
}
```

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `schemas` | Required | Array of strings | Expected SCIM 2.0 schema name for user object. |
| `name` | Required | JSON object | This object contains the user's given name and family name. |
| `department` | Required | String | Valid department string from the [department string documentation]({{site.baseurl}}/scim_api_appendix/#department-strings). |
| `permissions` | Required | JSON object | Permissions object as described in the [permissions object documentation]({{site.baseurl}}/scim_api_appendix/#permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Example request
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test workspace",
                "appGroupPermissions": ["basic_access","send_campaign_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
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
                "appGroupName": "Test workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

### Error states
If a user with this ID doesn't exist in Braze, the endpoint will respond with:

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

