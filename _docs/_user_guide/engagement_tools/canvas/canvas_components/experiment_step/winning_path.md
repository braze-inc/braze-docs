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

Because the winner is chosen after a period of time you choose, Winning Path is best for Canvases where users enter on a recurring or triggered basis. A Canvas with one-time entry can't send users down a Winning Path at a later time because all users go through paths simultaneously. 

However, you can accomplish this use case by adding a preliminary additional Experiment Path step, which delays your desired portion of users until the experiment is complete.

![A draft Canvas demonstrating how to use the Winning Path functionality in a Canvas with one-time entry.][2]{: style="max-width:80%"}

### Steps

1. Add an initial Experiment Path step (with Winning Path off) to split users between the final send group and the test group that will go through the step with Winning Paths enabled. 
2. Add a delay step to the final send group path. 
3. Add a second Experiment Path step to the test group (with Winning Path on). This step functions as normal, with users equally distributed between however many paths you'd like to test.

The duration of the delay step should be slightly longer than the experiment window to ensure the experiment has been completed once the users advance after the delay. After the step with Winning Paths enabled selects a winner, it will set 100% of future users to the winning path. The users waiting in the Delay step will be released and flow through to the winning path.

{% alert note %}
If you'd like this functionality to be built into Winning Path, please let the Braze product team know by [voting for it on the Braze Product Portal](https://portal.productboard.com/ko5rgqefrdssb5wesynqswxp/c/206-winning-path-for-one-time-sends?utm_medium=social&utm_source=portal_share).
{% endalert %}

## Using Winning Paths with local time delivery 

We don't recommend using local time delivery in Canvases with Winning Paths. This is because experiment windows begin when the first user passes through. Users who are in very early time zones may enter the step and trigger the start of the experiment window much earlier than you expect, which can result in the Experiment concluding before the bulk of your users in more typical time zones have had enough time to enter the Canvas and/or convert. 

Alternatively, if you wish to use local delivery, use an experiment window of 24-48 or more hours. That way, users in early time zones enter the canvas and trigger the experiment to start, but plenty of time in the experiment window remains. Users in later time zones will still have sufficient time to enter the Canvas and the Experiment Step with Winning Paths and possibly convert before the experiment window expires.

[1]: {% image_buster /assets/img/experiment_step/experiment_winning_path.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_onetime_workaround.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_path_distribution.png %}
