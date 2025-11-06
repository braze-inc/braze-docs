---
nav_title: Campaign and Canvas diagnostics
article_title: Campaign and Canvas diagnostics dashboard
page_order: 6.2
page_type: reference
description: "This reference article covers the campaign and Canvas diagnostics dashboard, which helps you understand why messages from your campaigns or Canvases may not have been sent as expected."
tool: 
  - Reports
toc_headers: "h2"
---

# Campaign and Canvas diagnostics dashboard

> The purpose of this dashboard is to help you understand why messages from your campaigns or Canvases may not have been sent as expected. It provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup.

{% alert important %}
The campaign and Canvas diagnostics dashboard is currently in early access. Contact your customer success manager if you're interested in participating in the early access.
{% endalert %}

## Key concepts

## Sent and delivered

It is crucial to understand that this dashboard reports on Braze's internal processing of a message, not its final delivery status.

A message marked as "sent" in this dashboard means Braze successfully processed and dispatched the message. For most channels, this means Braze handed off the message to the relevant third-party sending partner. It does not guarantee final delivery to the end-user's device.

When Braze "sends" a message, the final delivery may depend on external services. Consider the following examples for each channel:

- **Email:** Braze hands the message to an Email Service Provider (ESP). The ESP is then responsible for the final delivery. That ESP, for example, may report a "bounce" if the email address is invalid or the inbox is full.
- **SMS:** Braze hands the message to an SMS gateway (like Twilio). That gateway is responsible for the final delivery to the mobile carrier.
- **Push:** Braze hands the message to the appropriate push notification service (such as Apple Push Notification service for iOS or Firebase Cloud Messaging for Android). That service is responsible for the final delivery of the notification to the device.

### Data freshness

The data in this dashboard updates approximately every 15 minutes. Note that this is an approximation and the update frequency is not guaranteed; it may fluctuate based on system load.

## Configuring the dashboard

You can access the diagnostics dashboard by going to **Analytics** > **Dashboard Builder**.

![The dashboard builder with a list of different campaign and Canvas diagnostic dashboards.]({% image_buster /assets/img/campaign_canvas_dashboard.png %})

To run the dashboard and view your data:

1. Choose either **Campaigns** or **Canvases** as the source for your dashboard reports. 
2. Next, choose one or more campaigns or Canvases.
3. Select **Run Dashboard** to load the data for your selected filters.

