---
nav_title: Analytics
article_title: Multivariate and A/B test analytics
page_order: 10
page_type: reference
description: "This article explains how to view and interpret the results of a multivariate or A/B campaign."
---

# Multivariate and A/B test analytics

> This article explains how to view the results of a multivariate or A/B test. If you haven't set up your test yet, refer to [Creating multivariate and A/B tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) for steps.

After your campaign has launched, you can check how each variant is performing by selecting your campaign from the **Campaigns** section of the dashboard. 

## Analytics by optimization option

Your analytics view will vary depending on if you selected an [optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) during your initial setup.

### No optimization

If you selected **No optimization** when setting up your campaign, your analytics view will stay the same. The **Campaign Analytics** page of your campaign will show the performance of your variants against your control group, if you included one.

![Performance section of the Campaign Analytics for an email campaign with multiple variants. The table lists various performance metrics for each variant, such as recipients, bounces, clicks, and conversions.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

For more details, refer to the [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) article for your messaging channel.

### Winning Variant

If you selected **Winning Variant** for your optimization when setting up your campaign, you have access to an additional tab of your campaign analytics called **A/B Test Result**. After the Winning Variant is sent to the remaining users in your test, this tab shows the results of that send.

The **A/B Test Result** is divided into two tabs: **Initial Test** and **Winning Variant**.

{% tabs local %}
{% tab Initial Test %}

The **Initial Test** tab shows the metrics for each variant from the initial A/B test sent to a portion of your target segment. You can see a summary of how all the variants performed and whether or not there was a winner during the test.

If one variant outperformed all the others with better than 95% [confidence]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence), Braze marks that variant with a "Winner" label.

If no variant beats all the others with 95% confidence and you chose to send the best performing variant anyway, the best performing variant will still be sent out and indicated with the label "Winner".

