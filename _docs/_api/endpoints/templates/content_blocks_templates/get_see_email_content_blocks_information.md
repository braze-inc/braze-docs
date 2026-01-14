---
nav_title: "GET: See Content Blocks information"
article_title: "GET: See Content Blocks Information"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the See Content Blocks information Braze endpoint."
---

{% api %}
# See Content Block information
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Use this endpoint to call information for your existing [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Prerequisites
To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `content_blocks.info` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `content_block_id`  | Required | String | The Content Block identifier. <br><br>You can find this by either listing Content Block information through an API call or going to the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page, then scrolling to the bottom and searching for your Content Block API identifier.|
| `include_inclusion_data`  | Optional | Boolean | When set to `true`, the API returns back the Message Variation API identifier of campaigns and Canvases where this Content Block is included, to be used in subsequent calls.  The results exclude archived or deleted campaigns or Canvases. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `Content Block ID cannot be blank` | Make sure that a Content Block is listed in your request and is encapsulated in quotes (`""`). |
| `Content Block ID is invalid for this workspace` | This Content Block doesn't exist or is in a different company account or workspace. |
| `Content Block has been deleted—content not available` | This Content Block, though it may have existed earlier, has been deleted. |
| `Include Inclusion Data—error` | This parameter only accepts boolean values (true or false). Make sure the value for `include_inclusion_data` is not encapsulated in quotes (`""`), which causes the value to be sent as a string instead. See [request parameters](#request-parameters) for details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
