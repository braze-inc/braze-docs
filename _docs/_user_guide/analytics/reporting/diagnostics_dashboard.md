---
nav_title: Campaign and Canvas diagnostics dashboard
article_title: Campaign and Canvas diagnostics dashboard
page_order: 6.2
page_type: reference
description: "This reference article covers the campaign and Canvas diagnostics dashboard, which helps you understand why messages from your campaigns or Canvases may not have been sent as expected."
tool: 
  - Reports

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

![Campaign and Canvas diagnostics example from May 25 to May 31, 2025 for a welcome series campaign.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %})

## Interpreting the data

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
  - **Example:** You send a push campaign to 100 users, targeting both iOS and Android. If a user only has an iOS device, they will receive the iOS push ("sent") but will also trigger an abort for the Android push ("Not Enabled for Channel").
- **Multiple Message steps (Canvas only):** Your Canvas may have more than one message step in a given path. This dashboard aggregates all outcomes, so a single user could be counted multiple times if they pass through multiple message steps within the selected time range.
-**Test messages:** Test sending (which is counted in the dashboard) is making the total counts higher than the audience size. 
