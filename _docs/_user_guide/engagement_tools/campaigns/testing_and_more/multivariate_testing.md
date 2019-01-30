---
nav_title: Multivariate Testing
platform: Campaigns
subplatform: Testing and More
page_order: 5
---
# Multivariate Testing

##  Introduction to Multivariate Testing

### What is Multivariate Testing?

A multivariate test is an experiment that compares users’ responses to multiple versions of the same marketing campaign. These versions share similar marketing goals, but differ in wording and style. The objective is to identify the version of the campaign that best accomplishes your marketing goals. This section walks through how to use multivariate testing to test out differences in content. If you'd like to evaluate differences in message scheduling or timing (for instance, sending an abandoned cart message after 1 hour of inactivity versus 1 day of inactivity), please refer to our section on setting up a [Canvas][274].

As an example of a multivariate test, suppose you have two options for a push notification:

- This deal expires tomorrow!
- This deal expires in 24 hours!

Using a multivariate test, you can see which wording results in a higher conversion rate. The next time you send a push notification about a deal, you’ll know which type of wording is more effective.

### The Benefits of Multivariate Testing {#the-benefits-of}

Multivariate testing gives you an easy, clear way to learn about your audience. You no longer have to guess what users will respond to - every campaign becomes an opportunity to try different variants of a message and gauge audience response.

Specific scenarios in which multivariate testing could come in handy include:

- __The first time you’re trying out a messaging type.__ Worried about getting in-app messaging right the first time? Multivariate testing allows you to experiment and learn what resonates with your users.
- __The creation of onboarding campaigns and other campaigns that are constantly being sent out.__ Since most of your users will encounter this campaign, why not ensure that it's as effective as possible?
- __Cases in which you have multiple ideas for messages to send.__ If you are unsure of which to choose, run a multivariate test and then make a data-driven decision.
- __Investigating whether your users respond to “tried and true” marketing techniques.__ Marketers often stick to conventional tactics to engage with users, but every product’s user base is different. Sometimes, repeating your call to action and using social proof won’t get you the results you desired. Multivariate testing lets you step outside the box and discover unconventional tactics that work for your specific audience.

### Five Rules for Multivariate Testing {#five-rules-for}

Multivariate testing can unveil powerful insights regarding your users. To ensure that your test results are truly reflective of your users’ behaviors, you need to:

1. __Run the test on a large number of users.__
Large samples ensure that your results reflect the preferences of your average user and are less likely to be swayed by outliers. Larger sample sizes also allow you to identify winning variants that have smaller margins of victory.

2. __Randomly sort users into different test groups.__
Braze’s multivariate testing feature allows you to create up to eight randomly selected test groups. Randomizing is designed to remove bias in the test set and increase the odds of the test groups being similar in composition. This ensures that differing response rates are due to differences in your messages rather than your samples.

3. __Know what elements you are trying to test.__
Multivariate testing allows you to test differences between several versions of a message. In some cases, a simple test may be most effective, since isolating changes allows you to identify which elements had the greatest impact on response. Other times, presenting more differences between variants will let you examine outliers and compare different sets of elements. Neither method is necessarily wrong, provided you are clear from the beginning what you are trying to test for.

4. __Decide how long your test will run for before beginning the test, and don’t end your test early.__
Marketers are often tempted to stop tests after they see results that they like, biasing their findings. Resist the temptation to peek and never end your test early!

5. __Include a control group if possible.__
Including a control group lets you know whether your messages have a greater impact on user conversion than sending no message at all. Learn more about control groups [here][100].


##  Creating Multivariate Tests with Braze {#creating-tests}

### How To Create a Multivariate Test {#how-to-create}

#### Step 1: Create your campaign

On the Campaigns section of Braze's dashboard, click "Create Campaign" and select a channel for the campaign.

![AB_1_campaign][160]

#### Step 2: Compose your variants

Create up to 8 variants of your message. For some ideas on how to get started differentiating your variants, see [here][70].

![AB_2_variants][170]

#### Step 3: Schedule your campaign

Test scheduling works the same as scheduling any other Braze campaign. All of Braze's [standard campaign scheduling options][175] are available.

#### Step 4: Choose a segment to run your campaign on

Select a segment to send the campaign to. For best practices around choosing a segment to test with, see [here][80].

![AB_4_segments][180]

#### Optional Step: Limit the number of users to test with

