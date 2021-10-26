---
nav_title: Exception Events 
article_title: Exception Events
page_order: 4
page_type: reference
description: "This reference article describes exception events and how they impact your Canvas steps."
tool: Canvas

---

# Canvas exception events

When scheduling a step for a [Canvas][2], you have the option to set up an exception event while scheduling your canvas. You can add an exception event to a step as long as the audience is not immediately advanced. Users who perform the exception event will not be [advanced through the step][3] and will drop out of your Canvas audience.

![Canvas Exception Events][1]

Exception events will only trigger while a user is waiting to receive the Canvas step it’s associated with. If a user performs the same action on a previous Canvas step, the exception event will not trigger.

Exception events for an action-based step will work during the step delay or window. Scheduled steps don't have a window, and as a result, the exception event will only work if it happens during the delay.

For example, if you have an exception event for “Abandoned Cart” on the third step of your canvas, but a user abandons their cart while they are on the second step, the exception event will not trigger. In this example, the exception event will only trigger if the user abandons their cart while on the third step of your Canvas. 


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
