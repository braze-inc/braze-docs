---
nav_title: Transactional email campaigns
article_title: Transactional Email Campaigns
page_order: 10

description: "This reference article covers how to create and configure a new Braze Transactional Email campaign."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Transactional Email campaigns

> Braze Transactional Emails are sent to facilitate an agreed-upon transaction between a sender and the recipient. This reference article covers how to create a transactional email campaign in the Braze dashboard and generate a `campaign_id` to include in your API calls for our [`/transactional/v1/campaigns/{campaign_id}/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
Braze Transactional Email is only available as part of select Braze packages. Reach out to your Braze customer success manager or open a [support ticket]({{site.baseurl}}/braze_support/) for more details.
{% endalert %}

The transactional email campaign type is purpose-built for sending automated, non-promotional email messages to facilitate an agreed-upon transaction between you and your customers. This includes information such as:

- Order confirmations
- Password resets
- Billing alerts
- Shipping alerts

In short, you can use transactional emails to send business-critical notifications originating from your service for a single user where speed is of the utmost importance. 

{% alert important %}
Transactional emails differ from transactional campaigns, which can be used to target your users without additional costs. Transactional campaigns, for instance, can include messages sent after a user adds an item to their cart. Check out [audience targeting options]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) for more information. 
{% endalert %}

## Step 1: Create a new campaign

To create a new transactional email campaign, create a campaign and select **Transactional Email** as your messaging channel.

![Create Campaign dropdown with the highlighted option for transactional email.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Now, you can move on to configuring your transactional email campaign.

## Step 2: Configure your campaign

The campaign creation flow for Transaction Email campaigns is simplified compared to that of a [standard email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) to ensure your business-critical transaction email can reach all users.

As a result, you'll notice several settings you may be familiar with from other Braze campaign types are not required when setting up this campaign type:

- The **Delivery** step has been simplified to remove scheduling options. Transactional emails will always be triggered through the Braze REST API using the campaign ID shown on the **Delivery** page. Additional settings, like re-eligibility controls and frequency capping settings, have also been removed to confirm that all users are reachable for these critical transactional alerts when your service triggers a send request.
- The **Target Audiences** step has been removed. As transactional emails enroll your entire user base as eligible (including unsubscribed users), there is no need to specify filters or segments. As a result, if you have any logic to apply to who should receive this message, we recommend applying that logic before determining whether to make the API request to Braze to trigger the message to a specific user.
- The **Conversions** step has been removed. Transactional emails do not support conversion event tracking at this time.

![Compose, Delivery, and Confirm workflow to create a Transactional Email campaign.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

To configure your transactional email campaign, follow these steps:

1. Add a descriptive name so you can find the results on your **Campaigns** page after you've sent your messages.
2. Compose your email or select from a template.
3. Take note of your `campaign_id`. After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Transactional Email endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) article.
4. Click **Save Campaign**, and you're set to begin your API campaign!

{% alert note %}
The one-click list-unsubscribe setting for transactional email campaigns defaults to **Use workspace default**, similar to other email campaigns. Since this is intended for transactional messaging, Braze doesn't add one-click unsubscribe. To add a one-click unsubscribe to this campaign type, [edit this setting]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) under **Sending Info**.
{% endalert %}

### Disallowed tags in transactional emails

The `Connected Content` and `Promotion Code` Liquid tags are unavailable within transactional email campaigns.

Using the `Connected Content` tag requires Braze to make an outbound API request during our sending process, which can slow down the message sending process if the external service we request is experiencing latency. Similarly, the `Promotion Code` tag requires Braze to perform additional processing to evaluate the availability of a promotion before sending, which can slow the sending process should one not be available.

As a result, we do not support including `Connected Content` or `Promotion Code` tags within any field of your transactional email campaign.


