---
nav_title: "GET: Query List of Unsubscribed Email Addresses"
page_order: 1

layout: api_page

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines the usage of and parameters for using the Get Email Unsubscribes Braze endpoint."
---
{% api %}
# Retrieve List of or Query Email Unsubscribes
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

Use the /email/unsubscribes endpoint to return emails that have unsubscribed during the time period from `start_date` to `end_date`. You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/QueryingAllEmailUnsubscribesExample {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

You must provide an `end_date`, as well as either an `email` or a `start_date` .

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `sort_direction` | No | String | Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. |
| `email` | No * | String | If provided, we will return whether or not the user has unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

If your date range has more than `limit` number of unsubscribes, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

### Example Request 
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
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
      "unsubscribed_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "bar@braze.com",
      "unsubscribed_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "baz@braze.com",
      "unsubscribed_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}
