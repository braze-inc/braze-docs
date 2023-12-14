---
nav_title: "Campaign Interaction Data"
article_title: "Campaign Interaction Data"
permalink: "/campaign_data_retention/"
hidden: true
---

# About campaign interaction data availability

> This article covers information about campaign interaction data and its availability.

Campaign interaction data refers to how a user interacts with a campaign they received (for example, when a user opens campaign A or a user receives variant A). This data can be accessed for retargeting the moment you need it.

{% alert important %}
Campaign interaction data availability will be rolling out to customers in early 2024. <br><br> Support for Canvas interaction data will come soon after that.
{% endalert %}

Campaigns that use retargeting filters that are retargeting by tag are not exempt from expiration. Retargeting filters that are retargeting by tag include:
* Received Message from Campaign or Canvas with Tag
* Clicked/Opened Campaign or Canvas With Tag
* Last Received Message from Campaign or Canvas With Tag

### When is campaign interaction data available?

For active campaigns, interaction data is always available in real-time. If a campaign is “stopped,” it will be marked as “expired” after three months, unless it's used in retargeting filters. When expired, the campaign data will be moved to long-term storage with limited availability. 

However, this is temporary because you can restore this data by using its interaction data for retargeting. To restore your campaign, follow these steps:

1. Go to the expired campaign.
2. At the top of this campaign's landing page, click **Restore interaction data** in the banner.

![][1]

You will receive an email after the restoration is complete. You can also restore interaction data for multiple campaigns from the **Campaigns** page by selecting the campaigns and clicking the **Restore interaction data** button.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}


