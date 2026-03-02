---
nav_title: Messaging diagnostics dashboard
article_title: Messaging diagnostics dashboard
description: "This reference article covers the messaging diagnostics dashboard, which helps you understand why messages from your campaigns or Canvases may not have been sent as expected."
alias: /ccdd/
page_order: 4.5
---

# Messaging diagnostics dashboard

> The **Messaging Diagnostics** dashboard provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected.

## Key concepts

### Sent and delivered

It is crucial to understand that this dashboard reports on how Braze internally processed a message, not the message's final delivery status.

A message marked as "sent" in this dashboard means Braze successfully processed and dispatched the message. For most channels, this means Braze handed off the message to the relevant third-party sending partner. However, it does not guarantee final delivery to the user's device. 

When Braze "sends" a message, the final delivery may depend on external services. Consider the following examples for each channel.

| Channel | Example of final delivery |
| --- | --- |
| Content Cards | The card was sent and is eligible for viewing. |
| Email | Braze hands the message to an email service provider (ESP). The ESP is then responsible for the final delivery. That ESP, for example, may report a "bounce" if the email address is invalid or the inbox is full. |
| In-app messages | The message was surfaced to the user. |
| LINE | The message was successfully handed off to a sending partner. |
| Push | Braze hands the message to the appropriate push notification service (such as Apple Push Notification service for iOS or Firebase Cloud Messaging for Android). That service is responsible for the final delivery of the notification to the device. |
| SMS/MMS/RCS | Braze hands the message to an SMS gateway (like Twilio). That gateway is responsible for the final delivery to the mobile carrier. |
| Webhooks | The webhook request was made successfully, returning a `2xx` response. |
| WhatsApp | The message was successfully handed off to a sending partner. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Data freshness

The data in this dashboard updates approximately every 15 minutes. The update frequency is not guaranteed and may fluctuate based on system load.

## Configuring the dashboard

You can access the diagnostics dashboard by going to **Analytics** > **Dashboard Builder** and selecting **Messaging Diagnostics** from the list of Braze-created dashboards.

To run the dashboard and view your data:

1. Choose either **Campaigns** or **Canvases** as the source for your dashboard reports. 
2. Select one or more campaigns or Canvases.
3. Select **Run Dashboard** to load the data for your selected filters.

![Campaign and Canvas diagnostics example from May 25 to May 31, 2025 for a welcome series campaign.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interpreting the data

{% alert note %}
The dashboard only surfaces up to the last 7 days of data. 
{% endalert %}

### Summary tiles

At the top of the page, there are key summary tiles for your selected timeframe that show:

- **Total Aborts:** The total count of messages that were aborted. This includes Canvas audience members who didn’t enter the Canvas or exited the Canvas because they experienced a step failure or met exit criteria while performing an exit event.
- **Message Sends:** The total count of messages that Braze successfully processed and sent. 
  - **Email, SMS/MMS/RCS, WhatsApp, LINE, and push:** The message was successfully handed off to a sending partner.  
  - **Webhooks:** The webhook request was made successfully, returning a `2xx` response.  
  - **Content Cards:** The card was sent and is eligible for viewing.    
  - **In-app messages:** The message was displayed to the user.

### Message outcomes over time

This time series chart shows a day-by-day breakdown of the different reasons a message was aborted or a user was dropped from a Canvas. This chart doesn't display the number of sends.  

{% alert note %}
To keep the chart organized, any abort or drop reason with zero occurrences in your selected time range will not be displayed on the chart.
{% endalert %}

### Message outcomes breakdown

This chart shows the breakdown of all message outcomes within your selected time range. It provides a complete picture of:
- The total number of sends as a proportion of all outcomes.  
- The proportional breakdown of each abort and drop reason. This helps you quickly identify the most common reasons messages are not being sent.

### Abort outcomes

The following definitions explain the abort outcomes shown on the dashboard. Outcomes are grouped by category to make it easier to find the one you're investigating.

#### Content and rendering

| Abort outcome | Explanation |
| ---- | ---- |
| Content Card expired | The Content Card expired before the user saw it. |
| Content Card invalid | The Content Card had errors and was not sent to the user. Some common reasons for this include: {::nomarkdown}<ul><li> Maximum size exceeded (2 KB) </li><li> Expiration date is invalid </li><li> Message contains invalid characters </li></ul>{:/} |
| Connected Content failed | Braze tried to send the message, but Connected Content failed after the maximum number of retries (default is five). |
| In-app-message rendering timeout | After multiple attempts to retry, the Liquid could not be rendered and timed out. |
| Liquid abort | The [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) Liquid tag was called, so the send was canceled. |
| Liquid rendering timeout | It took too long to render the Liquid template. Most likely to occur for Banners (default timeout is 2 seconds; can be customized in app group settings). |
| Liquid syntax error | The Liquid template had a parsing error, so the message was canceled. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Campaign and Canvas state

| Abort outcome | Explanation |
| ---- | ---- |
| Delay step failure | The [Delay step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) failed, causing the user to exit the Canvas. This failure could happen when: {::nomarkdown}<ul><li> The variable provided to the personalized delay step was empty or an invalid type </li><li> The delay is past the maximum duration allowed within the Canvas</li></ul>{:/} |
| Exception or exit event | The user was previously eligible to receive the message, but either {::nomarkdown}<ul><li> performed an <a href="{{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">exception event</a> for an action-based campaign so the message was aborted, or </li><li> met the Canvas <a href="{{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">exit criteria</a> so they were dropped mid-journey.</li></ul>{:/} |
| Inactive campaign | The campaign was stopped while the message was in-flight so it was aborted. |
| Inactive Canvas | The Canvas was stopped before the user entered the journey. |
| Inactive Canvas step | This can occur in the Canvas if: {::nomarkdown}<ul><li> The Canvas step was deleted </li> <li>The Canvas was stopped, which causes all the steps to become inactive </li></ul>{:/} |
| Volume limited | The campaign met the set volume limit, so the send was canceled. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Rate limiting and timing

| Abort outcome | Explanation |
| ---- | ---- |
| Frequency capped | The user already received the maximum number of messages allowed per your workspace's [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) rules, so the send was canceled. |
| Quiet Hours abort | Quiet Hours was enabled for the campaign or Canvas step with the fallback set to **Abort message**. The user triggered the campaign or entered the Canvas message step during Quiet Hours so the message was aborted. However, this doesn't exit the user from the Canvas. |
| Rate limited over 72 hours | The message was throttled for longer than 72 hours due to [delivery speed rate limits]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), so the send was aborted. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### User eligibility and profile

