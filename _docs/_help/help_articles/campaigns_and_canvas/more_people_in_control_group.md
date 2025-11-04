---
nav_title: Handling a large control group
article_title: Handling a Large Control Group
page_order: 2

page_type: solution
description: "This help article describes why your control group might be larger than expected, and walks you through steps to fix this."
tool: Canvas
---

# Handling a large control group

When creating your Canvas, you may have expected your audience to split evenly between your control group and your variant group, like in the following [example](#example). We can explain why that is and how to fix it!

The group that a user joins depends on their settings. This can be either the control group or variant group. A user will enter a Canvas when they fit all of your criteria defined in the [Entry Step]({{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas). When setting up your Canvas, you define what percentage of users will enter each variant and the control group.

If your control group is large compared to your variant group (and this is not your intent), we recommend the following:
1. Set your entry audience filter to "Is Foreground Push Enabled".
2. Set your entry audience filter to "is Opted In or Subscribed".

When creating a Canvas with a control group, ensure that all users in the Entry Audience are able to receive messages within the Canvas (such as the Canvas contains push and email messages).

## Use case

Let's imagine the following scenario:
- A Canvas has a single variant and a control group.
- The first step of the variant is a push notification.
- 90% of users were selected to enter the variant, and 10% to enter the control group.

![Canvas Example]({% image_buster /assets/img_archive/trouble15.png %})

In this scenario, 90% of the users who enter the Canvas will enter the variant. 

If we look back to the active users, we can see that even though it contains 39.8k users with only 73% of them push enabled:

![Entry Audience]({% image_buster /assets/img_archive/trouble16.png %})

This means that even though we specified 90% of users to enter the variant, not all of those users are actually able to receive a push notification. These users who are unable to receive a push notification will still enter the variant regardless.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on December 3, 2020_

