---
nav_title: "GET: News Feed Cards List"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Segments
channel: News Feed
description: "This article outlines details about the News Feed Cards List Endpoint."
---
{% api %}
# News Feed Cards List Endpoint
{% apimethod get %}
/feed/list
{% endapimethod %}

This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `page` | No | Integer   | The page of cards to return, defaults to 0 (returns the first set of up to 100) |
| `include_archived` | No | Boolean   | Whether or not to include archived cards, defaults to false |
| `sort_direction`   | No | String    | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) Card API Identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner or DevPick (cross-promotional cards),
            "title" : (string) title of the card,
            "tags" : (array) tag names associated with the card
        },
        ...
    ]
}
```
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
