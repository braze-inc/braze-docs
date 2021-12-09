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

On your Braze dashboard, your campaigns are grouped by their status. Below are the different statuses your campaigns could have and descriptions on what they mean:

- __Draft__
    - Campaigns that are saved but not launched. Clicking on them allows you to continue editing and begin sending.


- __Active__
    - Campaigns that are in the process of sending and fall under one of the following behaviors:
        - Scheduled to send once and has not yet begun sending
        - Scheduled to send once and is currently sending (local time zone and Intelligent Timing campaigns send over the course of 24 hours)
        - Scheduled to send on a recurring schedule and has at least one occurrence that hasn't finished sending


- __Archived__
    - Campaigns that are no longer sending and are cleared from the "All Active" tab on the Dashboard, as well as the Detailed Statics graphs on the **Overview** and **Revenue** pages.
    - To [archive campaigns][2] click on the gear icon to the right of the campaign, or simply check it off and select **Archive Selected**.
    - You cannot edit an archived campaign, and would therefore need to unarchive it to do so.


- __Inactive__
    - Campaigns that have been paused but are still rendered editable. You can resume an inactive campaign by clicking the gear icon by the campaign's name and selecting **Resume**.


- __Multivariate Testing in Progress__
    - Campaigns with [multivariate tests][1] still running. Should they reach a point where a variant outperforms others with better than 95% confidence, the variant will be marked as the "winner."


- __Inactive Multivariate Test - Winner Selection Needed__
    - Campaigns with multivariate tests that have finished running and are in need of a Dashboard user to declare a winner to inform which variant the remaining users will receive.


- __Completed__
    - Campaigns that have finished sending and are not scheduled to send again in the future.



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/archiving_campaigns/#archiving-campaigns
