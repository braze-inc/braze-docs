---
nav_title: API campaigns
article_title: API Campaigns
page_order: 5
description: "This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign."
page_type: reference
tool: Campaigns

---
# API campaigns

> This reference article covers how to generate a `campaign_id` to include in your API calls and how to configure that campaign.

API campaigns are typically used for transactional messaging. When creating API campaigns (not [API-triggered campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)), the Braze dashboard is only used to generate a `campaign_id`, which lets you track analytics for campaign reporting. You can also generate a message variation ID, which is different for each variant in your campaign. 

You'll then send that information to your development team to use in the API request, along with:
- Campaign copy
- Audience membership
- Assets

After the campaign begins, you can view the results in the dashboard. API campaigns use the Braze [messaging APIs]({{site.baseurl}}/api/endpoints/messaging/), which have the same detailed reporting and retargeting options as campaigns created completely through the dashboard.

{% alert warning %}
Because API campaigns are typically transactional, all users are eligible for API campaigns, even those in your Global Control Group. A [one-click list-unsubscribe]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) header is not added to these sends. If you'd like to add a one-click list-unsubscribe header to all API campaigns, contact your customer success manager.
{% endalert %}

## Create a new campaign

Go to **Messaging** > **Campaigns** and select **Create Campaign**, then select **API Campaigns**. Now, you can move on to configuring your API campaign.

An [API-triggered campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) is different from an API campaign.

## Configure your campaign

To configure your campaign, perform the following steps:

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Click **Add Message** and add the messages types which will be included in your API campaign. This will allow you to generate a `campaign_id` and a message variation ID, which differs for each channel you include. 
3. Optionally, You can add a conversion event to track user conversions on a specific action or campaign goal.
4. Click **Save Campaign** and you're set to begin your API campaign!

## API calls

After you save your API campaign include the following in your API request: 
- The generated `campaign_id` fields with your API request where noted in the [Send Messages Endpoints]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints).
- A [message object]({{site.baseurl}}/api/objects_filters/#messaging-objects) for each platform included in the campaign. In the message object, provide the message variation ID. This will specify that statistics should be collected and displayed under that variant. The following message objects are supported: Android, Content Cards, email, iOS, Kindle, SMS/MMS, web push, and webhook.


