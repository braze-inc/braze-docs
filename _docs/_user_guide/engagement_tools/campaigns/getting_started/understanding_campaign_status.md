---
nav_title: Understanding Campaign Status
article_title: Understanding Campaign Status
page_order: 2
tool: Campaigns
page_type: reference
description: "This reference article gives an overview of the various statuses a campaign can have and what they mean."
---

# Understanding campaign status

> This reference article gives an overview of the various statuses a campaign can have and what they mean.

On your Braze dashboard, your campaigns are grouped by their status. Check out the different campaign statuses and descriptions for what they mean.

## Draft
Campaigns marked as drafts are saved but not launched campaigns. Clicking on them allows you to continue editing and begin sending.

## Active
Active campaigns are in the process of sending. They can fall under one of the following behaviors:
- Scheduled to send once and has not yet begun sending
- Scheduled to send once and is currently sending (local time zone and Intelligent Timing campaigns send over the course of 24 hours)
- Scheduled to send on a recurring schedule and has at least one occurrence that hasn't finished sending

## Archived
Archivced campaigns are no longer sent and are cleared from the **All Active** tab on the Braze dashboard. These campaigns are also removed from the detailed statistics graphs on the **Overview** and **Revenue** pages.

To [archive a campaign][2], click on the gear icon to the right of the campaign, or simply check it off and select **Archive Selected**.

## Inactive
Inactive campaigns have been paused but are still editable. You can resume an inactive campaign by clicking the gear icon by the campaign's name and selecting **Resume**.

## Multivariate Testing in Progress
This status marks campaigns with [multivariate tests][1] still running. If they reach a point where a variant outperforms others with better than 95% confidence, then the variant will be marked as the "winner."

## Inactive Multivariate Test - Winner Selection Needed
This status indicates campaigns with multivariate tests that have finished running and require a Braze dashboard user to [declare a winner][3] to select which variant the remaining users will receive.

## Completed
Completed campaigns have finished sending and are not scheduled to send again in the future.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/archiving_campaigns/#archiving-campaigns
[3]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-5-pick-the-action-that-determines-the-winner
