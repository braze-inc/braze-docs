---
nav_title: Send messages
article_title: Sending messages using the REST API
page_order: 1
page_type: reference
description: "This reference article covers the two ways to send messages programmatically using the Braze REST API."
---

# Sending messages using the REST API

> You can send messages from your backend in real time using two different Braze endpoints. Each has a different request shape: one requires the full message content in the request; the other requires a campaign ID and sends content defined in the dashboard.

This approach works with any messaging channel supported by the API (WhatsApp, email, SMS, push, Content Cards, webhooks, and more).

## Two ways to send

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **Campaign ID** | Optional. Omit it to send without dashboard campaign tracking, or provide an API campaign ID plus `message_variation_id` in each message to track in the dashboard. | Required. |
| **Message content** | You must include a `messages` object in the request (for example, `messages.whats_app`, `messages.email`). | Not accepted. Message content is defined in the campaign in the Braze dashboard. |
| **Use case** | Send a message with content fully specified in the API request. | Trigger a pre-built campaign (content in the dashboard) to specific recipients via the API. |

For full request and response details, see the [Send messages immediately (API only)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) and [Send campaigns using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) endpoint references.

---

## Option 1: Send with message content in the request (`/messages/send`)

Use this endpoint when you want to specify the full message content in the API request. You **must** include a `messages` object (for example, `messages.whats_app`, `messages.email`, or `messages.sms`). You can omit `campaign_id` to send without campaign tracking, or include an API campaign ID and `message_variation_id` in each message to track sends in the dashboard (see the [endpoint reference]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) for details).

**Required:** API key with the `messages.send` permission.

{% alert important %}
Each recipient in `external_user_ids` must already exist in Braze. To create users as part of a send, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) first, or use [Option 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (API-triggered campaign) instead.
{% endalert %}

### Example: WhatsApp template message

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

For the full WhatsApp object specification, see [WhatsApp object]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
The `/messages/send` endpoint only supports WhatsApp templates with TEXT or IMAGE headers. For DOCUMENT, VIDEO, or other media header types, use the [API-triggered campaign endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) or the Braze dashboard instead.
{% endalert %}

### Example: Email

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

For other channels, see [Messaging objects]({{site.baseurl}}/api/objects_filters/#messaging-objects).

---

## Option 2: Trigger a campaign with content in the dashboard (`/campaigns/trigger/send`)

Use this endpoint when the message content is built in the Braze dashboard (API-triggered campaign). You send a **required** `campaign_id` and recipients; you do **not** send a `messages` object.

**Required:** API key with the `campaigns.trigger.send` permission.

### Step 1: Create an API-triggered campaign

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create Campaign**, then **API-Triggered Campaign** (not "API Campaign").
3. Add your message channel (WhatsApp, email, SMS, etc.) and build the message content in the dashboard.
4. Note the **Campaign ID** (and **Send ID** if you use multiple message variants). You'll use these in the API request.

For more on building API-triggered campaigns, see [API-triggered delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

### Step 2: Trigger the campaign via the API

Send a POST request to `/campaigns/trigger/send` with `campaign_id` and `recipients` (or `broadcast`/`audience`). Do not include a `messages` object—content comes from the campaign.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

For the full request body (including `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), see the [Send campaigns using API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body) endpoint reference.

---

## Verify your integration

1. Send a request using one of the options above, with your own user ID as the recipient.
2. Confirm the message is delivered.
3. If using Option 2, check the campaign in the Braze dashboard to confirm the send is recorded.

## Considerations

- Use Braze [personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to tailor content where supported.
- Ensure your messaging complies with relevant regulations and includes required opt-out options and privacy notices.
- For more endpoints (scheduling, Canvas triggers, etc.), see [Messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/).
