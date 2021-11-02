---
nav_title: Changing Your Campaign After Launch
article_title: Changing Your Campaign After Launch
page_order: 0
tool: Campaigns
page_type: reference
description: "This reference article gives an overview of the result of editing certain aspects of a campaign post-launch."

---

# Changing your campaign after launch

> This article gives an overview of the result of editing certain aspects of a campaign post-launch.

## Triggered campaigns

All changes to Action-Based Delivery campaigns and API-Triggered Delivery campaigns take effect immediately for go-forward sends.

If these campaigns have been triggered, but not yet sent (for example, an Action-Based Delivery campaign with a 1-day delay is edited during the 1-day delay period), please refer to the guidance for Scheduled campaigns below.

## Scheduled campaigns

If you need to make changes to a campaign post-launch, please take note of the items below when editing your campaign to ensure your changes have the desired effects.

### Message content

Any message content changes (including titles, bodies, images, etc.) take effect immediately on saving for all message sends going forward. It is not possible to change the contents of messages that have already been dispatched.

### Scheduling and audience

If you edit your campaign's scheduled send time, or its audience, those changes won't be reflected in the actual campaign until after the end of the current 24 hour period.

### Send rate

When using a send rate limit, Braze "schedules" your messages in minute-granularity time slots, so if you want to change the message sending rate, you should follow the process below for immediate changes.

## Making immediate changes

If you need changes to take effect immediately, do the following:

1. Stop the affected campaign.
2. Duplicate the campaign.
3. Make edits on the duplicate campaign.

{% alert important %}
This resets eligibility for people who already received the original campaign, so you may need to filter the duplicate campaign for people who did not receive the original.
{% endalert %}
