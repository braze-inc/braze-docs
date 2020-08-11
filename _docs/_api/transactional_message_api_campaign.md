---
nav_title: API Campaigns
platform: REST APIs
page_order: 5

description: "This reference article covers how to create and configure a new Braze Transactional Message Campaign."
page_type: reference
hidden: true
tool:
  - Dashboard
  - Docs
platform:
  - APIs

alias: "/api/api_campaigns/transactional_campaigns"
---
# API Campaigns

> This reference article covers how to generate a `campaign_id` to include in your API calls for our [Transactional Message API endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) and how to configure that campaign.

## Create a New Campaign
![Select Transactional Email Campaign][1]{: style="float:right;max-width:30%;margin-left:15px;"}
Navigate to the Campaigns page in your company Braze account and click the `Create Campaign` button, then select `Transactional Email` under the Transactional section.

Now, you can move on to configuring your Transactional Campaign

## Configure Your Campaign

When launching a Transactional Campaign, Braze has simplified the campaign creation flow in order to ensure your business-critical transactional messages can reach all users. As a result, you'll see there are a few settings you may be familiar with that are not included here to ensure all users will qualify for this message and receive the message once you trigger it through our API.

- Re-eligibility settings from the Delivery page have been removed. All users will automatically be re-eligible to receive this campaign immediately.
- Target Users page has been removed and all users in your Braze instance will be eligible to receive this message when you tell us to send via an API Request
- Message Variation Distribution has been removed. Transactional Campaigns do not support a control group and will target 100% of the users
- The Conversion Event page has been removed. In order to facilitate sending as quickly as possible, Transactional Campaigns do not support Conversion Event Tracking at this time.

![Transactional Campaign Creation Flow][2]

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Compose your email or select from a template.
3. Take note of your `campaign_id`. After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Transactional Messaging Endpoint Spec]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)
4. Click `Save Campaign` and you're set to begin your API campaign!

[1]: {% image_buster /assets/img/transactional_email_campaign.png %} 
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}
