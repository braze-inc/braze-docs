---
nav_title: "GET: Query list of unsubscribed email addresses"
article_title: "GET: Query List of Unsubscribed Email Addresses"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines the details about the Retrieve list of or query email unsubscribes Braze endpoint."

---
{% api %}
# Query list of unsubscribed email addresses
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Use this endpoint to return the latest emails that have unsubscribed during the time period from `start_date` to `end_date`. For a full subscription state history, use [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) to track this data.

You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `email.unsubscribe` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `start_date` | Optional <br>(see note) | String in YYYY-MM-DD format| Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. |
| `end_date` | Optional <br>(see note) | String in YYYY-MM-DD format | End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. |
| `limit` | Optional | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | Optional | Integer | Optional beginning point in the list to retrieve from. |
| `sort_direction` | Optional | String | Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If `sort_direction` is not included, the default order is newest to oldest. |
| `email` | Optional <br>(see note) | String | If provided, we will return whether or not the user has unsubscribed. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
You must provide an `end_date`, as well as either an `email` or a `start_date`.
{% endalert %}

If your date range has more than `limit` number of unsubscribes, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

Entries are listed in descending order.

```json
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
