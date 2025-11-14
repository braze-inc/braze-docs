---
nav_title: Troubleshooting
article_title: Troubleshooting Canvases
page_order: 11
page_type: reference
description: "This page provides troubleshooting steps for Canvases."
tool: Canvas
---

# Troubleshooting Canvases

> This page helps you troubleshoot issues with your Canvases.

## Why did a user not receive a triggered Canvas step?

First, confirm that the custom event is being passed to Braze. Go to **Analytics** > **Custom Events Report**, and then select the respective custom event and date range. If the event doesn't display, confirm that it's set up correctly and that the user performed the correct action.

If the custom event displays, further troubleshoot by doing the following:

- Check the user's profile download to confirm they triggered the event and when they did it. If the event was triggered, compare the timestamp for when the event was triggered to the time the Canvas went live. The event may have been triggered before the Canvas went live.
- Review changelogs for the Canvas and any segments used in targeting to determine if the user was in the segment when their custom event was triggered. If they weren't in the segment, they wouldn't have received the Canvas step.
- Verify whether the user was entered into a control group through segmentation and consequently prevented from receiving the Canvas step.
- If there is a scheduled delay, check if the user's custom event was triggered before the delay. If the event was triggered before the delay, they wouldn't have received the Canvas step.

{% alert note %}
In-app messages can only be triggered by events sent through the SDK, not the REST API.
{% endalert %}

## Why isn't my Canvas sending as expected?

Canvases are robust and complex, and we know you dedicate time and care when creating them. So, if you find that your Canvas isn't sending the way you want it to, we recommend checking your Canvas schedule, entry audience, and entry settings, and reviewing the steps for [creating a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

### Schedule

- Is the Canvas [scheduled correctly]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types)?
- Have you selected the correct date and time?
- For [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), have users performed the specified actions since you launched the Canvas?

### Entry settings

The [entry settings]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=basics#selecting-entry-controls) are important for understanding how your Canvases are sending. Check if you have limited the number of people who will potentially enter the Canvas.

Users can also exit a Canvas if they're no longer eligible to receive messages. For example, if the Canvas only contains push notifications, and a user opts out of push after receiving the first step, then that user would drop out of the Canvas. Consider using [different Canvas steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) to add alternative user journeys.

### Segmenting your audience

Consider the following questions for your target audience:

- Have you selected the correct segment?
- How is the segment set up?
- Have you confirmed that the segment contains any users?
- Have you added any additional filters that would limit the number of users entering the Canvas?
- Do the users qualify to receive the first step of your variants? For example, if the first step of your Canvas is a push notification, but the entry audience is all push-disabled, then no users will receive messages.

## Why didn't my audience split evenly between the control group and variant group?

When creating your Canvas, you may have expected your audience to split evenly between your control group and your variant group, like in the following [use case](#use-case). Let's discuss why that is and how to fix it!

The group that a user joins depends on their settings. This can be either the control group or variant group. A user will enter a Canvas when they fit all of your criteria defined in the [Entry Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). When setting up your Canvas, you define what percentage of users will enter each variant and the control group.

If your control group is large compared to your variant group (and this is not your intent), we recommend the following:
1. Set your entry audience filter to **is Foreground Push Enabled**.
2. Set your entry audience filter for **Push Subscription Status**, **Email Subscription Status**, or both to **Opted In** or **Subscribed**.

When creating a Canvas with a control group, confirm that all users in the entry audience are able to receive messages within the Canvas (such as the Canvas contains push and email messages).

### Use case

Let's imagine the following scenario:
- A Canvas has a single variant and a control group.
- The first step of the variant is a push notification.
- 90% of users were selected to enter the variant, and 10% to enter the control group.

![Canvas example with 90% variant and 10% control group.]({% image_buster /assets/img_archive/trouble15.png %})

In this scenario, 90% of the users who enter the Canvas will enter the variant. 

If we look back to the active users, we can see that even though it contains 29.8k users, only 64% of them push enabled:

![Segment with the "Push Enabled" filter set to "true", and estimated users of 29.8k.]({% image_buster /assets/img_archive/trouble16.png %})

This means that even though we specified 90% of users to enter the variant, not all of those users are actually able to receive a push notification. These users who are unable to receive a push notification will still enter the variant regardless.