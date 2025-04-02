---
page_order: 2.2
nav_title: Banner Cards
article_title: Banner Cards
description: "This landing page is home to all things Banner Cards, including articles on how to create Banner Cards, and use cases."
channel:
- Banners
---

# Banner Cards

> With Banner Cards, you can create personalized messaging for your users all while extending the reach of your other channels, such as email or push notifications. Similar to [Content Cards](/docs/user_guide/message_building_by_channel/content_cards/about), you can embed cards directly in your app or website which let's you engage with users through an experience that feels natural.

{% alert important %}
Banner Cards are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## Use cases

Because Banner Cards never expire and are auto-personalized every time a user starts a new session, they’re great for:

- Highlighting featured content
- Notifying users about upcoming events
- Sharing updates on loyalty programs

## About Banner Cards

### Card expiration

By default, Banner Cards don't expire&#8212;however, you can choose an end date if needed.

### Placement IDs {#placement-ids}

Banner Card placements are unique to each workspace and can be used across 10 campaigns within a single workspace. Additionally, placements within each workspace must be assigned a unique ID. You'll create placements and assign them IDs when you [create a Banner Card campaign]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) or [embed Banner Cards into your app]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/).

{% alert important %}
Avoid modifying placement IDs after launching a Banner Card campaign.
{% endalert %}

### Card priority {#card-priority}

When multiple campaigns reference the same placement ID, cards are displayed in order of priority level. By default, newly-created Banner Cards are set to medium, but you can [manually set the priority]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority) to high, medium, or low. If multiple cards share the same priority level, the newest card will be displayed first.

### Metrics

These are the most important Banner Card metrics. For a full list of metrics, definitions, and calculations, refer to [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

| Metric | Definition |
| --- | --- |
| [Total Impressions]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | The number of times the message has been loaded and appears on a user’s screen, regardless of prior interaction (for example, if a user is shown a message twice, they will be counted twice). |
| [Unique Impressions]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | The total number of users who received and viewed a given message in a day. Each user is only counted once. |
| [Total Clicks]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | The total number (and percentage) of users who clicked within the delivered message, regardless of whether the same user clicks multiple times. |
| [Unique Clicks]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | The distinct number of recipients who have clicked within a message at least once and is measured by [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). Each user is only counted once. |
| [Primary Conversions]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Next steps

Now that you know about Banner Cards, you're ready for the next steps:

- [Creating Banner Card campaigns]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [Embedding Banner Cards into your app]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
