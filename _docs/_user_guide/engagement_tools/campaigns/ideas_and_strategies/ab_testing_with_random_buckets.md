---
nav_title: A/B Testing with Random Buckets
article_title: A/B Testing with Random Buckets
page_order: 7
page_type: tutorial
description: "This how-to article goes over the concept of A/B testing and variants and how you can use them in your Braze campaigns."
page_type: reference
tool:
  - Campaign

---

# A/B Testing with Random Buckets

> This article will cover the concept of A/B testing and Variants, how you can use them in your Braze campaigns, as well as how to assign and implement random bucket numbers to help gather useful data.

A random bucket number is a user attribute that can be used to create uniformly distributed segments of random users. These segments can be leveraged to conduct A/B tests for campaign variants over an extended period of time.

If you have [Canvas][13] in your Braze platform, you will be able to accomplish all of these use cases using Canvas UI.

Here's how you can set up an A/B test with random buckets:

## Step 1: Segment your users by the random bucket attribute

Apply the filter *Random Bucket #*. Once applied, the filter label will change to *Statistical sampling ID*.

{% alert note %}
Each user of your app is randomly assigned a random bucket number between 0-9999 (inclusive).
{% endalert %}

The example below partially documents the creation of segments for a campaign with three variants and a control group. Observe that segments receiving the campaign variants and the control segment do not necessarily need to be equal in size.

Consider the following sample plan for creating segments of equal size for three campaign series variants and a control. Bucket numbers 0 to 2499 correspond to the control segment; bucket numbers 2500 to 4999 correspond to the segment that will receive variant 1; bucket numbers 5000 to 7499 correspond to the segment that will receive variant 2; bucket numbers 7500 to 9999 correspond to the segment that will receive variant 3. You may want to use these types of segments if you want to run a test of three different variants (for instance, three different send times or three different combinations of message channels) and also include a control group.

![Filter Selection][1]

![Example filter][2]

For each of your created segments, including the control group, turn on [Analytics Tracking][14]. When evaluating the success of variants relative to the control group, you will be able to go into your [Custom Events][15] page and view how often each segment has completed certain custom events.

## Step 2: Create your campaign variants

### Step 2a: Create your first variant

Create a campaign and, on the Target Users page, select a segment of recipients. The segment you choose will be one that was created in the prior step.

![Select Campaign Recipient Segment][4]

### Step 2b: Build additional variants

[Duplicate][18] your initial campaign variant and modify it accordingly. For instance, you may decide to change the send time or the combination of messaging channels used. When targeting users, select the segment you wish to receive this new campaign variant. Repeat this step to create your remaining campaign variants. Your control group should not receive any variant of this campaign.

## Step 3: Build out additional messages in your test over time

If you wish, you can continue to send campaign variants to your random bucket segments over time by repeating step 2. One example use case is to test the difference between sending one group 2 notifications in one week, compared to 1. Be sure to plan the workflows of your campaign series variants in advance in order to maintain the integrity of your A/B test.

## Common Use Cases

Because creating a [multivariate test][16] allows you to easily test content, using random buckets is best suited for testing delivery, cadence, and channel combinations.

All of the below use cases can be accomplished within [Canvas][13], a tool built with these types of experiments in mind.

### Delivery

You can compare results between a campaign sent with [scheduled][11], [action-based delivery][17] and [intelligent timing][12].

### Cadence

You can test multiple messaging flows over a period of time. For instance, you can test two different onboarding cadences: one that sends 2 messages in the user's first 2 weeks, and one that sends 3 messages in the user's first 2 weeks. Or, when targeting lapsing users, you can test the effectiveness of sending two winback messages in a week, versus sending just one.

### Messaging channels

You can test the effectiveness of different message channel combinations. For instance, you can compare the impact of using just one email versus an email combined with a push.

### Campaign Variant Percentages

In a campaign, if a variant percentage is modified after initial creation, you will find that the users may be redistributed to other variants.

Initially, users are randomly assigned a particular variant before receiving a campaign for the first time. From then on, each successive time the campaign is received (or the user re-enters a campaign variant) - __they will receive the same variant unless the variant percentages are modified__. If the variant percentages change, users may be redistributed to other variants. Users stay in these variants until percentages are modified again. Control groups remain consistent if the variant percentage is unchanged. Users who previously received messages cannot enter the control group on a later send, nor can any user in the control group ever receive a message.


[1]: {% image_buster /assets/img_archive/random_buckets_filter.png %}
[2]: {% image_buster /assets/img_archive/random_buckets_filterexample.png %}
[4]: {% image_buster /assets/img_archive/random_buckets_target.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/
[12]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[13]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[15]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[17]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/duplicating_segments_and_campaigns/#cloning-a-campaign
