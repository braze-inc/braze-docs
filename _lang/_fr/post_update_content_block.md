---
nav_title: "POST: Update Content Block"
article_title: "POST: Update Content Block"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update Email Content Blocks Braze endpoint."
---

{% api %}
# Update Content Block
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

Use this endpoint below to update an [Email Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "content_block_id" : (required, string) Content block's API identifier.
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the content block. Must be less than 250 character,
  "content": (required, string) HTML or text content within content block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Request parameters

| Parameter          | Required | Data Type        | Description                                                                                                |
| ------------------ | -------- | ---------------- | ---------------------------------------------------------------------------------------------------------- |
| `content_block_id` | Required | String           | Your content block's API identifier.                                                                       |
| `name`             | Required | String           | Name of the content block. Must be less than 100 characters.                                               |
| `description`      | Optional | String           | Description of the content block. Must be less than 250 characters.                                        |
| `content`          | Required | String           | HTML or text content within content blocks.                                                                |
| `state`            | Optional | String           | Choose `active` or `draft`. Defaults to `active` if not specified.                                         |
| `tags`             | Optional | Array of strings | [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) must already exist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "content_block_id" :"content_block_id", 
  "name": "content_block",
  "description": "This is my content block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "content_block_id": "newly-generated-block-id",
  "liquid_tag": "generated-block-tag-from-content_block_name",
  "created_at": "time-created-in-iso",
  "message": "success"
}
```

### Possible errors
- `Content cannot be blank.`

- `Content must be a string.`

- `Content must be smaller than 50kb.` - The content in your content block must be less than 50kb total.

- `Content contains malformed liquid.` - The Liquid provided is not valid or parsable. Please try again or reach out to support.

- `Content Block cannot be referenced within itself.`

- `Content Block description cannot be blank.`

- `Content Block description must be a string.`

- `Content block description must be shorter than 250 characters.` - Your content block description must be less than 250 characters.

- `Content Block name cannot be blank.`

- `Content Block name must be a shorter than 100 characters.`

- `Content Block name can only contain alphanumeric characters.` - Content Block names can include any of the following characters: the letters (capitalized or lowercase) `A` through `Z`, the numbers `0` through `9`, dashes `-`, and underscores `_`. It cannot contain non-alphanumeric characters like emojis, `!`, `@`, `~`, `&`, and other "special" characters.

- `Content Block with this name already exists.`

- `Content Block name cannot be updated for active Content Blocks.`

- `Content Block state must be either Active or Draft.`

- `Active Content Block can not be updated to Draft. Please create a new Content Block.`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`

{% endapi %}
