---
nav_title: Intelligent Selection
page_order: 1
---

# Intelligent Selection {#intelligent-selection}

Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. A variant that appears to be performing better than others will go to more users, while variants that are underperforming will be targeted at fewer users. Each adjustment is made using a [statistical algorithm][227] that makes sure we are adjusting for real performance differences and not just random chance.

By looking at performance data in real-time and shifting campaign traffic toward winning variants gradually, Intelligent Selection ensures that more users receive your best performing variant, without any sacrifice in statistical confidence. Intelligent Selection will also rule out underperforming variants and identify high performing variants faster than a traditional A/B test. With Intelligent Selection, you can test more frequently and with greater confidence that your users will see your best message.

Intelligent Selection is ideal for campaigns that are scheduled to send multiple times. As Intelligent Selection needs initial results to begin adjusting your campaign, a campaign that sends only once will not benefit. For those campaigns, an A/B test per the above instructions would be more effective.

![Intelligent_Selection_Shot][271]

## Including a Control Group {#including-a-control-group}

When you create a multivariate or A/B test, you can reserve a percentage of your target audience for a randomized control group. Users in the control group will not receive the test, but Braze will monitor their conversion rate for the duration of the campaign. When viewing your results, you’ll be able to compare the conversion rates of your variants against a baseline conversion rate provided by your control group. This lets you compare not only the effects of your variants, but also compare the effects of your variants against the conversion rate that would result if you didn’t send a message at all.

The size of the control group for a campaign with Intelligent Selection will be based on the number of variants. If each variant is being sent to more than 20% of users, then the control group will be 20% and the variants will be split evenly across the remaining 80%. However, if you have multiple variants such that each variant is being sent to less than 20% of users, then the control group will have to become smaller. Once Intelligent Selection starts analyzing the performance of your test, the control group will grow or shrink based on the results.

{% alert note %}
Using a control group when determining winner by Opens or Clicks is not recommended. Because the control group won’t receive the message, those users cannot perform any opens or clicks. Therefore, that group’s conversion rate will be 0% by definition and does not constitute a meaningful comparison to the variants.
{% endalert %}

## Understanding Your Results {#understanding-your}

Congratulations on getting to this stage! However, receiving results is not the last step of the testing process. Now you need to understand what your results mean and apply these insights to your engagement strategy.

### Understanding Confidence {#understanding-confidence}

An important part of your results is the confidence of your results. For example, what if the Control Group had a 20% conversion rate and Variant A had a 25% conversion rate? This seems to indicate that sending Variant A is more effective than sending no message. Having a confidence of 95% means that the difference between the two conversion rates is likely due to an actual difference in users’ responses, and that there is only a 5% likelihood that the difference has occurred by chance.

Braze compares each variant’s conversion rate against the control’s conversion rate with a statistical procedure called a Z Test. A result of 95% or greater confidence, as in the above example, indicates that the variant is, statistically speaking, better than the control. A confidence of 0-5% indicates that the control is better, and any value between 5% and 95% means there is no statistically rigorous winner.

In general, a confidence of at least 95% is necessary to show that your results are reflective of users’ actual preferences, and not due to chance. In rigorous scientific tests, 95% confidence (or otherwise commonly referred to as the “p” value being less than 0.05) is the common benchmark used to determine statistical significance. If you continually fail to achieve 95% confidence, try increasing your sample size or decreasing the number of variants. Confidence does not describe whether one variant is better than the others.

### Statistically Insignificant Results — Now What? {#statistically-insignificant-results}

A test that doesn’t have a confidence of 95% can still hold important insights. Here are a few things you can learn from a test with statistically insignificant results:

- It’s possible that all of your variants had roughly the same effect. Knowing this saves you the time you would’ve spent making these changes. Sometimes, you may find that conventional marketing tactics, such as repeating your call to action, don’t necessarily work for your audience.

- While your results may have been due to chance, they can inform the hypothesis for your next test. If multiple variants appear to have roughly the same results, run some of them again alongside new variants to see if you can find a more effective alternative. If one variant does better, but not by a significant amount, you can perform another test in which this variant’s difference is more exaggerated.

- Keep testing! A test with insignificant results should lead to certain questions. Was there truly no difference between your variants? Should you have structured your test differently? You can answer these questions by running follow-up tests.

- While testing is useful for discovering which type of messaging generates the most response from your audience, it’s also important to understand which alterations in messaging have only a negligible effect.  This allows you to either continue testing for another more effective alternative, or save the time that may have been spent deciding between two alternate messages.

Whether or not your test has a clear winner, it can be helpful to run [follow-up test][140] to confirm your results or apply your findings to a slightly different scenario.


[2]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[3]: https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test
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
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.gif %}
[175]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#scheduling-your-campaign
[180]: {% image_buster /assets/img/ab_create_4.png %}
[205]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[210]: {% image_buster /assets/img/ab_create_8.png %}
[225]: https://www.optimizely.com/resources/sample-size-calculator/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[271]: {% image_buster /assets/img/intelligent_selection1.png %}
[272]: #intelligent-selection
[273]: {{ site.baseurl }}/help/best_practices/push/message_format/
[274]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