![Results of an initial test sent to determine the Winning Variant where no variant performed better than the others with enough confidence to meet the 95 percent confidence threshold for statistical significance.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### How the Winning Variant is selected

Braze tests all the variants against each other with [Pearson's chi-squared tests](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). This measures whether or not one variant statistically outperforms all others at a significance level of p < 0.05, or what we refer to as 95% significance. If so, the Winning Variant is indicated with the "Winner" label.

This is a separate test from the confidence score, which only describes the performance of a variant compared to the control with a numeric value between 0 and 100%.

A variant can do better than the control group, but the chi-squared testing checks if one variant is better than all of the rest. [Follow-up tests](#recommended-follow-ups) may yield more details.

{% endtab %}
{% tab Winning Variant %}

The **Winning Variant** tab shows the results of the second send, where each remaining user was sent the best performing variant from the initial test. Your **Audience %** will add up to the percentage of the target segment you reserved for the Winning Variant group.

![Results of the Winning Variant sent to the Winning Variant group.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

If you want to see the performance of the Winning Variant throughout the campaign, including the A/B test sends, check the **Campaign Analytics** page.

### Personalized Variant {#personalized-variant}

If you selected **Personalized Variant** for your optimization when setting up your campaign, the **A/B Test Result** is divided into two tabs: **Initial Test** and **Personalized Variant**.

{% tabs local %}
{% tab Initial Test %}

The **Initial Test** tab shows the metrics for each variant from the initial A/B test sent to a portion of your target segment.

![Results of an initial test sent to determine the best performing variant for each user. A table shows the performance of each variant based on various metrics for the target channel.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

By default, the test looks for associations between user’s custom events and their message variant preferences. This analysis detects whether custom events increase or decrease likelihood of responding to a particular message variant. These relationships are then used to determine which users gets which message variant in the final send.

The relationships between custom events and message preferences are displayed in the table on the **Initial Send** tab.

![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

If the test can't find a meaningful relationship between custom events and variant preferences, the test will fall back to a session-based analysis method.

{% details Fallback analysis method %}

**Session-based analysis method**<br>
If the fallback method is used to determine Personalized Variants, the **Initial Test** tab shows a breakdown of users' preferred variants based on a combination of certain characteristics. 

These characteristics are:

- **Recency:** When they last had a session
- **Frequency:** How often they have sessions
- **Tenure:** How long they have been a user

For example, the test may find that most users prefer Variant A, but users who had a session about 3–12 days ago, have between 1–12 days between sessions, and were created in the last 67–577 days tend to prefer Variant B. Therefore, users in that subpopulation received Variant B in the second send, while the rest received Variant A.

![The User Characteristics table, which shows which users are predicted to prefer Variant A and Variant B based on the three buckets they fall in for recency, frequency, and tenure.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**How Personalized Variants are selected**<br>
With this method, an individual user's recommended message is the sum of the effects of their specific recency, frequency, and tenure. Recency, frequency, and tenure are split into buckets, as illustrated in the **User Characteristics** table. The time range of each bucket is determined by the data for users in each individual campaign and will change from campaign to campaign. 

Each bucket can have a different contribution or "push" toward each message variant. The strength of the push for each bucket is determined from user responses in the initial send using [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression). This table only summarizes the results by displaying which variant users in each bucket tended to engage with. Any individual user's actual Personalized Variant depends on the sum of the effects of the three buckets they're in—one for each characteristic.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

The **Personalized Variant** tab shows the results of the second send, where each remaining user was sent the variant they were most likely to engage with.

The three cards on this page show your projected lift, overall results, and the projected results if you sent just the Winning Variant instead. Even if there's no lift, which can sometimes happen, the result is the same as sending only the Winning Variant (a traditional A/B test). 

- **Projected lift:** The improvement in your selected optimization metric for this send due to using Personalized Variants instead of a standard A/B test (if the remaining users only received the Winning Variant).
- **Overall results:** The results of the second send based on your chosen optimization metric (*Unique Opens*, *Unique Clicks*, or *Primary Conversion Event*).
- **Projected results:** The projected results of the second send based on your chosen optimization metric if you had sent just the Winning Variant instead. 

![Personalized Variant tab for a campaign optimized for unique opens. The cards show the Projected Lift, Overall Unique Opens (with Personalized Variant), and Projected Unique Opens (with Winning Variant).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

The table on this page shows the metrics for each variant from the Personalized Variant send. Your **Audience %** adds up to the percentage of the target segment you reserved for the Personalized Variant group.

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Understanding confidence {#understanding-confidence}

Confidence is the statistical measure of how certain we are that a difference in data, like conversion rates, is real and not just due to random chance.

{% alert note %}
Don't see confidence in your results? Confidence will only appear if you have a control group.
{% endalert %}

An important part of your results is the confidence of your results. For example, what if the Control Group had a 20% conversion rate and Variant A had a 25% conversion rate? This seems to indicate that sending Variant A is more effective than sending no message. Having a confidence of 95% means that the difference between the two conversion rates is likely due to an actual difference in users' responses and that there is only a 5% likelihood that the difference has occurred by chance.

Braze compares each variant's conversion rate against the control's conversion rate with a statistical procedure called a [Z&nbsp;Test](https://en.wikipedia.org/wiki/Z-test). A result of 95% or greater confidence, as in the preceding example, indicates that the difference is statistically meaningful. This is true anywhere you see a confidence metric in the Braze dashboard that describes the difference between two messages or user populations.

In general, a confidence of at least 95% is necessary to show that your results are reflective of users' actual preferences, and not due to chance. In rigorous scientific tests, 95% confidence (or otherwise commonly referred to as the "p" value being less than 0.05) is the common benchmark used to determine statistical significance. If you continually fail to achieve 95% confidence, try increasing your sample size or decreasing the number of variants. 

Confidence does not describe whether one variant is better than the others. It is purely a measure of how sure we are that the two (or more) conversion rates are actually different than each other. This is only a function of the sample size and the differences between the apparent conversion rates. Whether the overall rates are high or low does not affect the strength of the confidence measure. It's possible for one variant to have a very different conversion rate from another and yet not have a 95% or higher confidence. It's also possible for two sets of variants to have similar conversion/uplift rates, and yet different confidence.

### Statistically insignificant results

A test that doesn't have a confidence of 95% can still hold important insights. Here are a few things you can learn from a test with statistically insignificant results:

- It's possible that all of your variants had roughly the same effect. Knowing this saves you the time you would've spent making these changes. Sometimes, you may find that conventional marketing tactics, such as repeating your call to action, don't necessarily work for your audience.
- While your results may have been due to chance, they can inform the hypothesis for your next test. If multiple variants appear to have roughly the same results, run some of them again alongside new variants to see if you can find a more effective alternative. If one variant does better, but not by a significant amount, you can perform another test in which this variant's difference is more exaggerated.
- Keep testing! A test with insignificant results should lead to certain questions. Was there truly no difference between your variants? Should you have structured your test differently? You can answer these questions by running follow-up tests.
- While testing is useful for discovering which type of messaging generates the most response from your audience, it's also important to understand which alterations in messaging have only a negligible effect. This allows you to either continue testing for another more effective alternative, or save the time that may have been spent deciding between two alternate messages.

Whether or not your test has a clear winner, it can be helpful to run a [follow-up test](#recommended-follow-ups) to confirm your results or apply your findings to a slightly different scenario.

## Discrepancies between the control group and variant

In in-app message campaigns, the way users are tracked and how impressions are logged can cause discrepancies in the expected split between the control group and variant. This is because the actual impressions logged may not reflect this split, and Braze ultimately has no control over the individual user behavior of who will perform the trigger.

For example, let's say a campaign has a target audience of 200 users at launch, with 100 users in the control group and 100 users in the variant.

The 100 users in the variant receive the in-app message payload, and 50 of them perform the trigger action and see the in-app message. The 100 users in the control group are only tracked if they perform the campaign's trigger action, and 75 of them perform the trigger action and log an impression but don't see the in-app message.

Despite the initial 50/50 split, the unique impressions logged aren't balanced. The variant group has 50 impressions, while the control group has 75 impressions.

### In-app Message Delays 

In triggered in-app message campaigns that include delayed displays, control group impressions will be recorded at the point in time when the end user would have originally received the in-app message. For instance, if a campaign is set to delay the display by one hour, control group impressions will not be logged until the one-hour delay has passed. This ensures accurate tracking of impressions in relation to the intended timing of the message delivery.

## Recommended follow-ups {#recommended-follow-ups}

One multivariate and A/B test can (and should!) inspire ideas for future tests, as well as guide you toward changes in your messaging strategy. Possible follow-up actions include the following:

#### Change your messaging strategy based on test results

Your multivariate results may lead you to change the way you word or format your messaging.

#### Change the way you understand your users

Each test will shed light on your users' behaviors, how users respond to different messaging channels, and the differences (and similarities) among your segments.

#### Improve the way you structure future tests

Was your sample size too small? Were the differences between your variants too subtle? Each test provides an opportunity to learn how to improve future tests. If your confidence is low, your sample size is too small and should be enlarged for future tests. If you find no clear difference between how your variants performed, it's possible that the differences were too subtle to have a discernible effect on users' responses.

#### Run a follow-up test with a larger sample size

Larger samples will increase the chances of detecting small differences between variants.

#### Run a follow-up test using a different messaging channel

If you find that a particular strategy is very effective in one channel, you may want to test that strategy in other channels. If one type of message is effective in one channel but not effective in another, you may be able to conclude that certain channels are more conducive to certain types of messages. Or, perhaps there is a difference between users who are more likely to enable push notifications and those who are more likely to pay attention to in-app messages. Ultimately, running this sort of test will help you learn about how your audience interacts with your different communication channels.

#### Run a follow-up test on a different segment of users

To do this, create another test with the same messaging channel and variants, but choose a different segment of users. For instance, if one type of messaging was extremely effective for engaged users, it may be useful to investigate its effect on lapsed users. It's possible that the lapsed users will respond similarly, or they may prefer another one of the other variants. This test will help you learn more about your different segments and how they respond to different types of messages. Why make assumptions about your segments when you can base your strategy on data?

#### Run a follow-up test based on insights from a previous test

Use the insights you gather from past tests to guide your future ones. Does a previous test hint at one messaging technique being more effective? Are you unsure about what specific aspect of a variant made it better? Running follow-up tests based on these questions will help you generate insightful findings about your users.

#### Compare the long-term impact of different variants

If you're A/B testing re-engagement messages, don't forget to compare the long-term impact of different variants using [Retention Reports]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/). You can use Retention Reports to analyze how each variant impacted any user behavior of your choice days, weeks, a month after message receipt, and see if there is uplift.
