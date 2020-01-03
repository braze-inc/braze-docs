---
nav_title: "GET: News Feed Cards List"
page_order: 4

layout: api_page2

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

## Parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `api_key` | Yes | String    | App Group REST API Key |
| `page` | No | Integer   | The page of cards to return, defaults to 0 (returns the first set of up to 100) |
| `include_archived` | No | Boolean   | Whether or not to include archived cards, defaults to false |
| `sort_direction`   | No | String    | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. |

### Example URL
`https://rest.iad-01.braze.com/feed/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1&include_archived=true`

## Response

`Content-Type: application/json`

```json
Content-Type: application/json
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

{% endapi %}