Sometimes, you'll want to limit the number of users you send a test to, so that later, once you know which of your variants performs best, you will have users who haven't received the campaign and can be sent the winner. This typically most useful if your test isn't scheduled to recur and you won't be using [Intelligent Selection][90].

![Limit Users][190]

#### Step 5: Distribute users among your variants

Decide what percentage of your target segment should receive each of your variants. Or have [Intelligent Selection][90] handle the distribution for you.

![AB_control][200]

#### Step 6: Designate a Conversion Event

Setting a conversion event for a campaign allows you to see how many of the recipients of that campaign performed a particular action after receiving it. Unlike other campaigns, multivariate tests must define a conversion event. You can read more about our Conversion Events feature [here][205].

#### Step 7: Review and launch

On the confirmation page, review the details of your multivariate campaign and launch the test!

#### Step 8: View results

Once your campaign has launched, you can check how each variant is performing by selecting clicking on your campaign from the Campaigns section of the dashboard.

![AB_8_view_results][210]

You will see a summary of the campaign and statistics on how the different variants are performing. If one variant is outperforming the others with better than [95% confidence][120], Braze will mark that variant with a banner indicating that it is best performing.

| Messaging type | Projected winner is selected based on... |
| ---------------------| ------------- |
| Push | conversion rate (if unavailable, open rate) |
| Email | conversion rate (if unavailable, click rate) |
| In-app message | conversion rate (if unavailable, click rate) |

#### Step 9: Select a winner and continue sending

Once you are satisfied that one of your variants is the best performing, you can edit the campaign and adjust the distribution of users so that 100% of users receive the best performing variant. All users in the segment who have not yet received the campaign (including users who enter the segment at a future date) will then get the best performing variant, provided your campaign is scheduled to send again in the future. If you configured your campaign to only send to a limited number of users initially, this is typically when you would also remove that restriction, so that the best variant can reach as many of your segment users as possible.

Braze tests all the variants and control with a test called the Marascuillo procedure. It measures whether or not one variant statistically outperforms all of the others at a significance level of p < 0.05, or what we refer to as 95% confidence. If so, the winning variant is indicated with the "Winner" label. This is a separate test from the [confidence score][120], which only describes the performance of a variant compared to the control with a numeric value between 0 and 100%. [See this section for more details on how to understand Confidence][120]. Zero, one, or more variants can do better than control, but the Marascuillo procedure tests if one variant is better than all of the rest. [Follow-up tests][140] may yield more details.

![AB_winner][220]

### Tips For Different Channels {#tips-different-channels}

Depending on which channel you select, you'll be able to test different components of your message. Try to compose variants with an idea of what you want to test and what you hope to prove. What levers do you have to pull and what are the desired effects? While there are millions of possibilities that you can investigate using a multivariate test, we have some suggestions to get you started:

| Channel | Aspects of Message You Can Change | Results To Look For |
| ---------------------| --------------- | ------------- |
| Push | Wording, punctuation, use of images and emojis, deep links, presentation of numbers (e.g. "triple" vs. "increase by 200%"), presentation of time (e.g. "ends at midnight" vs. "ends in 6 hours")| Open and conversion rate |
| Email | Subject, display name, salutation | Open and conversion rate |
| - | Use of images, organization of text (e.g. bulleted vs. numbered lists) | Click and conversion  rate |
| - | Reply-to field, sign-off | Unsubscribe and conversion rate |
| In-app Notification | Aspects listed for "push," [message format][273] | Click and conversion rate |

In addition, the ideal length of your test may also vary depending on channel. Keep in mind the average amount of time most users may need to engage with each channel. For instance, if you're testing a push, you may achieve significant results faster than when testing email, since users see pushes immediately, but it may be days before they see or open an email. If you're testing in-app messages, keep in mind that users must open the app in order to see the campaign, so you should wait longer in order to collect results from both your most active app openers as well as your more typical users.

If you're unsure how long your test should run for, the [Intelligent Selection][272] feature can be useful for finding a winning variant efficiently.

### Choosing a Segment {#choosing-a-segment}

Since different segments of your users may respond differently to messaging, the success of a particular message says something about both the message itself and its target segment. Therefore, try to design a test with your target segment in mind. For instance, while active users may have equal response rates to “This deal expires tomorrow!” and “This deal expires in 24 hours!”, users who haven’t opened the app for a week may be more responsive toward the latter wording since it creates a greater sense of urgency.

