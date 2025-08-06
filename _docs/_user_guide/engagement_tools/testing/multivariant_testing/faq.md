---
nav_title: FAQ
article_title: Multivariate and A/B Test FAQs
page_order: 21
page_type: reference
toc_headers: h2
description: "This article covers FAQs for multivariate and A/B tests with Braze."
---

# Multivariate and A/B test FAQs

## Testing basics

### What is the difference between A/B testing and multivariate testing?

#### A/B testing

In A/B testing, the marketer is experimenting with a single variable within the campaign (such as email subject lines or message send time). This involves randomly dividing a subset of the audience into two or more groups, presenting each group with a different variation, and observing which variation exhibits the highest conversion rate. Typically, the best-performing variation is subsequently sent to the remainder of the audience.

#### Multivariate testing 

Multivariate testing is an extension of A/B testing, which allows the marketer to test multiple variables at once to determine the most effective combination. For example, you could test the subject line of your email message, the image that accompanies your text, and the color of the CTA button. This type of testing allows you to explore more variables and variation combinations within a single experiment, and obtain insights faster and more comprehensively than A/B testing. However, testing more variables and combinations within a single experiment requires a larger audience to yield statistical significance.

### How are A/B test results calculated?

Braze tests all the variants against each other with Pearson's chi-squared tests, which measure whether one variant statistically outperforms all others at a significance level of p < 0.05, or what we refer to as 95% significance. Across all variants that exceed this significance threshold, the best-performing variant is determined to be the “winner”.

This is a separate test from the confidence score, which only describes the performance of a variant compared to the control with a numeric value between 0 and 100%. Specifically, it represents our confidence that the standardized difference in conversion rate between the variant and control is significantly greater than chance.

### Why isn't the variant distribution even?

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Running and concluding tests

### When is the initial test over?

When using Winning Variant for single-send campaigns, the test is over when the Winning Variant Send Time arrives. Braze will deem a variant to be the winner if it shows the highest conversion rate by a statistically significant margin.

For recurring, action-based, and API-triggered campaigns, you can use Intelligent Selection to continuously track each variant’s performance data and continuously optimize campaign traffic toward top-performing variants. With Intelligent Selection, rather than explicitly defining an experiment group where users receive random variants, the Braze algorithm will continuously refine its estimate of the best-performing variant, potentially allowing for faster selection of the top performer.

### How does Braze handle users who received a message variant in a recurring campaign or Canvas entry step? 

Users are randomly assigned to a particular variant before receiving the campaign for the first time. Each successive time the campaign is received (or the user re-enters a Canvas variant), they will receive the same variant unless the variant percentages are modified. If the variant percentages change, users may be redistributed to other variants. Users stay in these variants until percentages are modified again. Users will only be redistributed for the variants that were edited.

For example, let’s say we have a campaign or Canvas with three variants. If only Variant A and Variant B are changed or updated, then users in Variant C won’t be redistributed because Variant C's variant percentage wasn't changed. Control groups remain consistent if the variant percentage is unchanged. Users who previously received messages can’t enter the control group on a later send, nor can any user in the control group ever receive a message.

#### What about Experiment Paths?

The same applies because the Canvas paths following an experiment are also variants.

#### Can I take actions to redistribute users in campaigns and Canvases?

The only way to redistribute users in Canvases is to use [Randomized Paths in Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), which will always randomize path assignments when users re-enter the Canvas. However, this isn’t a standard experiment and could invalidate any experiment results because the control group can become contaminated with treatment users.

## Confidence and bias

### Does confidence increase over time?

Confidence increases over time if all else holds constant. Holding constant means there aren’t other marketing factors that could influence variants, such as Variant A talking about a 25% off sale that ends midway through the test.

Confidence is a measurement of how confident Braze is that the variant is different from the control. As more messages are sent, the statistical power of the test increases, which would increase the confidence that measured differences in performance are not due to random chance. Generally, a larger sample size increases our confidence in identifying smaller differences in performance between variants and control.

### Can control and test group assignments introduce bias to testing?

There is no practical way that a user’s attributes or behaviors before the creation of a particular campaign or Canvas could vary systematically between variants and control. 

To assign users to message variants, Canvas variants, or their respective control groups, we start by linking their randomly generated user ID with the randomly generated campaign or Canvas ID. Next, we apply a sha256 hashing algorithm and divide that result by 100, and keep the remainder (also known as a modulus with 100). Finally, we order users into slices that correspond to the percentage assignments for variants (and optional control) chosen in the dashboard.

### Why can't I use rate limiting with a control group?

Braze currently doesn’t support rate limiting with A/B testing that has a control group. This is because rate limiting doesn’t apply to the control group in the same way as the variants, thus introducing bias. Instead, consider using [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), which automatically adjusts the percentage of users that will receive each variant based on analytics and the performance of the campaign.
