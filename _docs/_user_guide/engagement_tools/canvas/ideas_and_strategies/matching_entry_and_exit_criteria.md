---
nav_title: Matching exit criteria to entry events
article_title: Matching Exit Criteria to Entry Events
page_order: 5
page_type: tutorial
description: "Learn how to set up exit criteria and action paths that compare event properties against Canvas entry properties, so users only exit or branch when they complete the specific action they entered with."
tool: Canvas
---

# Matching exit criteria to entry events

> This article covers how to set up exit criteria and action paths that directly correlate to the Canvas entry event, so that users only exit or branch when they perform a specific action related to why they entered the Canvas.

By comparing event properties against [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/), you can create highly targeted flows. For example, in an abandoned checkout Canvas, you can configure a user to exit only when they purchase the exact item they abandoned, while continuing to receive reminder messages if they purchase a different item.

This approach uses [context variables]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) to compare properties across events. The pattern applies to many scenarios beyond eCommerce, including policy renewals, booking reminders, and subscription management.

## Exit criteria: Exiting the Canvas when a matching action occurs

Use [exit criteria]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/) when you want a user to leave the Canvas entirely after performing an action that matches their entry event.

### Example: Abandoned ticket purchase

In this scenario, a user enters the Canvas when they perform the custom event `Selected Ticket`, which contains a property called `event_id`. The exit criteria is configured so that when a user triggers the custom event `Purchased Ticket`—which also includes a property named `event_id`—the exit event property is compared to the entry event property. If the two match, the user exits the Canvas.

This means:

- If the user purchases the same ticket they originally selected, they exit the Canvas and stop receiving reminders.
- If the user purchases a different ticket, they remain in the Canvas and continue to receive follow-up messages about the original ticket.

To set this up:

1. Set up an action-based Canvas entry with the triggering custom event (such as `Selected Ticket`) and its relevant property (such as `event_id`).
2. In the **Target Audience** step, configure the exit criteria exception event with the completing custom event (such as `Purchased Ticket`).
3. Select **Add property filters**, then add a filter where the basic property `event_id` comparison is set to `equals`.
4. Turn on the **Personalize value** toggle, set the **Personalization type** to `Context Variables`, and set the **Attribute** to `event_id`.

This compares the `event_id` from the `Purchased Ticket` event against the `event_id` stored from the original Canvas entry event. For more detail on configuring these filters, see [Exit criteria examples]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#exit-criteria-examples).

## Action paths: Branching based on a matching action

Use [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) when you want a user to remain in the Canvas but follow a different path depending on whether their subsequent action matches the entry event.

### Example: Abandoned checkout with branching paths

In this scenario, a user who selected an item but didn't complete a purchase first receives an abandoned checkout message. The user is then held in an Action Path step for one week before being sorted into three pathways based on what they did during that period:

- **Completed the original purchase:** The custom event property ID equals the entry property ID. These users might receive a thank-you message or cross-sell recommendation.
- **Made a different purchase:** The custom event property ID does not equal the entry property ID. These users might receive a reminder about the original item.
- **Didn't make a purchase:** Falls through to the **Everyone Else** group. These users might receive a stronger incentive or final reminder.

To set this up:

1. Add an [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step and set the evaluation window (such as one week).
2. For the first action group (original purchase), add a trigger for the completing custom event (such as `Purchased_Ticket`). Select **Add property filters**, then add a filter where the basic property `event_id` comparison is set to `equals`. Turn on **Personalize value**, set the **Personalization type** to `Context Variables`, and set the **Attribute** to `event_id`.
3. For the second action group (different purchase), add the same trigger event but set the comparison to `does not equal` with the same context variable configuration.
4. Use the **Everyone Else** group for users who didn't perform the completing event at all.

For more detail on configuring these filters, see [Action Path examples]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-examples).

## Other applications

While this article uses an abandoned purchase example, you can apply the same pattern to any scenario where a completing action needs to correlate with the entry action, including:

- **Policy renewals:** Exit users who renew the specific policy that triggered the Canvas.
- **Booking reminders:** Branch users based on whether they confirmed or modified their original booking.
- **Subscription management:** Route users differently depending on whether they upgraded the specific plan they were prompted about.
- **Event registrations:** Exit users who complete registration for the specific event they showed interest in.

## Things to know

- The configurations in this article are illustrative examples. Test all components in your development environment before launching.
- Verify that the property names and data types in your entry events match those used in your exit criteria or action paths.
- Review [context variables]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) for details on how property comparisons work across events.