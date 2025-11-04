---
nav_title: Multivariate & A/B testing
article_title: Multivariate and A/B Testing
page_order: 2
page_type: reference
description: "This reference article explains Multivariate and A/B Testing and its benefits."
search_rank: 2
---

# Multivariate and A/B testing

> This page explains what multivariate and A/B testing are and their benefits. For steps on how to create a multivariate or A/B test, refer to [Creating multivariate and A/B tests with Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Multivariate and A/B testing can be  used using [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

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

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Tips for multivariate and A/B testing

Multivariate and A/B testing can unveil powerful insights regarding your users. To receive test results that are truly reflective of your users' behaviors, follow these guidelines.

#### Run the test on a large number of users

Large samples ensure that your results reflect the preferences of your average user and are less likely to be swayed by outliers. Larger sample sizes also allow you to identify Winning Variants that have smaller margins of victory.

#### Randomly sort users into different test groups

Multivariate testing allows you to create up to eight randomly selected test groups. Randomizing is designed to remove bias in the test set and increase the odds of the test groups being similar in composition. This ensures that differing response rates are due to differences in your messages rather than your samples.

#### Know what elements you're trying to test

Multivariate and A/B testing allows you to test the differences between several versions of a message. In some cases, a simple test may be most effective, since isolating changes allows you to identify which elements had the greatest impact on response. Other times, presenting more differences between variants will let you examine outliers and compare different sets of elements. Neither method is necessarily wrong, provided you are clear from the beginning what you are trying to test for.

#### Decide how long your test will run for, and don't end your test early

Before you begin the test, decide how long it will run for and stick to it. Marketers are often tempted to stop tests after they see results that they like, biasing their findings. Resist the temptation to peek and never end your test early!

#### Add your test to campaigns before they launch, not after

If you add your test to a campaign after it has launched, the test won't run properly and you may receive incorrect or misleading statistics. For example, if you add a test to a launched campaign that allows re-entry, users who re-enter the campaign will always go through the same path to prevent data inaccuracies with the test. Additionally, if you change any of the variants while the test is running, the change will invalidate your test and restart it.

For accurate test results:
1. Clone the launched campaign.
2. Stop the original campaign.
3. Then, add the test to the cloned campaign. 

#### If possible, include a control group

Including a [control group]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) lets you know whether your messages have a greater impact on user conversion than sending no message at all.


