---
nav_title: Experiment Paths 
article_title: Experiment Paths 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "This article covers Experiment Paths, a component allowing you to test multiple Canvas paths against each other and a control group at any point in the user journey."
tool: Canvas
---

# Experiment Paths

> Experiment Paths allow you to test multiple Canvas paths against each other and a control group at any point in the user journey. 

These components will enable you to track path performance to make informed decisions about your Canvas journey.

When you include a Experiment Paths component, it will randomly assign users to different paths (or an optional control group) you create. Portions of the audience will be assigned to different paths according to percentages you select, allowing you to test different messages or paths against each other and determine which is most effective.

![][0]{: style="float:right;max-width:50%;margin-left:15px;"}

Take advantage of Winning Paths to track performance over a period of time and then automatically send subsequent users down the path with the best performance.

## Use cases

Experiment Paths are best suited for testing delivery, cadence, message copy, and channel combinations.

- **Delivery:** Compare the results between messages sent with different time [delays]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), based on user actions ([Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)), and using [Intelligent Timing]({{site.baseurl}}/docs/user_guide/sage_ai/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadence:** Test multiple messaging flows over a specific period. For example, you could test two different onboarding cadences:
    - Cadence 1: Send 2 messages in the user's first 2 weeks
    - Cadence 2: Send 3 messages in the user's first 2 weeks
    
    When targeting lapsing users, you can test the effectiveness of sending two win-back messages in a week versus sending just one.
- **Message copy:** Similar to a standard [A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/), you can test different message copy to see which wording results in a higher conversion rate.<br><br>
- **Channel combinations:** Test the effectiveness of different message channel combinations. For example, you can compare the impact of using just an email versus an email combined with a push.

## Create an experiment path

To create an Experiment Paths component, first add a step to your Canvas. Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Experiment Paths**. 

In the default configuration of this component, there are two default paths, **Path 1** and **Path 2**, with 50% of the audience being sent down each path. Click the component to expand the **Experiment Settings** panel, and you'll see the configuration options for the component.

### Step 1: Choose the number of paths and audience distribution

You can add up to four paths by clicking **Add Path** and an optional control group by checking **Add a Control Group**. Using the percentage boxes for each path, you can specify the percentage of the audience that should go to each path and the control group. The provided percentages must add up to 100% to proceed. If you want to quickly set all the available paths (and control) to the same percentage, click **Distribute Paths Evenly**.

You can also choose whether users in the control group should continue down the Canvas or exit after the conversion tracking window for the **Control Group Behavior**. Optionally, you can add a description to explain to others what this experiment path intends to test or include additional information that might be helpful to note.

![Experiment Settings where you can add paths and distribute the percentage of users in each path.][1]

{% alert note %}
If Canvas re-eligibility is enabled, users who enter the Canvas and go down a randomly chosen path will go down the same path again if they become re-eligible and re-enter the Canvas. This maintains the validity of the experiment and associated analytics.
{% endalert %}

### Step 2: Turn on Winning Path or Personalized Paths (optional) {#step-2}

You can choose to optimize your experiment by turning on [Winning Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) or [Personalized Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Both options work by initially testing your paths with a portion of your audience. After the experiment ends, the remaining and subsequent users are sent down either the best performing path overall (Winning Path) or the best performing path for each user (Personalized Paths).

{% alert important %}
Personalized Paths is currently in beta. If you are interested in participating in the beta, reach out to your customer success manager.
{% endalert %}

### Step 3: Create paths

Lastly, you must build your downstream paths. Select **Done** and return to the Canvas builder. Click the <i class="fas fa-plus-circle"></i> plus button under each path to begin creating journeys using the usual Canvas tools as you see fit, and launch the Canvas when you are ready.

![Adding steps to each path that splits from an Experiment Path component.][3]{: style="max-width:75%"}

Keep in mind that paths and their downstream steps cannot be removed from a Canvas after they're created. However, when launched, you can modify the audience distribution across paths as you see fit. For example, if a day after launching a Canvas, you conclude that one path is superior to the rest based on the analytics, you can set that path to 100% and the others to 0%. Or, depending on your needs, you can continue sending users down multiple paths.

## Tracking performance

From the **Canvas Analytics** page, click the Experiment Path to open a [detailed table]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) identical to the **Analyze Variants** tab to compare detailed performance and conversion statistics across paths. You can also export the table via CSV and compare percent changes for metrics of interest relative to the path or control you select.

Each step in each path will display statistics in the [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/) view, just like any Canvas step. However, keep in mind that individual steps' analytics do **not** take into account the structure of the Experiment. The analytics in the Experiment Step should be used to compare across paths.

### Winning Path performance

If Winning Path was turned on, your analytics view is separated into two tabs: **Initial Experiment** and **Winning Path**.

- **Initial Experiment:** Shows the metrics for each path during the experiment window. You can see a summary of how all the paths performed for the specified conversion events, and which path was selected as the winner.
- **Winning Path:** Shows only the metrics for the Winning Path starting from the moment the Initial Experiment finished.

### Personalized Paths performance

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

### Additional settings

Experiment Paths will record users who enter each step and convert while in the assigned path. This will track all conversion events specified in the Canvas setup. On the **Additional Settings** tab, enter how many days (between 1 and 30) you'd like this experiment to track conversions. The time window you specify here will determine how long conversion events (chosen in Canvas setup) will be tracked for the experiment. The per-event conversion windows specified in Canvas setup will not apply to this step's tracking and will be replaced by this Conversion Window.


[0]: {% image_buster /assets/img/experiment_step/experiment_step.png %}
[1]: {% image_buster /assets/img/experiment_step/exp_settings.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}

