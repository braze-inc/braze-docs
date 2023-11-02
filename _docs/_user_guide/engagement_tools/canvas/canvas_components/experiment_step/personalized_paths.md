---
nav_title: Personalized Paths 
article_title: Personalized Paths in Experiment Paths 
page_type: reference
description: "Personalized Paths is similar to Personalized Variant in campaigns and lets you automate your A/B tests."
tool: Canvas
---

# Personalized Paths in Experiment Paths

> Personalized Paths is similar to [Personalized Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) in campaigns and lets you automate A/B tests in your Canvas.

When Personalized Paths is turned on in an Experiment Path step, a portion of users are held in a delay group while Braze tests the remaining paths against each other. After a period of time you choose, Braze sends users held in the delay group down the best-performing path for each user. Users who enter after the experiment is over will be sent down the path that performs best overall.

## Prerequisites

You can use Personalized Paths in your Experiment Step when your Canvas is set to send once. Personalized Paths is not available for recurring or triggered Canvases.

{% alert important %}
Personalized Paths is currently in beta. If you are interested in participating in the beta, reach out to your customer success manager.
{% endalert %}

## Using Personalized Paths

### Step 1: Add an Experiment Path

Add an [Experiment Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) to your Canvas, then turn on **Personalized Paths**.

![][1]{: style="max-width:75%;" }

### Step 2: Configure Personalized Paths settings

Specify the conversion event that should determine the winner. If there are no conversion events available, return to the first step of Canvas setup and [assign conversion events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Note that if you determine the winner with opens and clicks, only the first message in the path that generates opens or clicks will contribute to determining the winner.  

Then set the **Experiment Window**. The **Experiment Window** determines how long users will be sent down all paths before choosing a single winning path for all subsequent users. The window begins when the first user enters the step.

![][2]{: style="max-width:75%;" }

### Step 3: Determine fallback

By default, if the results of the test aren't enough to determine a statistically significant winner, all future users will be sent down the best-performing path.

Alternatively, you can select **Continue sending all future users the mix of paths**.

![][3]

This option will send future users down the mix of paths according to the percentages specified in the experiment path distribution.

![][4]

### Step 4: Add your paths and launch the Canvas

A single Experiment Path component can contain up to four paths. However, when Personalized Paths is turned on, you can add up to three paths in your Experiment. The fourth path should be reserved for the Delay Group that Braze automatically adds to your experiment.

Finish setting up your Canvas as needed, then launch it. When the first user has entered the experiment, you can check the Canvas to see analytics as they come in.

![][5]{: style="max-width:75%;" }

When the experiment window passes and the experiment is complete, Braze will send users in the delay group to their respective paths.

![][6]{: style="max-width:75%;" }

## Using Personalized Paths with local time delivery

We don't recommend using local time delivery in Canvases with Personalized Paths. This is because experiment windows begin when the first user passes through. Users who are in very early time zones may enter the step and trigger the start of the experiment window much earlier than you expect, which can result in the experiment concluding before the bulk of your users in more typical time zones have had enough time to enter the Canvas and convert.

Alternatively, if you wish to use local delivery, use an experiment window of 24-48 or more hours. That way, users in early time zones enter the Canvas and trigger the experiment to start, but plenty of time remains in the experiment window. Users in later time zones will still have enough time to enter the Canvas and the Experiment Step with Personalized Paths and possibly convert before the experiment window expires.

[1]: {% image_buster /assets/img/experiment_step/experiment_personalized_path.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %}
[4]: {% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %}
[5]: {% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}
[6]: {% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}
