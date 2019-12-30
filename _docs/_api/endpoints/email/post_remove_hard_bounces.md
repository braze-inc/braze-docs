---
nav_title: "POST: Remove Hard Bounced Emails"
page_order: 3

layout: api_page2

page_type: reference
platform: API
channel: Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about and using the Remove Hard Bounced Email Addresses Braze endpoint."
---

{% api %}

# Remove Hard Bounces

{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingHardBouncedEmailExample {% endapiref %}
{% apiref postman %}https://brazeapis.postman.co/collections/4689407-29829c45-e619-4c12-910f-564ec8ccfda9?version=latest&workspace=e6986601-aa60-4cf9-8366-b2238ee9edd6#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Request Body

`Content-Type: application/json`

```json
{
  "api_key": "{{api_key}}",
  "email": "example@123.com"
}
```

## Parameters

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |

{% endapi %}
