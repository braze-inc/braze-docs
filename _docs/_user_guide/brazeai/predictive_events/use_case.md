---
nav_title: Use Case
article_title: Use Case Predict Subscription Upgrades
description: "This example shows how a fictional brand uses Braze Predictive Events to define the outcomes that matter to their business—like upgrading to a pro membership—and build targeted strategies that improve results."
page_type: tutorial
---

# Use case: Predict subscription upgrades with smarter targeting

> This example shows how a fictional brand uses Braze Predictive Events to define the outcomes that matter to their business—like upgrading to a pro membership—and build targeted strategies that improve results. 

Jordan is a lifecycle strategist at Steppington, a fake health and fitness app with free and paid tiers. Jordan’s team has a goal to increase Pro plan upgrades without bombarding their entire free user base with discount messages. Currently, they send a “Try Pro for 50% off” promo to every free-tier user after seven days. While it drives some conversions (about 5% over 7 days), it also results in excessive outreach—including discounting users who were likely to upgrade anyway.

To improve targeting and reduce messaging fatigue, Jordan uses Predictive Events to model the likelihood that a user will upgrade to Pro within the next 7 days. He defines a custom event: `upgraded_to_pro`, then uses that to train a prediction model and segment users into smart, action-oriented groups. 

This tutorial walks through how Jordan created:

- A predictive model for `upgraded_to_pro` within 7 days
- Segments that help increase conversions while sending fewer total messages

## Step 1: Create a predictive model for upgrades

Jordan starts by defining the outcome that matters most for his upgrade strategy: a user moving from the free tier to Pro. Rather than relying on generic triggers like “time since signup,” he wants to forecast which users are actually likely to convert. This way his team can act on real signals, not just assumptions.

1. In the Braze dashboard, Jordan goes to **Analytics** > **Predictive Events**.
2. He [creates a new event prediction][1] and names it "Upgrade to Pro in 7 days"
3. As the target event, he selects his custom event: `upgraded_to_pro`.
4. Jordan sets the prediction window to 7 days, sets an update schedule, and creates the prediction.

![Prediction Settings showing the definition, window, audience, and update schedule for the prediction.][img1]

## Step 2: Segment users based on upgrade probability

Once training is complete, Braze assigns an [Event Likelihood Score][2] (0–100) to each eligible user. Jordan uses this score to create actionable segments—one for high-intent users who may not need a discount, and another for users who likely won’t convert without support.

1. Jordan navigates to Segments in Braze.
2. He creates two [segments][3] using the [Event Likelihood Score filter][4] and selects the prediction he created. The two segments are:
  - **Likely to upgrade:** Score more than 70
  - **Needs nudge to upgrade:** Score more than 40 and less than 70

{% alert tip %}
Predictive filters can be combined with any other user attributes or behaviors. Jordan plans to further refine these segments based on user interests—like prioritizing users who frequently use fitness tracking features. This gives him four subgroups to target more precisely, allowing content and messaging to match each user’s needs.
{% endalert %}

![Segment builder with two filters for Event Likelihood Score.][img2]

## Step 3: Personalize messaging by intent level

Now that Jordan has clear upgrade intent signals—and refined subgroups based on user behavior—he builds a messaging strategy that adapts to what each user needs. No more one-size-fits-all blasts.

He chooses email as the primary channel for this campaign. Why? Because Jordan wants to explain the value of Pro for high-intent users and make a compelling case to more hesitant users—both of which require space, visuals, and a strong CTA. Email gives him the flexibility to do that well without pressuring users, and lets him track performance through click behavior.

Jordan [creates a Canvas][5] that splits the experience based on the segments he just built. He adds an Audience Paths step to target:

- High intent, fitness-focused users
- High intent, other users
- Low intent, fitness-focused users
- Low intent, other users

![Canvas Audience Path with four paths for each intent type.][img3]

He also sets the Canvas conversion event to the custom event `upgraded_to_pro`, so Braze tracks upgrade conversions automatically as users progress through the flow.

### Example messages per path

{% tabs %}
{% tab High intent, fitness %}

These users are already active and heavily engaged with fitness tracking features. They’re likely to upgrade without extra incentives, so the message focuses on unlocking deeper insights and advanced tools that build on their existing habits.

