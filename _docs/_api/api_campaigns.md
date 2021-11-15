---
nav_title: API Campaigns
article_title: API Campaigns
page_order: 5
description: "This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign."
page_type: reference
alias: /api/api_campaigns/
tool: Campaigns

---
# API campaigns

> This reference article covers how to generate a `campaign_id` to include in your API calls and how to configure that campaign.

{% alert note %}
Campaigns sent through the <a href="{{site.baseurl}}/api/endpoints/messaging/"> Messaging API</a> can have the same detailed reporting and retargeting options as campaigns created on the dashboard.
{% endalert %}

## Create a new campaign

Navigate to the **Campaigns** page in your company Braze account and click __Create Campaign__, then select __API Campaigns__. Now, you can move on to configuring your API campaign.

{% alert note %}
An [API-triggered campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) is different from an API campaign.
{% endalert %}

## Configure your campaign

To configure your campaign, perform the following steps:

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Click **Add Message** and add the messages types which will be included in your API campaign. This will create a `Message Variation ID`, which will serve as your `campaign_id`. <br><br> After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Send Messages Endpoints][2].<br><br>
3. Optionally, You can add a conversion event to track user conversions on a specific action or campaign goal.
4. Click **Save Campaign** and you're set to begin your API campaign!

![Create API Campaigns][4]

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints
[4]: {% image_buster /assets/img/createapicampaigns.gif %} "API Campaign Creation"
