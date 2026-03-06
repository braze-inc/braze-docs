---
nav_title: Reporting
article_title: Content Card Reporting
page_order: 4
description: "This reference article provides an overview of the different Content Card reporting metrics and analytics options provided in the Braze dashboard."
channel:
  - content cards
tool:
  - Reports
  
---

# Content Card reporting

> This reference article provides an overview of the different Content Card reporting metrics and analytics options provided in the Braze dashboard.

## When sends are logged

The timing of a "Sent" event for Content Cards depends on the delivery type:

- **Scheduled delivery:** The send is logged as soon as the Content Card is created and queued for the user, regardless of whether the user has opened the app or viewed the card.
- **Action-based delivery:** The send is logged as soon as the user performs the triggering action, regardless of whether the user has viewed the card.

In both cases, the card only appears in the user's profile under **Campaigns Received** once they have actually viewed it in the app. The **Last Received Campaign** retargeting filter in segments measures against the user profile (viewed), not the backend send event.

{% alert note %}
If a user doesn't have the app installed when a Content Card is sent, they won't receive the card when they install the app later—unless the campaign is configured with a recurring schedule or is triggered by a custom event that fires after install.
{% endalert %}

{% multi_lang_include analytics/campaign_analytics.md channel="Content Card" %}