| Abort outcome | Explanation |
| ---- | ---- |
| Duplicate user identifier | Multiple users with a matching identifier (such as external ID, email address, phone number) were eligible to receive this message. To prevent duplicate sends to the same user, this message was aborted. |
| User failed pre-check for Message step | This pre-check runs before delivery validations. When this occurs, the user did not meet the basic pre-check for this Message step (user not found or ineligible for the Message step's channel). **Note:** For a multi-channel Message step, this means the user was not found; channel eligibility is only checked here for single-channel Message steps. |
| User failed pre-check for triggered message | For a triggered message, Braze runs a first-pass set of basic pre-checks for audience eligibility, re-eligibility, and channel eligibility before creating a message to send from this trigger. |
| User no longer eligible | The user was initially in the target audience, but no longer matched the audience criteria before Braze sent the message or entered the user into the Canvas. The time between the user initially meeting the audience criteria and falling out of audience could be due to delays from: {::nomarkdown}<ul><li>Intelligent timing</li><li>Quiet Hours</li><li>Local time</li><li>Delivery speed rate limits (not applicable for Canvas entry)</li><li>Messaging pipeline delays</li></ul>{:/} |
| User not eligible for step | The user exited the Canvas because they didn't meet the set [delivery validations]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) for the message step or because they were part of a [suppression list]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists). |
| User not re-eligible | The user triggered the message, but it wasn't sent because of re-eligibility settings (for example, they already received the message too recently, or re-eligibility is turned off). For API-triggered campaigns with re-eligibility or can-match-after-seconds configured, duplicate send prevented when multiple triggers targeted the same user; only applies when specific users are targeted, not when an audience is used. |
| User profile not found | The user either never existed or no longer exists in Braze. Some common cases include: {::nomarkdown}<ul><li> The user was targeted using API messaging but never existed in Braze. </li><li>The user was deleted before the message was sent or the Canvas step was executed. </li><li>The user was merged with another profile before the message was sent.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Channel and delivery

| Abort outcome | Explanation |
| ---- | ---- |
| Partner delivery timeout | Braze attempted to send this message to your delivery partner for 24 hours, but the partner returned temporary errors for the entire window. |
| Push credentials invalid | The [push credentials]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) for this app are missing or invalid, so the send was canceled. Update your credentials in **App Settings**. |
| User not enabled for Android push, app, or device | Push cannot be sent to this user. Some common reasons: {::nomarkdown}<ul><li> The user doesn't have the app installed.</li> <li> The user doesn't have a valid push token. </li> <li>The user doesn't have the necessary device for this push notification. </li> <li> The user has disabled notifications for this app in their device settings. </li> <li> The user is not subscribed or opted-in to receive push notifications.</li></ul>{:/} |
| User not enabled for iOS push, app, or device | Same as User not enabled for Android push, app, or device (see above). |
| User not enabled for Kindle push, app, or device | Same as User not enabled for Android push, app, or device (see above). |
| User not enabled for web push, app, or device | Same as User not enabled for Android push, app, or device (see above). |
| User not enabled for Content Cards | The user has not used any apps that include this Content Card. |
| User not enabled for email | Emails cannot be sent to this user. Some common reasons: {::nomarkdown}<ul><li> The user doesn't have an email address on their user profile. </li><li> The user's subscription state excludes them from receiving this email. </li><li> The user's email address has previously been marked invalid (hard bounce). </li><li> Messages sent to this email address are consistently marked as spam, so the send was canceled.</li></ul>{:/} |
| User not enabled for LINE | LINE messages cannot be sent to this user. Some common reasons: {::nomarkdown}<ul><li> The user doesn't have a phone number on their user profile. </li><li> The user's phone number has been marked invalid due to delivery failures. </li><li> The user's subscription state excludes them from receiving this message. </li><li> The user doesn't have a LINE ID.</li></ul>{:/} |
| User not enabled for SMS/MMS/RCS | SMS messages cannot be sent to this user. Some common reasons: {::nomarkdown}<ul><li> The user doesn't have a phone number on their user profile. </li><li> The user's phone number has been marked invalid due to delivery failures. </li><li> The user's phone number is not in valid E.164 format, and attempts to automatically format the number failed. </li><li> The user's subscription state excludes them from receiving the SMS message.</li><li>The user's phone number is in a blocked country.</li></ul>{:/} |
| User not enabled for WhatsApp | WhatsApp messages cannot be sent to this user. Some common reasons: {::nomarkdown}<ul><li> The user doesn't have a phone number on their user profile. </li><li> The user's phone number has been marked invalid due to delivery failures. </li><li> The user's subscription state excludes them from receiving this message. </li><li> The user doesn't have a WhatsApp account.</li></ul>{:/} |
| Webhook failed | The webhook received an unsuccessful response code (non `2xx`). See the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting) for more details. Logs that are more than 60 hours old are cleaned and no longer accessible; webhook errors are sampled up to 20 logs per hour. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### What does a "pre-check" failure mean?

