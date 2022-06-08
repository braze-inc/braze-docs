---
nav_title: "GET: Campaign Details"
article_title: "GET: Campaign Details"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Get Campaign Details endpoint."

---
{% api %}
# Campaign details endpoint
{% apimethod get %}
/campaigns/details
{% endapimethod %}

This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the `campaign_id`. If you want to retrieve Canvas data, refer to the [Canvas Details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) endpoint.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter     | Required | Data Type | Description             |
| ------------- | -------- | --------- | ----------------------- |
| `campaign_id` | Required      | String    | See [Campaign API identifier]({{site.baseurl}}/api/identifier_types/).<br><br> The `campaign_id` for API campaigns can be found on the **Developer Console** and the **Campaign Details** page within your dashboard; or you can use the [Campaign List Endpoint](#campaign-list-endpoint).   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request 
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Responses

### Campaign details endpoint API response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) date created as ISO 8601 date,
    "updated_at" : (string) date last updated as ISO 8601 date,
    "archived": (boolean) whether this campaign is archived,
    "draft": (boolean) whether this campaign is a draft,
    "name" : (string) campaign name,
    "description" : (string) campaign description,
    "schedule_type" : (string) type of scheduling action,
    "channels" : (array) list of channels to send via,
    "first_sent" : (string) date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) date and hour of last sent as ISO 8601 date,
    "tags" : (array) tag names associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) channel type of the message (as in, "email", "ios_push", "webhook", "content_card", "in-app_message", "sms"),
            "name": (string) name of the message in the dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see the following messages section ...
        }
    },
    "conversion_behaviors": (array) conversion event behaviors assigned to the campaign, see the following conversions behavior section.
}
```

### Messages

The `messages` response will contain information about each message. The following includes example message responses for each channel:

#### Push channels

```json
{
    "channel": (string) description of the channel, such as "ios_push" or "android_push"
    "alert": (string) alert body text,
    "extras": (hash) any key-value pairs provided
}
```

#### Email channel

```json
{
    "channel": "email",
    "subject": (string) subject,
    "body": (string) HTML body,
    "from": (string) from address and display name,
    "reply_to": (string) reply-to for message, if different than "from" address,
    "title": (string) name of the email,
    "extras": (hash) any key-value pairs provided
}
```

#### In-app message channel

```json
{
    "type": (string) description of in-app message type, such as "survey",
    "data": {
        "pages": [
            {
                "header": 
                    {
                         "text":(string) display text for the header of the survey,
                    }
                "choices": [
                    {
                       "choice_id": (string) choice identifier,
                       "text": (string) display text, 
                       "custom_attribute_key": (string) custom attribute key, 
                       "custom_attribute_value": (sting) custom attribute value,
                       "deleted": (boolean) deleted from live campaign, 
                    },
                    ...
                ]
            }
        ]
    }
}
```

#### Content Card channel

```json
{
    "channel": "content_cards",
    "name": (string) name of variant,
    "extras": (hash) any key-value pairs provided; only present if at least one key-value pair has been set
}
```

#### Webhook channel

```json
{
    "channel": "webhook",
    "url": (string) URL for webhook,
    "body": (string) payload body,
    "type": (string) body content type,
    "headers": (hash) specified request headers,
    "method": (string) HTTP method (e.g., "POST" or "GET"),
}
```

#### SMS channel

```json
{
  "channel": "sms",
  "body": (string) payload body,
  "from": (string) list of numbers associated with the subscription group,
  "subscription_group_id": (string) API id of the subscription group targeted in the SMS message
}
```

#### Control messages

```json
{
    "channel": (string) description of the channel that the control is for,
    "type": "control"
}
```

### Conversion behaviors

The `conversion_behaviors` array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. The following lists example conversion event behavior responses:

#### Clicks email

```json
{
    "type": "Clicks Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Opens email

```json
{
    "type": "Opens Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Makes purchase (any purchase)

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Makes purchase (specific product)

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "product": (string) name of the product, i.e., - "Feline Body Armor"
}
```

#### Performs custom event

```json
{
    "type": "Performs Custom Event",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "custom_event_name": (string) name of the event, i.e., - "Used Feline Body Armor"
}
```

#### Upgrades app

```json
{
    "type": "Upgrades App",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e., - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

#### Uses app

```json
{
    "type": "Starts Session",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e., - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
