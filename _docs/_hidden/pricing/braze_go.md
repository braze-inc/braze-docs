---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go offers streamlined access to the Braze customer engagement platform to help your marketing teams start anywhere and go everywhere. Designed for simplicity and efficiency, Braze Go is tailored for select emerging markets.

{% alert important %}
Braze Go is not available in all markets. If you are interested in learning more about Braze Go, contact your account manager.
{% endalert %}

Braze Go offers all of the same functionality as Braze, with the focused changes to the following features: 

- You can have up to 30 active campaigns.
- You can have up to 20 active Canvases.
- The total REST API default rate limit is 50,000 per hour, per workspace.
    - For non-Braze Go usage, learn more about [REST API limits]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).
- Campaign and Canvas interaction data retention is 2 months with no restoration.
    - For non-Braze Go usage, learn more about [messaging interaction data availability]({{site.baseurl}}/messaging_interaction_data/).

{% alert note %}
Interaction data for campaigns and Canvases is different from Snowflake data and has no effect whatsoever.
{% endalert %}

- Braze-to-Braze webhooks are not supported.
- Filters related to tags are not supported, specifically the following filters:
    - Clicked or Opened Campaign or Canvas with Tag
    - Last Received Message from Campaign or Canvas with Tag
    - Received Campaign or Canvas with Tag
- Braze may also implement a data retention policy for user profile events and purchase data that removes events, purchases, or both older than 1 year that have not been performed again in 1 year. However, this data would still be available in SQL Segment Extensions for 2 years.

If any functionality above is updated, this will be reflected in this article and noted in our [release notes]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).