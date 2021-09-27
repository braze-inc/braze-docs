---
nav_title: "GET: Query Invalid Phone Numbers"
article_title: "GET: Query Invalid Phone Numbers"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "This article outlines the usage of and parameters for using the retrieve a List of Invalid Phone Numbers Braze endpoint."
hidden: true
---
{% api %}
# Query or List Invalid Phone Numbers
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

This endpoint allows you to pull a list of phone numbers that have been deemed "invalid" within a certain time frame.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}
## Request Parameters

You must provide either a `start_date` and an `end_date` OR `phone_numbers`.

If you provide a `start_date`, an `end_date`, and `phone_numbers`, we prioritize the given phone numbers and disregard the date range.

| Parameter | Required | Data Type | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Optional* | String in YYYY-MM-DD format| Start date of the range to retrieve invalid phone numbers, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. |
| `end_date` | Optional* | String in YYYY-MM-DD format | End date of the range to retrieve invalid phone numbers. This is treated as midnight in UTC time by the API. |
| `limit` | Optional | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | Optional | Integer | Optional beginning point in the list to retrieve from. |
| `phone_numbers` | Optional* | Array | If provided, we will return whether or not those phone numbers have been detected as invalid phone numbers. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

If your date range has more than the `limit` number of invalid phone numbers, you will need to make multiple API calls with increasing the `offset` each time until a call returns either fewer than `limit` or zero results.

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response
Entries are listed in descending order.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": "12345678900",
      "invalid_detected_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "phone": "12345678901",
      "invalid_detected_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "phone": "12345678902",
      "invalid_detected_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}