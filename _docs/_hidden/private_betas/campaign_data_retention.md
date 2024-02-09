---
nav_title: "Messaging Interaction Data"
article_title: "Messaging Interaction Data"
permalink: "/messaging_interaction_data/"
hidden: true
---

# About messaging interaction data availability

> This article covers information about campaign and Canvas interaction data and its availability.

Messaging interaction data refers to how a user interacts with a campaign or Canvas they received (for example, when a user opens campaign A or a user receives variant A). This data can be accessed for retargeting the moment you need it.

{% alert important %}
Starting early 2024, messaging interaction data will be available according to the process outlined here.
{% endalert %}

Campaigns that use retargeting filters that are retargeting by tag are not exempt from expiration. Retargeting filters that are retargeting by tag include:

* Received Message from Campaign or Canvas with Tag
* Clicked/Opened Campaign or Canvas With Tag
* Last Received Message from Campaign or Canvas With Tag

Filters for a last received or engaged with message don't rely on campaign-specific interaction data.

### When is messaging interaction data available?

For active campaigns and Canvases, interaction data is always available in real-time. If a campaign or Canvas is "stopped," it will be marked as "expired" after three months, unless it's used in retargeting filters. When expired, the data will be moved to long-term storage with limited availability. However, this is temporary because you can restore this data by using its interaction data for retargeting. 

To restore your messaging data, follow these steps:

1. Go to the expired campaign or Canvas.
2. At the top of the campaign or Canvas landing page, click **Restore interaction data** in the banner.

![][1]

This restoration completion can vary depending on the amount of interaction data in a campaign or Canvas. In most cases, this process can range from 5 to 15 minutes. You will receive an email after the restoration is complete. You can also restore interaction data for multiple campaigns from the **Campaigns** page by selecting the campaigns and clicking the **Restore interaction data** button.

For tags that have expired campaigns or Canvases, go to the **Campaigns** or **Canvas** page and search by the relevant tag. Then, select the campaign or Canvas and click **Restore interaction data** to restore the tag. After another three months of inactivity, these campaigns or Canvases will expire again.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
