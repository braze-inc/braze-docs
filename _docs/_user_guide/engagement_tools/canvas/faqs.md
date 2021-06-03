---
nav_title: FAQs
title: Canvas FAQs
page_order: 6
description: "This article provides answers to frequently asked questions about Canvas."
tool: Canvas
---

# Canvas FAQs

> This article provides answers to some frequently asked questions about Canvas.

### How are user conversions tracked in a Canvas?

A user can only convert once per Canvas entry. 

Conversions are assigned to the most recent message received by the user for that entry. The summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message.

Each subsequent step will only show conversions that happened while that was the most recent step the user received.

{% details Examples %}

**Example 1:**

There is a Canvas path with 10 push notifications and the conversion event is "session start" ("Opens App"):

- User A opens the app after entering but before receiving the first message.
- User B opens the app after each push notification.

**Result:**

The summary will show two conversion while the individual steps will show a conversion of one on the first step and zero for all subsequent steps.

{% alert note %}
If quiet hours is active when the conversion event happens, the same rules apply.
{% endalert %}

**Example 2:**

There is a one-step Canvas with quiet hours:

1. User enters the Canvas.
2. First step is "delay: none", but is within quiet hours, so the message is suppressed.
3. User performs the conversion event.

**Result:**
The user will count as converted in the overall Canvas variant, but not the step since they didn't receive the step.

{% enddetails %}
