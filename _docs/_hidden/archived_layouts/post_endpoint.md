---
nav_title: "POST: [Endpoint name]"
article_title: "Example layout: POST: User Track"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
excerpt_separator: ""

description: "This article outlines details about and using this POST [endpoint name] Braze endpoint."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# [Endpoint Name]

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Use this endpoint to remove "invalid" phone numbers from the invalid list in Braze. This can be used to re-validate phone numbers after they have been marked as invalid.

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Rate limit

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Request Body

<!--This is where you can give more information about your endpoint request body. -->

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

### Request parameters

<!--This is a place for you to describe additional details for the parameters in the request body.-->

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `phone_number` | Required | Array of strings in e.164 format | An array of up to 50 phone numbers to modify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

<!--The following example demonstrates a request that will remove specific SMS numbers from Braze's invalid phone number list via the API:-->

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```
{% endapi %}
