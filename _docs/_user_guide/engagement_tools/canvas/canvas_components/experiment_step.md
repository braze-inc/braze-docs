---
nav_title: Experiment Step
title: Audience Path Step
alias: /audience_paths/
description: "Experiment Steps allow you to test multiple possible Canvas paths against each other and a control group at any point in the user journey."
page_order: 6
hidden: true
---

# Experiment Step

> Experiment Steps allow you to test multiple possible Canvas paths against each other and a control group at any point in the user journey.

Experiment Step will randomly assign users to the different paths (or optional control group) you create. Portions of the audience will be assigned to the different paths according to percentages you select, allowing you to test different messages or entirely different paths against each other and then determine which to keep or eliminate. After launching, analytics will allow you to track performance and see whether it differs across the different paths to help you determine which path should get what proportion of users (or all of them!).

![Experiment Step ][0]{: style="max-width:20%"}

## Create an Experiment Step,


To create an Experiment Step, add a step to your Canvas. Then, using the drop-down at the top of the new step, select `Experiment`.

In the default Experiment Step shown to the right, there are already two default paths, __Path 1__ and __Path 2__, with 50% of the audience being sent down each path. Click on the Experiment Step itself to expand the Experiment Settings panel, and you''ll see the configuration options for the step. Here you can

### 1. Choose The Number of Paths and Audience Distribution

![Experiment Settings][1]{: style="max-width:80%"}

You can add up to 4 paths by clicking `Add Path` and an optional control group by checking the box labeled `Add a Control Group`. Using the input boxes above each path, you can input the percentage of the audience that should go to each path as well as the control group. Naturally, the percentages must add up to 100% to proceed. The 'Distribute Paths Evenly' button allows you to quickly set all the available paths (and control) to the same percentage.

Optionally, you can add a Description as a note to yourself or others to explain what this Experiment Step intends to test or whatever else that might be convenient for you.

### 2. Select How Long To Track Conversions

The Experiment Step will keep its own record of users who enter each step and convert while in the assigned path. Only the Primary Conversion event of the canvas will be tracked by the Experiment Step. Using the input box at the bottom of the panel, enter how many days between 1 and 30 you'd like this Experiment Step to track conversions for.

### 3. Create Paths

Now it's time to build your downstream paths! Select `Done` and return to the Canvas builder.  Click the '+`' under each Path to begin creating journeys using all the usual tools of Canvas as you see fit, and launch the Canvas when you are ready.

## Tracking Performance

Each path will display statistics in the Canvas Analytics view just like any Canvas step. Additionally, clicking on the Experiment Step from Canvas Analytics will open a detailed table (identical to Analyze Variants)[https://www.braze.com/docs/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant] to compare detailed performance and conversion statistics across paths. This also includes the ability to export the table via CSV and compare % changes of metrics of interest relative to the path (or control) you select.


[0]: {% image_buster /assets/img/experiment_step/experiment_step.png %}
[1]: {% image_buster /assets/img/experiment_step/exp_settings.png %}
