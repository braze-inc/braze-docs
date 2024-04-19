---
nav_title: "GET: List workspace Apps"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "This article outlines details about the List workspace apps Braze endpoint."
---
{% api %}
# List workspace apps
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Use this endpoint to list the name and unique identifier (`api_key`) for apps in a workspace. 

Hitting this endpoint returns an object array called `apps`. Each object in `apps` contains the name and unique identifier for the app. 

{% apiref postman %}  {% endapiref %}

## Rate limit

This endpoint has a rate limit of 100 requests per day (24 hours).

## Request parameters

This request doesn't take parameters.

## Example request

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

### Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `401: Unauthorized` | API key does not have the required permissions. Make sure your API key has `apps.get` permissions. |
| `403: Forbidden` | The feature flipper is not on for this company. Contact your customer success manager for assistance. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
