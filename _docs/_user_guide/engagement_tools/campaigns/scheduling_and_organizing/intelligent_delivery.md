---
nav_title: Intelligent Delivery
platform: Campaigns
subplatform: Scheduling and Organizing
page_order: 1
---
# Intelligent Delivery

For more on Campaign Delivery, check out our [Campaign Set Up course on LAB](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

When scheduling a campaign, you have the option of using Braze's Intelligent Delivery feature, delivers your message to each user at the time which Braze determines that individual is most likely to engage. We calculate the optimal send time based on a statistical analysis of the user's past interactions with your app.

To use this feature, simply select __Intelligent Delivery__ when scheduling a campaign. The only difference between this option and "Send at a designated time" is that the time of day each user receives your message will be determined by Braze. You can still choose the day(s) on which your message will send and create a recurring campaign.

With Quiet Hours, you can designate a span of the day during which Intelligent Delivery will not send messages. This is useful if your campaign pertains to a specific event, sale or promotion. If a user's optimal time is calculated as being inside Quiet Hours, the edge of Quiet Hours closest to the optimal time will be chosen as the new optimal time. 

![Optimal Send Time][1]

If you're using Intelligent Delivery, Braze recommends that your campaign's segment filters allow for at least a 3-day window. For instance, instead of using the filters "first used more than 1 day ago" and "first used less than 3 days ago," we recommend using the filters "first used more than 1 day ago" and "first used less than 4 days ago." This is because time windows of less than 3 days may result in some users falling out of the segment before their optimal send time is reached.

### Not Enough Data

For users who have insufficient data to calculate an optimal send time, Braze instead uses the most popular time at which your app is used by all other users. This way, the optimal time for a user without enough individual data is informed by the times at which your app is popular with other users. If the most popular app usage time falls within Quiet Hours you specify, the edge of Quiet Hours that is closest to the most popular app time will be used instead. In the rare event that you are sending to an app where there's not enough data to calculate when the app is most used, e.g. a completely new app with no data, Intelligent Delivery falls back on 5PM in the user's local time zone.

So, it's important to be aware of the limitations of using Intelligent Delivery early in a user's lifecycle when limited data for Intelligent Delivery is available. It can, however, still be valuable.  Consider a user that has recorded only one session. The time in which that user recorded their session could very well be the best time to attempt to engage them. Intelligent Delivery would only use data from the user's first session, and as such would engage the user at that time.  In general, Intelligent Delivery can more effectively calculate the optimal send time later in a user's lifecycle.

### Triggered Campaigns and Canvases

If a triggered campaign or Canvas step are activated to send a user a message with Intelligent Delivery, it's possible that the user's optimal send time is before the time of day at which the campaign or step was triggered. In this case, the message will send immediately.

[1]: {% image_buster /assets/img/optimal-send-time.png %}
