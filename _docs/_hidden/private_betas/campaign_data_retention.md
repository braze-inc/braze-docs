---
nav_title: "Message Interaction Data Availability"
article_title: "Message Interaction Data Availability"
permalink: "/campaign_data_retention/"
hidden: true
---

# Message Interaction Data Availability

> This article covers the new Braze message data availability policy for campaign interaction data as well as the early access release of a feature related thereto. <br><br> Data stored in Braze is retained and usable for segmentation, personalization, and targeting for the lifetime of the Customer’s account. This means data such as user profile attributes, custom attributes, custom events, and purchases are stored indefinitely for active users unless removed by the Customer, for the duration of the contract.

The Braze Product team is releasing a feature that allows you to move interaction data between real-time and long-term storage. This enables access to interaction data for retargeting the moment customers need it. 

“Interaction data” refers to how a user interacts with a campaign it has received (for example, when a user opens campaign A or a user receives variant A). The main use case for interaction data is [retargeting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) users via filters based on messages they’ve received, such as “Filter by users who last received campaign A after a specific date.”

{% alert important %}
The Message Interaction Data Availability feature is currently in early access and only available for use with campaigns. Contact your customer success manager if you're interested in participating in the early access. <br><br> Message Interaction Data Availability for Canvas will be coming soon.
{% endalert %}

### When is message interaction data available?

For active campaigns, interaction data is always available in real-time.

If a campaign is “stopped”, it will be marked as “expired” after three months, unless it’s used in retargeting filters. When expired, data will be moved to long-term storage with limited availability. However, this is temporary since you can restore the data to become available by using its interaction data for retargeting. 

To restore your campaign, go to the expired campaign and click **Restore interaction data** in the banner that appears at the top of the campaign landing page. 

![][1]

[1]: {% image_buster /assets/img/restore_interaction_data.png %}


