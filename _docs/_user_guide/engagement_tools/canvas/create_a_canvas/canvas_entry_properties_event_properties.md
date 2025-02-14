---
nav_title: Context Properties and Event Properties
article_title: Canvas Context Properties and Event Properties
page_order: 4.2
page_type: reference
description: "This reference article describes the differences between Canvas context properties and event properties, and when to use each property."
tool: Canvas
---

# Canvas context properties and event properties

> Learn about Canvas context properties and event properties, including when to use each property and the differences in behavior. <br><br> For information about custom event properties in general, check out [Custom event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% alert important %}
Canvas context properties include Canvas entry properties. <br><br>Canvas context properties are currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How these properties work

Canvas context properties and event properties function differently within your Canvas workflows. 

- **Canvas context properties** are properties of events or API calls that trigger a user's entry into a Canvas.
- **Event properties** are properties of events that occur as a user moves through a Canvas journey are known as event properties.

The key difference here is Canvas context properties focuses on more than just events by also accessing the properties of entry payloads in API-triggered Canvases.

Note that for the lead Message step, event properties aren't supported. Instead, you can use Canvas context properties or add an Action Paths step with the corresponding event **before** the Message step that includes the event properties.

{% details Original Canvas editor details %}
As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This article is available for reference when using `canvas_entry_properties` and `event_properties`for the original Canvas workflow.
{% enddetails %}

### Summary of differences

Refer to the following table for a summary of differences between Canvas context properties and event properties.

| | Canvas context properties | Event properties
|----|----|----|
| **Persistence** | Can be referenced by all [Message][1] steps for the duration of a Canvas built using Canvas Flow. | - Can only be referenced once. <br> - Cannot be referenced by any subsequent Message steps. |
| **Original Canvas behavior** | - Can only reference `canvas_entry_properties` in the first full step of a Canvas. The Canvas must be action-based or API triggered. | - Can reference `event_properties` in any full step that uses action-based delivery in a Canvas. <br> - Cannot be used in scheduled full steps other than the first full step of an action-based Canvas. However, if a user is using a [Canvas component][2], the behavior follows the Canvas Flow rules for `event_properties`. |
| **Canvas Flow behavior** | Can reference `canvas_entry_properties` in any step of a Canvas. For post-launch behavior, refer to [Editing Canvases after launch]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | - Can reference `event_properties` in the first Message step **after** an [Action Paths][3] step where the action taken is a custom event or purchase event. <br> - Cannot be after the Everyone Else path of the Action Paths step. <br> - Can have other non-Message Canvas components in between the Action Paths and Message steps. If one of these non-Message components is an Action Paths step, the user can go through that action path's Everyone Else path. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Note that Canvas context properties are only available for reference in Liquid. To filter on the properties within the Canvas, use [event property segmentation]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) instead.
{% endalert %}

### In-app message channels

For in-app message channels, Canvas context properties can only be referenced in the Canvas editor if you have [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) turned on as part of the previous early access. However, event properties cannot be used for in-app message channels.

### Action paths

When an Action Path step contains a "Sent an SMS Inbound Message" or "Sent a WhatsApp Inbound Message" trigger, the subsequent Canvas steps can include an SMS or WhatsApp Liquid property. This mirrors how event properties work in Canvas Flow. This way you can leverage your messages to save and reference first-party data on user profiles and conversational messaging.

## Use case

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

To further understand the differences for `canvas_entry_properties` and `event_properties`, let's consider this scenario where users will enter an action-based Canvas if they perform the custom event "add item to wishlist". 

The `canvas_entry_properties` are configured in the [Entry Schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) step of creating a Canvas and will correspond to when a user enters a Canvas. These `canvas_entry_properties` can also be referenced in any Message step in Canvas Flow since Canvas Flow supports persistent entry properties. 

In this Canvas, we have a user journey that begins with an Action Paths step to determine if a user has added an item to their wishlist. From here, if the user has added an item, they will experience a delay before receiving a message "New item in your wishlist!" from the Message step. 

The first Message step in a user journey will have access to the custom `event_properties` from your Action Paths step. In this case, we're able to include ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` in this Message step as part of our message content. If a user doesn't add an item to their wishlist, they go through the Everyone Else path, meaning the `event_properties` can't be referenced and will reflect an invalid settings error.

Note that you'll only have access to `event_properties` if your Message step can be traced back to a non-Everyone Else path in an Action Paths step. If the Message step is connected to an Everyone Else path but can be traced back to an Action Paths step in the user journey, then you will also still have access to `event_properties`. For more information on these behaviors, check out [Message step][8].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
