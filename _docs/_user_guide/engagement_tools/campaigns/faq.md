---
nav_title: FAQ
article_title: Campaigns FAQ
page_order: 10
page_type: FAQ
description: "This page provides answers to frequently asked questions about campaigns."
tool: Campaigns

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about campaigns.

### How do I create a multichannel campaign?

To create a multichannel campaign, select **Messaging** > **Campaigns**. Then, select **Create Campaign** > **Multichannel**. From here, you can select from the following messaging channels: Content Cards, email, LINE, push notifications, SMS/MMS/RCS, webhook, or WhatsApp.

### Can I add a control group to my multichannel campaign?

No, control groups in campaigns are intended for single-channel messaging, such as Email A versus Email B. As an alternative, try using [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) for testing different channels, messaging content, and delivery timing. 

### What are some ways I can start testing and optimizing campaigns?

Multivariate campaigns and running Canvases with multiple variants are a great way to start! For example, you can run a [multivariate campaign]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) to test out one message that has different copies or subject lines. Canvases with multiple variants can help test entire workflows.

### Why did the open rate for my campaign decrease?

Low open rates aren't always correlated to a technical issue. There may be issues with email clipping, which results in a missing tracking pixel. However, it's also possible that fewer users are opening their emails due to the content or changes in audience size. 

### How are campaign audiences evaluated?

By default, campaigns check audience filters at entry time. For action-based campaigns with a delay, there is an option to re-evaluate segment criteria at the send time to ensure users are still part of the target audience when the message is sent. 

### Why is there a difference between the number of unique recipients and the number of sends for a given campaign or Canvas?

One potential explanation could be the campaign or Canvas has re-eligibility turned on, which means users who qualify for the segment and delivery settings will be able to receive the message more than once. If re-eligibility is not turned on, then the probable explanation for the difference between sends and unique recipients may be due to users having multiple devices, across platforms, associated with their profiles. 

For example, should you have a Canvas that has both iOS and web push notifications, a given user with both mobile and desktop devices could receive more than one message.

### Why does my campaign have a smaller reachable user base than the segment that I'm using for the campaign?

If you have a [Global Control Group]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) set up, this will prevent a percentage of your reachable audience from receiving campaigns. This means that the number of reachable users for your segment can sometimes be larger than the number of reachable users for your campaign, even if the campaign is using that same segment.

### What does local time zone delivery offer?

Local time zone delivery allows you to deliver messaging campaigns to a segment based on a user's individual time zone. Without local time zone delivery, campaigns will be scheduled based on your company's time zone settings in Braze. 

For example, a London-based company sending a campaign at 12 pm will reach users on the west coast of America at 4 am. If your app is only available in certain countries, this may not be a risk for you. Otherwise, we highly recommend avoiding sending early morning push notifications to your user base.

### How does Braze recognize a user's time zone?

Braze will automatically determine a user's time zone from their device. This ensures time zone accuracy and full coverage of your users. Users created through the User API or otherwise without a time zone will have your company's time zone as their default time zone until they are recognized in your app by the SDK. 

You can check your company's time zone in your [company settings]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) on the dashboard.

### When does Braze evaluate users for local time zone delivery?

For local time zone delivery, Braze evaluates users for their entry eligibility during these two instances:

- At Samoa time (UTC+13) of the scheduled day
- At local time of the scheduled day

For a user to be eligible for entry, they must be eligible for both checks. For example, if a Canvas is scheduled to launch on August 7, 2021 at 2 pm local time zone, then targeting a user located in New York would require the following checks for eligibility:

- New York on August 6, 2021 at 9 pm
- New York on August 7, 2021 at 2 pm

Note that the user needs to be in the segment for 24 hours prior to the launch. If the user is not eligible in the first check, then Braze will not attempt the second check.

For example, if a campaign is scheduled to be delivered at 7 pm UTC, we start queuing the campaign sends as soon as a time zone is identified (such as Samoa). This means we're getting ready to send the message, not sending the campaign. If users don't match any filters when we check eligibility, they won't fall into the target audience.

As another example, say you want to create two campaigns scheduled to send on the same day—one in the morning and one in the evening—and add a filter that users can only receive the second campaign if they've already received the first. With local time zone delivery, some users may not receive the second campaign. This is because we check eligibility when the user's time zone is identified, so if the scheduled time hasn't occurred in their time zone yet, they haven't received the first campaign, meaning they won't be eligible for the second campaign.

### How do I schedule a local time zone campaign?

When scheduling a campaign, choose to send it at a designated time and then select **Send campaign to users in their local time zone**.

Braze highly recommends that all local time zone campaigns be scheduled 24 hours in advance. Since such a campaign needs to send over an entire day, scheduling it 24 hours in advance ensures that your message will reach your entire segment. However, you can schedule these campaigns less than 24 hours in advance if necessary. Keep in mind that Braze will not send messages to any users who have missed the send time by more than 1 hour. 

For example, if it is 1 pm and you schedule a local time zone campaign for 3 pm, then the campaign will immediately send to all users whose local time is between 3 pm and 4 pm, but not to users whose local time is 5 pm. In addition, the send time you choose for your campaign needs to have not yet occurred in your company's time zone.

