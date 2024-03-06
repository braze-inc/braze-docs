---
nav_title: "Messaging Interaction Data"
article_title: "Messaging Interaction Data"
permalink: "/messaging_interaction_data/"
hidden: true
---

# About messaging interaction data availability

> This article covers information about campaign and Canvas interaction data and its availability.

### What is messaging interaction data?

Messaging interaction data refers to how a user interacts with a campaign or Canvas they received (for example, when a user opens campaign A or a user receives variant A). This data can be accessed for retargeting the moment you need it.

{% alert important %}
Starting in early 2024, messaging interaction data will be available according to the process outlined here.
{% endalert %}

Filters for a last received or engaged with message don't rely on campaign-specific interaction data. 

#### What's impacted

These following features will be affected by the expiration of interaction data:

{% alert note %}
These features can become available again if you restore the interaction data.
{% endalert %}

- User profile
    - The **Engagement** tab will not include the campaign under "Campaigns Received" or Canvas under "Canvas Messages Received"
- Retargeting filters
    - The objects will not be listed for any retargeting filter.
- Tag filters
    - Tag filters can still be used for retargeting, but will only include interaction data from objects that were not offloaded. For example:
        - Campaign A with tag "Tag1" has been offloaded
        - Campaign B with tag "Tag1" has not been offloaded
        - Segment with tag filter "Received message from Campaign or Canvas with Tag" with "Tag1" will only include users who received Campaign B
- Data exports
    - The `/users/export` endpoint will not include the object's interaction data.
    - "User Data" CSV export on object summary page can't be exported.
- The campaign or Canvas can't be launched

#### What's not impacted

The following features will **not** be affected by the expiration of interaction data:

- Campaign and Canvas setup 
- Campaign and Canvas analytics
- Last Clicked/Opened Any Email filter
- Analytics reports (such as Report Builder, Query Builder, and Engagement Reports)
- Currents
- Snowflake Data Share
- Segment Extensions
- Data points

### When is messaging interaction data available?

For active campaigns and Canvases, interaction data is always available in real time.

Stopped campaigns and Canvases will have their interaction data expire after three months unless they are used in retargeting filters. After expiration, the data will be moved to long-term storage with limited availability. However, this is temporary because you can restore this data.

### How do I restore messaging interaction data?

To restore your interaction data, follow these steps:

1. Go to the expired campaign or Canvas.
2. At the top of the campaign or Canvas landing page, click **Restore interaction data** in the banner.

![][1]

You can also restore interaction data for multiple campaigns from the Campaigns page by selecting the campaigns and clicking the Restore interaction data button.

It will vary how long the interaction data takes to restore, but in most cases, this process can range from 5 to 15 minutes. You will receive an email after the restoration is complete.

#### Restoring by tag

You can also restore interaction data for expired campaigns or Canvases with a given tag.

1. Go to the Campaigns or Canvas page and search by the relevant tag.
2. Select the desired campaigns or Canvases.
3. Click **Restore interaction data** to restore the data for those campaigns or Canvases.

After another three months of inactivity, these campaigns or Canvases will expire again.

#### Retargeting by tag

Campaigns that use retargeting filters that are retargeting by tag are not exempt from expiration. Retargeting filters that are retargeting by tag include:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
