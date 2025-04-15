---
nav_title: FAQ
article_title: Intelligence FAQ
page_order: 191
description: "This article provides answers to frequently asked questions about Intelligent Channel, Intelligent Selection, and Intelligent Timing."
---

# Frequently asked questions

> This article provides answers to frequently asked questions about the Intelligence Suite.

## Intelligent Selection

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

---

## Intelligent Timing

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

No, [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens) are excluded from calculations for optimal time. This means that send times are based solely on genuine user engagement, providing more accurate timing for your campaigns.

#### How precise is the optimal time?

Intelligent Timing schedules messages during each user’s “most engaged hour” based on their session starts and message open events. Within that hour, the message timing is rounded to the nearest five minutes. For example, if a user’s optimal time is calculated as 4:58 PM, the message will be scheduled for 5:00 PM. There may be slight delays in delivery due to system activity during busy periods.

#### What are the fallback calculations if there is not enough data?

If there are fewer than five relevant events for a user, Intelligent Timing uses the [fallback time][1] in your message settings. 

### Campaign management

#### How far in advance should I launch an Intelligent Timing campaign to successfully deliver it to all users in all time zones?

Braze calculates the optimal time at midnight in Samoa time, one of the first time zones in the world. In a single day, it spans approximately 48 hours. For example, someone whose optimal time is 12:01 am and lives in Australia has already had their optimal time pass, and it's "too late" to send to them. For these reasons, you need to schedule 48 hours in advance to successfully deliver to everyone in the world who uses your app.

#### Why is my Intelligent Timing campaign showing little to no sends?

Braze needs a baseline number of data points to make a good estimate. If there is not enough session data or the users targeted have little to no email clicks or opens (such as new users), Intelligent Timing may default to the workspace's most popular hour on that day of the week. If there isn't enough information about the workspace, we fall back to a default time of 5 pm. You can also choose to set a specific [fallback time]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options).

#### Why is my Intelligent Timing campaign sending past the scheduled date?

Your Intelligent Timing campaign might be sending past the scheduled date because you are leveraging A/B testing. Campaigns using A/B testing can automatically send the Winning Variant after the A/B test is over, increasing the duration of campaign sending. By default, Intelligent Timing campaigns will be scheduled to send out the Winning Variant to the remaining users for the following day, but you can change this send date.

We recommend that if you have Intelligent Timing campaigns, leave more time for the A/B test to finish and schedule the Winning Variant to send for two days out instead of one. 

### Technical considerations

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


[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing#fallback-time
