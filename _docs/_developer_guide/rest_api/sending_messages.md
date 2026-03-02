---
nav_title: Send messages
article_title: Sending messages using the REST API
page_order: 1
page_type: reference
description: "This reference article covers how to send messages programmatically using the Braze REST API and an API campaign."
---

# Sending messages using the REST API

> Use the Braze REST API to send messages from your backend in real time. This lets you trigger messages programmatically while tracking performance alongside your other campaigns and Canvases in the Braze dashboard.

This approach works with any messaging channel supported by the API, including:

- WhatsApp (template messages)
- Email
- SMS/MMS
- Push notifications (Android, iOS, web)
- Content Cards
- Webhooks

For example, you can notify consumers about account activity, send order confirmations, or deliver time-sensitive alerts, all triggered from your backend.

With this approach, you can:

- Trigger messages from your backend in real time.
- Track analytics alongside all of your marketing-owned campaigns and Canvases.
- Extend the use case with additional Braze features, such as message delays, follow-up retargeting, and A/B testing.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Braze REST API key | A key with the `messages.send` permission. To create one, go to **Settings** > **API Keys**. |
| Backend service | A backend service or scripting environment capable of making HTTP POST requests to the Braze REST API. |
| Messaging channel | At least one messaging channel configured in your workspace (for example, a WhatsApp template, email template, or push notification setup). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 1: Create an API campaign

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create Campaign**, then select **API Campaign**.
3. Enter a name and description for your campaign.
4. Select **Add Messaging Channel**, then select the channels you want to include (such as WhatsApp, email, or SMS).
5. Note the **Campaign ID** and **Message Variation ID** displayed on the campaign page. You need both values when constructing your API request.

For more details on setting up API campaigns, see [API campaigns]({{site.baseurl}}/api/api_campaigns/).

## Step 2: Send a message using the API

Use the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint to send a message. Include the campaign ID, the recipients, and a messaging object for your chosen channel in the request payload.

For the full list of request parameters, see the [`/messages/send` endpoint reference]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

{% alert important %}
Each recipient referenced in `external_user_ids` must already exist in Braze. If you need to create users as part of a send, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) first, or use an [API-triggered campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) instead, which allows you to create a recipient if one doesn't already exist.
{% endalert %}

### Example: WhatsApp template message

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

For details on the WhatsApp messaging object, see [WhatsApp object]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
The `/messages/send` endpoint only supports WhatsApp templates with TEXT or IMAGE headers. If your template uses a DOCUMENT, VIDEO, or other media header type, use the [API-triggered campaign endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) or the Braze dashboard instead.
{% endalert %}

### Example: Email

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID"
    }
  }
}
```

For details on the email messaging object, see [Email object]({{site.baseurl}}/api/objects_filters/messaging/email_object/).

### Other channels

Each channel has its own messaging object. For the full list and their parameters, see [Messaging objects]({{site.baseurl}}/api/objects_filters/#messaging-objects).

## Step 3: Verify your integration

After completing the setup, verify your integration:

1. Send an API request as described in [Step 2](#step-2-send-a-message-using-the-api), using your own user ID as the recipient.
2. Confirm the message is delivered.
3. In the Braze dashboard, go to the campaign results page and confirm the send is recorded.

## Considerations

- Use Braze [personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to tailor content to individual consumers, including dynamic content and user-specific data.
- Confirm that your messaging campaigns comply with relevant regulations and include necessary opt-out options and privacy notices.
- The Braze REST API offers additional [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) for scheduling messages, triggering campaigns, and more.
