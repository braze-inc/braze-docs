---
nav_title: Multivariate & A/B Testing
article_title: Multivariate and A/B Testing
page_order: 2
page_type: reference
description: "This reference article explains Multivariate and A/B Testing, their benefits, and how to create them with Braze."

---
# Multivariate and A/B testing

Multivariate and A/B Testing can be quickly utilized using our [Intelligent Selection]({{site.baseurl}}/user_guide/intelligence/intelligent_selection/) feature.

## What are multivariate and A/B testing?

An A/B test is an experiment that compares users’ responses to multiple versions of the same marketing campaign. These versions share similar marketing goals but differ in wording and style.

The objective is to identify the version of the campaign that best accomplishes your marketing goals. In this section, we'll walk through how to test the effectiveness of differences in content.

{% alert note %}
If you'd like to evaluate differences in message scheduling or timing (for instance, sending an abandoned cart message after 1 hour of inactivity versus 1 day of inactivity), please refer to our section on setting up a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Suppose you have two options for a push notification:

- "This deal expires tomorrow!"
- "This deal expires in 24 hours!"

Using an A/B test, you can see which wording results in a higher conversion rate. The next time you send a push notification about a deal, you’ll know which type of wording is more effective.

The above test only examines the effect of one variable—the copy in the push notification. A multivariate test is similar, except it tests the effects of two or more variables. Another variable we might want to test is whether to include an emoji at the end of the message. We'd now be testing two variables (or variates—not to be confused with variants), hence the term "multivariate". To do this, we'd need to test four total versions of the message—two options for the copy multiplied by two options for the emoji (present or not) equals four total message variants.

In Braze documentation, "multivariate test" is used interchangeably with "A/B test".

## The benefits of multivariate and A/B testing {#the-benefits-of}

Multivariate and A/B testing gives you an easy, clear way to learn about your audience. You no longer have to guess what users will respond to—every campaign becomes an opportunity to try different variants of a message and gauge audience response.

Specific scenarios in which multivariate and A/B testing could come in handy include:

- **When trying out a messaging type for the first time:** Worried about getting in-app messaging right the first time? Multivariate testing allows you to experiment and learn what resonates with your users.
- **When creating onboarding campaigns and other campaigns that are constantly sent out:** Since most of your users will encounter this campaign, why not ensure that it's as effective as possible?
- **When you have multiple ideas for messages to send:** If you're unsure of which to choose, run a test and then make a data-driven decision.
- **When investigating whether your users respond to "tried and true" marketing techniques:**  Marketers often stick to conventional tactics to engage with users, but every product’s user base is different. Sometimes, repeating your call-to-action and using social proof won’t get you the results you desired. Multivariate and A/B testing lets you step outside the box and discover unconventional tactics that work for your specific audience.

## Five rules for multivariate and A/B testing {#five-rules-for}

Multivariate and A/B testing can unveil powerful insights regarding your users. To ensure that your test results are truly reflective of your users’ behaviors, follow these guidelines:

