---
nav_title: Intelligence FAQs
article_title: Intelligence FAQs
page_order: 0
description: "This article provides answers to frequently asked questions about intelligent channel, intelligent selection, and intelligent timing."
---

# Intelligence FAQs

> This article provides answers to frequently asked questions about intelligent channel, intelligent selection, and intelligent timing.

## Intelligent Selection

### Why is re-eligibility not available when combined with intelligent selection?

We do not allow intelligent selection campaigns to have re-eligibility enabled because it would affect the integrity of the control variant.

Normally, users will re-enter into the same variant that they received before for campaigns with re-eligibility. With intelligent selection, it is not possible to guarantee that a user will receive the same campaign variant because the variant distribution would have shifted due to the optimum allocation aspect for this feature. 

For example, if a campaign is using the variants A(20%)/B(20%)/Control(60%), the variant distribution could be A(15%)/B(5%)/Control(60%) for the second round.

### Why are my intelligent selection variants showing equal sends during the early stages of my campaign?

Intelligent selection allocates variants for sending based on the current status of campaign conversion. It only determines the final variant allocations after the training period, where sends are sent evenly across variants. If you do not wish the intelligent selection to send evenly during the early stages of your campaign, use fixed variants for a traditional A/B test. 

### Will intelligent selection stop optimizing without picking a clear winner? 

Intelligent selection will stop optimizing when it has 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its current rate.

### Why can I not enable intelligent selection in my Canvas or campaign (greyed out)?

Intelligent selection will be unavailable if you have not added conversion events to your campaign or Canvas.

## Intelligent Timing

### Quiet hours

We do not recommend using both intelligent timing and quiet hours for your campaign or Canvas as it is counterproductive; this is because quiet hours are based on top-down assumptions about user behavior, where intelligent timing is based on user user activity.

### Why is my intelligent timing campaign showing little to no sends?

Braze needs a baseline number of data points to make a good estimate. If there is not enough session data or the users targeted have little to no email clicks or opens (e.g., new users), intelligent delivery may default to the app group's most popular hour on that day of the week. If there is insufficient information about the app group, we fall back to a default time defined in `DEFAULT_HOUR`. Note that there is also an option to set a fallback time. 

### How is the most popular app time determined?

The most popular app time is determined by the average session start time for the app group (in local time). This metric can be found in the dashboard when previewing delivery times for a campaign, shown in red. 

### Can I use intelligent timing and rate-limiting?

Braze does not recommend using intelligent timing and rate-limiting as there is no guarantee about when the message will be delivered. 

### Why is my intelligent timing campaign sending past the scheduled date? 

Your intelligent timing campaign might be sending past the scheduled date because you are leveraging A/B testing. Campaigns using A/B testing can send the winning variant automatically after the A/B test is over, which would increase the duration of campaign sending. By default, intelligent timing campaigns will be scheduled to send out the winning variant to the remaining users for the following day, but customers can change this send date. 

We recommend that users with intelligent timing campaigns leave more time for the A/B test to finish and schedule the winning variant to send for two days out instead of one. 

### What does "the edge of the window" mean? 

The edge of the window is defined as the time closest to the user's optimal time. For example, if the optimal time is 10 pm, but the intelligent delivery is 1 pm - 8 pm, the message will be sent at 8 pm. 

### Can I use intelligent timing while IP warming?

Braze does not recommend using intelligent timing when users are first IP warming as some of its behaviors can cause difficulties hitting daily volumes. This is caused by intelligent timing evaluating campaign segments twice. Once, when the campaign is first built, and a second time before sending to users to verify they should still be in that segment. This can cause segments to shift and change, often leading to some users falling out of the segment on the second evaluation. These users do not get replaced, impacting how close to the max user cap you can achieve. 

## Intelligent Delivery

### Send campaigns to users in their local time zone; when do we check the eligibility for users who meet the criteria (segment and/or audience filters)?

Braze performs two checks when campaigns are launched. Once, as soon as the first time zone is identified, which will begin the user cueing process, and the second, at the scheduled time to see if users are still eligible to receive the campaign. 

Be careful when creating campaigns that filter off of other campaigns' sends. For example, if you were to send out two campaigns on the same day for different times and add a filter that only allows users to receive the second campaign if they have received the first, users will not receive the second campaign as no one was eligible when the campaign was first created, and segments were formed.

### How far in advance should I launch an intelligent delivery campaign to successfully deliver it to all users in all time zones?

Braze calculates the optimal time at midnight in Samoan time, the first timezone in the world. In a single day, there are approximately 48 hours that it spans. For example, someone whose optimal time is 12:01 am who lives in Australia has already had their time pass, and it is "too late" to send to them. For these reasons, you need to schedule 48 hours in advance to ensure that everyone in the world who uses your app will get it successfully delivered. 

### Does intelligent delivery predict when a user is most likely to convert, or only when a user is most likely to open/click?

Intelligent delivery predicts when a user is most likely to open/click. 
