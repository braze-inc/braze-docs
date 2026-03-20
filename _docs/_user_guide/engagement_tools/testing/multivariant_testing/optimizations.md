---
nav_title: Optimizations
article_title: Optimize A/B Tests with Winning Variant or Personalized Variants
page_order: 1
page_type: reference
description: "Learn how to use Winning Variant or Personalized Variant when creating multivariate and A/B tests."
---

# Optimize A/B tests with Winning Variant or Personalized Variants

When [creating an A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) for email, push, webhook, SMS, and WhatsApp campaigns scheduled to send once, you can select an optimization. There are two optimization options: **Winning Variant** and **Personalized Variant**.

![Optimization options listed in the A/B Testing section when choosing your target audience. Three options are listed: No Optimization, Winning Variant, and Personalized Variant. Personalized Variant is selected.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Both options work by sending an initial test to a percentage of your target segment. After the test ends, the remaining users in your audience are sent either the best performing variant (Winning Variant) or the variant they're most likely to engage with (Personalized Variant).

{% alert tip %}
Optimizations are located in the **Target Audiences** step of campaign creation, under **A/B Testing**.
{% endalert %}

## Winning Variant

Sending the Winning Variant is similar to a standard A/B test. Users in this group will receive the Winning Variant when the initial test is complete.

1. Select **Winning Variant**, then specify what percentage of your campaign audience should be assigned to the Winning Variant group.
2. Configure the following additional settings.

| Field | Description |
| --- | --- | 
| Determine Winning Variant | The metric to optimize for. Choose between *Unique Opens* or *Clicks* for email, *Opens* for push, or *Primary Conversion Rate* for all channels. Selecting *Opens* or *Clicks* to determine the winner does not affect what you choose for the campaign's [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/). <br><br>Keep in mind that if you're using a control group, users in the control group can't perform *Opens* or *Clicks*, so the performance of the control group is guaranteed to be `0`. As a result, the control group can't win the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message. |
| Winning Variant Send Time | The date and time the winning variant is sent. |
| If No Winning Variant Can Be Determined | What happens if no variant wins by a statistically significant margin. Choose between sending the best performing variant anyway, or ending the test and not sending any further messages. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Personalized Variant

Use Personalized Variants to send each user in your target segment the variant they're most likely to engage with.

To determine the best variant for each user, Braze will send an initial test to a portion of your target audience to look for associations between user characteristics and message preferences. Based on how users respond to each variant in the initial test, these characteristics are used to determine which remaining users will get each variant. If no associations are found and no personalizations can be made, the Winning Variant is automatically sent to the remaining users. To learn more about how Personalized Variants are determined, refer to [Multivariate and A/B test analytics]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Select **Personalized Variant**, then specify what percentage of your campaign audience should be assigned to the Personalized Variant group.
2. Configure the following additional settings.

| Field | Description |
| --- | --- | 
| Determine Personalized Variant | The metric to optimize for. Choose between *Unique Opens* or *Clicks* for email, *Opens* for push, or *Primary Conversion Rate* for all channels. Selecting *Opens* or *Clicks* to determine the winner does not affect what you choose for the campaign's [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events). <br><br>Keep in mind that if you're using a control group, users in the control group can't perform *Opens* or *Clicks*, so the performance of the control group is guaranteed to be `0`. As a result, the control group can't win the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message. |
| Personalized Variant Send Time | The date and time the personalized variant is sent. |
| If No personalized Variant Can Be Determined | What happens if no Personalized Variants are found. Choose between sending the Winning Variant instead, or ending the test and not sending any further messages. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Analytics

To learn about the results of your A/B test with an optimization, refer to [Multivariate and A/B test analytics]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

