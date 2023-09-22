---
nav_title: "Message Interaction Data Availability"
article_title: "Message Interaction Data Availability"
permalink: "/campaign_data_retention/"
hidden: true
---

# Message interaction data availability

> This article covers the new Braze message data availability policy for campaign interaction data as well as the early access release of a feature related thereto. <br><br> Data stored in Braze is retained and usable for segmentation, personalization, and targeting for the lifetime of the Customer’s account. This means data such as user profile attributes, custom attributes, custom events, and purchases are stored indefinitely for active users unless removed by the Customer, for the duration of the contract.

Braze is releasing a feature that allows you to move interaction data between real-time and long-term storage. This enables access to interaction data for retargeting the moment customers need it. 

“Interaction data” refers to how a user interacts with a campaign it has received (for example, when a user opens campaign A or a user receives variant A). The main use case for interaction data is [retargeting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) users via filters based on messages they’ve received, such as “Filter by users who last received campaign A after a specific date.”

{% alert important %}
Message interaction data availability is currently in early access and only available for use with campaigns. Contact your customer success manager if you're interested in participating in the early access. <br><br> Support for message interaction data availability for use with Canvases will be coming soon.
{% endalert %}

### When is message interaction data available?

For active campaigns, interaction data is always available in real-time. If a campaign is “stopped,” it's marked as “expired” after three months, unless it’s used in retargeting filters. When expired, the campaign data will be moved to long-term storage with limited availability. 

However, this is temporary because you can restore this data by using its interaction data for retargeting. 

To restore your campaign, follow these steps:

1. Go to the expired campaign.
2. At the top of this campaign's landing page, click **Restore interaction data** in the banner.

![][1]

[1]: {% image_buster /assets/img/restore_interaction_data.png %}


