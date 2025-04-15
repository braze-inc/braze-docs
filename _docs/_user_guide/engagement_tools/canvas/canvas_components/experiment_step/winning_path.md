---
nav_title: Winning Path 
article_title: Winning Path in Experiment Paths 
page_type: reference
description: "This reference article covers Winning Path, a feature that lets you automate your A/B tests when turned on for an Experiment Path step."
tool: Canvas
---

# Winning Path in Experiment Paths

> Winning Path is similar to [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) in campaigns, and lets you automate your A/B tests.

When Winning Path is turned on in an Experiment Path step, after a specified period of time, all subsequent users will be sent down the path with the highest conversion rate.

## Using Winning Path

### Step 1: Add an Experiment Path

Add an [Experiment Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) to your Canvas, then turn on **Winning Path**.

![Settings in Experiment Path titled "Distribute Subsequent Users to Winning Path". The section includes a toggle for Winning Path, and options to configure the conversion event and experiment window.][1]

### Step 2: Configure Winning Path settings

Specify the conversion event that should determine the winner. If there are no conversion events available, return to the first step of Canvas setup and [assign conversion events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Note that if you determine the winner with opens and clicks, only the first message in the path that generates opens or clicks will contribute to determining the winner.

Next, set the **Experiment Window**. The **Experiment Window** specifies how long the experiment will run before the Winning Path is determined and all users that follow are sent down that path. The window begins when the first user enters the step.

![][2]

### Step 3: Determine fallback {#statistical-significance}

By default, if the results of the test aren't enough to determine a statistically significant winner, all future users will be sent down the best performing path.

Alternatively, you can select **Continue sending all future users the mix of paths**.

![][6]

This option will send future users down the mix of paths according to the percentages specified in the experiment path distribution.

![Percentages specified in the experiment distribution][3]

{% alert note %}
A Delay Group will only appear in your path distribution if your Canvas is set up for one-time entry and your Experiment step has three paths or fewer. Recurring and triggered Canvases will not have a Delay Group when Winning Path is turned on.
{% endalert %}

### Step 4: Add your paths and launch the Canvas

A single Experiment Path component can contain up to four paths. However, if your Canvas is set up for [one-time entry](#one-time-entry), one path must be reserved for the Delay Group that Braze automatically adds when Winning Path is turned on. This means for Canvases with one-time entry, you can add up to three paths to your experiment.

Finish setting up your Canvas as needed, then launch it. When the first user has entered the experiment, you can check the Canvas to see analytics as they come in and [track your experiment's performance]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

After a Winning Path concludes, all subsequent users who enter the Canvas will go down the Winning Path, including users who re-entered and were previously in the control group of the Experiment Path step.

## Analytics {#analytics}

If Winning Path was turned on, your analytics view is separated into two tabs: **Initial Experiment** and **Winning Path**.

- **Initial Experiment:** Shows the metrics for each path during the experiment window. You can see a summary of how all the paths performed for the specified conversion events and which path was selected as the winner.
- **Winning Path:** Shows only the metrics for the Winning Path starting from the moment the Initial Experiment finished.

## Things to know

### One-time entry {#one-time-entry}

When using Winning Paths in a Canvas where users are allowed to enter only once, a Delay Group is automatically included. During the duration of the experiment, a percentage of users will be held in the Delay Group while the remaining users enter your Experiment Paths.

![Experiment Step with a Delay Group for Winning Path][4]{: style="max-width:75%"}

When the test is complete and a Winning Path is determined, the users assigned to the Delay Group will be directed to the chosen path, and continue through the Canvas.

![Experiment Step with a Delay Group sent down the Winning Path][5]{: style="max-width:75%"}

### Local time delivery

We don't recommend using local time delivery in Canvases with Winning Paths. This is because experiment windows begin when the first user passes through. Users who are in very early time zones may enter the step and trigger the start of the experiment window much earlier than you expect, which can result in the Experiment concluding before the bulk of your users in more typical time zones have had enough time to enter the Canvas or convert, or both. 

Alternatively, if you wish to use local delivery, use an experiment window of 24-48 or more hours. That way, users in early time zones enter the Canvas and trigger the experiment to start, but plenty of time in the experiment window remains. Users in later time zones will still have sufficient time to enter the Canvas and the Experiment Step with Winning Paths and possibly convert before the experiment window expires.

[1]: {% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_winning_settings.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_path_distribution.png %}
[4]: {% image_buster /assets/img/experiment_step/experiment_one_time.png %}
[5]: {% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}
[6]: {% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %}
