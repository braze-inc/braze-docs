---
nav_title: Scheduled Delivery
page_order: 0

tools: campaigns
page_type: reference
description: "This reference article gives an overview of different ways to go about scheduling a campaign."
---

# Scheduled Delivery

Campaigns sent using time-based scheduled delivery are delivered on specified days.

![Time based][3]

## Option 1: Send as soon as Campaign is launched

If you choose to send a message as soon as it's launched, it will begin sending as soon as you finish creating your campaign.

![Immediately][10]

This type of schedule is designed for one-off campaigns that you wish to send immediately, such as messages about a current event. A sports app, for instance, may schedule push notifications on score updates using this option. In addition, when sending test messages aimed at just yourself or your team, this option allows you to deliver them immediately. If you plan on editing the campaign and re-sending it after viewing the test, be sure to check the box that makes users [re-eligible][24] to receive the campaign. By default, Braze sends a campaign to a user just once, unless that box is checked.

## Option 2: Sending at a Designated Time

Scheduling a campaign for a designated time allows you to specify the days and times your campaign will send. You can send a message once, daily, weekly or monthly at a certain time of day, as well as specify when your campaign should begin and end. If you choose Scheduled Delivery and don't choose to send at user local time, your campaign will send according to the time zone specified on your "Company Settings" page.

![Designated time][9]

### Local Time Zone Campaigns

You can deliver the message in users' local time zones so that members of your international audience won't receive a notification at 4 am. Local time zone campaigns need to be scheduled 24 hours in advance to ensure that eligible users from all time zones can receive it. Read [our FAQ page on this feature][25] to understand how local time zone campaigns work and the associated delivery rules.

Segments targeted with local time zone campaigns should include, at minimum, a 2-day window to incorporate users from all time zones. For instance, if your campaign is scheduled to send in the evening but has just a 1-day window, then some users may have fallen out of the segment when their time zone is reached. Examples of filters that create a 2-day window are "last used more than 1 day ago" and "last used less than 3 days ago," or "first purchased more than 7 days ago" and "first purchased less than 9 days ago."

### Use Cases

Designated time schedules are best suited for messages scheduled in advance and recurring campaigns - such as [onboarding][7] and retention - that run regularly on all qualified users.

## Option 3: Intelligent Timing

Intelligent Timing allows you to deliver a campaign to each user at a different time. Braze calculates each individual's time based on when that user typically engages with your app and its notifications. You can optionally specify that intelligent timing campaigns send only during a certain portion of the day - for instance, if you are notifying users of a promotion that ends at midnight, you may want your messages to send by 10 pm at the latest. Read our [page on Intelligent Timing][8] for more details on how this feature works.

![Intelligent Timing][14]

### Delivery Rules

Because a user's optimal time can be anytime over the course of 24 hours, all Intelligent Timing campaigns must be scheduled 24 hours in advance. In addition, similar to designated time campaigns, messages with a 1-day window will miss users who fall out of the segment before their optimal time in their time zone is reached. Segments for intelligent timing campaigns should incorporate at minimum a 3-day window to account for this.

### Use Cases

Intelligent Timing campaigns work best for one-off and recurring messages where there is some flexibility regarding delivery time - for instance, they aren't well suited for breaking news or timed announcements.

[3]: {% image_buster /assets/img_archive/time_based.png %}
[7]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[9]: {% image_buster /assets/img_archive/schedule_designated.png %}
[10]: {% image_buster /assets/img_archive/schedule_immediately.png %}
[14]: {% image_buster /assets/img_archive/schedule_intelligent.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[25]: {{site.baseurl}}/help/faqs/#how-does-local-time-zone-delivery-work
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
