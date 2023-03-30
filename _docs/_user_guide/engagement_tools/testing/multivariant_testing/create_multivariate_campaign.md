---
nav_title: Creating Tests
article_title: Creating Multivariate and A/B Tests
page_order: 1
page_type: reference
description: "This article explains how to create multivariate and A/B tests with Braze."
---

# Creating multivariate and A/B tests {#creating-tests}

> You can create a [Multivariate or A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) for any campaign that targets a single channel.

![][2]{: style="max-width:25%;float:right;margin-left:15px;" }

## Step 1: Create your campaign

Click **Create Campaign** and select a channel for the campaign from the section that allows multivariate and A/B testing. For detailed documentation on each messaging channel, refer to [Create a Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Step 2: Compose your variants

You can create up to 8 variants of your message, differentiating between titles, content, images, and more. The number of differences between the messages determines whether this is a multivariate or A/B test. An A/B test examines the effect of changing one variable, whereas a multivariate test examines two or more.

For some ideas on how to get started differentiating your variants, refer to [Tips for different channels](#tips-different-channels).

![][3]

## Step 3: Schedule your campaign

Scheduling your multivariate campaign works the same as scheduling any other Braze campaign. All standard [delivery types][4] are available.

{% alert important %}
If you want to use an [optimization](#optimizations) (available for select channels), schedule your campaign to deliver once. Optimizations aren't available for campaigns that repeat or have re-eligibility turned on.
{% endalert %}

## Step 4: Choose a segment and distribute your users across variants

Select segments to target, then distribute its members across your selected variants and the optional [control group](#including-a-control-group). For best practices around choosing a segment to test with, see [Choosing a segment](#choosing-a-segment).

For push, email, and webhook campaigns scheduled to send once, you can also use an [optimization](#optimizations). This will reserve a portion of your target audience from the A/B test and hold them for a second optimized send based on the results from the first test.

### Control group {#including-a-control-group}

You can reserve a percentage of your target audience for a randomized control group. Users in the control group don't receive the test, but Braze monitors their conversion rate for the duration of the campaign.

When viewing your results, you can compare the conversion rates of your variants against a baseline conversion rate provided by your control group. This lets you compare both the effects of your variants and the effects of your variants against the conversion rate that would result if you didn't send a message at all.

![A/B Testing panel that shows the percentage breakdown of the Control Group, Variant 1, Variant 2, and Variant 3 with 25% for each group.][5]

{% alert important %}
Using a control group when determining winner by Opens or Clicks is not recommended. Because the control group won't receive the message, those users cannot perform any opens or clicks. Therefore, that group's conversion rate is 0% by definition and does not constitute a meaningful comparison to the variants.
{% endalert %}

#### Control groups with Intelligent Selection

The size of the control group for a campaign with [Intelligent Selection][1] is based on the number of variants. If each variant is sent to more than 20% of users, then the control group is 20% and the variants are split evenly across the remaining 80%. However, if you have enough variants that each variant is sent to less than 20% of users, then the control group must become smaller. Once Intelligent Selection starts analyzing the performance of your test, the control group grows or shrinks based on the results.

### Optimizations {#optimizations}

For email, push, webhook, SMS, and WhatsApp campaigns scheduled to send once, you can select an optimization. There are two optimization options: **Winning Variant** and **Personalized Variant**.

![Optimization options listed in the A/B Testing section when choosing your target audience. Three options are listed: No Optimiziation, Winning Variant, and Personalized Variant. Personalized Variant is selected.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Both options work by sending an initial test to a percentage of your target segment. After the test ends, the remaining users in your audience are sent either the best performing variant (Winning Variant) or the variant they're most likely to engage with (Personalized Variant).

{% tabs %}
{% tab Winning Variant %}

Sending the winning variant is similar to a standard A/B test. Users in this group will receive the winning variant once the initial test is complete.

1. Select **Winning Variant**, then specify what percentage of your campaign audience should be assigned to the winning variant group.
2. Configure the following additional settings.

| Field | Description |
| --- | --- | 
| Optimization metric | The metric to optimize for. Choose between *Unique Opens* or *Clicks* for email, *Opens* for push, or *Primary Conversion Rate* for all channels. Selecting *Opens* or *Clicks* to determine the winner does not affect what you choose for the campaign's [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). <br><br>Keep in mind that if you're using a control group, users in the control group can't perform *Opens* or *Clicks*, so the performance of the control group is guaranteed to be `0`. As a result, the control group can't win the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message. |
| Initial test start date | The date and time the initial test starts. |
| Initial test end date | The date and time the initial test ends. This is when the winning variant is sent to the remaining users.<br><br>When sending in users' local time or with Intelligent Timing, the winning variant must be sent at least 24 hours after the A/B test to ensure delivery to all users in the winning variant group. |
| Fallback | What happens if no variant wins by a statistically significant margin. Choose between sending the best performing variant anyway, or ending the test and not sending any further messages. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Personalized Variant %}

Use personalized variants to send each user in your target segment the variant they're most likely to engage with.

To determine the best variant for each user, Braze will send an initial test to a portion of your target audience to look for associations between user characteristics and message preferences. Based on how users respond to each variant in the initial test, these characteristics are used to determine which remaining users will get each variant. If no associations are found and no personalizations can be made, the winning variant is automatically sent to the remaining users. To learn more about how personalized variants are determined, refer to [Multivariate and A/B test analytics]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Select **Personalized Variant**, then specify what percentage of your campaign audience should be assigned to the personalized variant group.
2. Configure the following additional settings.

| Field | Description |
| --- | --- | 
| Optimization metric | The metric to optimize for. Choose between *Unique Opens* or *Clicks* for email, *Opens* for push, or *Primary Conversion Rate* for all channels. Selecting *Opens* or *Clicks* to determine the winner does not affect what you choose for the campaign's [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events). <br><br>Keep in mind that if you're using a control group, users in the control group can't perform *Opens* or *Clicks*, so the performance of the control group is guaranteed to be `0`. As a result, the control group can't win the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message. |
| Initial test start date | The date and time the initial test starts. |
| Initial test end date | The date and time the initial test ends. This is when personalized variants are sent to the remaining users. We recommend 24 hours as a baseline to ensure statistically significant and meaningful results. The more time you allow for the test, the more responses will be received and the more Braze can optimize. This is especially important for email campaigns. Initial tests for personalized variants shouldn't last any less than 4 hours.<br><br>When sending in users' local time or with Intelligent Timing, personalized variants must be sent at least 24 hours after the A/B test to ensure delivery to all users in the personalized variant group. |
| Fallback | What happens if no personalized variants are found. Choose between sending the winning variant instead, or ending the test and not sending any further messages. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Step 5: Designate a conversion event (optional)

Setting a conversion event for a campaign allows you to see how many recipients of that campaign performed a particular action after receiving it.

This only affects the test if you chose **Primary Conversion Rate** in the previous steps. For more information, refer to [Conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). 

## Step 6: Review and launch

On the confirmation page, review the details of your multivariate campaign and launch the test! Next, learn how to [understand your test results]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

## Things to know

### Tips for different channels {#tips-different-channels}

Depending on which channel you select, you'll be able to test different components of your message. Try to compose variants with an idea of what you want to test and what you hope to prove.

What levers do you have to pull and what are the desired effects? While there are millions of possibilities that you can investigate using a multivariate and A/B test, we have some suggestions to get you started:

| Channel | Aspects of Message You Can Change | Results To Look For |
| ---------------------| --------------- | ------------- |
| Push | Copy <br> Image and Emoji Usage <br> Deep Links  <br> Presentation of numbers (e.g., "triple" versus "increase by 200%")  <br> Presentation of time (e.g., "ends at midnight" versus "ends in 6 hours") | Opens  <br> Conversion Rate |
| Email | Subject <br> Display Name <br> Salutation <br> Body Copy <br> Image and Emoji Usage <br> Presentation of numbers (e.g., "triple" versus "increase by 200%") <br> Presentation of time (e.g., "ends at midnight" versus "ends in 6 hours") | Opens  <br> Conversion Rate |
| In-app message | Aspects listed for "push" <br> [Message format][7] | Click <br> Conversion Rate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
When running A/B tests, don't forget to generate [funnel reports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/) that let you understand how each variant impacted your conversion funnel, especially if "conversion" for your business involves taking multiple steps or actions.
{% endalert %}

In addition, the ideal length of your test may also vary depending on the channel. Keep in mind the average amount of time most users may need to engage with each channel.

For instance, if you're testing a push, you may achieve significant results faster than when testing email, since users see pushes immediately, but it may be days before they see or open an email. If you're testing in-app messages, keep in mind that users must open the app in order to see the campaign, so you should wait longer in order to collect results from both your most active app openers as well as your more typical users.

If you're unsure how long your test should run for, the [Intelligent Selection][6] feature can be useful for finding a winning variant efficiently.

### Choosing a segment {#choosing-a-segment}

Since different segments of your users may respond differently to messaging, the success of a particular message says something about both the message itself and its target segment. Therefore, try to design a test with your target segment in mind.

For instance, while active users may have equal response rates to "This deal expires tomorrow!" and "This deal expires in 24 hours!", users who haven't opened the app for a week may be more responsive toward the latter wording since it creates a greater sense of urgency.

Additionally, when choosing which segment to run your test on, be sure to consider whether the size of that segment will be large enough for your test. In general, multivariate and A/B tests with more variants require a larger test group to achieve statistically significant results. This is because more variants will result in fewer users seeing each individual variant.

{% alert tip %}
As a guide, you likely need around 15,000 users per variant (including the control) to achieve 95% confidence in your test results. However, the exact number of users you need could be higher or lower than that depending on your particular case. For more exact guidance on variant sample sizes, consider referring to [Optimizely's Sample Size Calculator](https://www.optimizely.com/resources/sample-size-calculator/).
{% endalert %}

### Control and test group assigments and bias

A common question with control and test group assignments is wondering if they can introduce bias to your testing.

Users are assigned to message variants, Canvas variants, or their respective control groups by concatenating their (randomly generated) user ID with the (randomly generated) campaign or Canvas ID, taking the modulus of that value with 100, and then ordering users into slices that correspond to the percentage assignments for variants and optional control chosen in the dashboard. So, there is no practical way that users' behaviors prior to the creation of a particular campaign or Canvas could vary systematically between variants and control.

#### Mistakes to avoid

There are some common mistakes to avoid creating the appearance of differences based on the messaging channel if audiences are not filtered correctly.

For example, if you send a push message to a wide audience with a control, the test group will only send messages to users with a push token. However, the control group will include both users who do have a push token and users that don't. In this case, your initial audience for the campaign or Canvas must filter for having a push token (`Push Enabled` is `true`). The same must be done for eligibility to receive messages on other channels: opted in, has a push token, subscribed, etc.

{% alert note %}
If you use random bucket numbers for control groups manually, reference this list of [things to watch out for]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) in your control groups.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
[6]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
