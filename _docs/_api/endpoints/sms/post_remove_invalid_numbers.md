---
nav_title: "POST: Remove invalid phone numbers"
article_title: "POST: Remove Invalid Phone Numbers"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the Remove invalid phone numbers Braze endpoint."

---
{% api %}
# Remove invalid phone numbers
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> Use this endpoint to remove "invalid" phone numbers from our invalid list.

This can be used to re-validate phone numbers after they have been marked as invalid.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `sms.invalid_phone_numbers.remove` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `phone_number` | Required | Array of strings in e.164 format | An array of up to 50 phone numbers to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
