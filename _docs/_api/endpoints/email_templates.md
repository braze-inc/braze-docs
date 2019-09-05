---
nav_title: Templates
page_order: 1
search_rank: 3
---

# Templates

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

## Email Templates

### Creating Email Templates

Use the endpoints below to create email templates on the Braze dashboard. These templates will be available on the Templates and Media page. The response from this endpoint will include a field for `email_template_id`, which can be used to update the template in subsequent API calls.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/create`
US-02 | `https://rest.iad-02.braze.com/templates/email/create`
US-03 | `https://rest.iad-03.braze.com/templates/email/create`
US-04 | `https://rest.iad-04.braze.com/templates/email/create`
US-06 | `https://rest.iad-06.braze.com/templates/email/create`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/create`

```json
POST https://YOUR_REST_API_URL/templates/email/create
Content-Type: application/json
{
   "api_key": (required, string) your App Group REST API Key,
   "template_name": (required, string) the name of your email template,
   "subject": (required, string) the email template subject line,
   "body": (required, string) the email template body that may include HTML,
   "plaintext_body": (optional, string) a plaintext version of the email template body,
   "preheader": (optional, string) the email preheader used to generate previews in some clients
 }
```

### Updating Email Templates

Use the endpoints below to update email templates on the Braze dashboard. You can access an email template's `email_template_id` by navigating to it on the Templates and Media page. The email template creation API endpoint will also return an `email_template_id` reference.

All fields other than the `api_key` and `email_template_id` are optional, but you must specify at least one field to update.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/update`
US-02 | `https://rest.iad-02.braze.com/templates/email/update`
US-03 | `https://rest.iad-03.braze.com/templates/email/update`
US-04 | `https://rest.iad-04.braze.com/templates/email/update`
US-06 | `https://rest.iad-06.braze.com/templates/email/update`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/update`

```json
POST https://YOUR_REST_API_URL/templates/email/update
Content-Type: application/json
{
  "api_key": (required, string) your App Group REST API Key,
  "email_template_id": (required, string) your email template's API Identifier,
  "template_name": (optional, string) the name of your email template,
  "subject": (optional, string) the email template subject line,
  "body": (optional, string) the email template body that may include HTML,
  "plaintext_body": (optional, string) a plaintext version of the email template body,
  "preheader": (optional, string) the email preheader used to generate previews in some clients
}
```

### List Email Templates Available

Use the endpoints below to get a list of available templates.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/list`
US-02 | `https://rest.iad-02.braze.com/templates/email/list`
US-03 | `https://rest.iad-03.braze.com/templates/email/list`
US-04 | `https://rest.iad-04.braze.com/templates/email/list`
US-06 | `https://rest.iad-06.braze.com/templates/email/list`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/list`

#### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `modified_after`  | No | String in ISO 8601 | Retrieve only templates updated at or after the given time. |
| `modified_before`  |  No | String in ISO 8601 | Retrieve only templates updated at or before the given time. |
| `limit` | No | Positive Number | Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. |
| `offset`  |  No | Positive Number | Number of templates to skip before returning rest of the templates that fit the search criteria. |

#### Example Request

```
https://rest.iad-01.braze.com/templates/email/list?api_key=123abc-def5-3729-owod-23f9f3j30
```

#### Successful Response Properties

```json
GET https://YOUR_REST_API_URL/templates/email/list

