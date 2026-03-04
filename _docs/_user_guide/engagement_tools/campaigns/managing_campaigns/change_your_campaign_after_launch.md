---
nav_title: Edit your campaign after launch
article_title: Edit Your Campaign After Launch
page_order: 1
tool: Campaigns
page_type: reference
description: "This reference article gives an overview of the result of editing certain aspects of a campaign post-launch."

---

# Edit your campaign after launch

> This article gives an overview of the result of editing certain aspects of a campaign post-launch.

## Why you should stop a campaign before editing {#risks-of-editing-live}

{% alert important %}
Braze recommends stopping a campaign before making changes, rather than editing it while it's live. Editing a live campaign without stopping it first can lead to unexpected behavior, including users receiving the message twice.
{% endalert %}

When a campaign is launched, all eligible users are enqueued to receive the message. However, a user isn't marked as having received the campaign until the message is actually delivered — not when they're enqueued. If you edit a live campaign without stopping it first, Braze re-enqueues eligible users for the updated version while the original queue is still being processed. Users who haven't yet received the original message will be in both queues, which can result in:

- Users receiving the campaign twice (the original and the updated version), even if re-eligibility is turned off
- The original version of the campaign still being delivered to users in the first queue
- Unexpected audience counts in campaign analytics

This is most likely to occur with campaigns that target a large audience and are scheduled to send immediately, since there's a large queue of users being processed at once. For action-based campaigns with gradual triggers (such as sign-up events), the risk is lower because only a small number of users are typically queued at any given time.

To safely make changes, [stop the campaign](#stopping-your-campaign) first, then either edit the stopped campaign or [duplicate it](#making-immediate-changes) with your changes.

## Stopping your campaign

To stop a campaign, open your **Campaign Details** page and select **Stop Campaign**. When a campaign is stopped:

- Messages scheduled to be sent will be canceled.
- A/B tests where the initial test has already been sent will be permanently canceled.
- Events for messages that have already been sent (for example, open clicks) will still be tracked.

To restart your campaign, select **Resume**. Your campaign will continue sending messages and A/B tests, but any missed messages will not be re-sent or re-scheduled.

## Triggered campaigns

All changes to action-based delivery campaigns and API-triggered delivery campaigns take effect immediately for go-forward sends. 

If these campaigns have been triggered but not yet sent (for example, an action-based delivery campaign with a 1-day delay is edited during the 1-day delay period), refer to the following guidance for scheduled campaigns.

### Scheduled campaigns

If you need to make changes to a campaign post-launch, take note of the following items when editing your campaign to check that your changes have the desired effects.

### Message content

Any message content changes (including titles, bodies, and images) take effect immediately on saving for all message sends going forward. It isn't possible to change the contents of messages that have already been dispatched.

### Scheduling and audience

If you edit your campaign's scheduled send time or its audience, those changes are reflected in the actual campaign immediately.

#### Considerations

If your campaign uses Intelligent Timing or local time zone delivery, edits to the scheduled send time will not be reflected if the edit is made within 24 hours of the original send time. This is because:

- **Intelligent Timing:** Braze begins calculating the optimal send time at midnight Samoa time. If this time has already passed, the message will have begun processing. For more information, refer to [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Local time zone delivery:** Editing a local time zone campaign that is scheduled less than 24 hours in advance will not alter the message's schedule. For more information, refer to the [How do I schedule a local time zone campaign?]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign).

### Send rate

When using a send rate limit, Braze "schedules" your messages in minute-granularity time slots, so if you want to change the message sending rate, adhere to the following process for making immediate changes.

## Making immediate changes

If you need changes to take effect immediately, do the following:

1. Stop the affected campaign.
2. Duplicate the campaign.
3. Make edits on the duplicate campaign.

{% alert important %}
This resets eligibility for people who already received the original campaign, so you may need to filter the duplicate campaign for people who did not receive the original.
{% endalert %}

## Saving drafts of active campaigns {#campaign-drafts}

Drafts are great for making large-scale changes to active campaigns. By creating a draft, you're able to pilot planned changes before your next launch.

{% alert note %}
A campaign can only have one draft at a time. Additionally, analytics aren't available since the drafted changes haven't been launched yet.
{% endalert %}

To create a draft, do the following:

1. Go to your active campaign.
2. Make your changes.
3. Select **Save as Draft**. Note that after creating a draft, you cannot edit the active campaign until you either launch or discard your draft.

![A draft of an active campaign with an option to view the active campaign.]({% image_buster /assets/img/campaign_draft.png %})

As you're making edits to the draft, you can also reference the active campaign in the header of the campaign draft or the footer of the campaign analytics. 

To return to an active campaign, select **Edit Draft** from the analytics view or the active campaign view.

### In-app message prioritization

In-app message priority will update immediately (before the draft launches) when you select **Set Exact Priority** and specify the priority in relation to other campaigns or Canvases.
