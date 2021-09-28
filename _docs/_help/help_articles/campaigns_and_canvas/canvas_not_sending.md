---
nav_title: Why isn’t my Canvas sending?
article_title: Troubleshooting Canvas Delivery
page_order: 0

page_type: solution
description: "This help article walks you through troubleshooting delivery issues with your Canvas."
tool: Canvas
---

# My Canvas Isn't Sending

Canvases are robust and complex, and we know you dedicate time and care when creating them. So, if you find that your Canvas isn't sending the way you want it to send, we recommend that you...

* [Check Your Schedule](#schedule)
* [Check Your Segment](#segment)
* [Check Your Settings](#settings)


## Schedule

* Is the Canvas [scheduled correctly]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#scheduled-delivery)?
* Have you chosen the correct date and time?
* For [Action-Based]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#action-based-delivery), have users performed specified actions since you launched the Canvas?

## Segment

It is important to check your [Entry Audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#set-your-target-entry-audience):
* Have you chosen the correct Segment?
* How is the Segment set up?
* Have you ensured that the Segment contains any users?
* Have you added any additional filters that would limit the number of users entering the Canvas?
* Do the users _qualify_ to receive the first step of your variants? If the first step of your Canvas is a push notification, for example, but the Entry Audience are all Push Disabled, no users will receive any messages.

## Settings

The [Entry Settings]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas) are important, have you limited the number of people who will potentially enter the Canvas?

Users may also drop out of a Canvas if they are no longer eligible to receive messages. For example, if the Canvas only contained push notifications, and a user opted out of push after receiving the First Step - that user would drop out of the Canvas. Consider preempting this by using branching to add in alternative user journeys.


Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/) or review our comprehensive [Canvas documentation]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
