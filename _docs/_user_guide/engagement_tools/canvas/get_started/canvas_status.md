---
nav_title: Understanding Canvas Status
article_title: Understanding Canvas Status
page_order: 2
page_type: reference
description: "This reference article gives an overview of the various statuses a Canvas can have and what they mean."
tool: Canvas

---

# Understanding Canvas status

> On your Braze dashboard, your Canvases are grouped by their status. Check out the different Canvas statuses and descriptions for what they mean.

## Draft

Canvases marked as drafts are saved but not launched Canvases. To continue editing and begin sending the Canvas, select the draft.

## Active

Active Canvases are in the process of sending.

## Stopped

Stopped Canvases have been paused, but are still editable. To resume a stopped Canvas, select the <i class="fas fa-cog"></i> gear icon for a given Canvas then **Resume**.

### Behavior when active Canvases are stopped

When an active Canvas is stopped, users will be prevented from entering the Canvas.

#### Sent messages

No further messages will be sent to already entered users, regardless where a user currently sits in the flow. However, sends may not immediately stop; once a send request is sent to an email service provider (ESP), the message can't be stopped from being delivered. 

Additionally, users who are queued because of rate limiting won't be sent queued messages.

#### Delay steps

Users in delay steps will remain in the step until the time period passes, then will exit the Canvas. If there are no delay steps between the user and the last Canvas step, the user will exit the canvas.

### Behavior when stopped Canvases are reactivated

If you reactivate a stopped Canvas, users who were waiting for a message to deliver will receive the message. But if you reactivate that Canvas after the time the user would have been sent the message, the user won't receive the message.

## Archived

Archived Canvases are no longer sent and are cleared from the **All Active** tab on the Braze dashboard. These Canvases are also removed from the detailed statistics graphs on the **Overview** and **Revenue** pages.

To archive a Canvas, select the <i class="fas fa-cog"></i> gear icon for a given Canvas then **Archive Selected**.

## Idle

When a Canvas is no longer sending messages, Braze will assign an [idle status]({{site.baseurl}}/idle_campaigns_canvases/) to these Canvases to help sort and manage your list of Canvases. With this filter, you can view which Canvases will be automatically stopped and the associated stop date.
