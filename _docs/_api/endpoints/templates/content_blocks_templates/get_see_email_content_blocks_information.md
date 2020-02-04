---
nav_title: "GET: See Content Blocks Information"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the See Available Content Blocks Information Braze endpoint."
---

{% api %}
# See Content Block Information
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

This endpoint will call information for your exiting [Email Content Blocks]({{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `content_block_id`  | Yes | String | The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier.|

### Successful Response Properties
```json
{
  "content_block_id": "string",
  "name": "string",
  "content": "string",
  "description": "string",
  "content_type": "html or text",
  "tags":  "array of strings",
  "created_at": "time-in-iso",
  "last_edited": "time-in-iso",
  "inclusion_count" : integer,
  "message": "success"
}
```

## Possible Errors
- `Content Block ID cannot be blank.`
A Content Block has not been listed or is not encapsulated in quotes.

- `Content Block ID is invalid for this App Group.`
This Content Block does not exist or is in a different company account or app group.

- `Content Block has been deleted - content not available.`
This Content Block, though it may have existed earlier, has been deleted.

{% endapi %}
