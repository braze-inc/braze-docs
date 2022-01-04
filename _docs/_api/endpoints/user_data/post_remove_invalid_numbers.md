---
nav_title: "POST: Remove Invalid Phone Numbers"
article_title: "POST: Remove Invalid Phone Numbers"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines the usage of and parameters for using this Braze endpoint to remove a list of invalid phone numbers."
---
{% api %}
# Remove invalid phone numbers
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

This endpoint allows you to remove "invalid" phone numbers from Braze's invalid list. This can be used to re-validate phone numbers after they have been marked as invalid.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_number": ["12183095514","14255551212"]
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `phone_number` | Required | Array | An array of up to 50 phone numbers to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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