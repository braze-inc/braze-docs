---
nav_title: Send SMS messages
article_title: Sending SMS messages using the REST API
page_order: 2
page_type: reference
description: "This reference article walks through how to send SMS messages using the Braze REST API and an API campaign."
channel:
  - SMS
---

# Sending SMS messages using the REST API

> Use the Braze REST API to send transactional SMS messages from your backend in real time. This approach lets you build a service that sends SMS messages programmatically while tracking delivery analytics alongside your other campaigns and Canvases in the Braze dashboard.

This can be especially useful for high-volume, transactional messaging where the content is defined in your backend systems. For example, you can notify consumers when they receive a message from another user, inviting them to visit your website and check their inbox.

With this approach, you can:

- Trigger SMS messages from your backend in real time.
- Track analytics alongside all of your marketing-owned campaigns and Canvases.
- Extend the use case with additional Braze features, such as message delays, follow-up retargeting, and A/B testing.
- Optionally, switch to [API-triggered delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) to define your message templates in the Braze dashboard while still triggering sends from your backend.

To send an SMS message through the REST API, you need to set up an API campaign in the Braze dashboard, then use the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint to send the message.

## Prerequisites

To complete this guide, you need:

| Requirement | Description |
| --- | --- |
| Braze REST API key | A key with the `messages.send` permission. To create one, go to **Settings** > **API Keys**. |
| SMS subscription group | An SMS subscription group configured in your Braze workspace. |
| Backend service | A backend service or scripting environment capable of making HTTP POST requests to the Braze REST API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 1: Create an API campaign

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create Campaign**, then select **API Campaigns**.
3. Enter a name and description for your campaign, such as "SMS message notification".
4. Add relevant tags for identification and tracking.
5. Select **Add Messaging Channel**, then select **SMS**.
6. Note the **Campaign ID** and **Message Variation ID** displayed on the campaign page. You'll need both values when constructing your API request.

## Step 2: Send an SMS message using the API

Construct a POST request to the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint. Include the campaign ID, the recipient's external user ID, and the SMS content in the request payload.

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
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Replace the placeholder values with your actual IDs. The `body` field supports [Liquid personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), so you can tailor the message content to each recipient. For the full list of parameters supported by the SMS messaging object, see [SMS object]({{site.baseurl}}/api/objects_filters/messaging/sms_object/).

After constructing the request, send the POST request from your backend service to the Braze REST API.

## Step 3: Verify your integration

After completing the setup, verify your integration:

1. Send an API request as outlined in [Step 2](#step-2-send-an-sms-message-using-the-api), using your own user ID as the recipient.
2. Confirm the SMS message is delivered to your phone.
3. In the Braze dashboard, go to the campaign results page and confirm the send is recorded.
4. Monitor results closely as you scale your campaign.

## Considerations

- Confirm that your SMS campaigns comply with relevant regulations and carrier requirements. Include opt-out instructions (such as "Text STOP to opt out") in every message. For more information, see [SMS laws and regulations]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) and [Opt-in and opt-out keywords]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/).
- Use Braze [personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to tailor SMS content to individual consumers, including dynamic content and user-specific data.
- The Braze REST API offers additional [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) for scheduling messages, triggering campaigns, and more.
