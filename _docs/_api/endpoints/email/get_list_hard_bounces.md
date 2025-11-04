---
nav_title: "GET: Query hard bounced emails"
article_title: "GET: Query Hard Bounced Emails"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines the details about the Query or list hard bounced email addresses Braze endpoint."

---
{% api %}
# Query hard bounced emails
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Use this endpoint to pull a list of email addresses that have "hard bounced" your email messages within a certain time frame.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `email.hard_bounces` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Optional* | String in YYYY-MM-DD format| *One of `start_date` or `email` is required. This is the start date of the range to retrieve hard bounces and must be earlier than `end_date`. This is treated as midnight in UTC time by the API. |
| `end_date` | Required | String in YYYY-MM-DD format | End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. |
| `limit` | Optional | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | Optional | Integer | Optional beginning point in the list to retrieve from. |
| `email` | Optional* | String | *One of `start_date` or `email` is required. If provided, we'll return whether or not the user has hard bounced. Check that the email strings are formatted properly. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
You must provide an `end_date`, and either an `email` or a `start_date`. If you provide all three, `start_date`, `end_date`, and an `email`, we prioritize the emails given and disregard the date range.
{% endalert %}

If your date range has more than the `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results. Including `offset` and `limit` parameters with `email` can return an empty response.

## Example request
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response
Entries are listed in descending order.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
