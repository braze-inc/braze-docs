---
nav_title: Intelligent selection
article_title: Intelligent Selection
page_order: 1.0
description: "This article covers Intelligent Selection, a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant."
search_rank: 10
toc_headers: h2
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. 

## About Intelligent Selection

A variant that appears to be performing better than others will get sent to more users, while underperforming variants will be targeted at fewer users. Each adjustment is made using a [statistical algorithm](https://en.wikipedia.org/wiki/Multi-armed_bandit) that makes sure Braze is adjusting for real performance differences and not just random chance.

![A/B Testing section of a campaign with Intelligent Selection enabled.]({% image_buster /assets/img/intelligent_selection1.png %})

Intelligent Selection will:
- Repeatedly look at performance data and shift campaign traffic toward Winning Variants gradually.
- Check that more users receive your best-performing variant without sacrificing statistical confidence.
- Rule out underperforming variants and identify high-performing variants faster than a [traditional A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- Test more frequently and with greater confidence that your users will see your best message. 

Intelligent Selection works best for campaigns that send more than once. It needs early performance data to start optimizing, so single-send campaigns won’t benefit. For those campaigns, we recommend using a traditional [A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) instead.

## Prerequisites

{% tabs %}
{% tab Campaign %}
Before adding Intelligent Selection to your campaign, make sure you’ve set things up correctly:

- Your campaign sends on a recurring schedule. Single-send campaigns aren’t supported.
- You’ve added at least two message variants.
- You’ve defined a conversion event to measure performance across variants.
- The re-eligibility window is set to 24 hours or longer. Shorter windows aren’t supported, as they would affect the integrity of the control variant. To learn more, refer to [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
To use Intelligent Selection in a Canvas, confirm the following:
- Your Canvas includes at least two message variants in a Message step.
- You’ve added at least one conversion event.
{% endtab %}
{% endtabs %}

## Adding Intelligent Selection

You can add Intelligent Selection to your campaigns and Canvases.

{% tabs %}
{% tab Campaign %}
Intelligent Selection can be added to any multi-send campaign in the **Target Audiences** step of the Braze campaign composer. Campaigns that send only once are unable to leverage this feature.

{% alert note %}
Intelligent Selection cannot be used in campaigns with a re-eligibility period of less than 24 hours because it would affect the integrity of the control variant. To learn more, refer to [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Add at least one conversion event and two variants to your Canvas. Then, select one of the variant percentages in the Build step. 

![A Canvas with two variants, each set to 50% variant distribution, allowing Intelligent Selection to be enabled.]({% image_buster /assets/img/intelligent_selection.png %})

This allows you to edit the variant distribution and turn on Intelligent Selection. 

![Intelligent Selection option turned on for a Canvas]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection will not be available if you haven't yet added conversion events to your Canvas or if your campaign is composed of a solo variant.
{% endtab %}
{% endtabs %}

## Run time

For campaigns and Canvases, Intelligent Selection will run until it gathers enough evidence about the "true" conversion rates of the variants. "Enough" is determined by a special metric called "regret." You can think of it as similar to confidence in that Intelligent Selection will turn itself off when there's enough data to know which variant is best. 

In most cases, Intelligent Selection will choose one of the variants as the Winning Variant. This variant will be given 100% of the audience for future sends.

{% alert note %}
It's possible for Intelligent Selection to stop optimizing without picking a single clear winner. Intelligent Selection stops optimizing when it has a 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its present rate.
{% endalert %}

## Intelligent Selection variant distribution

Intelligent Selection bases its variant distribution on the current status of campaign conversions. It only determines the final distributions after the training period. 

This means that during the early stages of the campaign, both the 99% and 1% Intelligent Selections may receive approximately equal sends, but the final percentages for variant allocation may be set at 99%—1%.

If you don't want Intelligent Selection to send 50/50 during the early stages of the campaign, we recommend using a traditional A/B test with fixed variants.

## Frequently Asked Questions (FAQ) {#faq}

### Why is re-eligibility in less than 24 hours not available when combined with Intelligent Selection?

We don't allow Intelligent Selection campaigns to have re-eligibility in too short of a window because it would affect the integrity of the control variant. By creating a gap of 24 hours, we help ensure that the algorithm will have a statistically valid dataset to work with.

Normally, campaigns with re-eligibility will cause users to re-enter the same variant they received before. With Intelligent Selection, Braze can't guarantee that a user will receive the same campaign variant because the variant distribution would have shifted due to the optimum allocation aspect for this feature. If the user were to be allowed to re-enter before Intelligent Selection re-examines the variant performance, the data might be skewed due to users who re-entered.

For example, if a campaign is using these variants:

- Variant A: 20%
- Variant B: 20%
- Control: 60%

Then the variant distribution could be the following for the second round:

- Variant A: 15%
- Variant B: 25%
- Control: 60%

### Why are my Intelligent Selection variants showing equal sends during the early stages of my campaign?

Intelligent Selection allocates variants for sending based on the current status of campaign conversion. It only determines the final variant allocations after a training period, where sends are sent evenly across variants. If you don't want the Intelligent Selection to send evenly during the early stages of your campaign, use fixed variants for a traditional A/B test.

### Will Intelligent Selection stop optimizing without picking a clear winner?

Intelligent Selection will stop optimizing when it has 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its current rate.

### Why can't I enable Intelligent Selection in my Canvas or campaign (grayed out)?

Intelligent Selection will be unavailable if:

- You haven't added conversion events to your campaign or Canvas
- You are creating a single-send campaign
- You have reeligibility enabled with a window less than 24 hours
- Your Canvas is composed of a single variant with no additional variants or control groups added
- Your Canvas is composed of a single control group, with no variants added
