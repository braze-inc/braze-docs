---
nav_title: "GET: See Content Blocks Information"
article_title: "GET: See Content Blocks Information"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the See Available Content Blocks Information Braze endpoint."
---

{% api %}
# See Content Block information
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

This endpoint will call information for your existing [Email Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `content_block_id`  | Required | String | The content block identifier. <br><br>You can find this by either listing content block information through an API call or going to **Developer Console** > **API Settings**, then scrolling to the bottom and searching for your content block API identifier.|
| `include_inclusion_data`  | Optional | Boolean | When set to `true`, the API returns back the Message Variation API identifier of campaigns and Canvases where this content block is included, to be used in subsequent calls.  The results exclude archived or deleted campaigns or Canvases. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
  "content_block_id": "string",
  "name": "string",
  "content": "string",
  "description": "string",
  "content_type": "html or text",
  "tags":  "array of strings",
  "created_at": "time-in-iso",
  "last_edited": "time-in-iso",
  "inclusion_count" : "integer",
  "inclusion_data": "array",
  "message": "success",
}
```

### Possible errors

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| Content Block ID cannot be blank | Make sure that a Content Block is listed in your request and is encapsulated in quotes (`""`). |
| Content Block ID is invalid for this App Group | This Content Block doesn't exist or is in a different company account or app group. |
| Content Block has been deleted—content not available | This Content Block, though it may have existed earlier, has been deleted. |
| Include Inclusion Data—error | This parameter only accepts boolean values (true or false). Make sure the value for `include_inclusion_data` is not encapsulated in quotes (`""`), which causes the value to be sent as a string instead. See [request parameters](#request-parameters) for details. |
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
