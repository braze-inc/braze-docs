---
nav_title: "GET: App Group Apps"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "This article outlines details about the GET App Group Apps endpoint, which allows you to retrieve an `apps` object array."
---
{% api %}
# App group apps endpoint
{% apimethod get %}
/app_group/apps
{% endapimethod %}

Use this endpoint to list the name and unique identifier (`api_key`) for apps in an app group. Hitting this endpoint returns an object array called `apps`. Each object in `apps` contains the name and unique identifier for the app. 

{% apiref postman %}  {% endapiref %}

## Rate limit

This endpoint has a rate limit of 100 requests per day (24 hours).

## Request Parameters

This request doesn't take parameters.

## Example Request

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Possible Errors

- `401: Unauthorized` — API key does not have the required permissions. Make sure your API key has `apps.get` permissions.
- `403: Forbidden` — Feature flipper is not on for this company. Contact your Customer Success Manager for assistance.


{% endapi %}
