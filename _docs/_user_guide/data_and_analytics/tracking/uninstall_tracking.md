---
nav_title: Uninstall Tracking
page_order: 6
---
# Uninstall Tracking

Braze's Uninstall Tracking provides (1) daily app-level uninstall statistics in a time series graph on the App Usage page (2) campaign-level uninstall statistics in a time series graph on the Campaign Details page of a specific campaign. This statistic specifies the number of campaign recipients that uninstall each day. 

Showing aggregate uninstalls over time can help you visualize trends and anomalies so that you can monitor app uninstalls with ease. Similarly, tracking campaign-level uninstalls can reveal whether a specific campaign is driving or preventing app uninstalls. Braze automatically collects a base level of uninstall information from your regular push campaigns. However, because the frequency that different users receive push campaigns may vary, Braze offers Uninstall Tracking to provide a more accurate snapshot of uninstall activity among your users. You must opt-in to Uninstall Tracking on the dashboard; this feature is currently available for apps on iOS, Android, and Fire OS.

## Implementation

You can enable Uninstall Tracking in the App Settings section of the "Manage App Group" page. For each app you are interested in tracking, check the box in the uninstall tracking section.

![Uninstall Tracking Checkbox][1]

When uninstall tracking is enabled for an app, background push messages will be sent nightly to users who have not recorded a session or received a push in 24 hours. If you are interested in filtering Braze background push on iOS, you can use the utility method that was released in [iOS SDK version 2.13][iOS]; documentation for this methods can be found [here][iOS docs]. On Android, we are able to utilize Firebase Cloud Messaging's "dry run" feature to perform Uninstall Tracking without actually sending a notification to the device, and so filtering Braze uninstall background push is therefore unnecessary on Android. When Braze detects an uninstall, whether from Uninstall Tracking or normal push campaign delivery, we will record the best estimated time of the uninstall on the user. This time is stored in the user profile as a standard attribute.

![Uninstall Attribute][4]

This time can be used to define a segment of users for win-back campaigns. Using the Uninstalled filter on the Segments page, you can select users who uninstalled within a time range. Since determining the exact time of an uninstall is difficult, we recommend that uninstall filters have wider time ranges to make sure everyone who uninstalls falls into the segment at some point.

![Uninstall Segment][5]

## App-Level Analysis

Daily statistics on uninstalls are found on the App Usage page. The visualization can be broken down by segment, similar to other statistics Braze provides. View statistics for usage analytics, and then select Uninstalls from the dropdown to display the graph. The graph can then be broken down by segment, and by app, using the dropdowns. 

{% alert note %}
Note that apps without uninstall tracking enabled will report uninstalls from only a subset of their users (those who were targeted with push notifications), so daily uninstall totals may be higher than what is shown.
{% endalert %}

![Uninstall Graph Selection][2]

![Uninstall Graph][3]

## Uninstall Tracking for Campaigns

Campaign Uninstall Tracking allows you to see the number of users who received a specific campaign and subsequently uninstalled your app within the selected time frame. This tool gives marketers insight into how campaigns may be encouraging unintended negative user behaviors, and helps to measure overall campaign efficacy.

Braze tracks uninstalls by observing when push messages sent to users’ devices return a signal from either Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNs) that the app is no longer installed. If Global Uninstall Tracking is enabled for a particular app, Braze sends a daily silent push message to users to detect whether they have uninstalled (this “silent” push does not appear to users). If Braze detects that a user has uninstalled, that platform:

* Increments the App’s total uninstall count by 1.
* Increments the uninstall count for every campaign that the user successfully received in the past 24 hours by 1.
* If a user receives 3 campaigns in a 24 hour period and then uninstalls, we will increment the count of “uninstalls” for all 3 campaigns.

Uninstall Tracking is subject to restrictions placed on this information by FCM and APNs. Braze only increments the uninstall count when FCM or APNS tells us that a user has uninstalled, but these third-party systems reserve the right to notify us of uninstalls at any point in time. As a result, Uninstall Tracking should be used to detect directional trends as opposed to precise statistics.

To enable Uninstall Tracking, your user base should be on at least iOS SDK version 2.13. Turning on Uninstall Tracking for apps with users below this SDK version will send blank pushes to end users.

For more on using Uninstall Tracking, see [this blog post][7].

Uninstall statistics for campaigns are located on the Campaign Details page. For multichannel and multivariate campaigns, uninstalls can be broken down by channel and variant, respectively.

![Uninstall Campaign Level][6]

[1]: {% image_buster /assets/img_archive/Uninstall_Tracking2.png %} "Uninstall Tracking Checkbox"
[2]: {% image_buster /assets/img_archive/Uninstall_Tracking_App2.png %} "Uninstall Graph Selection"
[3]: {% image_buster /assets/img_archive/Uninstall_232.png %} "Uninstall Graph"
[4]: {% image_buster /assets/img_archive/User_Profile.png %} "Uninstall Attribute"
[5]: {% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment"
[7]: https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/
[iOS]: https://github.com/appboy/appboy-ios-sdk/blob/master/CHANGELOG.md "iOS Changelog"
[iOS docs]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/uninstall_tracking/
[6]: {% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %}