![Campaign and Canvas diagnostics example from May 25 to May 31, 2025 for a welcome series campaign.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interpreting the data

### Summary tiles  
At the top of the page, you will see key summary tiles. For your selected time frame, these show:

- **Total Aborts:** The total count of messages that were aborted and Canvas audience members who didn’t enter the Canvas or fell out of exited the Canvas due to either encountering a step failure or meeting the exit criteria performing an exit event. (TODO consult with CLX on language here)  
- **Message Sends:** The total count of messages that Braze successfully processed and sent:  
  * For email, SMS/MMS/RCS, WhatsApp, LINE and push this means the message was successfully handed off to a sending partner.  
  * For webhooks, this means the webhook request was made successfully, returning a 2xx response.  
  * For content cards, this means the card was sent and is eligible for viewing.    
  * For in-app-messages, this means the message was surfaced to the user.

### Message outcomes over time

This time series chart shows a day-by-day breakdown of the different reasons a message was aborted or a user was dropped from a Canvas. This chart doesn't display the number of _Sends_.  

{% alert note %}
To keep the chart organized, any abort or drop reason with zero occurrences in your selected time range will not be displayed as a line on the chart.
{% endalert %}

### Message outcomes breakdown

This chart shows the breakdown of all message outcomes within your selected time range. It provides a complete picture of:
- The total number of _Sends_ as a proportion of all outcomes.  
- The proportional breakdown of each abort and drop reason. This helps you quickly identify the most common reasons messages are not being sent.

The following table defines the outcomes available in this dashboard:

| Outcome | Explanation |
| ---- | ---- |
| Content Card expired | The Content Card expired before the user saw it |
| Content Card invalid | The Content Card had errors and was not sent to the user. Some common reasons for this include: {::nomarkdown}<ul><li> Maximum size exceeded (2 KB) </li><li> Expiration date is invalid </li><li> Message contains invalid characters </li></ul>{:/} |
| Personalized delay step failure | The [personalized delay step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) failed, causing the user to exit the Canvas. This failure could happen when: {::nomarkdown}<ul><li> the variable provided to the personalized delay step was empty or an invalid type </li><li> the delay is past the maximum duration allowed within the Canvas</li></ul>{:/} |
| Duplicate user identifier | Multiple users with a matching identifier (ex: external id, email address, phone number) were eligible to receive this message. To prevent duplicate sends to the same user, this message was aborted. |
| Exception or exit event | The user was previously eligible to receive the message, but either the user performed an [exception event for the action-based campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events) so the message was aborted **or** the user met the Canvas [exit criteria]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria) so they were dropped mid-journey. |
| Frequency capped | The user already received the maximum number of messages allowed per your workspace's [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) rules, so the send was canceled. |
| In-app-message rendering timeout | After multiple attempts to retry, the Liquid could not be rendered and timed out. |
| Inactive campaign | The campaign was stopped while the message was in-flight so it was aborted. |
| Inactive Canvas | The Canvas was stopped before the user entered the journey. |
| Inactive Canvas step | This can occur in the Canvas if: {::nomarkdown}<ul><li> the Canvas step was deleted </li> <li>the Canvas was stopped, which causes all the steps to become inactive </li></ul>{:/} |
| Liquid abort | The [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) Liquid tag was called, so the send was canceled. |
| Push credentials invalid | The [push credentials]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) for this app are missing or invalid, so the send was canceled. Update your credentials in App Settings. |
| Quiet hours abort | Quiet hours was enabled for the campaign or Canvas step with the fallback set to "Abort message". The user triggered the campaign or entered the Canvas message step during quiet hours so the message was aborted. However, this does not exit the user from the Canvas. |
| Rate limited over 72 hours | The message was throttled for longer than 72 hours due to [delivery speed rate limits]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), so the send was aborted. |
| Sent | The message was sent. However, this does not necessarily mean the message was delivered. For email, SMS/MMS/RCS, WhatsApp, LINE, and push, this means the message was successfully handed off to a sending partner. For webhooks, this means the webhook request was made successfully, returning a `2xx` response. For Content Cards, this means the card was sent and is eligible for viewing.    For in-app-messages, this means the message was surfaced to the user.  |
| User no longer eligible | The user was previously in the target audience, but no longer matched the audience criteria at the time of send, so the message was aborted. This can happen if there is a gap between the message launch or trigger and the message send time. |
| User no longer eligible for step | The user exited the Canvas because they didn't meet the [delivery validations]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) set for the Message step. |
| User not eligible | The user was not eligible due to audience eligibility, re-eligibility rules, or channel eligibility checks. For campaigns, this applies to messages who were triggered by an action-based or API-triggered campaign. For Canvases, it pertains to users that matched on configured interaction or behavioral events. |
| User not enabled for Android push, app, or device<br><br>User not enabled for iOS push, app, or device<br><br>User not enabled for Kindle push, app, or device<br><br>User not enabled for web push, app, or device | Some common reasons for this include: {::nomarkdown}<ul><li> The user doesn't have the app installed.</li> <li> The user doesn't have a valid push token. </li> <li>The user doesn't have the necessary device for this push notification. </li> <li> The user has disabled notifications for this app in their device settings. </li> <li> The user is not subscribed or opted-in to receive push notifications.</li></ul>{:/} |
| User not enabled for Content Cards | The user has not used any apps that include this content card. |
| User not enabled for email | Emails cannot be sent to this user. Some common reasons for this include: {::nomarkdown}<ul><li> The user doesn't have an email address on their user profile.  The user's subscription state excludes them from receiving this email. <li> The user's email address has previously been marked invalid (hard bounce). <li> Messages sent to this email address are consistently marked as spam, so the send was canceled.</li></ul>{:/} |
| User not enabled for LINE | LINE messages cannot be sent to this user. Some common reasons for this include: {::nomarkdown}<ul><li> The user doesn't have a phone number on their user profile. </li><li> The user's phone number has been marked invalid due to delivery failures. </li><li> The user's subscription state excludes them from receiving this message. </li><li> The user doesn't have a LINE ID.</li></ul>{:/} |
| User not enabled for SMS/MMS/RCS | SMS messages cannot be sent to this user. Some common reasons for this include: {::nomarkdown}<ul><li> The user doesn't have a phone number on their user profile. </li><li> The user's phone number has been marked invalid due to delivery failures. </li><li> The user's phone number is not in valid E.164 format, and attempts to automatically format the number failed. </li><li> The user's subscription state excludes them from receiving the SMS message.</li></ul>{:/} |
| User not enabled for WhatsApp | WhatsApp messages cannot be sent to this user. Some common reasons for this include: {::nomarkdown}<ul><li> The user doesn't have a phone number on their user profile. </li><li> The user's phone number has been marked invalid due to delivery failures. </li><li> The user's subscription state excludes them from receiving this message. </li><li> The user doesn't have a WhatsApp account.</li></ul>{:/} |
| User not re-eligible | The user triggered the message, but it wasn't sent because of re-eligibility settings. This can happen if the user already received the message too recently, or if re-eligibility is turned off. If the user triggered this campaign already and was found to be ineligible for the send, they will sit in a 4-hour lock that prevents them from triggering it again during that time, resulting in this outcome. |
| User profile not found | The user either never existed or no longer exists in Braze. Some common cases include: {::nomarkdown}<ul><li> The user was targeted using API messaging but never existed in Braze. </li><li> The user was deleted before the message was sent. </li><li>The user was merged with another profile before the message was sent.</li></ul>{:/} |
| Volume limited | The campaign met the set volume limit, so the send was canceled. |
| Webhook failed | The webhook received an unsuccessful response code (non `2xx`). See the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting) for more details. Logs that are more than 60 hours old are cleaned and no longer accessible, Webhook errors are sampled up to 20 logs per hour. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### Why is the sum of _Total Aborts_ and _Message Sends_ lower than my expected audience size?

