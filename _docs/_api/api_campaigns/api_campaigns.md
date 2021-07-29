---
nav_title: API Campaigns
platform: REST APIs
page_order: 5

description: "This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign."
page_type: reference
tool:
  - Dashboard
  - Docs
platform:
  - APIs

alias: /api/api_campaigns/
---
# API Campaigns

> This reference article covers how to generate a `campaign_id` to include in your API calls and how to configure that campaign.

{% alert note %}
Campaigns sent through the <a href="{{site.baseurl}}/api/endpoints/messaging/"> Messaging API </a>can have the same detailed reporting and retargeting options as campaigns created on the dashboard.
{% endalert %}

## Create a New Campaign
Navigate to the **Campaigns** page in your company Braze account and click __Create Campaign__, then select __API Campaigns__.

Now, you can move on to configuring your API campaign.

## Configure Your Campaign

![Create API Campaigns][4]

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Click the __Add Message__ button and add the messages types which will be included in your API campaign. This will create a `Message Variation ID`, which will serve as your `campaign_id`. <br> _After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Messaging API - Send Endpoint Spec][2]._
3. You can, optionally, add a conversion event to track user conversions on a specific action or campaign goal.
4. Click __Save Campaign__ and you're set to begin your API campaign!

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints
[3]: {% image_buster /assets/img/selectapicampaigns.png %} "Select API Campaigns"
[4]: {% image_buster /assets/img/createapicampaigns.gif %} "API Campaign Creation"
