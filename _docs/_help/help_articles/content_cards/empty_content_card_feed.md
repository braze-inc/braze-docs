---
nav_title: Empty Content Card Feed
page_order: 0
---

# New Users Do Not Have Cards in Their Feed

You cannot send cards to users who do not exist. Therefore, by definition, new users will not have any cards in their feed on their first session.

To ensure a new user receives cards, [create a Content Cards campaign]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/overview/#content-cards) that is triggered on session start events (with no re-eligibility, so that users only receive the campaign once).

They will receive this card on their next session. Alternatively, to send the card in their first session, call `requestContentCardsRefresh` on the SDK during that session, a few seconds after calling `requestImmediateDataFlush`.
