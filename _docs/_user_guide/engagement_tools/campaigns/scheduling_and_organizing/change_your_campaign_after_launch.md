---
nav_title: Changing Your Campaign After Launch
platform: Campaigns
subplatform: Scheduling and Organizing
page_order: 1.9

tool: Campaigns
page_type: reference
description: "This reference article gives an overview of the result of editing certain aspects of a campaign post-launch."
---

# Changing Triggered Campaigns After Launch

All changes to Action-Based Delivery campaigns and API-Triggered Delivery campaigns take effect immediately for go-forward sends.

If these campaigns had been triggered, but not yet sent (for example, an Action-Based Delivery campaign with a 1-day delay is edited during the 1-day delay period), please refer to the guidance for Scheduled Campaigns below.

# Changing Scheduled Campaigns After Launch

If you need to make changes to a campaign post-launch, please take note of the items below when editing your campaign to ensure your changes have the desired effects.

## Message Content

Any message content changes (including titles, bodies, images, etc.) take effect immediately on saving for all message sends going forward. It is not possible to change the contents of messages that have already been dispatched.

## Scheduling and Audience

If you edit your campaign's scheduled send time, or its audience, those changes won't be reflected in the actual campaign until __after the end of the current 24 hour period__.

## Send Rate

When using a send rate limit, Braze "schedules" your messages in minute-granularity time slots, so if you want to change the message sending rate, you should follow the process below for immediate changes. 

# What if you need your changes in place immediately?

If you need changes to take effect immediately, **stop the affected campaign**, duplicate it, and make edits on the duplicate campaign. Please note this resets eligibility for people who already received the original campaign, so you may need to filter the duplicate campaign for people who did not receive the original.
