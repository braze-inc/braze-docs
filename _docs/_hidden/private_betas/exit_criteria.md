---
nav_title: Exit Criteria 
article_title: Exit Criteria 
permalink: "/exit_criteria/"
hidden: true
page_type: reference
description: "This reference article covers the Exit Criteria feature for Canvas Flow."
tool: Canvas
---

# Exit criteria

In the **Target Audience** step of the Canvas Flow builder, you can use the Exit Criteria feature to identify which users you want to exit your Canvas. To add an exit criteria, click the dropdown to select your exception event then click **Add Trigger**.

By adding [exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directly to your Canvas entry rules, you can immediately exit users as soon as the event happens. These users will not receive any further messaging, which leads to a more targeted approach to your Canvas messaging with your audience.

For example, let's say you want to target users you haven't made any purchases yet. Click the dropdown to select **Make Purchase** as the exception event. Next, click **Add Trigger**. When your Canvas launches, your audience now excludes users who have made any purchases with the following Exit Criteria settings.

![Exit Criteria settings with "Makes Any Purchase" as the exception event, so if a user makes any purchase, then they will exit this Canvas.][1]  

You can use exit criteria in combination with [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) in your Canvas user journey. Since exit criteria identifies users at the launch of a Canvas, you can use Action Paths with the option **I want this group to exit the Canvas** enabled to exit users within an action group at the end of an evaluation period.


[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 