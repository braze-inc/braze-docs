---
nav_title: "GET: See Dashboard Developer Account Information"
article_title: "GET: See Dashboard Developer Account Information"
permalink: /get_see_developer_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the See Dashboard Developer Account Information Endpoint."
hidden: true
---

{% api %}
# See dashboard developer account information
{% apimethod get %}
/scim/v2/Users/YOUR_ID_HERE
{% endapimethod %}

This endpoint allows you to look up an existing dashboard developer account by specifying their email. For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/).

## Rate limit

{% include rate_limits.md endpoint='look up dashboard developer' %}

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Required | String | The developer's email address |
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
  "last_sign_in_at": "Thursday, January 1, 1970 12:00:00 AM",
  "entitlements": {
    "company": {
      "admin": false,
      "can manage company settings": false,
      "can add/remove app groups": false
    },
    "app_group": [
      {
        "app_group_id": "241adcd25789fabcded",
        "app_group_name": "Test App Group",
        "admin": false,
        "access campaigns, canvases, cards, segments, media library": true,
        "export user data": false,
        "send campaigns, canvases": true,
        "publish cards": false,
        "edit segments": false,
        "access dev console": false,
        "manage teams": false,
        "view usage data": false,
        "view billing details": false,
        "manage tags": false,
        "view user profiles": false,
        "manage dashboard users": false,
        "manage events, attributes, purchases": false,
        "manage email settings": false,
        "manage media library": false,
        "manage apps": false,
        "import and update user data": false,
        "manage external integrations": false,
        "view pii": false,
        "manage subscription groups": false,
        "team": [
          {
            "team_id": "241adcd25789fabcded",
            "team_name": "Test Team",
            "admin": false,
            "access campaigns, canvases, cards, segments, media library": true,
            "export user data": false,
            "send campaigns, canvases": true,
            "publish cards": false,
            "edit segments": false,
            "view user profiles": false,
            "manage dashboard users": false   
          } 
        ]
      } 
    ],
  }
}
```

{% endapi %}

