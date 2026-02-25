---
nav_title: Variant distribution
article_title: Variant distribution
page_order: 1
page_type: reference
description: "This reference article explains how Braze distributes users across variants in A/B and multivariate tests."
tool:
  - Campaign
  - Canvas
---

# Variant distribution

> When you set up an A/B or multivariate test, each send independently assigns users to variants based on the percentages you configure. Because assignment is randomized, the actual distribution may not match your percentages exactly—especially with smaller sample sizes.

## How it works

Every time a message is sent in a multivariate campaign, the system independently selects a random option according to the percentages you set and assigns a variant based on the result. It's like flipping a coin—anomalies are possible. If you've ever flipped a coin 100 times, you know that you probably won't get an exact 50-50 split between heads and tails every time, even though you only have two choices. You might get 52 heads and 48 tails.

If you have multiple variants that you want to split evenly, make sure the number of variants is a multiple of 100. Otherwise, some variants will have a higher percentage of users distributed to that variant compared to others. For example, if your campaign has 7 variants, there can't be an even variant distribution since 7 does not equally divide by 100 as a whole number. In this case, you would have 2 variants of 15% and 5 variants of 14%.

## In-app message distribution

When running an A/B test on in-app messages, your analytics may appear to show a higher variant distribution between one variant and another, even if they have an even percentage split. For example, consider the following graph of *Unique Recipients* for Variant A and Variant C.

![Unique Recipients graph showing Variant A with a consistently higher count than Variant C, despite an even percentage split.]({% image_buster /assets/img/variant_distribution_iam.png %})

Variant A has a consistently higher count of *Unique Recipients* than Variant C. This isn't due to variant distribution, but rather how *Unique Recipients* are calculated for in-app messages. For in-app messages, *Unique Recipients* are actually *Unique Impressions*, which is the total number of people who received and viewed the in-app message. This means if a user doesn't receive the message for whatever reason or decides not to view it, they are not included in the *Unique Recipients* count, and the variant distribution can appear skewed.
