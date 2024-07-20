---
nav_title: Exception Events 
article_title: Exception Events
page_order: 4
page_type: reference
description: "This reference article describes exception events and how they impact your Canvas components."
tool: Canvas

---

# Canvas exception events

{% alert important %}
As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This article is available for reference when setting up exception events for the original Canvas workflow. <br><br> Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It's an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

> When scheduling a component for a Canvas using the original Canvas editor, you have the option to set up an exception event. You can add an exception event to a component as long as the audience is not immediately advanced. Users who perform the exception event will not be [advanced through the step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) and will drop out of your Canvas audience.

Exception events will only trigger while a user is waiting to receive the associated Canvas component. If a user performs the same action on a previous Canvas step, the exception event will not trigger.

{% alert important %}
For Canvas Flow, exception events are only configured using [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). For example, you can define an Action Path and use the Everyone Else path as the exception.
{% endalert %}

Exception events for an action-based step will work during the step delay or window. Scheduled steps don't have a window, and as a result, the exception event will only work if it happens during the delay.

For example, if you have an exception event for "Abandoned Cart" on the third step of your Canvas, but a user abandons their cart while they are on the second step, the exception event will not trigger. In this example, the exception event will only trigger if the user abandons their cart while on the third step of your Canvas. 

![]({% image_buster /assets/img_archive/Canvas_Exception_Events.png %})


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
