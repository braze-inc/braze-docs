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

Interaction data is always available. For active campaigns and Canvases, interaction data is always available in real time. 

For stopped campaigns and Canvases, their interaction data expires after three months unless it's used in retargeting filters by active campaigns or Canvases. Expired interaction data is moved to long-term storage and is not available for use unless restored using the process described below.

Expired interaction data is never deleted and can be restored at any time.

#### Features that use interaction data

The following features use messaging interaction data:

- Retargeting filters that retarget on a specific campaign or Canvas
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- Retargeting filters that retarget on campaigns or Canvases of a certain tag
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
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
- The following retargeting filters:
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email 
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

### How do I restore messaging interaction data?

To restore your interaction data, follow these steps:

1. Go to the expired campaign or Canvas.
2. At the top of the campaign or Canvas landing page, click **Restore interaction data** in the banner.

![]({% image_buster /assets/img/restore_interaction_data.png %})

You can also restore interaction data for multiple campaigns from the Campaigns page by selecting the campaigns and clicking the Restore interaction data button.

It will vary how long the interaction data takes to restore, but in most cases, this process can range from 5 to 15 minutes. You will receive an email after the restoration is complete.

#### Restoring by tag

You can also restore interaction data for expired campaigns or Canvases with a given tag.

1. Go to the **Campaigns** or **Canvas** page and search by the relevant tag.
2. Select your campaigns or Canvases.
3. Select **Restore interaction data** to restore the data for those campaigns or Canvases.

After another three months of inactivity, these campaigns or Canvases will expire again.

#### Retargeting by tag

Campaigns that use retargeting filters that are retargeting by tag are not exempt from expiration. Retargeting filters that are retargeting by tag include:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

### When was messaging interaction data available in the past?

Previously, message interaction data was deleted when a campaign or Canvas:
- Had not sent messages in 25 calendar months, AND
- Was not used for retargeting in any active campaigns, Canvases, or Content Cards.

Campaigns and Canvases with previously deleted messaging interaction data cannot be used in retargeting filters for campaigns, Canvases, and segments.

