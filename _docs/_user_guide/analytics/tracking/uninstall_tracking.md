---
nav_title: Uninstall tracking
article_title: Uninstall Tracking
page_order: 6
page_type: reference
description: "This reference article covers implementing uninstall tracking for campaign-level and app-level statistics."
tool: Reports

---

# Uninstall tracking

> This article shows how you can view aggregate app uninstalls over time to locate trends and anomalies, and track campaign-level uninstalls to determine if a specific campaign is driving or preventing app installs.

Uninstall tracking in Braze provides the following details:

1. Daily app-level uninstall statistics in a time series graph on the **Home** page.
2. Campaign-level uninstall statistics in a time series graph on the **Campaign Details** page of a specific campaign. This statistic specifies the number of campaign recipients that uninstall each day.

{% alert note %} 
You must opt-in to uninstall tracking on your Braze dashboard. This feature is currently available for apps on iOS, Android, and Fire OS. 
{% endalert %}

## How it works

Braze automatically collects a base level of uninstall information from your regular push campaigns. However, because the frequency with which different users receive push campaigns may vary, we offer uninstall tracking to provide a more accurate snapshot of uninstall activity among your users.

## Turning on uninstall tracking

You can turn on uninstall tracking on the **App Settings** page, under **Settings**, for each app you want to track.

When uninstall tracking is turned on for an app, background push messages will be sent nightly to users who haven't recorded a session or received a push in 24 hours.

### Configuration

To configure uninstall tracking for your iOS application, use a [utility method]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). For your Android application, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). When Braze detects an uninstall, whether from uninstall tracking or normal push campaign delivery, we will record the best estimated time of the uninstall on the user. This time is stored in the user profile as a standard attribute and can be used to define a segment of users for win-back campaigns.

## Filtering segments by uninstalls

The **Uninstalled** filter selects users who uninstalled your app within a time range. Because it's difficult to determine the exact time of an uninstall, we recommend that uninstall filters have wider time ranges to make sure everyone who uninstalls falls into the segment at some point.

Daily statistics on uninstalls are on the **Home** page. 

![Uninstall segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

The graph can be broken down by app and segment, similar to other statistics Braze provides. In the **Performance overview** section, select your date range and, if desired, an app. Then, scroll down to the **Performance Over Time** graph and do the following:

1. In the **Statistics For** dropdown, select **Uninstalls**.
2. In the **Breakdown** dropdown, select **By segment**.
3. In the **Breakdown Values** dropdown, select the segments to include in the graph.

{% alert note %}
Apps without uninstall tracking enabled will report uninstalls from only a subset of their users (those who were targeted with push notifications), so daily uninstall totals may be higher than what is shown.
{% endalert %}

## Uninstall tracking for campaigns

Campaign uninstall tracking shows the number of users who received a specific campaign and subsequently uninstalled your app within the selected time frame. This tool gives insight into how campaigns may be encouraging unintended negative user behaviors and helps to measure overall campaign efficacy.

Uninstall statistics for campaigns are located on a specific campaign's **Campaign Analytics** page. For multichannel and multivariate campaigns, uninstalls can be broken down by channel and variant, respectively.

![Uninstall at the campaign-level.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### How it works

Braze tracks uninstalls by observing when push messages sent to users' devices return a signal from either Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNs) that the app is no longer installed. If Global Uninstall Tracking is turned on for a particular app, we send a daily silent push message to users to detect whether they have uninstalled. This "silent" push is sent to all users (unless the user has disabled silent pushes in their app settings); however, the push does not appear to users. If we detect that a user has uninstalled, we:

* Increment the app's total uninstall count by one.
* Increment the uninstall count for every campaign that the user successfully received in the past 24 hours by one.
* If a user receives three campaigns in a 24-hour period and then uninstalls, we increment the count of "uninstalls" for all three campaigns.

Uninstall tracking is subject to restrictions placed on this information by FCM and APNs. Braze only increments the uninstall count when FCM or APNs tell us that a user has uninstalled, but these third-party systems reserve the right to notify us of uninstalls at any point in time. As a result, uninstall tracking should be used to detect directional trends as opposed to precise statistics.

For more on using uninstall tracking, see our blog post [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Troubleshooting

### Why am I suddenly seeing a spike in uninstalls?

If you see a spike in app uninstalls, it may be due to Firebase Cloud Messaging (FCM) and Apple Push Notification Service (APNS) revoking old tokens at a different frequency.

{% alert note %} 
For privacy reasons, Braze’s push providers may revoke tokens at irregular intervals, meaning uninstall counts can sometimes spike in a given time period.<br><br>To validate these changes, monitor uninstall tracking alongside a user-action metric, such as direct push open rate. If uninstalls increase sharply but direct push opens remain stable, the spike likely reflects a partner revoking old tokens rather than actual user behavior.
{% endalert %}

### Why are the number of app uninstalls different from what's in APNs?

The difference is expected. 

Apple uses a randomized schedule to delay reporting when a push token becomes invalid, meaning that even after a user uninstalls an app, APNs may continue to return successful responses to push notifications for a period of time. This delay is intentional and designed to protect user privacy. No bounce or failure will be reported until APNs returns a `410` status for an invalid token.

