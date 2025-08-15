---
nav_title: Empty content card feed
article_title: Empty Content Card Feed
page_order: 0

page_type: solution
description: "This help article describes why new users may not have Content Cards in their feed, and how to resolve this issue."
channel: content cards
---

# Empty Content Card feed

When sending a Content Card campaign with scheduled delivery, the option you choose for [Card Creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#overview) can affect whether new users will have cards in their feed on their first session. If **Card Creation** is set to **At campaign launch**, users that are created after the campaign is launched won't receive the Content Card in their feed, because Braze evaluates audience membership when the campaign sends.

If you want a new user to receive cards, do one of the following:

- Create a scheduled delivery campaign and set **Card Creation** to **At first impression**. They will receive this card on their first session.
- Create an action-based delivery campaign. They will receive this card the next time they perform the selected action.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on April 17, 2023_
