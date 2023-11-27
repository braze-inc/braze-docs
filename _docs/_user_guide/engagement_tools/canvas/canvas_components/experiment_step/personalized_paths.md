---
nav_title: Personalized Paths 
article_title: Personalized Paths in Experiment Paths 
page_type: reference
description: "Personalized Paths is similar to Personalized Variant in campaigns and lets you personalize entire Canvas journeys based on each person's conversion likelihood."
tool: Canvas
---

# Personalized Paths in Experiment Paths

> Personalized Paths is similar to [Personalized Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) in campaigns and lets you personalize entire Canvas journeys for individual users based on conversion likelihood.

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

Then set the **Experiment Window**. The **Experiment Window** determines how long users will be sent down all paths before choosing the best path for each user in the delay group. The window begins when the first user enters the step.

![][2]{: style="max-width:75%;" }

### Step 3: Determine fallback

By default, if the results of the test aren't enough to determine a statistically significant winner, all future users will be sent down the best-performing path.

Alternatively, you can select **Continue sending all future users the mix of paths**.

![][3]

This option will send future users down the mix of paths according to the percentages specified in the experiment path distribution.

![][4]

### Step 4: Add your paths and launch the Canvas

A single Experiment Path component can contain up to four paths. However, when Personalized Paths is turned on, you can add up to three paths in your Experiment. The fourth path should be reserved for the Delay Group that Braze automatically adds to your experiment.

Finish setting up your Canvas as needed, then launch it. When the first user has entered the experiment, you can check the Canvas to see analytics as they come in and [track your experiment's performance]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

![][5]{: style="max-width:75%;" }

When the experiment window passes and the experiment is complete, Braze will send users in the delay group to their respective paths with the highest personalized likelihood of conversion.

![][6]{: style="max-width:75%;" }

## Analytics {#analytics}

If Personalized Paths was turned on, your analytics view is separated into two tabs: **Initial Experiment** and **Personalized Paths**.

{% tabs local %}
{% tab Initial Experiment %}

The **Initial Experiment** tab shows the metrics for each path during the experiment window. You can see a summary of how all the paths performed for the specified conversion events.

![Results of an initial test sent to determine the best performing variant for each user. A table shows the performance of each variant based on various metrics for the target channel.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

This page also shows a breakdown of users' preferred paths based on a combination of certain characteristics. These characteristics are:

- **Recency:** When they last had a session
- **Frequency:** How often they have sessions
- **Tenure:** How long they have been a user

![The User Characteristics table, which shows which users are predicted to prefer Path 1 and Path 2 based on the three buckets they fall in for recency, frequency, and tenure.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Think of recency as how recent their last interaction with you was, frequency as how often they engage, and tenure as the overall length of time they've been engaging with you. We group users into "buckets" based on these three things (as explained in the **User Characteristics** table) and then see which bucket likes which path more. It’s like sorting users into hundreds of different lists based on when they last shopped with you, how often they shop, and how long they've been customers.

When it comes to choosing a message for a user, Braze examines the buckets they fall into. Each bucket exerts a distinct influence on path selection for users. We quantify this influence using a statistical method called [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression), which is a way of predicting future behavior based on past actions. This method accounts for user interactions during the initial message send. This table only summarizes the results by displaying which path users in each bucket tended to engage with.

Ultimately, Braze combines all this data to select a tailored message path for each user, to make sure it's as engaging and relevant as possible for them.

{% alert note %}
The time intervals for each bucket are determined based on Canvas-specific user data, which may vary between Canvases.
{% endalert %}

{% endtab %}
{% tab Personalized Paths %}

The **Personalized Paths** tab shows the results of the final experiment, where the users in the Delay Group were sent down the best-performing path for them.

The three cards on this page show your projected lift, overall results, and the projected results if you sent just the winning path instead. Even if there's no lift, which can sometimes happen, the result is the same as sending only the winning path (a traditional A/B test).

- **Projected lift:** The improvement in your selected conversion event due to using Personalized Paths instead of sending every user down the overall best-performing path.
- **Overall results:** The results of the second send based on your conversion event.
- **Projected results:** The projected results of the second send based on your chosen optimization metric if you had sent just the winning variant instead.

![Personalized Paths tab for a Canvas. The cards show the Projected Lift, Overall Conversions (with Personalized Paths), and Projected Unique Opens (with Winning Path).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

The table on this page shows the metrics for each variant from the personalized variant send. Your **Audience %** adds up to the percentage of the target segment you reserved for the personalized variant group.

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Using Personalized Paths with local time delivery

We don't recommend using local time delivery in Canvases with Personalized Paths. This is because experiment windows begin when the first user passes through. Users who are in very early time zones may enter the step and trigger the start of the experiment window much earlier than you expect, which can result in the experiment concluding before the bulk of your users in more typical time zones have had enough time to enter the Canvas and convert.

Alternatively, if you wish to use local delivery, use an experiment window of 24-48 or more hours. That way, users in early time zones enter the Canvas and trigger the experiment to start, but plenty of time remains in the experiment window. Users in later time zones will still have enough time to enter the Canvas and the Experiment Step with Personalized Paths and possibly convert before the experiment window expires.

[1]: {% image_buster /assets/img/experiment_step/experiment_personalized_path.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %}
[4]: {% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %}
[5]: {% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}
[6]: {% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}
