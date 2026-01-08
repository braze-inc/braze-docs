---
nav_title: Context and event properties
article_title: Context and Event Properties
page_order: 4.2
page_type: reference
description: "This reference article describes the differences between context and event properties, and when to use each property."
tool: Canvas
---

# Context and event properties

> This reference article covers information about `context` and `event_properties`, including when to use each property and the differences in behavior. <br><br> For information about custom event properties in general, check out [Custom events properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Context properties and event properties function differently within your Canvas workflows. Properties of events or API calls that trigger a user's entry into a Canvas are known as `context`. Properties of events that occur as a user moves within a Canvas journey are known as `event_properties`. The key difference is `context` focuses on more than just events by also accessing the properties of entry payloads in API-triggered Canvases.

Refer to the following table for a summary of differences between context and event properties.

| | Context properties | Event properties |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistence** | Can be referenced by all [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) steps for the duration of a Canvas built using Canvas. | - Can only be referenced once. <br> - Cannot be referenced by any subsequent Message steps. |
| **Canvas behavior** | Can reference `context` in any step of a Canvas. For post-launch behavior, refer to [Editing Canvases after launch]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | - Can reference `event_properties` in the first Message step **after** an [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step where the action taken is a custom event or purchase event. <br> - Cannot be after the Everyone Else path of the Action Paths step. <br> - Can have other non-Message components in between the Action Paths and Message steps. If one of these non-Message components is an Action Paths step, the user can go through that action path's Everyone Else path. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

You can no longer create or duplicate Canvases using the original editor. Note that Canvas Context is not supported in the original Canvas editor, so this section is available for reference when using Canvas entry properties and event properties for the previous Canvas workflow.

**Canvas entry properties:**
- Must have persistent entry properties turned on. 
- Can only reference `canvas_entry_properties` in the first full step of a Canvas. The Canvas must be action-based or API triggered.

**Entry properties:**
- Can reference `event_properties` in any full step that uses action-based delivery in a Canvas.
- Cannot be used in scheduled full steps other than the first full step of an action-based Canvas. However, if a user is using a [Canvas component]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), the behavior follows the current Canvas workflow rules for `event_properties`.

**Event properties:**
- Cannot use `event_properties` in the lead Message step. Instead, you must use `canvas_entry_properties` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`.

{% enddetails %}

### Things to know

- Context is only available for reference in Liquid. To filter on the properties within the Canvas, use [event property segmentation]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) instead.
- For in-app message channels, `context` can only be referenced in a Canvas. `event_properties` can't be used for in-app message channels.
- You can't use `event_properties` in the lead Message step. Instead, you must use `context` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`. 
- When an Action Path step contains a "Sent an SMS Inbound Message" or "Sent a WhatsApp Inbound Message" trigger, the subsequent Canvas steps can include an SMS or WhatsApp Liquid property. This mirrors how event properties work in Canvases. This way you can leverage your messages to save and reference first-party data on user profiles and conversational messaging.

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Timestamps for triggers

If you're using timestamps with a [datetime type]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) from events that trigger action-based Canvases, which are referenced using [context]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties), timestamps are normalized to UTC.

Given this behavior, Braze strongly recommends you use a Liquid timezone filter like the following example to guarantee that your messages are sent with your [preferred timezone]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### Exceptions

- Timestamps are not normalized to UTC in the first step of a Canvas if that step is a Message step.
- Timestamps are not normalized to UTC in any Message step using the in-app message channel, regardless of its order in the Canvas.

## Use case

![An Action Path step followed by a Delay step and Message step for users who have added an item to their wishlist, and a path for everyone else.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

To further understand the differences for `context` and `event_properties`, let's consider this scenario where users will enter an action-based Canvas if they perform the custom event "add item to wishlist". 

Context is configured in the [Entry Schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) step of creating a Canvas and will correspond to when a user enters a Canvas. Context can also be referenced in any Message step.

In this Canvas, we have a user journey that begins with an Action Paths step to determine if a user has added an item to their wishlist. From here, if the user has added an item, they will experience a delay before receiving a message "New item in your wishlist!" from the Message step. 

The first Message step in a user journey will have access to the custom `event_properties` from your Action Paths step. In this case, we're able to include ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` in this Message step as part of our message content. If a user doesn't add an item to their wishlist, they go through the Everyone Else path, meaning the `event_properties` can't be referenced and will reflect an invalid settings error.

Note that you'll only have access to `event_properties` if your Message step can be traced back to a non-Everyone Else path in an Action Paths step. If the Message step is connected to an Everyone Else path but can be traced back to an Action Paths step in the user journey, then you will also still have access to `event_properties`. For more information on these behaviors, check out [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

