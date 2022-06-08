---
nav_title: Missing Push Notifications
article_title: Missing Push Notifications
page_order: 3

page_type: solution
description: "This help article walks you through troubleshooting steps you can take if users are not receiving your push notifications."
channel: push
---
# Missing push notifications

Experiencing delivery challenges with push notifications? There are a number of steps you can take to troubleshoot this issue by checking the:

* [Push subscription status](#check-push-subscription-status)
* [Segment](#check-segment)
* [Push notification caps](#check-push-notification-caps)
* [Rate limits](#check-rate-limits)
* [Control group status](#check-control-group-status)

### Push subscription status

Check your user profile in the [Engagement][1] tab in the **User Profile** section to see if you are actively registered for push for the app group that you are testing. If you are registered for multiple apps, you will see them listed in the **Push Registered For** field:

![Push Registered For][2]

You can also export the user profiles using Braze export endpoints:
- [Users by identifier][12]
- [Users by segment][13]
This will return a push token object that includes push enablement information per device.

### Segment

Make sure you fall into the segment that you are targeting (if this is a live campaign and not a test). In the **User Profile**, you will see a list of segments that the user currently falls into. Remember this is an ever-changing variable as segmentation is updated in real time.

![List of Segments][3]

### Push notification caps

Check the global frequency caps. It’s possible you did not receive the push notification because your app group has global frequency capping in place and you’ve already hit your push notification cap for the specified time frame.

You can do this by checking [global frequency capping][4] in the dashboard. If the campaign is set to abide by frequency capping rules, there will be a number of users impacted by these settings

![Campaign Details][5]

### Rate limits

If you have a rate limit set for your campaign or Canvas, you might be falling out of receiving messaging due to exceeding this limit. For more information, refer to [Rate Limiting][9].

### Control group status

If this is a single channel campaign or a Canvas with a control group, it’s possible you are falling into the control group.

  1. Check the [variant distribution][6] to see if there is a control group.
  2. If so, create a segment filtering for [in campaign control group][7] then [export the segment][8] and check if your user ID is on this list.

### Valid push token
A push token is an identifier that senders use to target specific devices with a push notification. So, if the device does not have a valid push token, then there is no way to send a push notification to it. 

### Push notification type

Check that you're using the correct type of push notification. For example, if you want to target a FireTV, then you would use a Kindle push notification, not an Android push campaign. Check out the following articles for more information on unstanding the Braze workflow for:
- [Apple Push Notification][10]
- [Firebase Cloud Messaging][11]

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on January 21, 2021_

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment