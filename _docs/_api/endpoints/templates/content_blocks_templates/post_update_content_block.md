---
nav_title: "POST: Update content block"
article_title: "POST: Update Content Block"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update Content Blocks Braze endpoint."

---
{% api %}
# Update Content Block
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> Use this endpoint to update a [Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Prerequisites
To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/api_key/) with the `content_blocks.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `content_block_id`|	Required |	String | Your Content Block's API identifier.|
| `name` | Optional | String | Name of the Content Block. Must be less than 100 characters. |
| `description` | Optional | String | Description of the Content Block. Must be less than 250 characters. |
| `content` | Optional | String | HTML or text content within Content Blocks.
| `state` | Optional | String | Choose `active` or `draft`. Defaults to `active` if not specified. |
| `tags` | Optional | Array of strings | [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) must already exist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `Content cannot be blank` |
| `Content must be a string` | Make sure your content is encapsulated in quotes (`""`). |
| `Content must be smaller than 50kb` | The content in your Content Block must be less than 50 KB total. |
| `Content contains malformed liquid` | The Liquid provided is not valid or parsable. Try again with valid Liquid or reach out to support. |
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
| `Content Block description must be a string` | Make sure your Content Block description is encapsulated in quotes (`""`). |
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
| `Content Block name can only contain alphanumeric characters` | Content Block names can include any of the following characters: the letters (capitalized or lowercase) `A` through `Z`, the numbers `0` through `9`, dashes `-`, and underscores `_`. It cannot contain non-alphanumeric characters like emojis, `!`, `@`, `~`, `&`, and other "special" characters. |
| `Content Block with this name already exists` | Try a different name. |
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
| `Tags must be an array` | Tags must be formatted as an array of strings, for example `["marketing", "promotional", "transactional"]`. |
| `All tags must be strings` | Make sure your tags are encapsulated in quotes (`""`). |
| `Some tags could not be found` | To add a tag when creating a Content Block, the tag must already exist in Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