{
  “count”: number of templates returned
  “templates”: [template with the following properties]:
    “email_template_id”: (string) your email template's API Identifier,
    “template_name”: (string) the name of your email template,
    “created_at”: (string, in ISO 8601),
    “updated_at”: (string, in ISO 8601)
}
```

### See Email Template Information

Use the endpoints below to get information on your email templates.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/info`
US-02 | `https://rest.iad-02.braze.com/templates/email/info`
US-03 | `https://rest.iad-03.braze.com/templates/email/info`
US-04 | `https://rest.iad-04.braze.com/templates/email/info`
US-06 | `https://rest.iad-06.braze.com/templates/email/info`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/info`

#### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `email_template_id`  | Yes | String | Your email template’s API Identifier. |

#### Example Request

```
https://rest.iad-01.braze.com/templates/email/info?api_key=123abc-def5-3729-owod-23f9f3j30& email_template_id=759c2ad9-eefc-4af1-bde4-602630644935
```

#### Successful Response Properties

```json
GET https://YOUR_REST_API_URL/templates/email/info
{
  “email_template_id”: (string) your email template's API Identifier,
  “template_name”: (string) the name of your email template,
  “subject”: (string) the email template subject line,
  “preheader”: (optional, string) the email preheader used to generate previews in some clients),
  “body”: (optional, string) the email template body that may include HTML,
  “plaintext_body”: (optional, string) a plaintext version of the email template body,
  “should_inline_css”
  “tags”: (string) tag names,
  “created_at”: (string, in ISO 8601),
  “updated_at”: (string, in ISO 8601)
}
```

Images in this response will show in the "body" variable as HTML.

## Content Blocks

Use these endpoints to manage your [Email Content Blocks]({{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/content_blocks/).

### List Available Content Blocks
This endpoint will list existing Content Block information.

```json
GET https://YOUR_REST_API_URL/content_blocks/list
```

#### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `modified_after`  | No | String in ISO 8601 | Retrieve only content blocks updated at or after the given time. |
| `modified_before`  |  No | String in ISO 8601 | Retrieve only content blocks updated at or before the given time. |
| `limit` | No | Positive Number | Maximum number of content blocks to retrieve, default to 100 if not provided, maximum acceptable value is 1000. |
| `offset`  |  No | Positive Number | Number of content blocks to skip before returning rest of the templates that fit the search criteria. |

#### Successful Response Properties
```json
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": "string",
      "name": "string",
      "content_type": "html or text",
      "liquid_tag": "string",
      "created_at": "time-in-iso",
      "last_edited": "time-in-iso"
    }
  ]
}
```

#### Possible Errors
- `Modified after time is invalid.`
The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).

- `Modified before time is invalid.`
The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).

- `Modified after time must be earlier than or the same as modified before time.`

- `Content Block number limit is invalid.`
The `limit` parameter must be an integer (positive number) greater than 0.

- `Content Block number limit must be greater than 0.`
The `limit` parameter must be an integer (positive number) greater than 0.

- `Content Block number limit exceeds maximum of 1000.`
The `limit` parameter must be an integer (positive number) greater than 0.

- `Offset is invalid.`
The `offset` parameter must be an integer (positive number) greater than 0.

- `Offset must be greater than 0.`
The `offset` parameter must be an integer (positive number) greater than 0.

### See Content Block Information
This endpoint will call information for an existing Content Block.

```json
GET https://YOUR_REST_API_URL/content_blocks/info
```

#### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `content_block_id`  | Yes | String | The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier.|

#### Successful Response Properties
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
  "message": "success"
}
```

#### Possible Errors
- `Content Block ID cannot be blank.`
A Content Block has not been listed or is not encapsulated in quotes.

- `Content Block ID is invalid for this App Group.`
This Content Block does not exist or is in a different company account or app group.

- `Content Block has been deleted - content not available.`
This Content Block, though it may have existed earlier, has been deleted.

### Create Content Block

This endpoint will create a Content Block.

```json
POST https://YOUR_REST_API_URL/content_blocks/create
```

#### Request Body
```json
{
  "api_key": "YOUR_API_KEY_HERE",
  "name": "content-block-1",
  "description": "This is my content block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["",""]
}
```

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `content_block_name` | Yes | String | Must be less than 100 characters. |
| `content_block_description` | No | String | The description of the content block. Must be less than 250 characters. |
| `content` | Yes | String | HTML or text content within Content Block.
| `content_block_state` | Optional | Choose "active" or "draft". Defaults to `active` if not specified. |
| `tags` | No | Array of Strings. | Tags must already exist.

#### Successful Response Properties

```json
{
  "content_block_id": "newly-generated-block-id",
  "content_block_liquid_tag": "generated-block-tag-from-content_block_name",
  "created_at": "time-created-in-iso",
  "message": "success"
}
```

#### Possible Errors
- `Content cannot be blank.`

- `Content must be a string.`

- `Content must be smaller than 50kb.`
The content in your content block must be less than 50kb total.

- `Content contains malformed liquid.`
The liquid provided is not valid or parsable. Please try again or reach out to support.

- `Content Block cannot be referenced within itself.`

- `Content Block description cannot be blank.`

- `Content Block description must be a string.`

- `Content block description must be shorter than 250 characters.`
Your content block description must be less than 250 characters.

- `Content Block name cannot be blank.`

- `Content Block name must be a shorter than 100 characters.`

- `Content Block name can only contain alphanumeric characters.`
Content Block names can include any of the following characters: the letters (capitalized or lowercase) `A` through `Z`, the numbers `0` through `9`, dashes `-`, and underscores `_`. It cannot contain non-alphanumeric characters like emojis, `!`, `@`, `~`, `&`, and other "special" characters.

- `Content Block with this name already exists.`

- `Content Block state must be either Active or Draft.`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`