This can happen for several reasons:

- **Audience criteria:** Fewer users than expected may have satisfied the audience criteria (for example, they weren't in the segment or didn't have the necessary attributes) when the campaign or Canvas was launched.
- **Processing in progress:** Messages may still be actively processing. Users may still be in earlier steps of the Canvas and have not reached any Message steps.
- **Data freshness:** The dashboard data updates approximately every 15 minutes, but this is not a guarantee. The newest data for this campaign or canvas may not have reached the dashboard yet.
- **Edge cases:** There is a small chance you are encountering an edge case that is not captured in this dashboard at this time. If you suspect this is the case, contact [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Why is the sum of _Total Aborts_ and _Message Sends_ greater than the audience for a campaign and Canvas?

This can occur for the following reasons:

- **Multi-channel messages:** The campaign or Canvas step was configured to send on multiple channels (such as SMS and email). A single user can receive a "sent" outcome for one channel (such as email) and an "abort" outcome for another (such as "User not enabled for SMS/MMS/RCS"). In this case, that one user would be counted twice in the chart: once as a "sent" and once as an "abort."
  - **Example:** You send a push campaign to 100 users, targeting both iOS and Android. If a user only has an iOS device, they will receive the iOS push ("sent") but will also trigger an abort for the Android push ("User not enabled for Android push, app, or device").
- **Multiple Message steps (Canvas only):** Your Canvas may have more than one message step in a given path. This dashboard aggregates all outcomes, so a single user could be counted multiple times if they pass through multiple message steps within the selected time range.
-**Test messages:** Test sending (which is counted in the dashboard) is making the total counts higher than the audience size. 
