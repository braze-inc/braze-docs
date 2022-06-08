---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 2
description: "When scheduling a campaign, you can use Intelligent Timing to deliver your message to each user at the time which Braze determines that an individual is most likely to engage. This article covers how to implement Intelligent Timing in your campaigns and Canvases."

---

# Intelligent Timing

> This article covers how to implement Intelligent Timing in your campaigns and Canvases. For more details on Intelligent Timing and its benefits, check out our [Intelligent Timing](https://learning.braze.com/intelligent-timing) Braze Learning course.

When [scheduling a campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/), you can use Intelligent Timing (previously Intelligent Delivery) to deliver your message to each user when Braze determines that an individual is most likely to engage (open or click).

Braze calculates the optimal send time based on a statistical analysis of your user’s past interactions with your messaging (on a per-channel basis) and app. To enable Intelligent Timing, select **Intelligent Timing** on the **Delivery** page when creating a scheduled delivery campaign. Note that this feature is not available for action-based and API-triggered campaigns, and not to be used with [quiet hours]({{site.baseurl}}/user_guide/intelligence/faqs/#/#can-i-use-quiet-hours-in-my-intelligent-timing-campaign), [rate-limiting]({{site.baseurl}}/user_guide/intelligence/faqs/#can-i-use-intelligent-timing-and-rate-limiting), or [IP warming]({{site.baseurl}}/user_guide/intelligence/faqs/#can-i-use-intelligent-timing-while-ip-warming) campaigns. 

## Campaign sending

With Intelligent Timing, you may choose the day(s) on which your message will send and, optionally, choose to send the campaign on a recurring schedule. We recommend only using Intelligent Timing when you can schedule the campaign at least 24 hours before the send date to ensure that users optimal times' have not passed when the campaign is launched. If a campaign is launched and a user's optimal time has already passed, the message goes out immediately. If it is more than an hour in the past, the message is not sent at all.

To ensure every eligible user can fall into and receive your campaign at their intelligent time, we recommend launching your campaign 48 hours before the scheduled time of send. In a single day, there are approximately 48 hours that it spans. Depending on where your users reside, they may need more than 24hrs to receive their intelligent time message as their intelligent time may have already passed when the campaign launches. 

![Specifying time-based scheduling options when Intelligent Timing is chosen, such as optimal send time.][1]

### Window of time

You may also designate a window of time during the day in which Intelligent Timing should send messages. This is useful if your campaign pertains to a specific event, sale, or promotion. 

If a user's optimal time is calculated as being outside this window, the message will be scheduled at the edge of the window closest to the initially calculated optimal time. This "edge" is the time closest to the user's optimal time. For example, if the optimal time is 10pm, but the intelligent delivery is 1pm to 8pm, the given message will be sent at 8pm.

## Segment filtering

When using Intelligent Timing, Braze recommends that your campaign's segment filters allow for at least a 3-day window. For example, instead of using the filters `First used more than 1 day ago` and `First used less than 3 days ago`, we recommend using the filters `First used more than 1 day ago` and `First used less than 4 days ago`. This is because time windows of less than three days may result in some users falling out of the segment before their optimal send time is reached.

![][3]

## Fallback options

For users who have insufficient data to calculate an optimal send time, there are two options to choose from.

**Option 1: Specify Fallback Time**
- You can specify a fallback time in users' local time zones by choosing **Custom Fallback** and entering your desired time. If the user has no time zone, the company time zone will be used instead.<br><br>If you launch a campaign with Intelligent Timing within 24 hours of the send date and enable a Custom Fallback, users whose optimal times have already passed will instead receive the campaign at the specified Custom Fallback time in their local time (or company time if they have no time zone). The message will send immediately if the specified Custom Fallback has already passed in a user's time zone.

**Option 2: Choose Most Popular Time Amongst Users**
- You can also set the fallback to be the most popular time when all other users use your app. If the most popular app usage time falls outside the delivery window you specified, the closest edge of this span will be used instead. <br><br>In the rare event that you are sending to an app where there's not enough data to calculate when the app is most used (e.g., a completely new app with no data), Intelligent Timing falls back on 5pm in the user's local time zone (or company time zone if the user has no local time).

It's important to be aware of the limitations of using Intelligent Timing early in a user's lifecycle when limited data is available. It can, however, still be valuable, as even users with a few recorded sessions can offer insights into their behavior. Intelligent Timing will more effectively calculate the optimal send time later in a user's lifecycle. 

## Triggered campaigns and Canvases

If a triggered campaign or Canvas step is activated to send a user a message with Intelligent Timing, it's possible that the user's optimal send time is before the time of day at which the campaign or step was triggered. In this case, the message will send immediately.

## Preview chart

On the **Delivery** and **Target Users** pages in the campaign wizard, you can generate a chart to see how many users will receive the message according to Intelligent Timing in each hour of the day. 

![Intelligent Timing preview chart showing estimates of the number of users who will receive the message in a specified hour, determined by their previous engagement data.][2]

To do this, first, make sure to specify an audience on the **Target Users** page. Once you do that, click **Refresh Data** to see the chart on the corresponding pages. Whenever you change any settings about Intelligent Timing or the audience, you'll need to click **Refresh Data** again to view an updated chart.  

The chart separately displays users who had enough data to compute an optimal time in blue and users who will receive a time according to your chosen fallback (custom fallback or most popular app time) in red. You can also toggle the calculation filters to choose what data is used to calculate the times in the chart (engagement data or most popular app time). For multichannel campaigns, you can examine the times separately per channel by changing the selected channel in the dropdown at the top of the chart.

[1]: {% image_buster /assets/img/optimal-send-time.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
