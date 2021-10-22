---
nav_title: Scheduled Delivery
article_title: Scheduled Delivery
page_order: 0
page_type: reference
description: "This reference article describes the differences between the time-based scheduling options for campaign delivery."
tool: Campaigns

---

# Scheduled delivery

Campaigns sent using time-based scheduled delivery are delivered on specified days.

![Time-based][3]

## Option 1: Send as soon as the campaign is launched

If you choose to send a message as soon as it's launched, it will begin sending as soon as you finish creating your campaign.

![Immediately][10]

This type of schedule is designed for one-off campaigns that you wish to send immediately, such as messages about a current event. A sports app, for instance, may schedule push notifications on score updates using this option. In addition, when sending test messages aimed at just yourself or your team, this option allows you to deliver them immediately. 

If you plan on editing the campaign and re-sending it after viewing the test, be sure to check the box that makes users [re-eligible][24] to receive the campaign. By default, Braze sends a campaign to a user just once unless that box is checked.

## Option 2: Send at a designated time

Scheduling a campaign for a designated time allows you to specify the days and times your campaign will send. You can send a message once, daily, weekly, or monthly at a certain time of day, as well as specify when your campaign should begin and end. This end date is inclusive, which means the last send will be on the end date. 

If you choose Scheduled Delivery and don't choose to send at user local time, your campaign will send according to the time zone specified on your **Company Settings** page.

![Designated time][9]

### Local time zone campaigns

You can deliver the message in users' local time zones so that members of your international audience won't receive a notification at inconvenient times. Local time zone campaigns need to be scheduled 24 hours in advance to ensure that eligible users from all time zones can receive them. Check out [Campaign FAQs][25] to understand how local time zone campaigns work and the associated delivery rules.

Segments targeted with local time zone campaigns should include, at minimum, a 2-day window to incorporate users from all time zones. For instance, if your campaign is scheduled to send in the evening but has just a 1-day window, some users may have fallen out of the segment when their time zone is reached. Examples of filters that create a 2-day window are "last used more than 1 day ago" and "last used less than 3 days ago," or "first purchased more than 7 days ago" and "first purchased less than 9 days ago."

### Use cases

Designated time schedules are best suited for messages scheduled in advance and recurring campaigns - such as onboarding and retention - that run regularly on all qualified users.

## Option 3: Intelligent Timing

[Intelligent Timing][8] allows you to deliver a campaign to each user at a different time. Braze calculates each individual's time based on when that user typically engages with your app and its notifications. You can optionally specify that Intelligent Timing campaigns send only during a certain portion of the day - for instance, if you are notifying users of a promotion that ends at midnight, you may want your messages to send by 10 pm at the latest.

![Intelligent Timing][14]

### Delivery rules

Because a user's optimal time can be any time over the course of 24 hours, all Intelligent Timing campaigns must be scheduled 24 hours in advance. In addition, similar to designated time campaigns, messages with a 1-day window will miss users who fall out of the segment before their optimal time in their time zone is reached. Segments for Intelligent Timing campaigns should incorporate at minimum a 3-day window to account for this.

If a user's profile does not have enough data to calculate an optimal time, you can choose a backup method to either send during the most popular time to use the app amongst all users or a set custom fallback time. 

### Use cases

Intelligent Timing campaigns work best for one-off and recurring messages where there is some flexibility regarding delivery time - for instance, they aren't well suited for breaking news or timed announcements.

[3]: {% image_buster /assets/img_archive/time_based.png %}
[7]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[9]: {% image_buster /assets/img_archive/schedule_designated.png %}
[10]: {% image_buster /assets/img_archive/schedule_immediately.png %}
[14]: {% image_buster /assets/img_archive/schedule_intelligent.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[25]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
