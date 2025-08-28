---
nav_title: Personalized Paths
article_title: Personalized Paths in Experiment Paths 
page_type: reference
description: "Personalized Paths lets you personalize any point of a Canvas journey for individual users based on conversion likelihood."
tool: Canvas
---

# Personalized Paths in Experiment Paths

> Personalized Paths is similar to [Personalized Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) in campaigns and lets you personalize any point of a Canvas journey for individual users based on conversion likelihood.

## How Personalized Paths works

When Personalized Paths is turned on in an Experiment Path step, the behavior is slightly different depending on if your Canvas is set to send once or to recur:

- **Single-send Canvas:** A group of users is held back in a delay group. The remaining users pass into an initial test to train a predictive model for a duration you configure—at least 24 hours for best results. After the test, a model is created to learn which user behaviors were associated with a greater likelihood of converting on a given path. Finally, each user in the delay group is sent down the path most likely to result in conversion for them based on the behaviors they exhibit and what the predictive model learned during the initial test.
- **Recurring, action-triggered, and API-triggered Canvases:** An initial experiment is performed on all users who enter the Experiment Path during a specified window. To maintain the integrity of the experiment, if a user receives multiple messages before the window ends, they'll be assigned to the same variant each time. After the experiment window, each user is sent down the path most likely to result in conversion for them.

## Using Personalized Paths

### Step 1: Add an Experiment Path

Add an [Experiment Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) to your Canvas, then turn on **Personalized Paths**.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Step 2: Configure Personalized Paths settings

Specify the conversion event that should determine the winner. If there are no conversion events available, return to the first step of Canvas setup and [assign conversion events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

If you choose opens or clicks as your conversion event, make sure the first step in the path is a [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). Braze only counts engagement from the first Message step in each respective path. If the path starts with a different step (like a Delay or Audience Path step) and the message comes later, that message won’t be included when evaluating performance.

Then set the **Experiment Window**. The **Experiment Window** determines how long users will be sent down all paths before choosing the best path for each user in the delay group. The window begins when the first user enters the step.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Step 3: Determine fallback

By default, if the results of the test aren't enough to determine a statistically significant winner, all future users will be sent down the single best-performing path.

Alternatively, you can select **Continue sending all future users the mix of paths**.

![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

This option will send future users down the mix of paths according to the percentages specified in the experiment path distribution.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Step 4: Add your paths and launch the Canvas

{% tabs local %}
{% tab Single-send Canvas %}

A single Experiment Path component can contain up to four paths. However, for single-send Canvases, you can add up to three paths when Personalized Paths is turned on. The fourth path should be reserved for the Delay Group that Braze automatically adds to your experiment.

Finish setting up your Canvas as needed, then launch it. When the first user has entered the experiment, you can check the Canvas to see analytics as they come in and [track your experiment's performance]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

When the experiment window passes and the experiment is complete, Braze will send users in the delay group to their respective paths with the highest personalized likelihood of conversion based on the recommendation of the predictive model.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Recurring or action-triggered or API-triggered Canvas %}

You can test up to four paths in a single Experiment Path. Add your paths and finish setting up your Canvas as needed, then launch it.  

When the first user has entered the experiment, you can check the Canvas to see analytics as they come in and [track your experiment's performance]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

When the experiment window passes and the experiment is complete, all subsequent users to enter the Canvas will be sent down the path most likely to result in conversion for them.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Analytics {#analytics}

If Personalized Paths was turned on, your analytics view is separated into two tabs: **Initial Experiment** and **Personalized Paths**.

{% tabs local %}
{% tab Initial Experiment %}

The **Initial Experiment** tab shows the metrics for each path during the experiment window. You can see a summary of how all the paths performed for the specified conversion events.

![Results of an initial experiment sent to determine the best performing path for each user. A table shows the performance of each path based on various metrics for the target channel.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

By default, the test looks for associations between user’s custom events and their path preferences, or the message variant a user best responds to. This analysis detects whether custom events increase or decrease likelihood of responding to a particular path. These relationships are then used to determine which users gets assigned which path after the experiment window passes.

The relationships between custom events and path preferences are displayed in the table on the **Initial Experiment** tab.

![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

If the test can't find a meaningful relationship between custom events and path preferences, the test will fall back to a session-based analysis method.

{% details Fallback analysis method %}

**Session-based analysis method**<br>
If the fallback method is used to determine Personalized Paths, the **Initial Experiment** tab shows a breakdown of users' preferred variants based on a combination of certain characteristics.

These characteristics are:

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

**How Personalized Paths are selected**<br>
With this method, an individual user's recommended message is the sum of the effects of their specific recency, frequency, and tenure. Recency, frequency, and tenure are split into buckets, as illustrated in the **User Characteristics** table. The time range of each bucket is determined by the data for users in each individual Canvas and will change from Canvas to Canvas.

Each bucket can have a different contribution or "push" toward each path. The strength of the push for each bucket is determined from user responses in the initial experiment using [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression). This table only summarizes the results by displaying which path users in each bucket tended to engage with. Any individual user's actual Personalized Path depends on the sum of the effects of the three buckets they're in—one for each characteristic.

{% enddetails %}

{% endtab %}
{% tab Personalized Paths %}

The **Personalized Paths** tab shows the results of the final experiment, where the users in the Delay Group were sent down the best-performing path for them.

The three cards on this page show your projected lift, overall results, and the projected results if you sent just the Winning Path instead. Even if there's no lift, which can sometimes happen, the result is the same as sending only the Winning Path (a traditional A/B test).

- **Projected lift:** The improvement in your selected conversion event due to using Personalized Paths instead of sending every user down the overall best-performing path.
- **Overall results:** The results of the second send based on your conversion event.
- **Projected results:** The projected results of the second send based on your chosen optimization metric if you had sent just the Winning Variant instead.

![Personalized Paths tab for a Canvas. The cards show the Projected Lift, Overall Conversions (with Personalized Paths), and Projected Unique Opens (with Winning Path).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Using Personalized Paths with local time delivery

We don't recommend using local time delivery in Canvases with Personalized Paths. This is because experiment windows begin when the first user passes through. Users who are in very early time zones may enter the step and trigger the start of the experiment window much earlier than you expect, which can result in the experiment concluding before the bulk of your users in more typical time zones have had enough time to enter the Canvas and convert.

Alternatively, if you wish to use local delivery, use an experiment window of 24-48 or more hours. That way, users in early time zones enter the Canvas and trigger the experiment to start, but plenty of time remains in the experiment window. Users in later time zones will still have enough time to enter the Canvas and the Experiment Step with Personalized Paths and possibly convert before the experiment window expires.

