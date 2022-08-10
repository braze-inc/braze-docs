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

Though similar in name, Canvas entry properties and event properties function differently within your Canvas workflows. Properties of events or API calls that trigger a user's entry into a Canvas are known as `canvas_entry_properties`. An example of a `canvas_entry_properties` is **EXAMPLE**. Properties of events that occur as a user moves through a Canvas journey are known as `event_properties`. The key difference here is `canvas_entry_properties` focus on properties of events that trigger a Canvas.

Note that behavior can vary across workflows built with the original Canvas editor or with Canvas Flow. For example, in the original Canvas editor, you can use `event_properties` in the first Full Step if it's an action-based step. In Canvas Flow, Full Steps aren't supported, so this does not apply. 

Check out this table for a brief summary of differences between `canvas_entry_properties` and `event_properties`.

| | Canvas Entry Properties | Event Properties
|----|----|----|
| Liquid | `canvas_entry_properties` | `event_properties` |
| Persistence | Can be referenced by all [Message][1] steps for the duration of a Canvas. | - Can only be referenced once. <br> - Cannot be referenced by any subsequent Message steps. |
| Original Canvas workflow | Can only reference `canvas_entry_properties` in the first Full Step of a Canvas. The Canvas must be action-based or API triggered. | You can reference `event_properties` in any Full Step that uses action-based delivery in a Canvas. However, if a user is using a [Canvas component][2] in the original Canvas editor, the behavior follows the Canvas Flow rules for `event_properties`. |
| Canvas Flow | Can reference `custom_entry_properties` in any step of a Canvas. | - Can reference `event_properties` in the first Message step **after** an [Action Paths][3] step where the action taken is a custom event or purchase event. <br> - Cannot be after the Everyone Else path of the Action Paths step. <br> - Can have other non-Message Canvas components in between the Action Path and Message Step. If one of these non-Message Canvas components is an Action Paths step, the user can go through that Action Paths' Everyone Else path. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Examples




[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/