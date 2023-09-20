---
nav_title: "Campaign Interaction Data Retention"
article_title: "Campaign Interaction Data Retention"
permalink: "/campaign_data_retention/"
hidden: true
---

# Campaign Interaction Data Retention

> This article covers the new Braze data retention for campaign interactions. <br><br> Data stored in Braze is retained and usable for segmentation, personalization, and targeting for the lifetime of the Customer’s account. This means data such as user profile attributes, custom attributes, custom events, and purchases are stored indefinitely for active users unless removed by the Customer, for the duration of the contract.

The Braze Messaging & Automation team is planning to provide indefinite data retention for customers who use retargeting. This new feature will allow customers to continue accessing the data they need, while also allowing Braze to move the data to a more scalable storage option. "Data" in this case refers to "interaction data", which are interactions to a campaign. For example, when a user opens a campaign A, or a user receives variant A. The main use case for interaction data is [retargeting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) users based on messages they’ve received.

{% alert important %}
Campaign Interaction Data Retention is currently in early access. Contact your account manager if you're interested in participating in the early access.
{% endalert %}

#### What is it?

Campaign interactions are data related to End Users' interactions with a campaign. They are used for retargeting filters and to determine campaign re-eligibility. 

#### When is it expired?

Campaign interaction data will expire for campaigns that have been stopped for over three months, unless they're used in retargeting.
 
#### What happens after expiration?

When your campaign has expired, you can restore it to continue using its data for retargeting. 

With this new policy, it's possible for a campaign's previous interaction data to expire if the campaign wasn't used in a retargeting filter before its expiration date. Based on [Braze Data Retention Information]({{site.baseurl}}/api/data_retention/), it's possible for a campaign's previous interaction data to be permanently deleted if the campaign was not used in a retargeting filter before its permanent deletion date. 




