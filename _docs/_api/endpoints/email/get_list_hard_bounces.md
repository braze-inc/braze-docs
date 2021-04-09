---
nav_title: "GET: Query Hard Bounced Emails"
page_order: 0

layout: api_page

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines the usage of and parameters for using the retrieve a List of Hard Bounced Email Addresses Braze endpoint."
---
{% api %}
# Query or List Hard Bounced Emails
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

This endpoint allows you to pull a list of email addresses that have "hard bounced" your email messages within a certain time frame.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

You must provide an `end_date`, as well as either an `email` or a `start_date`.

| Parameter | Required | Data Type | Description |
| ----------|-----------| ----------|----- |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve hard bounces, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `email` | No * | String | If provided, we will return whether or not the user has hard bounced |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

If your date range has more than the `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

### Sample Response

Entries are listed in descending order.

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "emails": [
    {
      "email": "foo@braze.com",
      "hard_bounced_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "bar@braze.com",
      "hard_bounced_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "baz@braze.com",
      "hard_bounced_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}
