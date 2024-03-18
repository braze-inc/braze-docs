---
nav_title: "Messaging Interaction Data"
article_title: "Messaging Interaction Data"
permalink: "/messaging_interaction_data/"
hidden: true
---

# About messaging interaction data availability

> This article covers information about campaign and Canvas interaction data and its availability.

### What is messaging interaction data?

Messaging interaction data refers to how a user interacts with a campaign or Canvas they received (for example, when a user opens campaign A or a user receives variant A). This data is used for retargeting.

{% alert important %}
Starting in early 2024, messaging interaction data will be available according to the process outlined here.
{% endalert %}

### When is messaging interaction data available?

For active campaigns and Canvases, interaction data is always available in real time.

Stopped campaigns and Canvases will have their interaction data expire after three months unless they are used in retargeting filters. After expiration, the data will be moved to long-term storage with limited availability. However, this is temporary because you can restore this data.

#### Features that use interaction data

The following features use messaging interaction data:

- Retargeting filters, including filters that retarget by tag
- **Campaigns Received** and **Canvas Messages Received** lists on the user profile
- `/users/export` endpoint
- **User Data** CSV exports on campaign and Canvas summary pages

These features will not include expired interaction data in their results. To include expired interaction data in the results for these features, restore the campaign or Canvas with expired data.

#### Features that don't use interaction data

The following features **do not** use messaging interaction data, meaning these features are unaffected by the expiration of messaging interaction data:

- Campaign and Canvas setup
- Campaign and Canvas analytics
- Analytics reports (such as Report Builder, Query Builder, and Engagement Reports)
- Currents
- Snowflake Data Share
- Segment Extensions
- Data points
- Filters for a last received or engaged with message (such as Last Clicked/Opened Any Email)

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

### When was messaging interaction data available in the past?

Previously, messaging interaction data was deleted when a campaign or Canvas had not sent messages in 25 calendar months and was not used for retargeting in any active campaigns, Canvases, or Content Cards. 

Campaigns and Canvases with previously deleted messaging interaction data cannot be used in retargeting filters for campaigns, Canvases, and segments.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
