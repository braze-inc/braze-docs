---
nav_title: Statuses
article_title: Campaign and Canvas statuses
page_order: 1
description: "Learn about statuses for campaigns and Canvases and how to use them in the dashboard."
tool:
    - Campaigns
    - Canvas
---

# Campaign and Canvas statuses

> Learn about statuses for campaigns and Canvases and how you can use them in the dashboard.

## Filtering by status

To filter your campaigns or Canvases by status, select **All Statuses**, then choose a status.

![The 'All Statuses' dropdown in the Braze dashboard.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Changing the status

To change the status of a campaign or Canvas, select the <i class="fas fa-ellipsis-vertical"></i> menu, then choose a status.

![A list of Canvases in the Braze dashboard, with the menu open for one of the Canvases.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Available statuses

These are the available statuses for campaigns and Canvases:

| Status | Description |
| --- | --- |
| Active | Active campaigns and Canvases are in the process of sending. By default, you'll see active campaigns and Canvases on the respective pages. |
| Draft | Drafts of campaigns and Canvases are saved but not launched. To continue editing and begin sending, you can select the draft by going to **Messaging** in the Braze dashboard and selecting **Canvas** or **Campaigns**. |
| Archived | Archived campaigns and Canvases are messages that are no longer being sent. These campaigns and Canvases are also removed from the statistic graphs on the [**Home**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) and [**Revenue**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) pages.|
| Stopped | Stopped campaigns and Canvases are paused, but you can still edit them. To resume a Canvas, go to the **Summary** step of the Canvas builder and select **Resume Canvas**. For campaigns, select the <i class="fas fa-ellipsis-vertical"></i> menu, then **Resume**. For more information, refer to [Stopped Canvas behavior](#stopped-canvas-behavior). |
| Idle | When a campaign or Canvas is no longer sending messages, Braze will assign it an idle status to help sort and manage your list of campaigns and Canvases. You can view which campaigns or Canvases will be automatically stopped and the associated stop date. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Stopped Canvas behavior {#stopped-canvas-behavior}

When a Canvas is stopped, the following occurs:

- **Scheduled messages:** Your scheduled messages won't be sent, regardless of a user's place in the Canvas. This also includes users who were queued because of rate limiting.
- **Email sends:** Email sends may not stop immediately, as your email service provider (ESP) may continue processing your existing requests.
- **Delay steps:** Users in a [delay step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) will remain there as normal, but will exit the Canvas when the set period ends.
- **Draft changes:** Any draft changes to the Canvas will be discarded when the Canvas is stopped.

To resume the Canvas, go to the **Summary** step of the Canvas builder and select **Resume Canvas**. When reactivated, any previously-stopped messages will be sent as scheduled&#8212;as long as the scheduled time hasn't already passed.

## Best practices

### Monitor your messages by status

You can monitor your messages by status to review the performance details. For example, if you have a series of active campaigns, you can evaluate the performance of each campaign with their engagement metrics and make adjustments as needed. If instead you have a few stopped Canvases, you can consider whether they should be resumed for messaging or archived entirely.

{% alert tip %}
Looking for more ways to stay organized? Add [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) to provide more context at-a-glance.
{% endalert %}

### Audit your active messages

By performing audits of your active campaigns and Canvases, you can assess the relevance and performance, and remove or update any outdated campaigns and Canvases to keep your messaging fresh.
