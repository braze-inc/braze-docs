---
nav_title: "POST: Update Content Block"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the Update Email Content Blocks Braze endpoint."
---
{% api %}
# Update Content Block
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

Use this endpoint below to update an [Email Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Request Body
```json
{
  "api_key": "YOUR_API_KEY_HERE",
  "content_block_id" :"123a45b6-cd78-9e01-g234-hi56j7k8l9m0", 
  "name": "content-block-1",
  "description": "This is my content block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["",""]
}
```

### Request Parameter Details

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
|`content_block_id`|	Yes |	String |	Your Content Block's API Identifier.|
| `name` | Yes | String | Can only be provided when the content block is in a draft state. Must be less than 100 characters. |
| `description` | No | String | The description of the content block. Must be less than 250 characters. |
| `content` | Yes | String | HTML or text content within Content Block.
| `state` | Optional | Choose "active" or "draft". Defaults to `active` if not specified. Can not set an active content block to draft. |
| `tags` | No | Array of Strings. | Tags must already exist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Successful Response Properties

```json
{
  "content_block_id": "newly-generated-block-id",
  "liquid_tag": "generated-block-tag-from-content_block_name",
  "created_at": "time-created-in-iso",
  "message": "success"
}
```

### Possible Errors
- `Content cannot be blank.`

- `Content must be a string.`

- `Content must be smaller than 50kb.` - The content in your content block must be less than 50kb total.

- `Content contains malformed liquid.` - The liquid provided is not valid or parsable. Please try again or reach out to support.

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
