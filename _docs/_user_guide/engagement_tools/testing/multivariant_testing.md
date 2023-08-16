---
nav_title: Multivariate & A/B Testing
article_title: Multivariate and A/B Testing
page_order: 2
page_type: reference
description: "This reference article explains Multivariate and A/B Testing and its benefits."
search_rank: 2
---

# Multivariate and A/B testing

> This page explains what multivariate and A/B testing are and their benefits. For steps on how to create a multivariate or A/B test, refer to [Creating multivariate and A/B tests with Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Multivariate and A/B testing can be quickly utilized using [Intelligent Selection]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/).

## What are multivariate and A/B testing?

### A/B test

An A/B test is an experiment that compares users' responses to multiple versions of the same marketing campaign. These versions share similar marketing goals but differ in wording and style.

The objective is to identify the version of the campaign that best accomplishes your marketing goals. In this section, we'll walk through how to test the effectiveness of differences in content.

{% alert note %}
If you'd like to evaluate differences in message scheduling or timing (for instance, sending an abandoned cart message after one hour of inactivity versus one day of inactivity), refer to our section on [setting up a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Suppose you have two options for a push notification:

- "This deal expires tomorrow!"
- "This deal expires in 24 hours!"

Using an A/B test, you can see which wording results in a higher conversion rate. The next time you send a push notification about a deal, you'll know which type of wording is more effective. However, this test only examines the effect of one variable—the copy in the push notification.

### Multivariate test

A multivariate test is similar to an A/B test, except it tests the effects of two or more variables. Let's go back to our push notification example. Another variable we might want to test is whether to include an emoji at the end of the message. We'd now be testing two variables (or variates—not to be confused with variants), hence the term "multivariate". To do this, we'd need to test four total versions of the message—two options for the copy multiplied by two options for the emoji (present or not) equals four total message variants.

In Braze documentation, "multivariate test" is used interchangeably with "A/B test", as the process for setting them up is the same.

## Benefits of multivariate and A/B testing {#the-benefits-of}

Multivariate and A/B testing gives you an easy, clear way to learn about your audience. You no longer have to guess what users will respond to—every campaign becomes an opportunity to try different variants of a message and gauge audience response.

Specific scenarios in which multivariate and A/B testing could come in handy include:

- **When trying out a messaging type for the first time:** Worried about getting in-app messaging right the first time? Multivariate testing allows you to experiment and learn what resonates with your users.
- **When creating onboarding campaigns and other campaigns that are constantly sent out:** Since most of your users will encounter this campaign, why not ensure that it's as effective as possible?
- **When you have multiple ideas for messages to send:** If you're unsure of which to choose, run a test and then make a data-driven decision.
- **When investigating whether your users respond to "tried and true" marketing techniques:** Marketers often stick to conventional tactics to engage with users, but every product's user base is different. Sometimes, repeating your call-to-action and using social proof won't get you the results you desired. Multivariate and A/B testing lets you step outside the box and discover unconventional tactics that work for your specific audience.

### Variant distribution

The distribution between variants is not always even. Variant distribution works by independently selecting a random option each time it sends a message-it doesn't plan out sending so that it exactly matches the percentages you have set.

If you have multiple variants that you want to split evenly, you also need to make sure the number of variants are a multiple of 100%. Otherwise, some variants will have a higher percentage of users distributed to that variant compared to others. For example, if your campaign has 7 variants, there can't be an even variant distribution since 7 does not equally divide by 100 as a whole number. In this case, you would have 2 variants of 15% and 5 variants of 14%. 

## Five rules for multivariate and A/B testing {#five-rules-for}

Multivariate and A/B testing can unveil powerful insights regarding your users. To ensure that your test results are truly reflective of your users' behaviors, follow these guidelines.

#### Run the test on a large number of users

Large samples ensure that your results reflect the preferences of your average user and are less likely to be swayed by outliers. Larger sample sizes also allow you to identify winning variants that have smaller margins of victory.

#### Randomly sort users into different test groups

Braze's multivariate feature allows you to create up to eight randomly selected test groups. Randomizing is designed to remove bias in the test set and increase the odds of the test groups being similar in composition. This ensures that differing response rates are due to differences in your messages rather than your samples.

#### Know what elements you're trying to test

Multivariate and A/B testing allows you to test the differences between several versions of a message. In some cases, a simple test may be most effective, since isolating changes allows you to identify which elements had the greatest impact on response. Other times, presenting more differences between variants will let you examine outliers and compare different sets of elements. Neither method is necessarily wrong, provided you are clear from the beginning what you are trying to test for.

#### Decide how long your test will run for, and don't end your test early

Before you begin the test, decide how long it will run for and stick to it. Marketers are often tempted to stop tests after they see results that they like, biasing their findings. Resist the temptation to peek and never end your test early!

#### If possible, include a control group

Including a [control group]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) lets you know whether your messages have a greater impact on user conversion than sending no message at all.


[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.png %}
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[180]: {% image_buster /assets/img/ab_create_4.png %}
[210]: {% image_buster /assets/img/ab_create_8.png %}
[10]: {% image_buster /assets/img/ab_send_winning_variant.png %}
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[intelselection]: {{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
