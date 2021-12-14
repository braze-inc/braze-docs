---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1
description: "Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant."

---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. 

A variant that appears to be performing better than others will get sent to more users, while underperforming variants will be targeted at fewer users. Each adjustment is made using a [statistical algorithm][227] that makes sure we are adjusting for real performance differences and not just random chance.

![Intelligence selection][3]

Intelligent Selection will:
- Repeatedly look at performance data and shift campaign traffic toward winning variants gradually
- Ensure that more users receive your best-performing variant without sacrificing satistical confidence.
- Rule out underperforming variants and identify high-performing variants faster than a [traditional A/B test][1].
- Allows you to test more frequently and with greater confidence that your users will see your best message. 

Intelligent Selection is ideal for campaigns that are scheduled to send multiple times. Initial results are needed to begin adjusting your campaign; therefore, a campaign that sends only once will not benefit. For those campaigns, an [A/B test][1] would be more effective.

## How do I add Intelligent Selection to my campaigns?

Campaign:
Intelligent Selection can be added to any multi-send campaign in the "Target Users" step of the Braze campaign wizard. Single send campaigns will be unable to leverage this feature.

Canvas:
When adding variants into your Canvas, click on one of the variant percentages. This will allow you to edit the variant distribution and turn on Intelligent Selection. Intelligent Selection will not be available if you have not yet added conversion events to your Canvas or if your campaign is composed of a solo variant or solo control group.<br><br>![Canvas intelligent selection][2]

## For how long will it run?

For campaigns and Canvases, Intelligent Selection will run until it gathers enough evidence about the "true" conversion rates of the variants. "Enough" is determined by a special metric called "regret". You can think of it as similar to Confidence: when there's enough data to know which variant is best, Intelligent Selection will turn itself off. In most cases, the algorithm will choose one of the variants as the winning variant. This variant will be given 100% of the audience for future sends.

{% alert note %}
It's possible for Intelligent Selection to stop optimizing without picking a single clear winner. Intelligent Selection stops optimizing when it has a 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its current rate.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[2]: {% image_buster /assets/img/intelligent_selection.png %}
