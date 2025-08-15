---
nav_title: Intelligent timing
article_title: Intelligent Timing
page_order: 1.3
description: "This article provides an overview of Intelligent Timing (previously Intelligent Delivery) and how you can leverage this feature in your campaigns and Canvases."

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Use Intelligent Timing to deliver your message to each user when Braze determines that user is most likely to engage (open or click), referred to as their optimal send time. This makes it easier for you to check that you're messaging your users at their preferred time, which can lead to higher engagement.

## About Intelligent Timing

Braze calculates the optimal send time based on a statistical analysis of your user's past interactions with your app, and their interactions with each messaging channel. The following interaction data is used: 

- Session times
- Push Direct Opens
- Push Influenced Opens
- Email Clicks
- Email Opens (excluding [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))

For example, Sam might open your emails in the morning regularly, but she opens your app and interacts with notifications in the evening. That means Sam would receive an email campaign with Intelligent Timing in the morning, while she would receive campaigns with push notifications in the evening, when she's more likely to engage.

If a user doesn't have enough engagement data for Braze to calculate the optimal send time, you can specify a fallback time.

## Use cases

- Send recurring campaigns that aren't time sensitive
- Automate campaigns with users from multiple time zones
- When messaging your most engaged users (they'll have the most engagement data)

## Using Intelligent Timing

This section describes how to configure Intelligent Timing for your campaigns and Canvases.

{% tabs local %}
{% tab Campaign %}
### Step 1: Add intelligent timing

1. Create a campaign and compose your message.
2. Select the **Scheduled Delivery** as your delivery type.
3. Under **Time-Based Scheduling Options**, select **Intelligent Timing**.
4. Set the entry frequency. For one-time sends, select **Once** and select a send date. For recurring sends, select **Daily**, **Weekly**, or **Monthly** and configure the recurrence options. See [limitations](#limitations) for more guidance.
5. Optionally, configure [Quiet Hours](#quiet-hours).
6. Specify a [fallback time](#campaign-fallback). This is when the message will send if a user's profile doesn't have enough data to calculate an optimal time.

![Campaign scheduling screen showing Intelligent Timing with fallback time and Quiet Hours settings]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Quiet Hours {#quiet-hours}

Use Quiet Hours to prevent messages from sending during specific hours. This is helpful when you want to avoid sending messages during early morning hours or overnight, while still allowing Intelligent Timing to determine the best delivery window.

{% alert note %}
Quiet Hours has replaced the **Only send within specific hours** setting. Instead of choosing when messages can be sent, you now choose when they shouldn’t be sent. For example, to send messages between 4 pm and 6 pm, set Quiet Hours from 6 pm to 4 pm the next day.
{% endalert %}

1. Select **Enable Quiet Hours**.
2. Select the start and end time when **not** to send messages.

![Quiet Hours toggle turned on with start and end time set to block message delivery overnight]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

When Quiet Hours are turned on, Braze won't send messages during the quiet period—even if that time matches a user's optimal send time. If a user's optimal time falls within the quiet window, the message will be sent instead at the nearest edge of the window.

For example, if Quiet Hours are set from 10:00 PM to 6:00 AM, and a user's optimal time is 5:30 AM, Braze will hold the message and deliver it at 6:00 AM—the closest time outside the quiet window.

#### Preview delivery times

To see an estimate of how many users will receive the message in each hour of the day, use the preview chart (campaigns only).

1. Add segments or filters in the Target Audiences step.
2. In the section **Preview Delivery Times for** (which appears in both the Target Audiences and Schedule Delivery steps), select your channel.
3. Click **Refresh Data**.

![Delivery preview chart for Android Push showing peak engagement time between 12 to 2 PM, and the most popular app time being 2 PM.]({% image_buster /assets/img/intel-timing-preview.png %})

### Step 2: Choose a send date

Next, select a send date for your campaign. Keep the following in mind, when scheduling campaigns with Intelligent Timing:

#### Launch campaign 48 hours in advance

Launch your campaign at least 48 hours before the scheduled send date. This is because of variations in time zones. Braze calculates the optimal time at midnight in Samoa time (UTC+13), one of the first time zones in the world. A single day spans about 48 hours across the globe, which means that if you launch a campaign within that 48-hour buffer, it's possible that a user's optimal time has already passed in their time zone, and the message won't send.

{% alert important %}
If a campaign is launched and a user's optimal time is less than an hour in the past, the message goes out immediately. If the optimal time is more than an hour in the past, the message is not sent at all.
{% endalert %}

#### 3-day window for segment filters

If you're targeting an audience that has performed an action in a certain period of time, allow for at least a 3-day window in your segment filters. For example, instead of `First used app more than 1 day ago` and `First used app less than 3 days ago`, use 1 day and 4 days.

![Filters for the target audience where the campaign targets users who first used app between 1 and 4 days ago.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

This is also because of time zones—selecting a period of less than 3 days may cause some users to fall out of the segment before their optimal send time is reached.

For more information, refer to [FAQ: Intelligent Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Schedule wining variants 2 days after A/B test

If you are leveraging [A/B testing with an optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), such as automatically sending the **Winning Variant** or using a **Personalized Variant**, Intelligent Timing may affect the duration and timing of your campaign.

When using Intelligent Timing, we recommend scheduling the Winning Variant send time at least **2 days after** the A/B test begins. For example, if your A/B test starts on April 16 at 4:00 PM, schedule the Winning Variant to send no sooner than April 18 at 4:00 PM. This gives Braze enough time to evaluate user behavior and send messages at the optimal time.

![A/B testing sections showing A/B test with Winning Variant selected, with winning criteria, send date, and local send time selected]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Step 3: Choose a delivery window (optional)

Optionally, you can choose to limit the delivery window. This may be useful if your campaign pertains to a specific event, sale, or promotion, but is generally not recommended when using Intelligent Timing. For more information, refer to [limitations](#limitations).

When specified, Braze only uses engagement data within that window to determine a user's optimal delivery time. If there isn't enough engagement data within that window, the message sends at your set fallback time.

To set a delivery window:

1. When configuring Intelligent Timing, select **Only send messages within specific hours**.
2. Enter the start and end time of the delivery window.

![Checkbox for "Only send messages within specific hours" selected, where the time window is set to between 8 am and 12 am in the user's local time.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Step 4: Choose a fallback time {#campaign-fallback}

Choose a fallback time to use if a user's profile doesn't have enough data to calculate an optimal delivery time.

![Scheduling a campaign with Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Step 5: Preview delivery times

To see an estimate of how many users will receive the message in each hour of the day, use the preview chart.

1. Add segments or filters in the Target Audiences step.
2. In the section **Preview Delivery Times for** (which appears in both the Target Audiences and Schedule Delivery steps), select your channel.
3. Select **Refresh Data**.

![Example preview of delivery times for Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Whenever you change any settings about Intelligent Timing or your campaign audience, refresh the data again to view an updated chart.

The chart shows users who had enough data to calculate an optimal time in blue and users who will use the fallback time in red. Use the calculation filters to adjust the preview view for a more granular look at either user group.
{% endtab %}

{% tab Canvas %}

### Step 1: Add Intelligent Timing

In your Canvas, add a [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), then go to **Delivery Settings** and select **Using Intelligent Timing**.

Messages will be sent to users who entered the step that day at their optimal local time. However, if their optimal time has already passed that day, it'll be delivered at that time during the following day instead. Message steps that target multiple channels may send or attempt to send messages at different times for different channels. When the first message in a Message step attempts to send, all users are auto-advanced.

### Step 2: Choose a fallback time

Choose a fallback time for the message to send to users in your audience who don't have enough engagement data for Braze to calculate an optimal send time. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Step 4: Add a Delay step

Unlike with campaigns, you don't need to launch your Canvas 48 hours before the send date because Intelligent Timing is set on the step level, not the Canvas level.

Instead, add a [Delay step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) of at least a two calendar days between the user entering the Canvas and when they receive the Intelligent Timing step.

#### Calendar vs. 24-hour days

When using Intelligent Timing after a Delay step, the delivery date may vary depending on how you calculate your delay. This only applies when your delay is set to **After a duration**, as there is a difference between how "days" and "calendar days" are calculated.

- **Days:** 1 day is 24 hours, calculated from the time the user enters the Delay step.
- **Calendar days:** 1 day is the period from when the user enters the Delay step to midnight in their time zone. This means 1 calendar day could be as short as a few minutes.

When using Intelligent Timing, we recommend that you use calendar days for your delays instead of 24-hour days. This is because with calendar days, the message will send on the last day of the delay, at the optimal time. With a 24-hour day, there's a chance the user's optimal time is before they entered the step, which means there will be an extra day added to their delay.

For example, say Luka's optimal time is 2:00 pm. He enters the Delay step at 2:01 pm on March 1, and the delay is set to 2 days.

- Day 1 ends on March 2 at 2:01 pm
- Day 2 ends on March 3 at 2:01 pm

However, Intelligent Timing is set to deliver at 2 pm, which has already passed. So Luka won't receive the message until the following day: March 4 at 2:00 pm.

![Graphic depicting the difference between days and calendar days where if a user's optimal time is 2 pm but they enter the delay step at 2:01 pm and the delay is set to 2 days. Days delivers the message 3 days later because the user entered the step after their optimal time, whereas calendar days delivers the message 2 days later, on the last day of the delay.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limitations

- In-app messages, Content Cards, and webhooks are delivered immediately and not given optimal times.
- Intelligent Timing is not available for action-based or API-triggered campaigns.
- Intelligent Timing should not be used in the following scenarios:
    - **Rate limiting:** If both rate limiting and Intelligent Timing are used, there is no guarantee about when the message will be delivered. Daily recurring campaigns with Intelligent Timing do not accurately support a total message send cap.
    - **IP warming campaigns:** Some Intelligent Timing behaviors can cause difficulties in hitting daily volumes that are needed when you are first warming up your IP. This is because Intelligent Timing evaluates segments twice—once when the campaign or Canvas is first created, and again before sending to users to verify that they should still be in that segment. This can cause segments to shift and change, often leading to some users falling out of the segment on the second evaluation. These users don't get replaced, impacting how close to the maximum user cap you can achieve.

## Troubleshooting

### Preview chart showing few users with optimal times

Braze needs a certain amount of engagement data to make a good estimate. If there isn't enough session data or the targeted users have little to no clicks or opens (such as new users), Braze will default to the fallback time. Depending on your configuration, this could be either the most popular app time or a custom fallback time.

### Impact of time zone on Intelligent Timing delivery

Intelligent Timing relies on the specified local time zone of each user, so the scheduled delivery date and time may vary across users.

If users don't receive messages as expected, check that the time zone field in their profile is populated correctly. If the time zone field is empty, the user may receive messages that align with the company's time zone instead of their local time.

### Sending past the scheduled date

Your Intelligent Timing campaign might be sending past the scheduled date if you are leveraging [A/B testing with an optimization]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Campaigns using A/B testing optimizations can automatically send the Winning Variant after the initial test is over, increasing the duration of the campaign. By default, campaigns with an optimization will send the Winning Variant to the remaining users the day after the initial test, but you can change this send date.

If you use Intelligent Timing, we recommend leaving more time for the A/B test to finish and scheduling the Winning Variant to send for 2 days after the initial test instead of 1 day.

## Frequently Asked Questions (FAQ) {#faq}

### General

#### What does Intelligent Timing predict?

Intelligent Timing focuses on predicting when a user is most likely to open or click your messages to ensure your messages reach users at optimal engagement times.

#### Is Intelligent Timing calculated separately for each day of the week?

No, Intelligent Timing isn’t tied to specific days. Instead, it personalizes send times based on each user’s unique engagement patterns and the channel you’re using, such as email or push notifications. This ensures your messages reach users when they’re most receptive.

### Calculations

#### What data is used to calculate the optimal time for each user?

To calculate the optimal time, Intelligent Timing:

1. Analyzes the interaction data for each user recorded by the Braze SDK. This includes:
  - Session times
  - Push direct opens
  - Push influenced opens
  - Email clicks
  - Email opens (excluding machine opens)
2. Groups these events by time, identifying the optimal send time for each user.

#### Are Machine Opens included when calculating optimal time?

No, [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) are excluded from calculations for optimal time. This means that send times are based solely on genuine user engagement, providing more accurate timing for your campaigns.

#### How precise is the optimal time?

Intelligent Timing schedules messages during each user’s “most engaged hour” based on their session starts and message open events. Within that hour, the message timing is rounded to the nearest five minutes. For example, if a user’s optimal time is calculated as 4:58 PM, the message will be scheduled for 5:00 PM. There may be slight delays in delivery due to system activity during busy periods.

#### What are the fallback calculations if there is not enough data?

If there are fewer than five relevant events for a user, Intelligent Timing uses the fallback time in your message settings. 

### Campaigns

#### How far in advance should I launch an Intelligent Timing campaign to successfully deliver it to all users in all time zones?

Braze calculates the optimal time at midnight in Samoa time, one of the first time zones in the world. In a single day, it spans approximately 48 hours. For example, someone whose optimal time is 12:01 am and lives in Australia has already had their optimal time pass, and it's "too late" to send to them. For these reasons, you need to schedule 48 hours in advance to successfully deliver to everyone in the world who uses your app.

#### Why is my Intelligent Timing campaign showing little to no sends?

Braze needs a baseline number of data points to make a good estimate. If there is not enough session data or the users targeted have little to no email clicks or opens (such as new users), Intelligent Timing may default to the workspace's most popular hour on that day of the week. If there isn't enough information about the workspace, we fall back to a default time of 5 pm. You can also choose to set a specific fallback time.

#### Why is my Intelligent Timing campaign sending past the scheduled date?

Your Intelligent Timing campaign might be sending past the scheduled date because you are leveraging A/B testing. Campaigns using A/B testing can automatically send the Winning Variant after the A/B test is over, increasing the duration of campaign sending. By default, Intelligent Timing campaigns will be scheduled to send out the Winning Variant to the remaining users for the following day, but you can change this send date.

We recommend that if you have Intelligent Timing campaigns, leave more time for the A/B test to finish and schedule the Winning Variant to send for two days out instead of one. 

### Functionality

#### When does Braze check the eligibility criteria for segment and audience filters?

Braze performs two checks when a campaign is launched:

1. **Initial check:** At midnight in the first timezone on the day of send.
2. **Scheduled time check:** Just before sending at the time Intelligent Timing selected for the user.

Be careful when filtering based on other campaign sends to avoid targeting ineligible segments. For example, if you were to send out two campaigns on the same day for different times, and add a filter that only allows users to receive the second campaign if they’ve received the first, users won’t receive the second campaign. This is because no one was eligible when the campaign was first created and segments were formed.

#### Can I use Quiet Hours in my Intelligent Timing campaign?

Quiet Hours can be used on a campaign that uses Intelligent Timing. The Intelligent Timing algorithm will avoid Quiet Hours so that it still sends the message to all eligible users. That said, we recommend turning Quiet Hours off unless there are policy, compliance, or other legal implications to when messages can and can't be sent.

#### What happens if the optimal time for a user is within the Quiet Hours? 

If the determined optimal time falls within Quiet Hours, Braze finds the nearest edge of the Quiet Hours and schedules the message for the next allowable hour before or after Quiet Hours. The message is enqueued to send at the closest boundary of Quiet Hours relative to the optimal time.

#### Can I use Intelligent Timing and rate-limiting?

Rate limiting can be used on a campaign that uses Intelligent Timing. However, the nature of rate limiting means that some users may receive their message at a less-than-optimal time, particularly if a large number of users relative to the rate limit size are scheduled at the fallback time because of insufficient data. 

We recommend using rate limiting on an Intelligent Timing campaign only when there are technical requirements that must be met using rate limiting.

#### Can I use Intelligent Timing while IP warming?

Braze doesn’t recommend using Intelligent Timing when users are first IP warming, as some of its behaviors can cause difficulties hitting daily volumes. This is caused by Intelligent Timing evaluating campaign segments twice. Once when the campaign is first built, and a second time before sending to users to verify they should still be in that segment.

This can cause segments to shift and change, often leading to some users falling out of the segment on the second evaluation. These users don’t get replaced, impacting how close to the maximum user cap you can achieve.

#### How is the most popular app time determined?

The most popular app time is determined by the average session start time for the workspace (in local time). This metric can be found in the dashboard when previewing times for a campaign, shown in red.

#### Does Intelligent Timing account for machine opens?

Yes, machine opens are filtered out by Intelligent Timing, so they do not influence its output.

#### How can I make sure Intelligent Timing works as well as possible?

Intelligent Timing uses each user’s individual history of message engagement at whatever times they received messages. Before using Intelligent Timing, make sure that you have sent users messages at different times of the day. That way, you can “sample” when might be the best time for each user. Inadequately sampling different times of day may result in Intelligent Timing picking a suboptimal time of send for a user.



