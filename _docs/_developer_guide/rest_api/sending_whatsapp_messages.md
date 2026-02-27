---
nav_title: Send WhatsApp messages
article_title: Sending WhatsApp messages using the REST API
page_order: 1
page_type: reference
description: "This reference article walks through how to send WhatsApp template messages using the Braze REST API and an API campaign."
channel:
  - WhatsApp
---

# Sending WhatsApp messages using the REST API

> Use the Braze REST API to trigger WhatsApp template messages from your backend in real time. This approach lets you build a service that sends WhatsApp messages programmatically while tracking performance alongside your other campaigns and Canvases in the Braze dashboard.

For example, you can notify consumers when they receive a message from another user, inviting them to visit your website and check their inbox.

With this approach, you can:

- Trigger templated WhatsApp messages from your backend in real time.
- Track analytics alongside all of your marketing-owned campaigns and Canvases.
- Extend the use case with additional Braze features, such as message delays, follow-up retargeting, and A/B testing.

To send a WhatsApp message through the REST API, you need to set up an API campaign in the Braze dashboard, then use the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint to send the message.

{% alert note %}
This guide assumes you've already created a WhatsApp template message. If you haven't, see [Create WhatsApp templates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates).
{% endalert %}

## Prerequisites

To complete this guide, you need:

| Requirement | Description |
| --- | --- |
| Braze REST API key | A key with the `messages.send` permission. To create one, go to **Settings** > **API Keys**. |
| WhatsApp template | A pre-approved WhatsApp template message configured in your Braze workspace. |
| Backend service | A backend service or scripting environment capable of making HTTP POST requests to the Braze REST API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 1: Create an API campaign

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create Campaign**, then select **API Campaign**.
3. Enter a name and description for your campaign, such as "WhatsApp message notification".
4. Add relevant tags for identification and tracking.
5. Select **Add Messaging Channel**, then select **WhatsApp**.
6. Note the **Campaign ID** and **Message Variation ID** displayed on the campaign page. You'll need both values when constructing your API request.

## Step 2: Send a WhatsApp message using the API

Construct a POST request to the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint. Include the campaign ID, the recipient's external user ID, and the WhatsApp template details in the request payload.

{% alert important %}
Each recipient referenced in `external_user_ids` must already exist in Braze. API-only sends don't create new user profiles. If you need to create users as part of a send, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) first, or use an [API-triggered campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) instead.
{% endalert %}

### Example request

{% raw %}
```json
POST https://rest.iad-01.braze.com/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY

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
{% endraw %}

Replace the placeholder values with your actual IDs. For the full list of parameters supported by the WhatsApp messaging object, see [WhatsApp object]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
The `/messages/send` endpoint only supports WhatsApp templates with TEXT or IMAGE headers. If your template uses a DOCUMENT, VIDEO, or other media header type, use the [Campaigns Triggered API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) or the Braze dashboard instead.
{% endalert %}

After constructing the request, send the POST request from your backend service to the Braze REST API.

## Step 3: Verify your integration

After completing the setup, verify your integration:

1. Send an API request as outlined in [Step 2](#step-2-send-a-whatsapp-message-using-the-api), using your own user ID as the recipient.
2. Confirm the WhatsApp message is delivered to your phone.
3. In the Braze dashboard, go to the campaign results page and confirm the send is recorded.
4. Monitor results closely as you scale your campaign.

## Considerations

- Use Braze [personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to tailor WhatsApp content to individual consumers, including dynamic content and user-specific data.
- Confirm that your WhatsApp campaigns comply with relevant regulations, such as GDPR and opt-in consent requirements. Include necessary opt-out options and privacy notices. For more information, see [Opt-ins and opt-outs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/).
- The Braze REST API offers additional [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) for scheduling messages, triggering campaigns, and more.