A "pre-check" refers to a high-speed, bundled validation check that runs at the very beginning of a pipeline stage (such as a message being triggered or a sending of a Canvas message step). Think of it as an early exit designed for maximum speed. Instead of running many separate, resource-intensive checks (like validating every detail of a user's profile), Braze bundles several basic validations into one "first pass".

If a user fails this single bundled check, they are dropped immediately. This bundled approach allows Braze to process massive volumes of messages at high speed and can contribute to faster, more stable performance for your campaigns and Canvases by reducing processing latency for each message.

### Why is the sum of _Total Aborts_ and _Message Sends_ lower than my expected audience size?

This can happen for several reasons:

- **Audience criteria:** Fewer users than expected may have satisfied the audience criteria (for example, they weren't in the segment or didn't have the necessary attributes) when the campaign or Canvas was launched.
- **Processing in progress:** Messages may still be actively processing. Users may still be in earlier steps of the Canvas and have not reached any Message steps.
- **Data freshness:** The dashboard data updates approximately every 15 minutes, but this is not a guarantee. The newest data for this campaign or Canvas may not have reached the dashboard yet.
- **Edge cases:** There is a small chance you are encountering an edge case that is not captured in this dashboard at this time. If you suspect this is the case, contact [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Why is the sum of _Total Aborts_ and _Message Sends_ greater than the audience for a campaign and Canvas?

This can occur for the following reasons:

- **Multi-channel messages:** The campaign or Canvas step was configured to send on multiple channels (such as SMS and email). A single user can receive a "sent" outcome for one channel (such as email) and an "abort" outcome for another (such as "User not enabled for SMS/MMS/RCS"). In this case, that one user would be counted twice in the chart: once as a "sent" and once as an "abort."
  - **Example:** You send a push campaign to 100 users, targeting both iOS and Android. If a user only has an iOS device, they will receive the iOS push ("sent") but will also trigger an abort for the Android push ("User not enabled for Android push, app, or device").
- **Multiple Message steps (Canvas only):** Your Canvas may have more than one message step in a given path. This dashboard aggregates all outcomes, so a single user could be counted multiple times if they pass through multiple message steps within the selected time range.
- **Test messages:** Test sending (which is counted in the dashboard) is making the total counts higher than the audience size. 
