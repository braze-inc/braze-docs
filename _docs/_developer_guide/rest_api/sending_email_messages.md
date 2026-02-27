---
nav_title: Send email messages
article_title: Sending email messages using the REST API
page_order: 3
page_type: reference
description: "This reference article walks through how to send email messages using the Braze REST API and an API campaign."
channel:
  - email
---

# Sending email messages using the REST API

> Use the Braze REST API to send transactional emails from your backend in real time. This approach lets you build a service that sends emails programmatically while tracking delivery analytics alongside your other campaigns and Canvases in the Braze dashboard.

This can be especially useful for transactional messaging where the content is defined in your backend systems. For example, you can notify consumers when they receive a message from another user, inviting them to visit your website and check their inbox.

With this approach, you can:

- Trigger emails from your backend in real time.
- Track analytics alongside all of your marketing-owned campaigns and Canvases, including opens, clicks, and bounces.
- Use message interaction data to trigger subsequent messages, such as follow-up retargeting.
- Extend the use case with additional Braze features, such as message delays and A/B testing.
- Optionally, switch to [API-triggered delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) to define your email templates in the Braze dashboard while still triggering sends from your backend.

To send an email through the REST API, you need to set up an API campaign in the Braze dashboard, then use the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint to send the message.

## Prerequisites

To complete this guide, you need:

| Requirement | Description |
| --- | --- |
| Braze REST API key | A key with the `messages.send` permission. To create one, go to **Settings** > **API Keys**. |
| Braze app ID | The identifier for your app within your workspace. To find it, go to **Settings** > **App Settings**. This value is required in the `app_id` field of the email messaging object. For more information, see [App identifier]({{site.baseurl}}/api/identifier_types/). |
| HTML email content | The HTML body of your email message, prepared in advance. |
| Backend service | A backend service or scripting environment capable of making HTTP POST requests to the Braze REST API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 1: Create an API campaign

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create Campaign**, then select **API Campaign**.
3. Enter a name and description for your campaign, such as "Email message notification".
4. Add relevant tags for identification and tracking.
5. Select **Add Messaging Channel**, then select **Email**.
6. Note the **Campaign ID** displayed on the campaign page. You'll need this value when constructing your API request. Optionally, note the **Message Variation ID** as well — include it in your request if you want to attribute send statistics to a specific message variation.

## Step 2: Send an email using the API

Construct a POST request to the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint. Include the campaign ID, the recipient's external user ID, and the email content in the request payload.

{% alert important %}
Each recipient referenced in `external_user_ids` must already exist in Braze. API-only sends don't create new user profiles. If you need to create users as part of a send, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) first, or use an [API-triggered campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) instead.
{% endalert %}

### Example request

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Replace `YOUR_REST_ENDPOINT` with the [REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints) for your workspace.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

Replace the placeholder values with your actual IDs. The `from` field must use the format `"Display Name <email@address.com>"`. The `body` field accepts valid HTML and supports [Liquid personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), so you can tailor the email content to each recipient. For the full list of parameters supported by the email messaging object, see [Email object]({{site.baseurl}}/api/objects_filters/messaging/email_object/).

After constructing the request, send the POST request from your backend service to the Braze REST API.

## Step 3: Verify your integration

After completing the setup, verify your integration:

1. Send an API request as outlined in [Step 2](#step-2-send-an-email-using-the-api), using your own user ID as the recipient.
2. Confirm the email is delivered to your inbox.
3. In the Braze dashboard, go to the campaign results page and confirm the send is recorded.
4. Monitor results closely as you scale your campaign.

## Considerations

- Confirm that your email campaigns comply with relevant regulations, such as GDPR and CAN-SPAM, by including necessary opt-out options and privacy notices. For more information, see [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) and [Email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/).
- Use Braze [personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to tailor email content to individual consumers, including dynamic content and user-specific data.
- The Braze REST API offers additional [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) for scheduling messages, triggering campaigns, and more.
