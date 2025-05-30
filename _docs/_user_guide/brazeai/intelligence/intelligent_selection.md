---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1
description: "This article covers Intelligent Selection, a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant."
search_rank: 10
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. 

A variant that appears to be performing better than others will get sent to more users, while underperforming variants will be targeted at fewer users. Each adjustment is made using a [statistical algorithm][227] that makes sure we are adjusting for real performance differences and not just random chance.

![A/B Testing section of a campaign with Intelligent Selection enabled.][3]

Intelligent Selection will:
- Repeatedly look at performance data and shift campaign traffic toward Winning Variants gradually.
- Check that more users receive your best-performing variant without sacrificing statistical confidence.
- Rule out underperforming variants and identify high-performing variants faster than a [traditional A/B test][1].
- Test more frequently and with greater confidence that your users will see your best message. 

Intelligent Selection is ideal for campaigns that are scheduled to send multiple times. Initial results are needed to begin adjusting your campaign; therefore, a campaign that sends only once will not benefit. For those campaigns, an [A/B test][1] would be more effective.

## How do I add Intelligent Selection to my campaigns?

### Campaign Intelligent Selection

Intelligent Selection can be added to any multi-send campaign in the **Target Audiences** step of the Braze campaign composer. Campaigns that send only once are unable to leverage this feature.

### Canvas Intelligent Selection

Add at least one conversion event and two variants to your Canvas. Then, select one of the variant percentages in the Build step. 

![A Canvas with two variants, each set to 50% variant distribution, allowing Intelligent Selection to be enabled.][2]

This allows you to edit the variant distribution and turn on Intelligent Selection. 

![Intelligent Selection option turned on for a Canvas][4]

Intelligent Selection will not be available if you haven't yet added conversion events to your Canvas or if your campaign is composed of a solo variant.

{% alert note %}
We do not allow the use of Intelligent Selection with campaigns with re-eligibility enabled in under 24 hours because it would affect the integrity of the control variant. Check out [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection) to learn more.
{% endalert %}

## For how long will it run?

For campaigns and Canvases, Intelligent Selection will run until it gathers enough evidence about the "true" conversion rates of the variants. "Enough" is determined by a special metric called "regret." You can think of it as similar to confidence in that Intelligent Selection will turn itself off when there's enough data to know which variant is best. 

In most cases, Intelligent Selection will choose one of the variants as the Winning Variant. This variant will be given 100% of the audience for future sends.

{% alert note %}
It's possible for Intelligent Selection to stop optimizing without picking a single clear winner. Intelligent Selection stops optimizing when it has a 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its present rate.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[2]: {% image_buster /assets/img/intelligent_selection.png %}
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[4]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit

