---
nav_title: Winning Path 
article_title: Winning Path in Experiment Paths 
page_order: 1
page_type: reference
description: "This reference article covers Winning Path, a feature that lets you automate your A/B tests when turned on for an Experiment Path step."
tool: Canvas
---

# Winning Path in Experiment Paths

> Winning Path is similar to [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations) in campaigns, and lets you automate your A/B tests. When Winning Path is turned on in an Experiment Path step, after a specified period of time, all subsequent users will be sent down the path with the highest conversion rate.

This feature is best for Canvases with entries that are recurring or triggered, but can be used for Canvases with one-time entry with [a few extra steps](#one-time-entry).

## Using Winning Path

Add an [Experiment Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) to your Canvas, then turn on **Winning Path**.

![Settings in Experiment Path titled "Distribute Subsequent Users to Winning Path". The section includes a toggle for Winning Path, and options to configure the conversion event and experiment window.][1]

### Winning Path settings

Specify the conversion event that should determine the winner. If there are no conversion events available, return to the first step of Canvas setup and [assign conversion events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Note that if you determine the winner with opens and clicks, only the first message in the path that generates opens or clicks will contribute to determining the winner.  

Then set the **Experiment Window**. The **Experiment Window** specifies how long the experiment will run before the Winning Path is determined and all users that follow are sent down that path. The window begins when the first user enters the step.

### Statistical significance

By default, if the results of the test aren't enough to determine a statistically significant winner, all future users will be sent down the best performing path. Alternatively, you can select **Continue sending all future users the mix of paths**, which will send future users down the mix of paths according to the percentages specified in the experiment distribution.

![Percentages specified in the experiment distribution][3]

## Using Winning Paths with one-time entry {#one-time-entry}

When using Winning Paths in a Canvas where users are allowed to enter only once, a Delay Group is automatically included. During the duration of the experiment, a percentage of users will be held in the Delay Group while the remaining users enter your Experiment Paths. 

![Experiment Step with a Delay Group for Winning Path][4]{: style="max-width:75%"}

When the test is complete and a Winning Path is determined, the users assigned to the Delay Group will be directed to the chosen path, and continue through the Canvas.

![Experiment Step with a Delay Group sent down the Winning Path][5]{: style="max-width:75%"}

## Using Winning Paths with local time delivery 

We don't recommend using local time delivery in Canvases with Winning Paths. This is because experiment windows begin when the first user passes through. Users who are in very early time zones may enter the step and trigger the start of the experiment window much earlier than you expect, which can result in the Experiment concluding before the bulk of your users in more typical time zones have had enough time to enter the Canvas and/or convert. 

Alternatively, if you wish to use local delivery, use an experiment window of 24-48 or more hours. That way, users in early time zones enter the canvas and trigger the experiment to start, but plenty of time in the experiment window remains. Users in later time zones will still have sufficient time to enter the Canvas and the Experiment Step with Winning Paths and possibly convert before the experiment window expires.

[1]: {% image_buster /assets/img/experiment_step/experiment_winning_path.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_path_distribution.png %}
[4]: {% image_buster /assets/img/experiment_step/experiment_one_time.png %}
[5]: {% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}
