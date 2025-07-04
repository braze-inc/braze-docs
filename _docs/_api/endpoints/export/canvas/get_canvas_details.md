---
nav_title: "GET: Export Canvas Details"
article_title: "GET: Export Canvas Details"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export Canvas details Braze endpoint."

---
{% api %}
# Export Canvas details
{% apimethod get %}
/canvas/details
{% endapimethod %}

> Use this endpoint to export metadata about a Canvas, such as the name, time created, current status, and more.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5188873c-13a3-4aaf-a54b-9fa1daeac5f8 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `canvas.details` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Required | String | See [Canvas API Identifier]({{site.baseurl}}/api/identifier_types/) |
| `post_launch_draft_version` | Optional | Boolean | For Canvases that have a post-launch draft, setting this to `true` will show any draft changes available. Defaults to `false` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Responses

{% alert note %}
All Canvas steps have a `next_paths` field, which is an array of `{name, next_step_id}` data. For full steps and Message steps, the `next_step_ids` field will be present, but will not contain data for other Canvas Flow steps.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "created_at": (string) the date created as ISO 8601 date,
  "updated_at": (string) the date updated as ISO 8601 date,
  "name": (string) the Canvas name,
  "description": (string) the Canvas description,
  "archived": (boolean) whether this Canvas is archived,
  "draft": (boolean) whether this Canvas is a draft,
  "enabled": (boolean) whether this Canvas is active or not,
  "has_post_launch_draft": (boolean) whether this Canvas has a post-launch draft,
  "schedule_type": (string) the type of scheduling action,
  "first_entry": (string) the date of first entry as ISO 8601 date,
  "last_entry": (string) the date of last entry as ISO 8601 date,
  "channels": (array of strings) step channels used with Canvas,
  "variants": [
    {
      "name": (string) the name of variant,
      "id": (string) the API identifier of the variant,
      "first_step_ids": (array of strings) the API identifiers for first steps in variant,
      "first_step_id": (string) the API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)
    },
    ... (more variations)
  ],
  "tags": (array of strings) the tag names associated with the Canvas,
  "teams" : (array) the names of the Teams associated with the Canvas,
  "steps": [
    {
      "name": (string) the name of step,
      "type" (string) the type of Canvas component,
      "id": (string) the API identifier of the step,
      "next_step_ids": (array of strings) IDs for next steps that are full steps or Message steps,
      "next_paths": { (array of objects)
      // for Decision Splits, this property should evaluate to "Yes" or "No"
      // for Audience Path and Action Paths, this property should evaluate to the group name
      // for Experiment Paths, this property should evaluate to the path name
      // for other steps, this property should evaluate to "null"
        "name": (string) name the name of step,
        "next_step_id": (string) IDs for next steps that are full steps or Message steps,
        }
      "channels": (array of strings) the channels used in step,
      "messages": {
          "message_variation_id": (string) {  // <=This is the actual id
              "channel": (string) the channel type of the message (for example, "email"),
              // channel-specific fields for this message, see Campaign Details endpoint API Response for example message responses
          }
      }
    },
    ... (more steps)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

### Messages by channel

The following is an example response that includes Canvas messages sent through different channels (email, push, SMS, and in-app messages):

```json
{
  "message": "success",
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-10T12:00:00Z",
  "name": "Multi-Channel Engagement",
  "description": "Complete profile reminder via multiple channels",
  "archived": false,
  "draft": false,
  "enabled": true,
  "has_post_launch_draft": true,
  "schedule_type": "date",
  "first_entry": "2023-01-01T12:00:00Z",
  "last_entry": "2023-01-10T12:00:00Z",
  "channels": ["email", "push", "sms", "in_app_message"],
  "variants": [
    {
      "name": "Variant 1",
      "id": "variant_1_id",
      "first_step_ids": ["step_1"]
    }
  ],
  "tags": ["engagement", "multi-channel"],
  "teams": ["Marketing Team"],
  "steps": [
    {
      "name": "Welcome Email",
      "type": "email",
      "id": "step_1",
      "next_step_ids": ["step_2"],
      "next_paths": [
        {
          "name": "Next Step",
          "next_step_id": "step_2"
        }
      ],
      "channels": ["email"],
      "messages": {
        "message_1": {
          "channel": "email",
          "subject": "Welcome to Kitchenerie!",
          "body": "<html><body>Welcome to the Kitchenerie family, {{first_name}}!</body></html>",
          "created_at": "2023-01-01T12:00:00Z",
          "updated_at": "2023-01-01T12:00:00Z"
        }
      }
    },
    {
      "name": "Follow-Up Push Notification",
      "type": "push",
      "id": "step_2",
      "next_step_ids": ["step_3"],
      "next_paths": [
        {
          "name": "Next Step",
          "next_step_id": "step_3"
        }
      ],
      "channels": ["push"],
      "messages": {
        "message_2": {
          "channel": "push",
          "title": "Don't Forget to Complete Your Kitchenerie Profile",
          "body": "Complete your Kitchenerie profile for access to special offers and local events.",
          "created_at": "2023-01-02T12:00:00Z",
          "updated_at": "2023-01-02T12:00:00Z"
        }
      }
    },
    {
      "name": "Reminder SMS",
      "type": "sms",
      "id": "step_3",
      "next_step_ids": ["step_4"],
      "next_paths": [
        {
          "name": "Next Step",
          "next_step_id": "step_4"
        }
      ],
      "channels": ["sms"],
      "messages": {
        "message_3": {
          "channel": "sms",
          "body": "Hi {{first_name}}, remember to complete Kitchenerie your profile!",
          "created_at": "2023-01-03T12:00:00Z",
          "updated_at": "2023-01-03T12:00:00Z"
        }
      }
    },
    {
      "name": "In-App Message",
      "type": "in_app_message",
      "id": "step_4",
      "next_step_ids": [],
      "next_paths": [],
      "channels": ["in_app_message"],
      "messages": {
        "message_4": {
          "channel": "in_app_message",
          "header": "Complete Your Kitchenerie Profile",
          "body": "Complete your Kitchenerie profile to unlock access to savings and local events!",
          "created_at": "2023-01-04T12:00:00Z",
          "updated_at": "2023-01-04T12:00:00Z"
        }
      }
    }
  ],
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
