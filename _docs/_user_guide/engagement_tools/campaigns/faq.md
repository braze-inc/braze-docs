---
nav_title: FAQs
article_title: Campaign FAQs
page_order: 7
page_type: FAQ
description: "This page provides answers to frequently asked questions about Campaigns."
tool: Campaigns

---

# Campaign FAQs

### Why is there a difference between the number of unique recipients and the number of sends for a given campaign or Canvas?

One potential explanation for this difference could be due to the campaign or Canvas having re-eligibility turned on. By having this on, users who qualify for the segment and delivery settings will be able to receive the message more than once. If re-eligibility is not turned on, then the probable explanation for the difference between sends and unique recipients may be due to users having multiple devices, across platforms, associated with their profiles. 

For example, should you have a Canvas that has both iOS and web push notifications, a given user with both mobile and desktop devices could receive more than one message.

### What does local time zone delivery offer?

Local time zone delivery allows you to deliver messaging campaigns to a segment based on a user’s individual time zone. Without local time zone delivery, campaigns will be scheduled based on your company’s time zone settings in Braze. 

For example, a London-based company sending a campaign at 12pm will reach users on the west coast of America at 4am. If your app is only available in certain countries, this may not be a risk for you, otherwise, we highly recommend avoiding sending early morning push notifications to your user base!

### How does Braze recognize a user's time zone?

Braze will automatically determine a user’s time zone from their device. This ensures time zone accuracy and full coverage of your users. Users created through the User API or otherwise without a time zone will have your company’s time zone as their default time zone until they are recognized in your app by the SDK. 

To check your company’s time zone, look at your [Company Settings]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/) on the dashboard. Click on your name in the top toolbar and then click **Company Settings**.

### How do I schedule a local time zone campaign?

When scheduling a campaign, you need to choose to send it at a designated time, and then check **Send campaign to users in their local time zone**.

Braze highly recommends that all local time zone campaigns are scheduled 24 hours in advance. Since such a campaign needs to send over the course of an entire day, scheduling them 24 hours in advance ensures that your message will reach your entire segment. However, you can schedule these campaigns less than 24 hours in advance if necessary. Keep in mind that Braze will not send messages to any users that have missed the send time by more than 1 hour. 

For example, if it is 1pm and you schedule a local time zone campaign for 3pm, then the campaign will immediately send to all users whose local time is 3-4pm, but not to users whose local time is 5pm. In addition, the send time you choose for your campaign needs to have not yet occurred in your company’s time zone.

Editing a local time zone campaign that is scheduled less than 24 hours in advance will not alter the message’s schedule. If you decide to edit a local time zone campaign to send at a later time (for instance, 7pm instead of 6pm), users who were in the targeted segment when the original send time was chosen will still receive the message at the original time (6pm). If you edit a local time zone to send at an earlier time (for instance, 4pm instead of 5pm), then the campaign will still send to all segment members at the original time (5pm). 

{% alert note %}
For Canvas steps, users do not need to be in the step for 24 hours to receive the next step for local time zone delivery. 
{% endalert %}

If you have allowed users to become re-eligible for the campaign, then they will receive it again at the original time (5pm). For all subsequent occurrences of your campaign, however, your messages only send at your updated time.

### When do changes to local time zone campaigns take effect?

Target segments for local time zone campaigns should include at least a 48-hour window for any time-based filters to guarantee delivery to the entire segment. For example, consider a segment targeting users on their second day with the filters:

- First used app more than 1 day ago
- First used app less than 2 days ago

Local time zone delivery may miss users in this segment based on the delivery time and the users’ local time zone. This is because a user can leave the segment by the time their time zone triggers delivery.

### What changes can I make to scheduled campaigns ahead of launch?

When the campaign is scheduled, edits to anything other than the message composition need to be made before we enqueue the messages to send. As per all campaigns, you can’t edit conversion events after it is launched.

For Canvas entries, refer to above. For Canvas steps:

- Scheduled changes will only apply to users who are not already waiting to receive the step.
- Audience changes default to apply to everyone unless you’ve selected **Evaluate At Enqueue Time**, in which case it’s similar behavior to above.

### What is the "safe zone" before messages on a scheduled campaign are enqueued?

- **One-time scheduled campaigns**—can be edited up until the scheduled send time.
- **Recurring scheduled campaigns**—can be edited up until the scheduled send time.
- **Local Send Time campaigns**—can be edited up to 24 hours prior to the scheduled send time.
- **Optimal Send Time campaigns**—can be edited up to 24 hours prior to the day the campaign is scheduled to send on.

### What if I make an edit within the "safe zone"?

Changing the send time on campaigns within this time can lead to undesired behavior, for example:

- Braze will not send messages to any users that have missed the send time by more than 1 hour.
- Pre-enqueued messages may still send at the originally enqueued time, rather than the adjusted time.

### What should I do if the "safe zone" has already passed?

To ensure campaigns operate as desired, we recommend stopping the current campaign (this will abort any enqueued messages). You can then duplicate the campaign, making the changes as necessary and launch the new campaign. You may need to exclude users from this campaign who have already received the first campaign.

Please ensure you re-adjust campaign schedule times to allow for time zone sending.