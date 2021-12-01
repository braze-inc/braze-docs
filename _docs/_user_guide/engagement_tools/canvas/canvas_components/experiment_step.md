---
nav_title: Experiment Paths Step
article_title: Experiment Paths Step
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Experiment Paths allow you to test multiple Canvas paths against each other and a control group at any point in the user journey."
tool: Canvas
---

# Experiment Paths Step

> The Experiment Paths Step allows you to test multiple Canvas paths against each other and a control group at any point in the user journey. These steps will enable you to track path performance to make informed decisions about your Canvas journey.

A Canvas Experiment Paths Step will randomly assign users to different paths (or an optional control group) you create. Portions of the audience will be assigned to different paths according to percentages you select, allowing you to test different messages or paths against each other and determine which is most effective. After launching, analytics will allow you to track performance and see whether results differ across the different paths to help you determine which path should get what proportion of users (or all of them!).

![Experiment Paths Step][0]{: style="max-width:60%"}

## Create an Experiment Paths Step

To create an Experiment Paths Step, add a step to your Canvas. Then, using the dropdown at the top of the new step, select **Experiment**.

In the default configuration of this step, there are two default paths, **Path 1** and **Path 2**, with 50% of the audience being sent down each path. Click the Experiment Paths Step itself to expand the **Experiment Settings** panel, and you'll see the configuration options for the step. 

### Step 1: Choose the number of paths and audience distribution

![Experiment Settings][1]{: style="max-width:80%"}

You can add up to 4 paths by clicking **Add Path** and an optional control group by checking **Add a Control Group**. Using the percentage boxes above each path, you can specify the percentage of the audience that should go to each path and the control group. The provided percentages must add up to 100% to proceed. If you want to quickly set all the available paths (and control) to the same percentage, click **Distribute Paths Evenly**.

Select whether users in the Control Group should continue down the Canvas or exit after the conversion tracking window using the checkbox provided.

{% alert note %}
If Canvas re-eligibility is enabled, users who enter the Canvas and go down a randomly chosen path will go down the same path again if they become re-eligible and re-enter the Canvas. This maintains the validity of the experiment and associated analytics.
{% endalert %}

Optionally, you can add a description to explain to others what this Experiment Paths Step intends to test or include other information that might be helpful to note.

### Step 2: Select how long to track conversions

The Experiment Paths Step will record users who enter each step and convert while in the assigned path. This step will track only the **Primary Conversion** event of the Canvas. Use the input box at the bottom of the panel to enter how many days (between 1 and 30) you'd like this Experiment to track conversions.

### Step 3: Create paths

Lastly, you must build your downstream paths. Select **Done** and return to the Canvas builder. Click <i class="fas fa-plus-circle"></i>**Plus** under each path to begin creating journeys using the usual Canvas tools as you see fit, and launch the Canvas when you are ready. 

Keep in mind that once created, **paths and their downstream steps cannot be removed from a Canvas**. However, once launched, you can modify the audience distribution across paths as you see fit. For example, if a day after launching a Canvas, you conclude that one path is superior to the rest based on the analytics, you can set that path to 100% and the others to 0%. Or, depending on your need, you can continue sending users down multiple paths.

## Tracking performance

Each path will display statistics in the [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/) view, just like any Canvas step. Additionally, clicking on the Experiment Paths Step from Canvas Analytics will open a detailed table [identical to Analyze Variants]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) to compare detailed performance and conversion statistics across paths. You can also export the table via CSV and compare percent changes for metrics of interest relative to the path or control you select.

[0]: {% image_buster /assets/img/experiment_step/experiment_step.png %}
[1]: {% image_buster /assets/img/experiment_step/exp_settings.png %}
