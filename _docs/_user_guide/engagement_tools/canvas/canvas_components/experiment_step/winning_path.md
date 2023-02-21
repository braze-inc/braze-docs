---
nav_title: Winning Path 
article_title: Winning Path in Experiment Paths 
page_order: 1
page_type: reference
description: "Winning Path lets you automate your A/B tests when turned on for an Experiment Path step."
tool: Canvas
---

# Winning Path in Experiment Paths

Winning Path is similar to [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations) in campaigns, and lets you automate your A/B tests. When Winning Path is turned on in an Experiment Path step, after a specified period of time, all subsequent users will be sent down the path with the highest conversion rate.

This feature is best for Canvases with entries that are recurring or triggered, but can be used for Canvases with one-time entry with [a few extra steps](#one-time-entry).

{% alert important %}
Winning Path is currently in early access. If you're interested in participating in the early access, reach out to your customer success manager.
{% endalert %}

## Using Winning Path

Add an [Experiment Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) to your Canvas, then turn on **Winning Path**. 

![Settings in Experiment Path titled "Distribute Subsequent Users to Winning Path". The section includes a toggle for Winning Path, and options to configure the conversion event and experiment window.][1]

Specify the conversion event that should determine the winner. If there are no conversion events available, return to the first step of Canvas setup and [assign conversion events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events).

Then set the **Experiment Window**. The **Experiment Window** specifies how long the experiment will run before the Winning Path is determined and all users that follow are sent down that path. The window begins when the first user enters the step.

## Using Winning Paths with one-time entry {#one-time-entry}

Because the winner is chosen after a period of time you choose, Winning Path is best for Canvases where users enter on a recurring or triggered basis. A Canvas with one-time entry can't send users down a Winning Path at a later time because all users go through paths simultaneously. 

However, you can accomplish this use case by adding a preliminary additional Experiment Path step, which delays your desired portion of users until the experiment is complete.

![A draft Canvas demonstrating how to use the Winning Path functionality in a Canvas with one-time entry.][2]{: style="max-width:80%"}

### Steps

1. Add an initial Experiment Path step (with Winning Path off) to split users between the final send group and the test group that will go through the step with Winning Paths enabled. 
2. Add a delay step to the final send group path. 
3. Add a second Experiment Path step to the test group (with Winning Path on). This step functions as normal, with users equally distributed between however many paths you'd like to test.

The duration of the delay step should be slightly longer than the Experiment Window to ensure the experiment has been completed once the users advance after the delay. After the step with Winning Paths enabled selects a winner, it will set 100% of future users to the winning path. The users waiting in the Delay step will be released and flow through to the winning path.

{% alert note %}
If you'd like this functionality to be built into Winning Path, please let the Braze product team know by [voting for it on the Braze Product Portal](https://portal.productboard.com/ko5rgqefrdssb5wesynqswxp/c/206-winning-path-for-one-time-sends?utm_medium=social&utm_source=portal_share).
{% endalert %}

[1]: {% image_buster /assets/img/experiment_step/experiment_winning_path.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_onetime_workaround.png %}
