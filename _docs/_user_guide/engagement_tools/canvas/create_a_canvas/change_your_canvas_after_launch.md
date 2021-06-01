---
nav_title: Change Your Canvas After Launch
platform: Canvas
subplatform: Create a Canvas
page_order: 3
description: "This reference article covers the different aspects of a Canvas that can be changed after the initial launch."
page_type: reference
tool:
  - Canvas
  - Dashboard
---

# Changing Your Canvas After Launch

> This reference article covers the different aspects of a Canvas that can be changed after the initial launch.

## Initial Conditions

| **Editable**                         | **Not-Editable**      |
|----------------------------------|-------------------|
| Initial Condition                | Conversion Events |
| Target Audience                  |                   |
| Stop / Resume Initial Condition |                   |
| Workflow Name                    |                   |
{: .reset-td-br-1 .reset-td-br-2}

## Canvas Graph

| **Editable**                                     | **Not-Editable**         |
|------------------------------------------------|----------------------|
| Stop / Resume Execution of All Workflow Steps | Deleting Steps       |
| Insert Workflow Steps                          | Deleting Variants    |
| Add New Connections                            | Deleting Connections |
| Add New Variants                               |                      |
| Variant Distribution                           |                      |
{: .reset-td-br-1 .reset-td-br-2}

## Individual Step

| **Editable**                           | **Not-Editable**                                 |
|-------------------------------------|----------------------------------------------|
| Name                                | Schedule Type (change from delay to trigger) |
| Message Content                     | Control Percentages                          |
| Step Message Platforms (add/delete) |                                              |
| Triggers                            |                                              |
| Audience                            |                                              |
| Exception Events                    |                                              |
| Delays / Windows                    |                                              |
{: .reset-td-br-1 .reset-td-br-2}


## Making Edits Post Launch

There are a number of things to know if you plan to edit or add more steps to any other step in Canvas after launching:

- Users who have not yet entered the Canvas __will__ be eligible for newly created steps.
- Users who have already passed newly created steps __will__ be eligible next time they re-enter if you have allowed users to re-enter the Canvas in Canvas Entry Settings.
- Users who are currently in a Canvas, but have not reached the points where new steps are added __will__ be eligible to receive those new steps.
- You cannot edit or delete existing connections nor can you insert a step between existing connected steps once a Canvas is launched.
- Users already in the Canvas will fall out when a Canvas is stopped.

## Canvas Variant Percentages

In Canvas, if a variant percentage is modified, you will find that the users may be redistributed to other variants.

Initially, users are randomly assigned a particular variant before receiving a campaign for the first time. From then on, each successive time the campaign is received (or the user re-enters a canvas variant) - __they will receive the same variant unless the variant percentages are modified__. If the variant percentages change, users may be redistributed to other variants. Users stay in these variants until percentages are modified again. Control groups remain consistent if the variant percentage is unchanged. Users who previously received messages cannot enter the control group on a later send, nor can any user in the control group ever receive a message.

## Local Send Time

Local send time Canvases can be edited up to 24 hours prior to the schedules send time. This window is called is "safe zone". Please note that if you intend to make changes to your Canvas that require you to make a new Canvas entirely, please remember to exclude users who received the first Canvas and re-adjust the Canvas schedule times to allow for timezone sending. 
