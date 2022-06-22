---
nav_title: "GET: See Dashboard Developer Account Information"
article_title: "GET: See Dashboard Developer Account Information"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the See Dashboard Developer Account Information Endpoint."
permalink: /scim/get
hidden: true
---

{% api %}
# See dashboard developer account information
{% apimethod get %}
/scim/v2/Users/user@test.com
{% endapimethod %}

This endpoint allows you to look up an existing dashboard developer account by specifying their email. 

## Rate limit

{% include rate_limits.md endpoint='look up dashboard developer' %}

## Request parameters

| Parameter | Required | Data type | Description |
| --------- | -------- | --------- | ----------- |
| `id` | Required | String | Email of |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/user@test.com' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Response
```json

```

{% endapi %}

