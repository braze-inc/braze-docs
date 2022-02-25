---
nav_title: Empty Content Card Feed
article_title: Empty Content Card Feed
page_order: 0

page_type: solution
description: "This help article describes why new users may not have Content Cards in their feed, and how to resolve this issue."
channel: content cards
---

# Empty Content Card feed

You cannot send cards to users who do not exist. By definition, new users will not have any cards in their feed on their first session.

If you want a new user to receive cards, create a [Content Cards campaign]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/#content-cards) that is triggered on the [`SessionStart` event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/#session-start-event) with no re-eligibility so that users only receive the campaign once. They will receive this card on their next session. 

Alternatively, you can send the card in their first session. Call [`requestContentCardsRefresh`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/refreshing_the_feed/#refreshing-content-cards) on the SDK during that session after calling `requestImmediateDataFlush`.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on June 3, 2021_