Additionally, when choosing which segment to run your test on, be sure to consider whether the size of that segment will be large enough for your test. In general, multivariate tests with more variants require a larger test group to achieve [statistically significant results][120]. This is because more variants will result in fewer users seeing each individual variant. As a crude guide, you will likely need around 15,000 users per variant (including the control) to achieve 95% confidence in your test results. However, the exact number of users you need could be higher or lower than that depending on your particular case. For more exact guidance on variant sample sizes, consider referring to [Optimizely's Sample Size Calculator][225].

### Intelligent Selection {#intelligent-selection}

Intelligent Selection is a feature that analyzes the performance of a campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. A variant that appears to be performing better than others will go to more users, while variants that are underperforming will be targeted at fewer users. Each adjustment is made using a [statistical algorithm][227] that makes sure we are adjusting for real performance differences and not just random chance.

By looking at performance data in real-time and shifting campaign traffic toward winning variants gradually, Intelligent Selection ensures that more users receive your best performing variant, without any sacrifice in statistical confidence. Intelligent Selection will also rule out underperforming variants and identify high performing variants faster than a traditional A/B test. With Intelligent Selection, you can test more frequently and with greater confidence that your users will see your best message.

Intelligent Selection is ideal for campaigns that are scheduled to send multiple times. As Intelligent Selection needs initial results to begin adjusting your campaign, a campaign that sends only once will not benefit.

![Intelligent_Selection_Shot][271]

### Including a Control Group {#including-a-control-group}

When you create a multivariate test, you can reserve a percentage of your target audience for a randomized control group. Users in the control group will not receive the test, but Braze will monitor their conversion rate for the duration of the campaign. When viewing your results, you'll be able to compare the conversion rates of your variants against a baseline conversion rate provided by your control group. This lets you compare not only the effects of your variants, but also compare the effects of your variants against the conversion rate that would result if you didn't send a message at all.

The size of the control group for a campaign with Intelligent Selection will be based on the number of variants. If each variant is being sent to more than 20% of users, then the control group will be 20% and the variants will be split evenly across the remaining 80%. However, if you have multiple variants such that each variant is being sent to less than 20% of users, then the control group will have to become smaller. Once Intelligent Selection starts analyzing the performance of your test, the control group will grow or shrink based on the results.	

{% comment %}
  If you choose to use Intelligent Selection, having a control group is optional and is turned off by default. If turned on, the size of the control group for a campaign will be based on the number of variants. If each variant is being sent to more than 20% of users, then the control group will be 20% and the variants will be split evenly across the remaining 80%. However, if you have multiple variants such that each variant is being sent to less than 20% of users, then the control group will have to become smaller. Once Intelligent Selection starts analyzing the performance of your test, the control group will grow or shrink based on the results.
  ![controlgroupsforintelligentselection][1]
{% endcomment %}


## Understanding Your Multivariate Test Results {#understanding-your}

Congratulations on getting to this stage! Receiving your multivariate test results is, however, not the last step of the testing process.  Now you need to understand what your results mean and apply these insights to your engagement strategy.

### Understanding Confidence {#understanding-confidence}

An important part of your results is the confidence of your test.  The confidence shows the reliability of your test results.  For instance, your results may show that “A” had a 20% click rate and “B” had a 25% click rate.  This seems to indicate that “B” is the more effective message.  Having a confidence of 95% means that the difference between the two click rates is likely due to an actual difference in users’ responses, and that there is only a 5% likelihood that the difference is due to chance.

Braze compares each variant's conversion rate against the control's conversion rate with a statistical procedure called a Z Test. A result of 95% or greater confidence, as in the above example, indicates that the variant is, statistically speaking, better than the control. A confidence of 0-5% indicates that the control is better, and any value between 5% and 95% means there is no statistically rigorous winner.

In general, a confidence of at least 95% is necessary to show that your results are reflective of users’ actual preferences, and not due to chance.  In rigorous scientific tests, 95% confidence (or otherwise commonly referred to as the "p" value being less than 0.05) is the common benchmark used to determine statistical significance.  If you continually fail to achieve 95% confidence, try increasing your sample size or decreasing the number of variants.

### Statistically Insignificant Results — Now What? {#statistically-insignificant-results}

A test that doesn't have a confidence of 95% can still hold important insights. Here are a few things you can learn from a test with statistically insignificant results:

- It's possible that all of your variants had roughly the same effect. Knowing this saves you the time you would've spent making these changes. Sometimes, you may find that conventional marketing tactics, such as repeating your call to action, don't necessarily work for your audience.
- While your results may have been due to chance, they can inform the hypothesis for your next test. If multiple variants appear to have roughly the same results, run some of them again alongside new variants to see if you can find a more effective alternative. If one variant does better, but not by a significant amount, you can perform another test in which this variant's difference is more exaggerated.
- Keep testing! A test with insignificant results should lead to certain questions. Was there truly no difference between your variants? Should you have structured your test differently? You can answer these questions by running [follow-up tests.][140]

While multivariate testing is useful for discovering which type of messaging generates the most response from your audience, it’s also important to understand which alterations in messaging have only a negligible effect.  This allows you to either continue testing for another more effective alternative, or save the time that may have been spent deciding between two alternate messages.

Whether or not your multivariate test has a clear winner, it can be helpful to run [follow-up test][140] to confirm your results or apply your findings to a slightly different scenario.

## Recommended Follow-ups {#recommended-follow-ups}

One multivariate test can (and should!) inspire ideas for future multivariate tests, as well as guide you toward changes in your messaging strategy. Possible follow-up actions include:

- __Changing your messaging strategy based on test results.__  Your multivariate results may lead you to change the way you word or format your messaging.

- __Changing the way you understand your users.__ Each multivariate test will shed light on your users’ behaviors, how users respond to different messaging channels, and the differences (and similarities) among your segments.

- __Improving the way you structure future multivariate tests.__  Was your sample size too small? Were the differences between your variants too subtle? Each multivariate test provides an opportunity to learn how to improve future tests.  If your confidence is low, your sample size is too small and should be enlarged for future tests.  If you find no clear difference between how your variants performed, it’s possible that their differences were too subtle to have a discernible effect on users' responses.

- __Running a follow-up test with a larger sample size.__
Larger samples will increase the chances of detecting small differences between variants.

- __Running a follow-up test using a different messaging channel.__
If you find that a particular strategy is very effective in one channel, you may want to test that strategy in other channels.  If one type of message is effective in one channel but not effective in another, you may be able to conclude that certain channels are more conducive to certain types of messages.  Or, perhaps there is a difference between users who are more likely to enable push notifications and those who are more likely to pay attention to in-app messages.  Ultimately, running this sort of test will help you learn about how your audience interacts with your different communication channels.

- __Running a follow-up test on a different segment of users.__
To do this, create another test with the same messaging channel and variants, but choose a different segment of users.  For instance, if one type of messaging was extremely effective for engaged users, it may be useful to investigate its effect on lapsed users. It’s possible that the lapsed users will respond similarly, or they may prefer another one of the other variants.  This sort of test will help you learn more about your different segments and how they respond to different sorts of messages.  Why make assumptions about your segments when you can base your strategy on data?

- __Running a follow-up test based on insights from a previous test.__
Use the intuitions you gather from past tests to guide your future ones. Does a previous test hint at one messaging technique being more effective? Are you unsure about what specific aspect of a variant made it better? Running follow-up tests based on these questions will help you generate insightful findings about your users.

[1]: {% image_buster /assets/img/control_group_check_intelligent_selection.png %}
[10]: #introduction-to
[20]: #what-is
[30]: #the-benefits-of
[40]: #five-rules-for
[50]: #creating-tests
[60]: #how-to-create
[70]: #what-can-you-test
[80]: #choosing-a-segment
[90]: #intelligent-selection
[100]: #including-a-control-group
[110]: #understanding-your
[120]: #understanding-confidence
[130]: #statistically-insignificant-results
[140]: #recommended-follow-ups
[150]: #recap
[160]: {% image_buster /assets/img_archive/multivariate-screen-1.png %}
[170]: {% image_buster /assets/img_archive/multivariate-screen-2.png %}
[175]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#scheduling-your-campaign
[180]: {% image_buster /assets/img_archive/multivariate-screen-3.png %}
[190]: {% image_buster /assets/img_archive/multivariate-screen-4.png %}
[200]: {% image_buster /assets/img_archive/multivariate-screen-5.png %}
[205]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[210]: {% image_buster /assets/img_archive/UpdatedMVBreakdown.png %}
[220]: {% image_buster /assets/img_archive/multivariate-screen-7.png %}
[225]: https://www.optimizely.com/resources/sample-size-calculator/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[230]: {% image_buster /assets/img_archive/UpdatedMVWinner.png %}
[271]: {% image_buster /assets/img_archive/Intelligent_Selection_Shot.png %}
[272]: #intelligent-selection
[273]: {{ site.baseurl }}/help/best_practices/push/message_format/
[274]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
