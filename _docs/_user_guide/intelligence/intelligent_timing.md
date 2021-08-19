---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 2
description: "When scheduling a campaign, you can use Intelligent Timing to deliver your message to each user at the time which Braze determines that an individual is most likely to engage. This article covers how to implement intelligent timing in your campaigns and Canvases."

---

# Intelligent Timing

For more on Campaign Delivery, check out our [Campaign Set Up LAB course](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

> When scheduling a campaign, you can use Intelligent Timing (previously Intelligent Delivery) to deliver your message to each user at the time which Braze determines that an individual is most likely to engage. 

Braze calculates the optimal send time based on a statistical analysis of your user’s past interactions with your messaging (on a per channel basis) and app. To enable Intelligent Timing, simply select Intelligent Timing on the Delivery page when creating a scheduled delivery campaign. Note that this feature is not available for Action-Based or API-Triggered campaigns.

With Intelligent Timing, you may choose the __day(s) on which your message will send__ and, optionally, choose to send the campaign on a recurring schedule. We recommend only using Intelligent Timing when you can schedule the campaign __at least 24 hours in advance__ of the send date to ensure that users optimal times’ have not passed when the campaign is launched. If a campaign is launched and a user’s optimal time has already passed, the message goes out immediately. If it is more than an hour in the past, the message is not sent at all.

You may also designate __a window of time__ during the day in which Intelligent Timing should send messages. This is useful if your campaign pertains to a specific event, sale or promotion. If a user’s optimal time is calculated as being outside this window, the message will be scheduled at the edge of the window closest to the initially calculated optimal time. This "edge" is the time closest to the user's optimal time. For example, if the optimal time is 10pm but the intelligent delivery is 1pm to 8pm, the given message will be sent at 8pm.

When using Intelligent Timing, Braze recommends that your campaign’s segment filters allow for at least a 3-day window. For instance, instead of using the filters “first used more than 1 day ago” and “first used less than 3 days ago,” we recommend using the filters “first used more than 1 day ago” and “first used less than 4 days ago.” This is because time windows of less than 3 days may result in some users falling out of the segment before their optimal send time is reached. 

![Optimal Send Time][1]

## Fallback Options

For users who have insufficient data to calculate an optimal send time, there are two options to choose from.

__Option 1: Specify Fallback Time__<br>
You can specify a fallback time in users’ local time zones by choosing the Custom Fallback option and entering your desired time. (If the user has no time zone, the company time zone will be used instead.) If you launch a campaign with Intelligent Timing within 24 hours of the send date, and you enable the Custom Fallback, users whose optimal times have already passed will instead receive the campaign at the specified Custom Fallback time in their local time (or company time if they have no time zone). If the specified Custom Fallback has already passed in a user’s time zone, the message will send immediately.

__Option 2: Choose Most Popular Time Amongst Users__<br>
You can also choose the most popular time at which your app is used by all other users as the fallback. If the most popular app usage time falls outside the delivery window you specified, the closest edge of this span will be used instead. In the rare event that you are sending to an app where there’s not enough data to calculate when the app is most used (e.g. a completely new app with no data) Intelligent Timing falls back on 5PM in the user’s local time zone (or company time zone if the user has no local time).

It’s important to be aware of the limitations of using Intelligent Timing early in a user’s lifecycle when limited data for Intelligent Timing is available. It can, however, still be valuable. Consider a user that has recorded only one session. The time in which that user recorded their session could very well be the best time to attempt to engage them. Intelligent Timing would only use data from the user’s first session, and as such would engage the user at that time. In general, Intelligent Timing more effectively calculates the optimal send time later in a user’s lifecycle.


## Triggered Campaigns and Canvases

If a triggered campaign or Canvas step is activated to send a user a message with Intelligent Timing, it's possible that the user's optimal send time is before the time of day at which the campaign or step was triggered. In this case, the message will send immediately.

## Preview Chart

![Intelligent Timing Preview Chart][2]


On the Delivery and Target Users pages, you can generate a chart to see how many users will receive the message according to Intelligent Timing in each hour of the day. First, make sure to specify an audience on the Target Users page. Once you do that, click “Refresh Data” to see the chart on the corresponding pages. Whenever you change any settings about Intelligent Timing or the audience, you’ll need to click “Refresh Data” again to get an updated chart.  

The chart also separately displays users who had enough data to compute an optimal time in blue and users who will receive a time according to your chosen fallback (Custom Fallback or Most Popular App Time) in red. You can separately enable the bars representing users with optimal times calculated with Engagement Data or your chosen Fallback by clicking the checkbox next to their labels in the legend. For multichannel campaigns, you can examine the times separately per channel by changing the selected channel in the dropdown at the top of the chart.

[1]: {% image_buster /assets/img/optimal-send-time.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}