---
nav_title: Exit Criteria 
article_title: Exit Criteria 
permalink: "/exit_criteria/"
page_order: 4.5
page_type: reference
description: "This reference article covers the Exit Criteria feature for Canvas Flow."
tool: Canvas
---

# Exit criteria

In the **Target Audience** step of the Canvas Flow builder, you can set up exit criteria to identify which users you want to exit your Canvas. To add an exit criteria, click the dropdown to select your exception event then click **Add Trigger**.

By adding [exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directly to your Canvas entry rules, you can immediately exit users as soon as the event happens. These users will not receive any further messaging, which leads to a more targeted approach to your Canvas messaging with your audience.

For example, let's say you want to target users who haven't made any purchases yet. Click the dropdown to select **Make Purchase** as the exception event. Next, click **Add Trigger**. When your Canvas launches, your audience now excludes users who have made any purchases with the following Exit Criteria settings.

![Exit Criteria settings with "Makes Any Purchase" as the exception event, so if a user makes any purchase, then they will exit this Canvas.][1]

Additional exception events include:
* Starting a session
* Performing a custom event or conversion event
* Adding an email address
* Changing custom attribute value
* Adding values to a custom attribute array
* Updating subscription status or subscription group status
* Interacting with a campaign
* Entering a location
* Triggering a geofence
* Sending an SMS inbound message


[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 