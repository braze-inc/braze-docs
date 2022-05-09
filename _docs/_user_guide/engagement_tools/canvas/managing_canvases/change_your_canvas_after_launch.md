---
nav_title: Editing Canvases After Launch
article_title: Editing Canvases After Launch
page_order: 1
description: "This reference article covers the different aspects of a Canvas that can be changed after the initial launch."
page_type: reference
tool:
  - Canvas

---

# Editing Canvases after launch

> This reference article covers what can be changed in a Canvas after the initial launch.

## Overview

There are a number of things to know if you plan to edit or add more steps to any other step in Canvas after launching:

- Users who have not yet entered the Canvas will be eligible for newly created steps.
- Users who have already passed newly created steps will be eligible next time they re-enter if you have allowed users to re-enter the Canvas in Canvas Entry Settings.
- Users who are currently in a Canvas, but have not reached the points where new steps are added will be eligible to receive those new steps. 
- You cannot edit or delete existing connections nor can you insert a step between existing connected steps once a Canvas is launched.
- If you update the **Delay** or **Window** settings for a step, only new users entering the Canvas and users that haven't been queued for that step yet will receive the message at the updated delay.
- If a delay step is the last step in the Canvas, users who reach that step are automatically advanced out of the Canvas and won't receive any newly created steps. 

{% alert note %}
Stopping a Canvas won’t flush users who are waiting to receive messages. If you re-enable the Canvas and users are still waiting for the message, they will receive it (unless the time they should’ve been sent the message has passed, then they won’t receive it).
{% endalert %}

## Initial conditions

The following table describes what is editable and not editable after a Canvas launches.

| **Editable**                     | **Not-Editable**  |
|----------------------------------|-------------------|
| Canvas Name and Description      | Conversion Events |
| Teams and Tags                   |                   |
| Entry Type                       |                   |
| Entry Schedule                   |                   |
| Entry Controls                   |                   |
| Subscription Status              |                   |
| Rate Limiting                    |                   |
| Frequency Capping                |                   |
| Quiet Hours                      |                   |
| Target Audience                  |                   |
{: .reset-td-br-1 .reset-td-br-2}

## Canvas graph

The following table describes what aspects of a Canvas are editable and not editable after launch.

| **Editable**                                   | **Not-Editable**     |
|------------------------------------------------|----------------------|
| Stop / Resume Execution of All Canvas Steps    | Deleting Steps       |
| Insert Canvas Steps                            | Deleting Variants    |
| Add New Connections                            | Deleting Connections |
| Add New Variants                               |                      |
| Variant Distribution*                          |                      |
{: .reset-td-br-1 .reset-td-br-2}

_*Control variant distribution may only be decreased after launch._

## Individual step

The following table describes what details for individual Canvas steps are editable and not editable after launch.

| **Editable**                        | **Not-Editable**                             |
|-------------------------------------|----------------------------------------------|
| Name                                | Schedule Type (change from delay to trigger) |
| Message Content                     | Control Percentages                          |
| Step Message Platforms (add/delete) |                                              |
| Triggers                            |                                              |
| Audience                            |                                              |
| Exception Events                    |                                              |
| Delays / Windows                    |                                              |
{: .reset-td-br-1 .reset-td-br-2}

## Canvas variant percentages

In Canvas, if a variant percentage is modified, you will find that the users may be redistributed to other variants.

Initially, users are randomly assigned a particular variant before receiving a campaign for the first time. From then on, each successive time the campaign is received (or the user re-enters a Canvas variant), they will receive the same variant unless the variant percentages are modified.

If the variant percentages change, users may be redistributed to other variants. Users stay in these variants until percentages are modified again. Note that for Canvases using branching with `NOT` filters with random bucket numbers, users may not receive the same branch each time in their user journey when they re-enter the Canvas.

### Control groups

Control groups remain consistent if the variant percentage is unchanged. Users who previously received messages cannot enter the control group on a later send, nor can any user in the control group ever receive a message.

## Local send time

Local send time Canvases can be edited up to 24 hours prior to the schedules send time. This window is called is "safe zone". Note that if you intend to make changes to your Canvas that require you to make a new Canvas entirely, remember to exclude users who received the first Canvas and re-adjust the Canvas schedule times to allow for time zone sending.
