---
nav_title: Uninstall Tracking
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

{% alert note %}
If you're using the older navigation, **App Settings** is **Settings** and is located under **Manage Settings**.
{% endalert %}

When uninstall tracking is turned on for an app, background push messages will be sent nightly to users who haven't recorded a session or received a push in 24 hours.

### Configuration

To configure uninstall tracking for your iOS application, use a [utility method][iOS docs]. For your Android application, use [`BrazeNotificationUtils.isUninstallTrackingPush()`][8]. When Braze detects an uninstall, whether from uninstall tracking or normal push campaign delivery, we will record the best estimated time of the uninstall on the user. This time is stored in the user profile as a standard attribute and can be used to define a segment of users for win-back campaigns.

## Filtering segments by uninstalls

The **Uninstalled** filter on the **Segments** page selects users who uninstalled your app within a time range. Because it's difficult to determine the exact time of an uninstall, we recommend that uninstall filters have wider time ranges to make sure everyone who uninstalls falls into the segment at some point.

![Uninstall segment.][5]

### App-level analysis

Daily statistics on uninstalls are on the **Home** page. The graph can be broken down by app and segment, similar to other statistics Braze provides. In the **Performance overview** section, select your date range and, if desired, an app. The, scroll down to the **Performance Over Time** graph and do the following:

1. In the **Statistics For** dropdown, select **Uninstalls**.
2. In the **Breakdown** dropdown, select **By segment**.
3. In the **Breakdown Values** dropdown, select the segments to include in the graph.

{% alert note %}
Apps without uninstall tracking enabled will report uninstalls from only a subset of their users (those who were targeted with push notifications), so daily uninstall totals may be higher than what is shown.
{% endalert %}

![Uninstall graph selection.][2]

## Uninstall tracking for campaigns

Campaign uninstall tracking shows the number of users who received a specific campaign and subsequently uninstalled your app within the selected time frame. This tool gives insight into how campaigns may be encouraging unintended negative user behaviors and helps to measure overall campaign efficacy.

Uninstall statistics for campaigns are located on a specific campaign's **Campaign Analytics** page. For multichannel and multivariate campaigns, uninstalls can be broken down by channel and variant, respectively.

![Uninstall at the campaign-level.][6]

### How it works

Braze tracks uninstalls by observing when push messages sent to users' devices return a signal from either Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNs) that the app is no longer installed. If Global Uninstall Tracking is turned on for a particular app, we send a daily silent push message to users to detect whether they have uninstalled. This "silent" push is sent to all users (unless the user has disabled silent pushes in their app settings); however, the push does not appear to users. If we detect that a user has uninstalled, we:

* Increment the app's total uninstall count by one.
* Increment the uninstall count for every campaign that the user successfully received in the past 24 hours by one.
* If a user receives three campaigns in a 24-hour period and then uninstalls, we increment the count of "uninstalls" for all three campaigns.

Uninstall tracking is subject to restrictions placed on this information by FCM and APNs. Braze only increments the uninstall count when FCM or APNs tell us that a user has uninstalled, but these third-party systems reserve the right to notify us of uninstalls at any point in time. As a result, uninstall tracking should be used to detect directional trends as opposed to precise statistics.

For more on using uninstall tracking, see our blog post [Uninstall Tracking: An Industry Look at its Strengths and Limitations][7].

## Troubleshooting

### Why am I suddenly seeing a spike in uninstalls?

If you see a spike in app uninstalls, it may be due to Firebase Cloud Messaging (FCM) and Apple Push Notification Service (APNS) revoking old tokens at a different frequency.

### Why are the number of app uninstalls different from what's in the APNs?

The difference is expected. APNs will start returning a 410 status for these tokens on a fuzzy schedule.

[1]: {% image_buster /assets/img_archive/Uninstall_Tracking2.png %} "Uninstall Tracking Checkbox"
[2]: {% image_buster /assets/img_archive/Uninstall_Tracking_App2.png %} "Uninstall Graph Selection"
[4]: {% image_buster /assets/img_archive/User_Profile.png %} "Uninstall Attribute"
[5]: {% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment"
[6]: {% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %}
[7]: https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/
[iOS docs]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html
