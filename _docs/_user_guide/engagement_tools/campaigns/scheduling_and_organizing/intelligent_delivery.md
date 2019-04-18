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

You also have the option of specifying a certain time range during which your message should send. This is useful if your campaign pertains to a specific event, sale or promotion. If a user's optimal time is calculated as being outside this range, the closest edge of the sending window to the optimal time will be chosen as the new optimal time. 

![Optimal Send Time][1]

If you're using Intelligent Delivery, Braze recommends that your campaign's segment filters allow for at least a 3-day window. For instance, instead of using the filters "first used more than 1 day ago" and "first used less than 3 days ago," we recommend using the filters "first used more than 1 day ago" and "first used less than 4 days ago." This is because time windows of less than 3 days may result in some users falling out of the segment before their optimal send time is reached.

### Not Enough Data

For users who have insufficient data to calculate an optimal send time, Braze instead uses the average session start time of all other users in the same campaign. This way, the optimal time for a user without enough individual data is informed by the times at which your app is popular with other users. In the rare event that you are sending to an audience for whom a useful average session start time cannot be calculated, e.g. a group of all new users, Intelligent Delivery falls back on 5PM in the user's local time zone.

So, it's important to be aware of the limitations of using Intelligent Delivery early in a user's lifecycle when limited data for Intelligent Delivery is available. It can, however, still be valuable.  Consider a user that has recorded only one session. The time in which that user recorded their session could very well be the best time to attempt to engage them. Intelligent Delivery would only use data from the user's first session, and as such would engage the user at that time.  In general, Intelligent Delivery can more effectively calculate the optimal send time later in a user's lifecycle.

### Intelligent Delivery Preview

You can get a preview of times chosen for users by Intelligent Delivery with the Preview function. This will show you a distribution of optimal times calculated for a sample of users from your audience, as well as the number of users for whom the group average session start time was used in place of a personalized optimal time.

![Send Time Preview][2]

[1]: {% image_buster /assets/img/optimal-send-time.png %}
[2]: {% image_buster /assets/img/optimal-time-preview.png %}