1. **Run the test on a large number of users.** Large samples ensure that your results reflect the preferences of your average user and are less likely to be swayed by outliers. Larger sample sizes also allow you to identify winning variants that have smaller margins of victory.
2. **Randomly sort users into different test groups.** Braze's multivariate feature allows you to create up to eight randomly selected test groups. Randomizing is designed to remove bias in the test set and increase the odds of the test groups being similar in composition. This ensures that differing response rates are due to differences in your messages rather than your samples.
3. **Know what elements you're trying to test.** Multivariate and A/B testing allows you to test the differences between several versions of a message. In some cases, a simple test may be most effective, since isolating changes allows you to identify which elements had the greatest impact on response. Other times, presenting more differences between variants will let you examine outliers and compare different sets of elements. Neither method is necessarily wrong, provided you are clear from the beginning what you are trying to test for.
4. **Decide how long your test will run for before beginning the test, and don’t end your test early!** Marketers are often tempted to stop tests after they see results that they like, biasing their findings. Resist the temptation to peek and never end your test early!
5. **If possible, include a control group.** Including a [control group](#including-a-control-group) lets you know whether your messages have a greater impact on user conversion than sending no message at all.

## Creating multivariate and A/B tests with Braze {#creating-tests}

### Step 1: Create your campaign

Click **Create Campaign** and select a channel for the campaign from the section that allows multivariate and A/B testing. For detailed documentation on each messaging channel, refer to [Create a Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

![Create Your Campaign][160]{: style="max-width:30%" }

### Step 2: Compose your variants

You can create up to eight variants of your message, differentiating between titles, content, images, and more. The number of differences between the messages determines whether this is a multivariate or A/B test. 

For some ideas on how to get started differentiating your variants, see the section in this article on [Tips for different channels][70].

![Compose Your Variants][170]

### Step 3: Schedule your campaign

Test scheduling works the same as scheduling any other Braze campaign. All of Braze's standard [delivery types][175] are available.

### Step 4: Choose a segment and distribute your users across variants

Select segments to target, then distribute its members across your selected variants, as well as reserving a portion to send to the winning variant, if necessary.

Decide what percentage of your target segment should receive each of your variants, be in the control group (if any), and what percentage should receive the winning variant once the A/B test is complete.

#### Including a control group {#including-a-control-group}

When you create a multivariate or A/B test, you can reserve a percentage of your target audience for a randomized control group. Users in the control group don't receive the test, but Braze monitors their conversion rate for the duration of the campaign.

When viewing your results, you can compare the conversion rates of your variants against a baseline conversion rate provided by your control group. This lets you compare not only the effects of your variants, but also compare the effects of your variants against the conversion rate that would result if you didn’t send a message at all.

The size of the control group for a campaign with [Intelligent Selection][intelselection] is based on the number of variants. If each variant is sent to more than 20% of users, then the control group is 20% and the variants are split evenly across the remaining 80%. However, if you have multiple variants such that each variant is sent to less than 20% of users, then the control group must become smaller. Once Intelligent Selection starts analyzing the performance of your test, the control group grows or shrinks based on the results.

{% alert important %}
Using a control group when determining winner by Opens or Clicks is not recommended. Because the control group won’t receive the message, those users cannot perform any opens or clicks. Therefore, that group’s conversion rate is 0% by definition and does not constitute a meaningful comparison to the variants.
{% endalert %}

Sending the winning variant automatically is only available for Email, Push, and Webhook campaigns scheduled to send once.

![Choose a Segment][180]

For best practices around choosing a segment to test with, see the section below on [Choosing a Segment][80].

### Step 5: Pick the action that determines the winner

The Winning Variant can be measured by `Unique Opens` or `Clicks` for email, `Opens` for Push, or `Primary Conversion Rate` for all channels. Selecting `Opens` or `Clicks` to determine the winner does not affect what you choose for the campaign’s [conversion events][2].

Keep in mind that if you’re using a control group, users in the control group can't perform `Opens` or `Clicks`, so the “performance” of the control group is guaranteed to be `0`. As a result, the control group cannot “win” the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message.

### Step 6: Schedule when to send the winning variant

Choose a date and time when the winning variant should be sent out.

{% alert note %}
When sending in users’ local time or with Intelligent Timing, the winning variant must be sent at least 24 hours after the A/B test to ensure delivery to all users in the winning variant group.
{% endalert %}

In the dropdown below the date, you can also choose whether or not to send the best performing variant even if it does not win by a statistically significant margin.

#### (Optional) Designate a conversion event

Setting a conversion event for a campaign allows you to see how many recipients of that campaign performed a particular action after receiving it.

This only affects the test if you chose **Primary Conversion Rate** in the previous steps. For more information, refer to [Conversion events][2]. 

### Step 7: Review and launch

On the confirmation page, review the details of your multivariate campaign and launch the test!

## Viewing results of a multivariate campaign

Once your campaign has launched, you can check how each variant is performing by selecting your campaign from the **Campaigns** section of the dashboard. When the testing campaign is complete, you can see a summary of how all the variants performed and whether or not there was a winner during the test.

If one variant outperformed all the others with better than 95% [confidence][confidence], Braze marks that variant with a “Winner” banner. If no variant beats all the others with 95% confidence and you chose to send the best performing variant anyway, the “best” performing variant will still be sent out and indicated with a label that reads “Sent as Winning Variant”.

On the analytics page, you can also see the performance of the Winning Variant throughout the campaign (including the A/B test sends).

![View Results][210]

{% alert note %}
Braze tests all the variants against each other with [Pearson’s chi-squared tests](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). This measures whether or not one variant statistically outperforms all others at a significance level of p < 0.05, or what we refer to as 95% significance. If so, the winning variant is indicated with the “Winner” label.
<br><br>
This is a separate test from the confidence score, which only describes the performance of a variant compared to the control with a numeric value between 0 and 100%.
{% endalert %}

A variant can do better than the control group, but the chi-squared testing checks if one variant is better than all of the rest. [Follow-up tests](#recommended-follow-ups) may yield more details.

### Understanding confidence {#understanding-confidence}

An important part of your results is the confidence of your results. For example, what if the Control Group had a 20% conversion rate and Variant A had a 25% conversion rate? This seems to indicate that sending Variant A is more effective than sending no message. Having a confidence of 95% means that the difference between the two conversion rates is likely due to an actual difference in users’ responses and that there is only a 5% likelihood that the difference has occurred by chance.

Braze compares each variant’s conversion rate against the control’s conversion rate with a statistical procedure called a [Z&nbsp;Test](https://en.wikipedia.org/wiki/Z-test). A result of 95% or greater confidence, as in the above example, indicates that the difference is statistically meaningful. This is true anywhere you see a confidence metric in the Braze dashboard that describes the difference between two messages or user populations.

In general, a confidence of at least 95% is necessary to show that your results are reflective of users’ actual preferences, and not due to chance. In rigorous scientific tests, 95% confidence (or otherwise commonly referred to as the “p” value being less than 0.05) is the common benchmark used to determine statistical significance. If you continually fail to achieve 95% confidence, try increasing your sample size or decreasing the number of variants. Confidence does not describe whether one variant is better than the others.

{% details Statistically insignificant results %}

A test that doesn’t have a confidence of 95% can still hold important insights. Here are a few things you can learn from a test with statistically insignificant results:

- It’s possible that all of your variants had roughly the same effect. Knowing this saves you the time you would’ve spent making these changes. Sometimes, you may find that conventional marketing tactics, such as repeating your call to action, don’t necessarily work for your audience.
- While your results may have been due to chance, they can inform the hypothesis for your next test. If multiple variants appear to have roughly the same results, run some of them again alongside new variants to see if you can find a more effective alternative. If one variant does better, but not by a significant amount, you can perform another test in which this variant’s difference is more exaggerated.
- Keep testing! A test with insignificant results should lead to certain questions. Was there truly no difference between your variants? Should you have structured your test differently? You can answer these questions by running follow-up tests.
- While testing is useful for discovering which type of messaging generates the most response from your audience, it’s also important to understand which alterations in messaging have only a negligible effect.  This allows you to either continue testing for another more effective alternative, or save the time that may have been spent deciding between two alternate messages.

Whether or not your test has a clear winner, it can be helpful to run follow-up test to confirm your results or apply your findings to a slightly different scenario.

{% enddetails %}

### Tips for different channels {#tips-different-channels}

Depending on which channel you select, you’ll be able to test different components of your message. Try to compose variants with an idea of what you want to test and what you hope to prove.

What levers do you have to pull and what are the desired effects? While there are millions of possibilities that you can investigate using a multivariate and A/B test, we have some suggestions to get you started:

| Channel | Aspects of Message You Can Change | Results To Look For |
| ---------------------| --------------- | ------------- |
| Push | Copy <br> Image and Emoji Usage <br> Deep Links  <br> Presentation of numbers (e.g. "triple" vs. "increase by 200%")  <br> Presentation of time (e.g. "ends at midnight" vs. "ends in 6 hours") | Opens  <br> Conversion Rate |
| Email | Subject <br> Display Name <br> Salutation <br> Body Copy <br> Image and Emoji Usage <br> Presentation of numbers (e.g. "triple" vs. "increase by 200%") <br> Presentation of time (e.g. "ends at midnight" vs. "ends in 6 hours") | Opens  <br> Conversion Rate |
| In-app Notification | Aspects listed for "push" <br> [Message format][273] | Click <br> Conversion Rate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
When running A/B tests, don’t forget to generate [funnel reports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/funnel_reports/) that let you understand how each variant impacted your conversion funnel, especially if "conversion" for your business involves taking multiple steps or actions.
{% endalert %}

In addition, the ideal length of your test may also vary depending on the channel. Keep in mind the average amount of time most users may need to engage with each channel.

For instance, if you’re testing a push, you may achieve significant results faster than when testing email, since users see pushes immediately, but it may be days before they see or open an email. If you’re testing in-app messages, keep in mind that users must open the app in order to see the campaign, so you should wait longer in order to collect results from both your most active app openers as well as your more typical users.

If you're unsure how long your test should run for, the [Intelligent Selection][272] feature can be useful for finding a winning variant efficiently.

### Choosing a segment {#choosing-a-segment}

Since different segments of your users may respond differently to messaging, the success of a particular message says something about both the message itself and its target segment. Therefore, try to design a test with your target segment in mind.

For instance, while active users may have equal response rates to “This deal expires tomorrow!” and “This deal expires in 24 hours!”, users who haven’t opened the app for a week may be more responsive toward the latter wording since it creates a greater sense of urgency.

Additionally, when choosing which segment to run your test on, be sure to consider whether the size of that segment will be large enough for your test. In general, multivariate and A/B tests with more variants require a larger test group to achieve statistically significant results. This is because more variants will result in fewer users seeing each individual variant.

{% alert tip %}
As a crude guide, you likely need around 15,000 users per variant (including the control) to achieve 95% confidence in your test results. However, the exact number of users you need could be higher or lower than that depending on your particular case. For more exact guidance on variant sample sizes, consider referring to [Optimizely's Sample Size Calculator](https://www.optimizely.com/resources/sample-size-calculator/).
{% endalert %}

## Recommended follow-ups {#recommended-follow-ups}

One multivariate and A/B test can (and should!) inspire ideas for future tests, as well as guide you toward changes in your messaging strategy. Possible follow-up actions include the following:

**Change your messaging strategy based on test results**<br>
Your multivariate results may lead you to change the way you word or format your messaging.

**Change the way you understand your users**<br>
Each test will shed light on your users’ behaviors, how users respond to different messaging channels, and the differences (and similarities) among your segments.

**Improve the way you structure future tests**<br>
Was your sample size too small? Were the differences between your variants too subtle? Each test provides an opportunity to learn how to improve future tests. If your confidence is low, your sample size is too small and should be enlarged for future tests.  If you find no clear difference between how your variants performed, it’s possible that the differences were too subtle to have a discernible effect on users' responses.

**Run a follow-up test with a larger sample size**<br>
Larger samples will increase the chances of detecting small differences between variants.

**Run a follow-up test using a different messaging channel**<br>
If you find that a particular strategy is very effective in one channel, you may want to test that strategy in other channels.  If one type of message is effective in one channel but not effective in another, you may be able to conclude that certain channels are more conducive to certain types of messages.  Or, perhaps there is a difference between users who are more likely to enable push notifications and those who are more likely to pay attention to in-app messages.  Ultimately, running this sort of test will help you learn about how your audience interacts with your different communication channels.

**Run a follow-up test on a different segment of users**<br>
To do this, create another test with the same messaging channel and variants, but choose a different segment of users.  For instance, if one type of messaging was extremely effective for engaged users, it may be useful to investigate its effect on lapsed users. It’s possible that the lapsed users will respond similarly, or they may prefer another one of the other variants.  This sort of test will help you learn more about your different segments and how they respond to different sorts of messages.  Why make assumptions about your segments when you can base your strategy on data?

**Run a follow-up test based on insights from a previous test**<br>
Use the insights you gather from past tests to guide your future ones. Does a previous test hint at one messaging technique being more effective? Are you unsure about what specific aspect of a variant made it better? Running follow-up tests based on these questions will help you generate insightful findings about your users.

**Compare the long-term impact of different variants**<br>
If you’re A/B testing re-engagement messages, don’t forget to compare the long-term impact of different variants via [Retention Reports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/retention_reports/). You can use Retention Reports to analyze how each variant impacted any user behavior of your choice days, weeks, a month after message receipt, and see if there’s uplift.

[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.png %}
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[180]: {% image_buster /assets/img/ab_create_4.png %}
[210]: {% image_buster /assets/img/ab_create_8.png %}
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[intelselection]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
