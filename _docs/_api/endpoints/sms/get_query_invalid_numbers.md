---
nav_title: "GET: Query invalid phone numbers"
article_title: "GET: Query Invalid Phone Numbers"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about Query invalid phone numbers Braze endpoint."
---
{% api %}
# Query invalid phone numbers
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> Use this endpoint to pull a list of phone numbers that have been marked "invalid" within a certain time frame. See [Invalid Phone Number Handling]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers) documentation for more information.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `sms.invalid_phone_numbers` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Optional <br>(see note) | String in YYYY-MM-DD format| Start date of the range to retrieve invalid phone numbers, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. |
| `end_date` | Optional <br>(see note) | String in YYYY-MM-DD format | End date of the range to retrieve invalid phone numbers. This is treated as midnight in UTC time by the API. |
| `limit` | Optional | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | Optional | Integer | Optional beginning point in the list to retrieve from. |
| `phone_numbers` | Optional <br>(see note) | Array of Strings in e.164 format | If provided, we will return the phone number if it has been found to be invalid. |
| `reason` | Optional <br>(see note) | String | Available values are "provider_error" (provider error indicates phone cannot receive SMS) or "deactivated" (phone number has been deactivated). If omitted, all reasons are returned. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
You must provide either a `start_date` and an `end_date` OR `phone_numbers`. If you provide all three, `start_date`, `end_date`, and `phone_numbers`, we prioritize the given phone numbers and disregard the date range.
{% endalert %}

If your date range has more than the `limit` number of invalid phone numbers, you will need to make multiple API calls with increasing the `offset` each time until a call returns either fewer than `limit` or zero results.

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response
Entries are listed in descending order.

```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}
