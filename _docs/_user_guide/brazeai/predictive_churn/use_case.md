---
nav_title: Use Case
article_title: Use Case Reduce Churn With Timely Content
description: "This example shows how a fictional brand uses Predictive Churn to proactively reduce user drop-off."
page_type: tutorial
---

# Use case: Reduce churn with timely content re-engagement

> This example shows how a fictional brand uses Predictive Churn to proactively reduce user drop-off. Instead of waiting for churn to happen, predict which users are at risk and deliver tailored messages while they’re still active.

Let's say Camila is a CRM manager at MovieCanon, a streaming platform for indie films, documentaries, and international series.

Camila’s team has spotted a troubling trend: users sign up, stream a movie or two, and then disappear. Historically, they’ve tried sending a generic “We miss you” email a week later—but with only a 3% conversion rate, it’s too little, too late. Most users don’t re-engage, and churn becomes inevitable.

Camila wants to change that. Instead of reacting to churn after it happens, she uses Predictive Churn to identify users who are likely to become inactive within the next 14 days—giving her team the opportunity to re-engage people while they’re still active.

This tutorial walks through how Camila:

- Creates a churn prediction model based on user behavior
- Segments users by risk level
- Builds a re-engagement campaign tailored to those most at risk
- Evaluates impact using campaign analytics

## Step 1: Create a churn prediction model

Camila starts by modeling the outcome she wants to avoid: users becoming inactive. For MovieCanon, churn means not starting a stream within 14 days—so that’s the behavior she wants to predict.

1. In the Braze dashboard, Camila goes to **Analytics** > **Predictive Churn**.
2. She creates a new churn prediction and names it "Churn risk in 2 weeks".
3. To define churn, she selects `do not` and the custom event `stream_started`, which indicates active engagement.
4. She sets the prediction window to 14 days—meaning the model will identify users who are likely to go 14 days without starting a new stream.

![Churn definition showing churn defined as a user who does not perform a custom event "stream_started" in the last 14 days.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5. She selects a prediction audience that includes all users who have triggered relevant events in the past 30 days—giving the model enough recent behavior to learn from.
6. She sets the prediction update schedule to weekly so scores stay current.
7. She selects **Create prediction**.

The model then begins training, analyzing behaviors like recent sessions, frequency of viewing, and content interactions to surface patterns that predict drop-off. Camila gets an email an hour later that her prediction has finished training, so she opens it in Braze and checks the [prediction quality]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality) score. It’s labeled “Good,” which means the model’s predictions are likely to be accurate and reliable. Confident in the model’s performance, she moves on.

## Step 2: Segment users by churn risk

After the model finishes training, Braze assigns each eligible user a [Churn Risk Score]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) between 0–100. 

To determine a starting threshold for targeting, Camila uses the prediction audience slider to preview how many users fall into each score range and how accurate the prediction is at that level. She balances coverage and precision based on expected true positives. Based on this, she decides to target risk scores higher than 70. 

1. Camila navigates to Segments in Braze.
2. She creates a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) using the [Churn Risk Score filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) and selects the churn prediction she created:
   - **Likely to churn:** Score more than 70

![Segment filtering for users with a churn risks score more than 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Step 3: Target at-risk users with recurring re-engagement content

With her prediction and segment ready, Camila sets up a recurring campaign that automatically reaches users who become at risk each week.

1. Camila creates a recurring campaign and enables [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), so each message is delivered when each individual user is most likely to engage rather than relying on a fixed day and time.
2. She targets the "Likely to churn" segment she just created.
3. She sets the campaign conversion event to the custom event `stream_started`, to track how many users actually return to view content.
4. Camila chooses email as her primary channel—it gives her the space to highlight multiple personalized content picks in a visually rich format without too much pressure. The email includes:
   - A personalized watchlist powered by [AI Item Recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/), dynamically selected from MovieCanon’s catalog
   - A call to action that brings them directly into the app.

This ensures that each week, MovieCanon reaches only the users who need a nudge—no over-messaging, no guesswork.

### Example email

- **Subject line:** Don’t leave these titles hanging
- **Header:** Your next great watch is waiting
- **Body:** Haven’t hit play in a bit? No worries—we’ve lined up a few picks just for you. From slow-burn thrillers to award-winning documentaries, there’s something here with your name on it.
- **CTA:** View more picks

## Step 4: Measure performance

After a few weeks, Camila checks her [campaign analytics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) to evaluate how well the strategy is performing. 

She sees:

- *Open Rate:* 31%
- *Click Rate:* 15%
- *Conversion Rate* (started stream within 48 hours): 11%

Compared to the old “We miss you” campaign (where conversion rates hovered around 3%), this new flow reduces churn in the target group by 28%. She digs into the [funnel report]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) to spot where users drop off. While open and click rates are strong, she notices slight friction between click and conversion—prompting her to consider testing CTA copy or experimenting with layout.

To understand long-term impact, Camila also tracks the volume of users entering the “Likely to churn” segment week over week. This helps her assess the overall health of the lifecycle and inform retention strategy at a broader level. Finally, she revisits the [Prediction Analytics]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) page for her churn prediction to compare predicted versus actual churners—a useful check to make sure the model is performing as expected.

Based on these insights, Camila plans to A/B test subject lines, test different timing windows, and experiment with content formats like carousel-style recommendations in an in-app message.

With Predictive Churn, Intelligent Timing, and AI-powered personalization, Camila’s team isn’t just reacting to churn—they’re getting ahead of it. And her campaign runs quietly in the background, reaching the right people, at the right time, with content they’ll actually care about.