Editing a local time zone campaign that is scheduled less than 24 hours in advance will not alter the message's schedule. If you decide to edit a local time zone campaign to send at a later time (for instance, 7 pm instead of 6 pm), users who were in the targeted segment when the original send time was chosen will still receive the message at the original time (6 pm). If you edit a local time zone to send at an earlier time (for instance, 4 pm instead of 5 pm), then the campaign will still send to all segment members at the original time (5 pm). 

{% alert note %}
For Canvas components, users do not need to be in the component for 24 hours to receive the next component in the user journey for local time zone delivery. 
{% endalert %}

If you have allowed users to become re-eligible for the campaign, then they will receive it again at the original time (5 pm). For all subsequent occurrences of your campaign, however, your messages are only sent at your updated time.

### When do changes to local time zone campaigns take effect?

Target segments for local time zone campaigns should include at least a 48-hour window for any time-based filters to guarantee delivery to the entire segment. For example, consider a segment targeting users on their second day with the following filters:

- First used app more than 1 day ago
- First used app less than 2 days ago

Local time zone delivery may miss users in this segment based on the delivery time and the users' local time zone. This is because a user can leave the segment by the time their time zone triggers delivery.

### What changes can I make to scheduled campaigns ahead of launch?

When the campaign is scheduled, edits to anything other than the message composition need to be made before we enqueue the messages to send. As per all campaigns, you can't edit conversion events after it is launched.

### I updated my scheduled campaign. Why didn't it launch?

This can happen when a campaign is scheduled to launch at the exact time that it was updated. For example, if it's currently 3:10 pm and you changed the campaign to launch at 3:10 pm and selected **Update campaign**, it's now past 3:10 pm, meaning the scheduled time for launch has passed. Instead of scheduling the campaign for the same time, select **Send as soon as campaign launch**.

### What is the "safe zone" before messages on a scheduled campaign are enqueued?

We recommend making changes to messages within the following times:

- **One-time scheduled campaigns:** Edit up until the scheduled send time.
- **Recurring scheduled campaigns:** Edit up until the scheduled send time.
- **Local send time campaigns:** Edit up to 24 hours before the scheduled send time.
- **Optimal send time campaigns:** Edit up to 24 hours before the day the campaign is scheduled to send.

If you make changes to your message outside of these recommendations, you may not see the updates reflected in the message sent. For example, if you edit the send time three hours before a campaign is scheduled to send at 12 pm local time, the following may occur:

- Braze will not send messages to any users that have missed the send time by more than one hour.
- Pre-enqueued messages may still be sent at the originally enqueued time, rather than the adjusted time.

If you need to make changes, we recommend stopping the current campaign (this will cancel any enqueued messages). You can then duplicate the campaign, make the changes as necessary, and launch the new campaign. You may need to exclude users from this campaign who have already received the first campaign. Make sure to re-adjust campaign schedule times to allow for time zone sending.

### Why does the number of users entering a campaign not match the expected number?

The number of users entering a campaign may differ from your expected number because of how audiences and triggers are evaluated. In Braze, an audience is evaluated before the trigger (unless using a [change in attribute]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) trigger). This will cause users to drop out of the campaign if they're not initially part of your selected audience before any trigger actions are evaluated.

{% alert tip %}
For further assistance with campaign troubleshooting, be sure to contact Braze Support within 30 days of your issue's occurrence, as we only have the last 30 days of diagnostic logs.
{% endalert %}

### What's the difference between the CSV Export User Data and CSV Export Email Address options on my campaign analytics page?

Selecting the **CSV Export Email Addresses** option will only download data for users with email addresses. For example, if you have a segment of 100,000 users, but only 50,000 of those users have email addresses, and you click **CSV Export Email Addresses**, then you should expect to see only 50,000 rows of data in the CSV file. In comparison, selecting **CSV Export User Data** will export all user data.

### Can I search for a campaign by its API identifier?

Yes, use the filter `api_id:YOUR_API_ID` on the **Campaigns** page to search for a campaign by its API identifier. Refer to [searching for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) to learn more.

### What is the difference between API campaigns and API-triggered campaigns?

API-triggered campaigns allow you to manage campaign copy, multivariate testing, and re-eligibility rules within the Braze dashboard while triggering the delivery of that content from your own servers and systems. These messages can also include additional data to be templated into the messages in real time.

API campaigns are used to track the messages sent using the API. Unlike most campaigns, you don't specify the message, recipients, or schedule but instead pass the identifiers into your API calls. 

### What is the difference between action-based and API-triggered campaigns?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Action-based

Action-based delivery campaigns or event-triggered campaigns are very effective for transactional or achievement-based messages and allow you to trigger them to send after a user completes a certain event. 

| Pros | Cons | 
| ---- | ---- |
| • Visibility of incoming JSON payloads into the platform (if event triggered by test user) via the **Message Activity Log**<br><br>• Personalization elements are included in the custom event properties<br><br>• Custom event can be used to create Segments of users eligible for the message | • Consumes data points |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### API-triggered

API-triggered and server-triggered campaigns are ideal for handling more advanced transactions, allowing you to trigger the delivery of campaign content from your own servers and systems. The API request to trigger the message can also include additional data to be templated into the message in real time.

| Benefits | Considerations | 
| ---- | ---- |
| • Does not consume data points<br><br>• Personalization elements are included in the JSON payload properties | • Does not allow you to create a segment of users eligible for the message in the JSON payload properties<br><br>• Not able to see incoming JSON payloads with the **Message Activity Log**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

