---
nav_title: Empty Content Card Feed
page_order: 0

page_type: solution
description: "This help article describes why new users may not have Content Cards in their feed, and how to resolve this issue."
channel: content cards
no_index: true
---

# New Users Do Not Have Cards in Their Feed

You cannot send cards to users who do not exist. Therefore, by definition, new users will not have any cards in their feed on their first session.

If you want a new user to receive cards, [create a Content Cards campaign]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/#content-cards) that is triggered on session start events (with no re-eligibility, so that users only receive the campaign once). They will receive this card on their next session. 

Alternatively, you can send the card in their first session; just call `requestContentCardsRefresh` on the SDK during that session, a few seconds after calling `requestImmediateDataFlush`.
