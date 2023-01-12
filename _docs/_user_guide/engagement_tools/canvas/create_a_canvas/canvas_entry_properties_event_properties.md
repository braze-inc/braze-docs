---
nav_title: Canvas Entry Properties and Event Properties
article_title: Canvas Entry Properties and Event Properties
page_type: reference
description: "This reference article describes the differences between Canvas entry properties and event properties, and when to use each property."
tool: Canvas
page_order: 8
---

# Canvas entry properties and event properties

> This reference article covers information about `canvas_entry_properties` and `event_properties`, including when to use each property and the differences in behavior.

Though similar in name, Canvas entry properties and event properties function differently within your Canvas workflows. Properties of events or API calls that trigger a user's entry into a Canvas are known as `canvas_entry_properties`. Properties of events that occur as a user moves through a Canvas journey are known as `event_properties`. The key difference here is `canvas_entry_properties` focuses on more than just events by also accessing the properties of entry payloads in API-triggered Canvases.

{% alert important %}
For the original Canvas editor and Canvas Flow, you can't use `event_properties` in the lead Message step. Instead, you must use `canvas_entry_properties` or add an Action Paths step with the corresponding event **before** the Message step that includes `event_properties`.
{% endalert %}

Behavior can vary between workflows built with the original Canvas editor versus Canvas Flow. For example, in the original Canvas editor, you can use `event_properties` in the first full step if it's an action-based step. In Canvas Flow, full steps aren't supported, so this does not apply. 

Check out this table for a summary of differences between `canvas_entry_properties` and `event_properties`.

| | Canvas Entry Properties | Event Properties
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistence** | Can be referenced by all [Message][1] steps for the duration of a Canvas for Canvas Flow only. | - Can only be referenced once. <br> - Cannot be referenced by any subsequent Message steps. |
| **Original Canvas behavior** | - Must have persistent entry properties enabled. <br> - Can only reference `canvas_entry_properties` in the first full step of a Canvas. The Canvas must be action-based or API triggered. | - Can reference `event_properties` in any full step that uses action-based delivery in a Canvas. <br> - Cannot be used in scheduled full steps other than the first full step of an action-based Canvas. However, if a user is using a [Canvas component][2] in the original Canvas editor, the behavior follows the Canvas Flow rules for `event_properties`. |
| **Canvas Flow behavior** | Can reference `canvas_entry_properties` in any step of a Canvas. | - Can reference `event_properties` in the first Message step **after** an [Action Paths][3] step where the action taken is a custom event or purchase event. <br> - Cannot be after the Everyone Else path of the Action Paths step. <br> - Can have other non-Message Canvas components in between the Action Paths and Message steps. If one of these non-Message Canvas components is an Action Paths step, the user can go through that action path's Everyone Else path. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
For in-app message channels, `canvas_entry_properties` can only be referenced in Canvas Flow and in the original Canvas editor if you have [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) enabled in the original editor as part of the previous early access. However, `event_properties` cannot be used for in-app message channels.
{% endalert %}

## Example

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Here's an example that explains behavior for `canvas_entry_properties` and `event_properties` in Canvas Flow. Let's say we have an action-based Canvas. In this scenario, users will enter this Canvas if they perform the custom event "add item to wishlist". 

The `canvas_entry_properties` are configured in the [Entry Schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) step of creating a Canvas and will correspond to when a user enters a Canvas. These `canvas_entry_properties` can also be referenced in any Message step in Canvas Flow since Canvas Flow supports persistent entry properties. 

In this Canvas, we have a user journey that begins at an Action Paths step to determine if a user has added an item to their wishlist. From here, if the user has added an item, then they will experience a delay before receiving a message "New item in your wishlist!" from the Message step. The first Message step in a user journey will have access to the custom `event_properties` from your Action Paths step, so in this case, we're able to include `` {% raw %} {{event_properties.${property_name}}} {% endraw %}`` here in this Message step as part of our message content. 

If a user doesn't add an item to their wishlist, they go through the Everyone Else path, so the `event_properties` can't be referenced and will reflect an invalid settings error.

Note that you’ll only have access to `event_properties` if your Message step can be traced back to a non-Everyone Else path in an Action Paths step. If the Message step is connected to an Everyone Else path but can be traced back to an Action Paths step in the user journey, then you will also still have access to `event_properties`. For more information on these behaviors, check out [Message][8].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