- **Subject line:** Go further with your fitness goals
- **Header:** Your progress deserves Pro
- **Body:** You’ve already built a strong routine. With Pro, you can go deeper—track progress across muscle groups, set weekly performance goals, and unlock advanced analytics tailored to how you move.
- **CTA:** Start your free Pro trial

{% endtab %}
{% tab High intent, other %}
These users are showing strong signals of engagement—like browsing Pro features or frequent app activity—but aren’t specifically focused on fitness tracking. The message highlights broader Pro benefits like coaching and personalization to nudge them over the line.

- **Subject line:** You’re almost there—Pro is ready when you are
- **Header:** Unlock more ways to move
- **Body:** You’ve been exploring what Pro has to offer. Now’s your chance to access custom plans, 1:1 coaching content, and guided programs built to match your unique goals—whether that’s strength, balance, or staying consistent.
- **CTA:** Start your free Pro trial

{% endtab %}
{% tab Low intent, fitness %}
These users dabble in fitness features but haven’t taken steps toward upgrading. The message leans into their fitness interests while reducing friction with a limited-time offer—helping them see Pro as a low-risk way to level up their routine.

- **Subject line:** Ready to train smarter? Try Pro at 50% off
- **Header:** Your workout upgrade is waiting
- **Body:** Pro gives you everything you need to start strong—easy-to-follow workout plans, expert tips, and real progress tracking. Try it now for 50% off, and cancel anytime.
- **CTA:** Get 50% off Pro

{% endtab %}
{% tab Low intent, other %}

These users show minimal engagement overall. They’re unlikely to upgrade without a compelling incentive, so the message takes a simple, benefits-first approach with a discount and soft language to invite exploration without pressure.

- **Subject line:** 50% off Pro—just for this weekend
- **Header:** Ready when you are
- **Body:** Build your first personalized fitness plan, track your progress, and access exclusive workouts—all for half the price. Try Pro for less and cancel anytime.
- **CTA:** Get 50% off Pro

{% endtab %}
{% endtabs %}

## Step 4: Measure results and optimize your strategy

After the campaign runs, Jordan reviews performance in [Canvas Analytics][8] to understand how well the personalized paths performed—and whether combining predictive intent with behavioral signals improved upgrade rates.

Email performance by path:

- **High intent, fitness**
   - *Open Rate:* 34%
   - *Click Rate:* 20%
   - *Conversion Rate:* 13%
   - No discount used
- **High intent, other**
   - *Open Rate:* 30%
   - *Click Rate:* 17%
   - *Conversion Rate:* 11%
   - No discount used
- **Low intent, fitness**
   - *Open Rate:* 27%
   - *Click Rate:* 12%
   - *Conversion Rate:* 8%
   - 50% off offer included
- **Low intent, other**
   - *Open Rate:* 23%
   - *Click Rate:* 9%
   - *Conversion Rate:* 6%
   - 50% off offer included

Compared to the team’s previous one-size-fits-all campaign (where a blanket discount after 7 days led to just 5% conversions and over-messaging) the targeted approach shows meaningful lift across all groups, with improved efficiency and fewer unnecessary discounts.

The [funnel report][9] also shows a clear reduction in drop-off across key steps, particularly for low-intent users who received personalized messaging. More users are opening, clicking, and upgrading—proving the value of intent-based targeting.

Jordan uses these insights to:

- Explore A/B tests on subject lines and CTA phrasing
- Reassess the discount threshold for mid-intent users
- Continue refining segments based on additional behaviors like content views or app feature usage

With Predictive Events and layered segmentation, his team now has a scalable strategy that adapts messaging based on user intent and behavior—driving more upgrades while preserving brand trust.



[1]: {(site.baseurl)}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction
[2]: {(site.baseurl)}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score
[3]: {(site.baseurl)}/user_guide/engagement_tools/segments/creating_a_segment
[4]: {(site.baseurl)}/user_guide/engagement_tools/segments/segmentation_filters#event-likelihood-score
[5]: {(site.baseurl)}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas
[6]: {(site.baseurl)}/user_guide/engagement_tools/canvas/canvas_components/audience_paths
[7]: {(site.baseurl)}/user_guide/engagement_tools/messaging_fundamentals/conversion_events
[8]: {(site.baseurl)}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics
[9]: {(site.baseurl)}/user_guide/analytics/reporting/funnel_reports
[img1]: {% image_buster /assets/img/ai_use_cases/prediction_settings.png %}
[img2]: {% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %}
[img3]: {% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %}