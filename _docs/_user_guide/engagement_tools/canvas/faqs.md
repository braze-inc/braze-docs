---
nav_title: FAQs
article_title: Canvas FAQs
page_order: 6
description: "This article provides answers to frequently asked questions about Canvas."
tool: Canvas

---

# Canvas FAQs

> This article provides answers to some frequently asked questions about Canvas.

### What happens if the audience and send time are identical for a Canvas that has one variant, but multiple branches?

We enqueue a job for each step—they run at around the same time, and one of them "wins". In practice, this may be sorted somewhat evenly, but it's likely to have at least a slight bias toward the step that was created first. 

Moreover, we can't make any guarantees about exactly what that distribution will look like. If you want to ensure an even split, add a [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/) filter to ensure it.

### What happens when you stop a Canvas?

When you stop a Canvas:

- Users will be prevented from entering the Canvas.
- No further messages will be sent out, despite where a user is in the flow.
- **Exception:** Email Canvases will not immediately stop. Once the send requests go to SendGrid, there is nothing we can do to stop them from being delivered to the user.

{% alert note %}
Stopping a Canvas won't flush users who are waiting to receive messages. If you re-enable the Canvas and users are still waiting for the message, they will receive it (unless the time they should've been sent the message has passed, then they won't receive it).
{% endalert %}

### When does an exception event trigger?

[Exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) only trigger while the user is waiting to receive the Canvas step it's associated with. If a user performs an action in advance, the exception event will not trigger.

If you want to except users who have performed a certain event in advance, use [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) instead.

### How does editing a Canvas affect users already in the Canvas?

If you edit some of the steps of a multi-step Canvas, users who were already in the audience but have not received the steps will receive the updated version of the message. Note that this will only happen if they haven't been evaulated for the step yet.

For more information on what you can or can't edit after launch, check out [Changing Your Canvas After Launch]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/change_your_canvas_after_launch/).

### How are user conversions tracked in a Canvas?

A user can only convert once per Canvas entry. 

Conversions are assigned to the most recent message received by the user for that entry. The summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message. Each subsequent step will only show conversions that happened while that was the most recent step the user received.

{% details Examples %}

#### Example 1

There is a Canvas path with 10 push notifications and the conversion event is "session start" ("Opens App"):

- User A opens the app after entering but before receiving the first message.
- User B opens the app after each push notification.

**Result:**
The summary will show two conversion while the individual steps will show a conversion of one on the first step and zero for all subsequent steps.

{% alert note %}
If quiet hours is active when the conversion event happens, the same rules apply.
{% endalert %}

#### Example 2

There is a one-step Canvas with quiet hours:

1. User enters the Canvas.
2. First step has no delay, but is within quiet hours, so the message is suppressed.
3. User performs the conversion event.

**Result:**
The user will count as converted in the overall Canvas variant, but not the step since they didn't receive the step.

{% enddetails %}
