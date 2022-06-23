---
nav_title: "POST: Create New Dashboard Developer Account"
article_title: "POST: Create New Dashboard Developer Account"
permalink: /post_create_developer_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Create New Dashboard Developer Account Endpoint."
hidden: true

---

{% api %}
# Create a new dashboard developer account
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

This endpoint allows you to create a new dashboard developer account by specifying email, given and family names, entitlements (for setting permissions at the company, app group, and team level). For information on how to obtain a SCIM token, visit [Automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning/). 

## Rate limit

{% include rate_limits.md endpoint='create dashboard developer' %}

## Request body
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```
```
{
  "schemas": (required, array of strings),
  "id": (required, string),
  "userName": (required, string),
  "name": (required, JSON object),
  "departments": (required, string),
  "entitlements": (required, JSON object)
}
```

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| Schemas | Required | Array of strings | Expected SCIM 2.0 schema name for user object. |
| `id` | Required | String | The developer's email address |
| `username` | Required | String | The username that the developer will need to log into Braze (usually the same as email address) |
| `name` | Required | JSON object | This object contains the developer's first name and last name |
| `departments` | Required | String | This string declares what department this user belongs to. Available options include:<br>- "agency / third party"<br>- "bi / analytics"<br>- "C-suite"<br>- "Engineering"<br>- "Finance"<br>- "marketing / editorial"<br>- "product management" |
| `entitlements` | Required | JSON object | This object allows for setting the developer's permissions at a company, app group, and team level. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
--data raw '{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "id": "user@test.com",
  "userName": "user@test.com",
  "name": {
    "givenName": "Test",
    "familyName": "User"
  },
  "department": "finance",
  "entitlements": {
    "company": {
      "admin": false,
      "can manage company settings": false,
      "can add/remove app groups": false
    },
    "app_group": [
      {
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

## Response
```json
CContent-Type: application/json
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

### Error states

If a developer with this email address already exists in Braze, the endpoint will respond with:
```json
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```
{% endapi %}
