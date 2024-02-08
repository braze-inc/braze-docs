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
Starting early 2024, campaign interaction data will be available according to the process outlined here.<br><br>This process will extend to Canvas interaction data in the future.
{% endalert %}

Campaigns that use retargeting filters that are retargeting by tag are not exempt from expiration. Retargeting filters that are retargeting by tag include:

* Received Message from Campaign or Canvas with Tag
* Clicked/Opened Campaign or Canvas With Tag
* Last Received Message from Campaign or Canvas With Tag

Filters for a last received or engaged with message don't rely on campaign-specific interaction data.

### When is campaign interaction data available?

For active campaigns, interaction data is always available in real-time. If a campaign is "stopped," it will be marked as "expired" after three months, unless it's used in retargeting filters. When expired, the campaign data will be moved to long-term storage with limited availability. However, this is temporary because you can restore this data by using its interaction data for retargeting. 

To restore your campaign, follow these steps:

1. Go to the expired campaign.
2. At the top of this campaign's landing page, click **Restore interaction data** in the banner.

![][1]

This restoration completion can vary depending on the amount of interaction data in a campaign. In most cases, this process can range from 5 to 15 minutes. You will receive an email after the restoration is complete. You can also restore interaction data for multiple campaigns from the **Campaigns** page by selecting the campaigns and clicking the **Restore interaction data** button.

For tags that have expired campaigns, go to the **Campaigns** page and search by the relevant tag. Then, select the campaigns and click **Restore interaction data** to restore the tag. After another three months of inactivity, these campaigns will expire again.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
