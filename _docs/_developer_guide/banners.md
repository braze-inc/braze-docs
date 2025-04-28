---
page_order: 2.2
nav_title: Banners
article_title: Banners
description: "This landing page is home to all things Banners, including articles on how to create Banners, and use cases."
channel:
- Banners
---

# Banners

> With Banners, you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. Similar to [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), you can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

{% alert important %}
Banners are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## About Banners
Banners allow marketing and product teams to personalize app or website content dynamically, reflecting real-time user eligibility and behavior. They persistently display messages inline, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session.

Using a simple drag-and-drop editor, marketers can design and launch Banners without developer assistance, reducing complexity and improving efficiency.

### Use cases

Because Banners never expire and are auto-personalized every time a user starts a new session, they’re great for:

- Highlighting featured content, trending products, or promotions
- Notifying users about upcoming events or important dates
- Promoting loyalty programs and personalized offers
- Guiding users through onboarding flows and account setup
- Upselling or cross-selling complementary products

## Features

### Drag & drop editor {#drag-drop-editor}
Banners feature an intuitive drag-and-drop editor designed for marketers, allowing for quick, no-code creation of engaging, personalized in-line messages. With the editor, you can easily customize Banners by adding and arranging various content elements without developer support.

Key capabilities:
- Easy content building: Drag rows and editor blocks to structure your Banner, including images, text, buttons, email capture forms, and custom HTML.
- Real-time preview: Instantly preview your Banners across different device views, ensuring a seamless user experience on mobile and desktop.
- Flexible personalization: Utilize Braze's built-in personalization options and Liquid logic, refreshing dynamically for each user's session.
- Custom HTML support: Add custom HTML blocks when advanced customization or integration with existing web styles is required.

### Placement IDs {#placement-ids}

Banner placements are unique to each workspace and can be used across 10 campaigns within a single workspace. Additionally, placements within each workspace must be assigned a unique ID. You'll create placements and assign them IDs when you [create a Banner campaign]({{site.baseurl}}/developer_guide/banners/creating_campaigns/) or [embed Banners into your app]({{site.baseurl}}/developer_guide/banners/embedding_banners/).

{% alert important %}
Avoid modifying placement IDs after launching a Banner campaign.
{% endalert %}

### Banner priority {#card-priority}

When multiple campaigns reference the same placement ID, Banners are displayed in order of priority level. By default, newly created Banners are set to medium, but you can [manually set the priority]({{site.baseurl}}/developer_guide/banners/creating_campaigns/#set-priority) to high, medium, or low, or specify an exact priority via drag-and-drop. If multiple Banners share the same priority level, the newest Banner will be displayed first.

### Card expiration

By default, Banners don't expire, making them ideal for long-term, persistent messages. However, you have the option to set an expiration date if necessary.

### Metrics

These are the most important Banner metrics. For a full list of metrics, definitions, and calculations, refer to [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

| Metric | Definition |
| --- | --- |
| [Total Impressions]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | The number of times the message has been loaded and appears on a user’s screen, regardless of prior interaction (for example, if a user is shown a message twice, they will be counted twice). |
| [Unique Impressions]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | The total number of users who received and viewed a given message in a day. Each user is only counted once. |
| [Total Clicks]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | The total number (and percentage) of users who clicked within the delivered message, regardless of whether the same user clicks multiple times. |
| [Unique Clicks]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | The distinct number of recipients who have clicked within a message at least once and is measured by [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). Each user is only counted once. |
| [Primary Conversions]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | The number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Next steps

Now that you know about Banners, you're ready for the next steps:

- [Creating Banner campaigns]({{site.baseurl}}/developer_guide/banners/creating_campaigns/)
- [Embedding Banners into your app]({{site.baseurl}}/developer_guide/banners/embedding_banners/)
