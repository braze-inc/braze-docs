---
nav_title: "GET: [Endpoint Name]"
page_order:

layout: api_page
excerpt_separator: ""

page_type: reference
platform: API

channel:
  - Email
  - Push
tool:
  - Canvas
  - Campaigns

description: "This article outlines the usage of and parameters for using the Get [endpoint name] Braze endpoint."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# Query or List [Item Endpoint "Gets"]

{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

This is the description of the endpoint. For example: "Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database. All API requests are made over HTTPS."

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Query Parameters

You must provide an `end_date`, as well as either an `email` or a `start_date` .

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `start_date` | No * | String in YYYY-MM-DD format| Start date of the range to retrieve hard bounces, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. |
| `end_date` | No * | String in YYYY-MM-DD format | End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. |
| `limit` | No | Integer | Optional field to limit the number of results returned. Defaults to 100, maximum is 500. |
| `offset` | No | Integer | Optional beginning point in the list to retrieve from |
| `email` | No * | String | If provided, we will return whether or not the user has hard bounced |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

If your date range has more than `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

### Sample Response

Entries are listed in descending order.

```json
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
