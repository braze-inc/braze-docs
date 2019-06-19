---
nav_title: Empty Content Card Feed
page_order: 0
---

# New Users Do Not Have Cards in Their Feed

If brand new users, in their first session, do not have any cards in their feed you should...

- Create triggered campaigns (with no re-eligibility) that send to users on their Session start.
Or...

- After a short time (a second or two) after the user opens the session, call `requestImmediateDataFlush`, then `requestContentCardsRefresh` explicitly.
