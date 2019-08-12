---
nav_title: Dispatch ID Behavior
page_order: 1
---

# Dispatch ID Behavior

> Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled".

A `dispatch_id` is the ID of the message dispatch - a unique ID for each "transmission sent from Braze. Users who are send a scheduled message get the same `dispatch_id`, while action-based or API-triggered messages will receive a unique `dispatch_id` per user.

These IDs are __per user, per Campaign/Canvas Step for triggered (action-based or API-triggered) messages__. This can result in two different users having different `dispatch_ids` for a single Campaign or Canvas Step.

## Dispatch ID Behavior in Canvas

Even through Canvas steps beyond the scheduled Entry Step are called "scheduled", they are technically triggered Campaigns, which are triggered "to send at a scheduled time" relative to when the recipient received the previous step or entered the canvas.

Thus, all Canvas steps beyond the first will have a unique `dispatch_id`.

For example, if Becky and Tom are both included in your Canvas entry step audience, then they will have the same `dispatch_id` for that step. If they both advance to the next step, they will have different `dispatch_ids` for that step, even if they advance through to the same next step.

## Dispatch ID Behavior in Campaigns

Scheduled Campaign messages get the same `dispatch_id`. Action-based or API-triggered Campaign messages will get a unique `dispatch_id` per user.

Multi-channel Campaigns will have the same behavior as described above.

For example, if Becky and Tom are both included in your scheduled Campaign audience, then they will have the same `dispatch_id`.

If they are included in the audience of an API-triggered Campaign, they will have different `dispatch_ids`.
