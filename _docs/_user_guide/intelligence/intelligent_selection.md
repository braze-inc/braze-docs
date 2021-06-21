---
nav_title: Intelligent Selection
page_order: 1
description: "Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant."
Tool:
  - Dashboard
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. 

A variant that appears to be performing better than others will go to more users, while variants that are underperforming will be targeted at fewer users. Each adjustment is made using a [statistical algorithm][227] that makes sure we are adjusting for real performance differences and not just random chance.

By repeatedly looking at performance data and shifting campaign traffic toward winning variants gradually, Intelligent Selection ensures that more users receive your best-performing variant, without any sacrifice in statistical confidence. Intelligent Selection will also rule out underperforming variants and identify high performing variants faster than a [traditional A/B test][1]. With Intelligent Selection, you can test more frequently and with greater confidence that your users will see your best message.

Intelligent Selection is ideal for campaigns that are scheduled to send multiple times. As Intelligent Selection needs initial results to begin adjusting your campaign, a campaign that sends only once will not benefit. For those campaigns, an [A/B test][1] would be more effective.

![Intelligent_Selection_Shot][271]

## For how long will it run?

For Campaigns and Canvases, Intelligent Selection will run until it gathers enough evidence about the "true" conversion rates of the variants. "Enough" is determined by a special metric called "regret". You can think of it as similar to Confidence: when there's enough data to know which variant is best, Intelligent Selection will turn itself off. In most cases, one of the variants will be chosen by the algorithm as the winning variant. This variant will be given 100% of the audience for future sends.

{% alert note %}
It's possible for Intelligent Selection to stop optimizing without picking a single clear winner. Intelligent Selection stops optimizing when it has a 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its current rate.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[271]: {% image_buster /assets/img/intelligent_selection1.png %}
