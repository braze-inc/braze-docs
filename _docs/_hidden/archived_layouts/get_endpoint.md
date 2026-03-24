---
nav_title: "GET: [Endpoint name]"
article_title: "Example layout: GET: [Endpoint Name]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "This article outlines the usage of and parameters for using the Get [endpoint name] Braze endpoint."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# Query or List [Item Endpoint "Gets"]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Use this endpoint to pull a list of phone numbers that have been deemed "invalid" within a certain time frame.

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Rate limit

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

<!--This is where you can give more information about your endpoint parameters. -->

| Parameter | Required | Data Type | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Optional <br>(see note) | String in YYYY-MM-DD format| Start date of the range to retrieve invalid phone numbers, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. |
| `end_date` | Optional <br>(see note) | String in YYYY-MM-DD format | End date of the range to retrieve invalid phone numbers. This is treated as midnight in UTC time by the API. |
| `limit` | Optional | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | Optional | Integer | Optional beginning point in the list to retrieve from. |
| `phone_numbers` | Optional <br>(see note) | Array of Strings in e.164 format | If provided, we will return the phone number if it has been found to be invalid. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
You must provide either a `start_date` and an `end_date` OR `phone_numbers`. If you provide all three, `start_date`, `end_date`, and `phone_numbers`, we prioritize the given phone numbers and disregard the date range.
{% endalert %}

## Example request

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

<!-- An example response that defines the different variables returned-->
```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}
