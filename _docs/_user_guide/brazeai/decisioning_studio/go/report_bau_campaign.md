---
nav_title: Report on BAU campaign
article_title: Reporting on BAU campaign
page_order: 10
description: "This article provides answers to frequently asked questions about reporting on a Business as Usual (BAU) campaign in the BrazeAI Decisioning Studio Go portal."
---

# Reporting on Business as Usual campaign

> This article provides answers to frequently asked questions about reporting on a Business as Usual (BAU) campaign in the BrazeAI Decisioning Studio™ Go portal.

## About reporting on BAU campaign

By default, the BrazeAI Decisioning Studio™ Go portal reporting will compare the BrazeAI Decisioning Studio™ Go and random control groups. In addition to comparing these two groups, you may have a Business as Usual (aka BAU) group that you'd like to compare BrazeAI Decisioning Studio™ Go's performance against. By setting up BAU reporting, you can view the performance of all three groups in a single place in the BrazeAI Decisioning Studio™ Go portal.

The primary benefit of setting up BAU reporting is the application of BrazeAI Decisioning Studio™ Go's invalid click filtering, which, when applied to all three experiment groups, allows for the most accurate and fair (or "apples to apples") click performance comparison by removing any additional noise from suspected machine clicks and clicks to the unsubscribe link.

## Requirements

Before setting up BAU reporting, first ensure that there is an apples-to-apples comparison between the BAU treatment group, the BrazeAI Decisioning Studio™ Go, and the random control group. This includes checking that:

- No recipient can belong to more than one group (for the entire duration of the experiment).
- Recipients are randomly assigned to the groups, such as no bias in the group assignments.
- Any options available to the BAU group (creative, frequency, time, incentive, or offer) are available to the BrazeAI Decisioning Studio™ Go and the random control group

Without an "apples to apples" experiment design, BAU reporting can be confusing or misleading.

After you have validated your experiment design, the following details are required to set up BAU reporting:
- One or more campaign IDs from your integrated activation platform (Braze, Salesforce Marketing Cloud, or Klaviyo) where all communications in the campaign are BAU communications
    - For Braze, campaigns and Canvases are accepted
    - For Salesforce Marketing Cloud, only Journeys are accepted
    - For Klaviyo, only Flows are accepted
- One audience ID from your integrated activation platform that tracks the recipients that are in the BAU audience each day
    - For Braze, only segments are accepted
    - For Salesforce Marketing Cloud, only data extensions are accepted
    - For Klaviyo, only segments are accepted

If you don't have an existing audience that tracks your BAU audience, you must create one.

{% alert note %}
**For Braze customers only:** Make sure your Braze Current export to BrazeAI Decisioning Studio™ Go includes data from your BAU campaigns.
{% endalert %}

## Considerations

Similar to BrazeAI Decisioning Studio™ Go more generally, BAU reporting only covers click KPIs, not conversion KPIs.

At this time, we do not support filtering to specific Canvas step IDs. Events from all Canvas steps will be included in BAU data. Note that this has the potential to invalidate comparisons against BAU if only certain Canvas steps should be included.

## Setting up a BAU campaign 

Follow the instructions in your BrazeAI Decisioning Studio™ Go portal. You must have one or more [campaign IDs and an audience ID](#what-are-the-requirements-to-use-in-portal-bau-reporting).