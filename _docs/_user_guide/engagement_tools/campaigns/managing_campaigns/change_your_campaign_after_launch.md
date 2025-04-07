---
nav_title: Editing Your Campaign After Launch
article_title: Editing Your Campaign After Launch
page_order: 1
tool: Campaigns
page_type: reference
description: "This reference article gives an overview of the result of editing certain aspects of a campaign post-launch."

---

# Editing your campaign after launch

> This article gives an overview of the result of editing certain aspects of a campaign post-launch.

## Stopping your campaign

To stop a campaign, open your **Campaign Details** page and select the **Stop Campaign** button in the bottom right of the page. When a campaign is stopped:

- Messages scheduled to be sent will be canceled.
- A/B tests where the initial test has already been sent will be permanently canceled.
- Events for messages that have already been sent (for example, open clicks) will still be tracked.
- Campaigns can be restarted by selecting **Resume**.

After resuming, this campaign will continue sending messages and A/B tests, but any missed messages will not be re-sent or re-scheduled.

## Triggered campaigns

All changes to action-based delivery campaigns and API-triggered delivery campaigns take effect immediately for go-forward sends. 

If these campaigns have been triggered but not yet sent (for example, an action-based delivery campaign with a 1-day delay is edited during the 1-day delay period), refer to the following guidance for scheduled campaigns.

### Scheduled campaigns

If you need to make changes to a campaign post-launch, take note of the following items when editing your campaign to check that your changes have the desired effects.

### Message content

Any message content changes (including titles, bodies, and images) take effect immediately on saving for all message sends going forward. It isn't possible to change the contents of messages that have already been dispatched.

### Scheduling and audience

If you edit your campaign's scheduled send time or its audience, those changes are reflected in the actual campaign immediately.

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

As you create and launch campaigns, you can also make edits to an active campaign and save it as a draft, allowing you to pilot your changes prior to another launch.

If you have a campaign that requires large-scale changes, you can create a draft for these edits.

![A draft of an active campaign with an option to view the active campaign.]({% image_buster /assets/img/campaign_draft.png %})

You can create drafts within an active campaign to build, save, and quality-check prior to launching these changes in the active campaign. These drafts don't have any analytics since the draft changes aren't launched yet. A campaign can only have one draft at a time.

To create a draft, do the following:

1. Go to your active campaign.
2. Make your changes.
3. Select the **Save as Draft** button in the campaign footer. Note that edits to the active campaign cannot be made while a draft of a campaign exists. You can update the campaign to apply changes, or discard the draft.

To reference the active campaign, select **View Active Campaign** in the footer from the analytics view or the campaign header from the draft. To return to an active campaign, select **Edit Draft** from the analytics view or the active campaign view.

### In-app message prioritization

In-app message priority will update immediately (before the draft launches) when you select **Set Exact Priority** and specify the priority in relation to other campaigns or Canvases.
