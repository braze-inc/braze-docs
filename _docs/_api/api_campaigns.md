---
nav_title: API Campaigns
article_title: API Campaigns
page_order: 5
description: "This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign."
page_type: reference
tool: Campaigns

---
# API campaigns

> This reference article covers how to generate a `campaign_id` to include in your API calls and how to configure that campaign.

{% alert note %}
Campaigns sent through the <a href="{{site.baseurl}}/api/endpoints/messaging/"> Messaging API</a> can have the same detailed reporting and retargeting options as campaigns created on the dashboard.
{% endalert %}

## Create a new campaign

Navigate to the **Campaigns** page in your Braze account and click **Create Campaign**, then select **API Campaigns**. Now, you can move on to configuring your API campaign.

{% alert note %}
An [API-triggered campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) is different from an API campaign.
{% endalert %}

## Configure your campaign

To configure your campaign, perform the following steps:

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Click **Add Message** and add the messages types which will be included in your API campaign. This will allow you to generate a `campaign_id` and a message variation ID, which differs for each channel you include. 
3. Optionally, You can add a conversion event to track user conversions on a specific action or campaign goal.
4. Click **Save Campaign** and you're set to begin your API campaign!

## API calls

After you save your API campaign include the following in your API request: 
- Include the generated `campaign_id` fields with your API request where noted in the [Send Messages Endpoints][2].
- Include a [message object]({{site.baseurl}}/api/objects_filters/#messaging-objects) for each platform included in the campaign. In the message object, provide the message variation ID. This will specify that statistics shoud be collected and displayed under that variant. The following message objects are supported: Android, Content Cards, email, iOS, Kindle, SMS/MMS, web push, and webhook.

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints

