---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 2
description: "This article provides an overview of Intelligent Timing (previously Intelligent Delivery) and how you can leverage this feature in your campaigns and Canvases."

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use Intelligent Timing to deliver your message to each user when Braze determines that user is most likely to engage (open or click), referred to as their optimal send time. This makes it easier for you to check that you're messaging your users at their preferred time, which can lead to higher engagement.

## Use cases

- Send recurring campaigns that aren't time sensitive
- Automate campaigns with users from multiple time zones
- When messaging your most engaged users (they'll have the most engagement data)

## How it works

Braze calculates the optimal send time based on a statistical analysis of your user's past interactions with your app, and their interactions with each messaging channel. The following interaction data is used: 

- Session times
- Push Direct Opens
- Push Influenced Opens
- Email Clicks
- Email Opens (excluding [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens))

For example, Sam might open your emails in the morning regularly, but she opens your app and interacts with notifications in the evening. That means Sam would receive an email campaign with Intelligent Timing in the morning, while she would receive campaigns with push notifications in the evening, when she's more likely to engage.

If a user doesn't have enough engagement data for Braze to calculate the optimal send time, you can specify a [fallback time](#fallback-time).

## Using Intelligent Timing

This section describes how to configure Intelligent Timing for your campaigns and Canvases.

### Campaigns

To use Intelligent Timing in your campaigns:

1. Create a campaign and compose your message.
2. Select **Scheduled Delivery** as your delivery type.
3. Under **Time-Based Scheduling Options**, select **Intelligent Timing**.
4. Select the send date. See [campaign nuances](#campaign-nuances) for considerations.
5. Determine if you want to [only send messages within specific hours](#sending-within-specific-hours).
6. Specify a [fallback time](#fallback-time). This is when the message will send if a user's profile doesn't have enough data to calculate an optimal time.

![Scheduling a campaign with Intelligent Timing][1]

#### Sending messages within specific hours {#sending-within-specific-hours}

If desired, you can choose to limit the optimal time to within a specific window of time. This is useful if your campaign pertains to a specific event, sale, or promotion, but is generally not recommended otherwise. Sending within specific hours functions similarly to Quiet Hours, which is not recommended with Intelligent Timing, as it is counterproductive. See the section in this article on [limitations](#limitations) for more.

1. When configuring Intelligent Timing, select **Only send messages within specific hours**.
2. Enter the start and end time of the delivery window.

![Checkbox for "Only send messages within specific hours" selected, where the time window is set to between 8 am and 12 am in the user's local time.][4]

When a delivery window is specified, Braze only looks at engagement data within the window to determine a user's optimal time. If there isn't enough engagement data within that window, the message sends at the [fallback time](#fallback-time) specified.

#### Preview delivery times

To see an estimate of how many users will receive the message in each hour of the day, use the preview chart (campaigns only).

1. Add segments or filters in the Target Audiences step.
2. In the section **Preview Delivery Times for** (which appears in both the Target Audiences and Schedule Delivery steps), select your channel.
3. Click **Refresh Data**.

![][2]

Whenever you change any settings about Intelligent Timing or your campaign audience, refresh the data again to view an updated chart.

The chart shows users who had enough data to calculate an optimal time in blue and users who will use the fallback time in red. Use the calculation filters to adjust the preview view for a more granular look at either user group.

#### Campaign nuances

Here are some nuances you should be aware of when scheduling campaigns with Intelligent Timing.

##### Launching the campaign

Launch your campaign at least 48 hours before the scheduled send date. This is because of variations in time zones. Braze calculates the optimal time at midnight in Samoa time (UTC+13), one of the first time zones in the world. A single day spans about 48 hours across the globe, which means that if you launch a campaign within that 48-hour buffer, it's possible that a user's optimal time has already passed in their time zone, and the message won't send.

{% alert important %}
If a campaign is launched and a user's optimal time is less than an hour in the past, the message goes out immediately. If the optimal time is more than an hour in the past, the message is not sent at all.
{% endalert %}

##### Choosing segments

If you're targeting an audience that has performed an action in a certain period of time, allow for at least a 3-day window in your segment filters. For example, instead of `First used these apps more than 1 day ago` and `First used these apps less than 3 days ago`, use 1 day and 4 days.

![Filters for the target audience where the campaign targets users who first used these apps between 1 and 4 days ago.][3]

This is also because of time zones—selecting a period of less than 3 days may cause some users to fall out of the segment before their optimal send time is reached.

Learn more about [when Braze checks the eligibility criteria for segments and filters]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

##### A/B tests with optimizations

If you are leveraging [A/B testing with an optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), such as automatically sending the Winning Variant after the A/B test is over, the duration of the campaign will increase. By default, Intelligent Timing campaigns will send the Winning Variant to the remaining users the day after the initial test, but you can change this send date.

We recommend that if you're using both Intelligent Timing and A/B testing, schedule the Winning Variant to send 2 days after the initial test instead of 1 day.

![A/B Testing section of the Target Audiences step where the test ends and sends the Winning Variant two days after the initial test starts.][5]

### Canvas

This section describes how to use Intelligent Timing in your Canvases. The steps vary slightly depending on which Canvas workflow you're using.

{% alert important %}
As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This section is available for reference to understand how Intelligent Timing works in the original editor.<br><br>Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It's an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

{% tabs %}
{% tab Canvas Flow %}

In Canvas Flow, Intelligent Timing is set in Message steps. To use Intelligent Timing in your Canvas:

1. Add a [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) to your Canvas.
2. Go to **Delivery Settings**.
3. Select **Using Intelligent Timing**.
4. Specify a [fallback time](#fallback-time).

A user who enters this step will receive the message at their optimal time on the day they enter IF that time has not yet passed. Note that if a user's optimal time (in local time) has passed on the day they enter a message step, it will send on the next day at the optimal time. Message steps that target multiple channels may send or attempt to send messages at different times for different channels. When the first message in a Message step attempts to send, all users are auto-advanced.

#### Delay steps and Intelligent Timing

When using Intelligent Timing after a [Delay step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), the delivery date may be different depending on how you calculate your delay. This only applies when your delay is set to **After a duration**, as there is a difference between how "days" and "calendar days" are calculated.

- **Days:** 1 day is 24 hours, calculated from the time the user enters the Delay step.
- **Calendar days:** 1 day is the period from when the user enters the Delay step to midnight in their time zone. This means 1 calendar day could be as short as a few minutes.

When using Intelligent Timing, we recommend that you use calendar days for your delays instead of 24-hour days. This is because with calendar days, the message will send on the last day of the delay, at the optimal time. With a 24-hour day, there's a chance the user's optimal time is before they entered the step, which means there will be an extra day added to their delay.

For example, say Luka's optimal time is 2:00 pm. He enters the Delay step at 2:01 pm on March 1, and the delay is set to 2 days.

- Day 1 ends on March 2 at 2:01 pm
- Day 2 ends on March 3 at 2:01 pm

However, Intelligent Timing is set to deliver at 2 pm, which has already passed. So Luka won't receive the message until the following day: March 4 at 2:00 pm.

![Graphic depicting the difference between days and calendar days where if a user's optimal time is 2 pm but they enter the delay step at 2:01 pm and the delay is set to 2 days. Days delivers the message 3 days later because the user entered the step after their optimal time, whereas calendar days delivers the message 2 days later, on the last day of the delay.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}

{% endtab %}
{% tab Original Canvas workflow %}

In the original Canvas workflow, Intelligent Timing is set in the delay section of a Full Step. To use Intelligent Timing in your Canvas:

1. Add a step to your Canvas.
2. Open the **Delay** for your step.
3. Select **Scheduled**.
4. Set a delay using *after*, *in*, or *on the next*.
   - If you select *after*, set the delay in days or weeks. Delays are automatically calculated using calendar days, which means the message sends on the last day of the delay at the user's optimal time. Intelligent Timing is not available for delays shorter than 1 day.
5. Select **Using Intelligent Timing**.
6. Specify a [fallback time](#fallback-time).

{% endtab %}
{% endtabs %}

#### Launching the Canvas

Unlike with campaigns, you don't need to worry about launching your Canvas 48 hours before the send date. This is because Intelligent Timing is set on the step level, not the Canvas level. Instead, we recommend that there is at least a 48-hour delay between the user entering the Canvas and receiving the step where Intelligent Timing is used.

### Fallback time {#fallback-time}

You need to choose a fallback time for the message to send to users in your audience who don't have enough engagement data for Braze to calculate an optimal send time. There are two options:

- the most popular time to use the app among all users
- a specific custom fallback time (in the user's local time zone)

#### Most popular app time

The most popular app time is determined by the average session start time for your workspace (in local time). This time is displayed in red on the [preview chart](#preview-delivery-times) (campaigns only).

For campaigns, if you specified a [delivery window](#sending-within-specific-hours) and the most popular time to use your app falls outside of that window, the message will send closest to the edge of the delivery window. For example, if your delivery window is 1 pm to 8 pm and the most popular app time is 10 pm, the message will send at 8 pm.

**Not enough session data**<br>
In the rare event that your app doesn't have enough session data to calculate when the app is most used (a completely new app with no data), the message will send at 5 pm in the user's local time zone. If the user's local time is unknown, it will send at 5 pm in your company time zone.

It's important to be aware of the limitations of using Intelligent Timing early in a user's lifecycle when limited data is available. It can still be valuable, as even users with few recorded sessions can offer insights into their behavior. However, Braze can more effectively calculate the optimal send time later in a user's lifecycle.

#### Custom fallback time

Use the custom fallback time to choose a different time to send the message. Similar to the most popular app time, the message will send at the fallback time in the user's local time zone. If the user's local time zone is unknown, it will send in your company time zone.

For campaigns with a custom fallback time specified, if you launch the campaign within 24 hours of the send date, users whose optimal times have already passed will receive the campaign at the custom fallback time. If the custom fallback time has already passed in their time zone, the message will send immediately.

## Limitations

- In-app messages, Content Cards, and webhooks are delivered immediately and not given optimal times.
- Intelligent Timing is not available for action-based or API-triggered campaigns.
- Intelligent Timing should not be used in the following scenarios:
    - **Quiet Hours:** Using both Quiet Hours and Intelligent Timing is counterproductive, as Quiet Hours are based on a top-down assumption about user behavior, such as not messaging someone in the middle of the night, whereas Intelligent Timing is based on user activity. Maybe Sam checks her app notifications at 3 am a lot. We don't judge.
    - **Rate limiting:** If both rate limiting and Intelligent Timing are used, there is no guarantee about when the message will be delivered. Daily recurring campaigns with Intelligent Timing do not accurately support a total message send cap.
    - **IP warming campaigns:** Some Intelligent Timing behaviors can cause difficulties in hitting daily volumes that are needed when you are first warming up your IP. This is because Intelligent Timing evaluates segments twice—once when the campaign or Canvas is first created, and again before sending to users to verify that they should still be in that segment. This can cause segments to shift and change, often leading to some users falling out of the segment on the second evaluation. These users don't get replaced, impacting how close to the maximum user cap you can achieve.

## Troubleshooting

### Preview chart showing few users with optimal times

Braze needs a certain amount of engagement data to make a good estimate. If there isn't enough session data or the targeted users have little to no clicks or opens (such as new users), Braze will default to the fallback time. Depending on your configuration, this could be either the most popular app time or a custom fallback time.

### Sending past the scheduled date

Your Intelligent Timing campaign might be sending past the scheduled date if you are leveraging [A/B testing with an optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Campaigns using A/B testing optimizations can automatically send the Winning Variant after the initial test is over, increasing the duration of the campaign. By default, campaigns with an optimization will send the Winning Variant to the remaining users the day after the initial test, but you can change this send date.

If you use Intelligent Timing, we recommend leaving more time for the A/B test to finish and scheduling the Winning Variant to send for 2 days after the initial test instead of 1 day.


[1]: {% image_buster /assets/img/intelligent_timing_1.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
[4]: {% image_buster /assets/img/intelligent_timing_hours.png %}
[5]: {% image_buster /assets/img/intelligent_timing_ab_test_duration.png %}
