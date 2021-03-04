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

This endpoint will call information for your exiting [Email Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.<br><br>Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset. Please update your API calls accordingly.
{% endalert %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `content_block_id`  | Yes | String | The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier.|
| `include_inclusion_data`  | No | Boolean | When set to 'true', the API returns back the Message Variation API ID of Campaigns and Canvases where this content block is included, to be used in subsequent calls.  The results exclude archived or deleted Campaigns or Canvases. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id=12345678910' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

### Successful Response Properties

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
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

### Example Request with including inclusion data
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id=12345678910&include_inclusion_data=true' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

### Successful Response Properties

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
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
  "inclusion_data": "array"
  "message": "success",
}
```

## Possible Errors
- `Content Block ID cannot be blank.` - A Content Block has not been listed or is not encapsulated in quotes.

- `Content Block ID is invalid for this App Group.` - This Content Block does not exist or is in a different company account or app group.

- `Content Block has been deleted - content not available.` - This Content Block, though it may have existed earlier, has been deleted.

- `Include Inclusion Data - error` - One of true or false is not provided

{% endapi %}
