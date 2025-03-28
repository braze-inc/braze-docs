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

Draft Canvases are saved, but not launched. To continue editing, select your draft from the list.

## Active

Active Canvases are in the process of sending.

## Stopped

Stopped Canvases are paused, but are still editable. Users can no longer enter the Canvas. When stopped:

| Scenario | Details |
|----------|---------|
| **Sent Messages**| No additional messages will be sent, regardless of a user's place in the Canvas. This includes users who were queued due to rate limiting.<br><br>Note that your email service provider (ESP) may continue processing any messages you've already requested. |
| **Delay steps** | Users in a [delay step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) will stay there until the set time passes, then they'll exit the Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

To reactivate the Canvas, select the <i class="fas fa-cog"></i> gear icon, then **Resume**. When reactivated, previously-stopped messages will be sent like normal&#8212;as long as their scheduled send time hasn't already passed.

## Archived

Archived Canvases are no longer sent and are cleared from the **All Active** tab on the Braze dashboard. These Canvases are also removed from the detailed statistics graphs on the **Overview** and **Revenue** pages.

To archive a Canvas, select the <i class="fas fa-cog"></i> gear icon, then **Archive Selected**.

## Idle

When a Canvas is no longer sending messages, Braze will assign an [idle status]({{site.baseurl}}/idle_campaigns_canvases/) to these Canvases to help sort and manage your list of Canvases. With this filter, you can view which Canvases will be automatically stopped and the associated stop date.
