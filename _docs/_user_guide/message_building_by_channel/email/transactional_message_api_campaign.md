---
nav_title: Transactional Campaigns
article_title: Transactional Email Campaigns
page_order: 5

description: "This reference article covers how to create and configure a new Braze Transactional Email campaign."
page_type: reference
tool:
  - Campaigns
channel: email

alias: "/api/api_campaigns/transactional_campaigns"
---

# Transactional Email campaigns

> This reference article covers how to create a Transactional Email campaign in the Braze dashboard and generate a `campaign_id` to include in your API calls for our [Transactional Email API endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

Transactional Emails are emails sent to facilitate an agreed-upon transaction between you and your customers. You can create Transactional Email campaigns to send automated, non-promotional email messages, such as:

- Order confirmations
- Password resets
- Billing alerts

In short, use Transactional Emails to send business-critical notifications originating from your service for a single user where speed is of the utmost importance.

{% alert important %}
Transactional Email is only available as part of select Braze packages. Please reach out to your Braze Customer Success Manager or open a [support ticket]({{site.baseurl}}/braze_support/) for more details.
{% endalert %}

## Create a new campaign

To create a new Transaction Email campaign, navigate to the **Campaigns** page and click **Create Campaign**, then select **Transactional Email** from the dropdown.

![Select Transactional Email Campaign][1]{: style="float:right;max-width:30%;margin-left:15px;"}

Now, you can move on to configuring your Transactional Email campaign.

## Configure your campaign

The campaign creation flow for Transaction Email campaigns is simplified compared to that of a [standard email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/) to ensure your business-critical transaction email can reach all users.

As a result, you'll notice a few settings you may be familiar with from other Braze campaign types are not required when setting up this campaign type:

- The **Delivery** step has been simplified to remove scheduling options. Transactional Emails will always be triggered through Braze's REST API using the Campaign ID shown on the **Delivery** page. Additional settings you may be used to finding on this page, like re-eligibility controls and frequency capping settings, have also been removed to ensure all users are reachable for these critical transactional alerts when your service triggers a send request.
- The **Target Users** step has been removed. As Transactional Emails enroll your entire user base as eligible (including unsubscribed users) there is no need to specify filters or segments. As a result, if you have any logic to apply to who should receive this message, we recommend applying that logic before determining whether to make the API request to Braze to trigger the message to a specific user.
- The **Conversions** step has been removed. Transactional Emails do not support Conversion Event Tracking at this time.

![Transactional Campaign Creation Flow][2]

To configure your Transactional Email campaign, follow these general steps:

1. Add a descriptive name so you can find the results on your **Campaigns** page after you've sent your messages.
2. Compose your email or select from a template.
3. Take note of your `campaign_id`. After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Transactional Email Endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) article.
4. Click **Save Campaign** and you're set to begin your API campaign!

### Disallowed tags in transactional emails

The `Connected Content` and `Promotion Code` Liquid tags are currently not available within Transactional Email campaigns.

Using the `Connected Content` tag requires Braze to make an outbound API request during our sending process, which can slow down the message sending process if the external service we request is experiencing latency. Similarly, the `Promotion Code` tag requires Braze to perform additional processing to evaluate the availability of a promotion before sending, which can slow the sending process should one not be available.

As a result, we do not support including `Connected Content` or `Promotion Code` tags within any field of your Transactional Email campaign.


[1]: {% image_buster /assets/img/transactional_email_campaign.png %} 
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}
