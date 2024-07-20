---
nav_title: Exit Criteria 
article_title: Exit Criteria 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "This reference article covers the Exit Criteria feature for Canvas Flow."
tool: Canvas
---

# Exit criteria

> In the **Target Audience** step of the Canvas builder, you can set up exit criteria to identify which users you want to exit your Canvas. 

To add exit criteria, click the dropdown to select your exception event, then click **Add Trigger**. 

By adding [exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directly to your Canvas entry rules, you can exit users as soon as the event happens at the end of the step. This helps achieve a more targeted approach to Canvas messaging with your audience. You can also include segments and filters in the exit criteria, meaning users who match the segment or filter will exit the Canvas and will not receive any further messaging.

To target users who haven't made any purchases yet, click the dropdown to select **Make Purchase** as the exception event. Next, click **Add Trigger**. When your Canvas launches, your audience now excludes users who have made any purchases with the following Exit Criteria settings. In the following example, this exit criteria is also applied to the "Used in last day" segment for any user who has made exactly one purchase.

![Exit Criteria settings with "Makes Any Purchase" as the exception event, so if a user makes any purchase, then they will exit this Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %})

If the first step in a Canvas is a Delay step with a five-day delay, then the exit criteria will apply at the end of this step. So, if a user meets the exit criteria, they will exit at the end of the five days.

{% alert note %}
Array attributes aren’t currently supported as exit criteria on exception events.
{% endalert %}

Additional exception events include:
* Starting a session
* Performing a custom event or conversion event
* Adding an email address
* Changing custom attribute value
* Updating subscription status or subscription group status
* Interacting with a campaign
* Entering a location
* Triggering a geofence
* Sending an SMS inbound message
* Segment membership
* Adding filters

