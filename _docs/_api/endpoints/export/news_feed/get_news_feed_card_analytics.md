---
nav_title: "GET: News Feed Card Analytics"
page_order: 4

layout: api_page

page_type: reference
channel: News Feed
platform: API
tool: Segments
description: "This article outlines details about and using the Segments List endpoint to export a list of available Segments."
---
{% api %}
# News Feed Card Analytics Endpoint
{% apimethod get %}
/feed/data_series
{% endapimethod %}

This endpoint allows you to retrieve a daily series of engagement stats for a card over time.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Parameters

<<<<<<< HEAD
| Parameter   | Required | Data Type | Description |
| ----------- | -------- | --------- | ----------- |
| `card_id`   | Yes      | String    | Card API Identifier |
| `length`    | Yes      | Integer   | Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `unit`      | No       | String   | Unit of time between data points - can be "day" or "hour" (defaults to "day")  |
| `ending_at` | No       | DateTime (ISO 8601 string) | Date on which the data series should end - defaults to time of the request |                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
The `card_id` for a given card can be found in the Developer Console page and on the card details page within your dashboard or you can use the [News Feed List Endpoint](#news-feed-list).
{% endalert %}

### Example URL
`https://rest.iad-01.braze.com/feed/data_series?card_id=card identifier&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00`

### Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id=card%20identifier&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

`Content-Type: application/json`

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) ,
            "impressions" : (int),
            "unique_clicks" : (int),
            "unique_impressions" : (int)
        },
        ...
    ]
}
```

{% endapi %}
