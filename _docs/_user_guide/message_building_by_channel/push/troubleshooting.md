---
nav_title: Troubleshooting
article_title: Troubleshooting Push
page_order: 23
page_type: reference
description: "This page contains troubleshooting steps for various issues relating to the Push messaging channel."
channel: push
---

# Troubleshooting Push

> This page helps you troubleshoot various issues you may experience with the Push messaging channel.

## Missing push notifications

Experiencing delivery challenges with push notifications? There are a number of steps you can take to troubleshoot this issue by checking the:

- [Push subscription status](#push-subscription-status)
- [Segment](#segment)
- [Push notification caps](#push-notification-caps)
- [Rate limits](#rate-limits)
- [Control group status](#control-group-status)
- [Valid push token](#valid-push-token)
- [Push notification type](#push-notification-type)
- [Current app](#current-app)

#### Push subscription status

Pushes can only be sent to subscribed or opted-in users. Check your user profile in the [Engagement]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) tab in the **User Profile** section to confirm if you are actively registered for push for the workspace that you are testing. If you are registered for multiple apps, you will find them listed in the **Push Registered For** field:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

You can also export the user profiles using Braze export endpoints:
- [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Either endpoint will return a push token object that includes push enablement information per device.

#### Segment

Make sure you fall into the segment that you are targeting (if this is a live campaign and not a test). In the **User Profile**, you will see a list of segments that the user currently falls into. Remember this is an ever-changing variable as segmentation is updated in real time.

![List of Segments]({% image_buster /assets/img_archive/trouble2.png %})

You can also confirm that the user is part of the segment by using **User Lookup** when creating a segment.

![User Lookup section with a search field.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Push notification caps

Check the global frequency caps. It's possible you did not receive the push notification because your workspace has global frequency capping in place and you've already hit your push notification cap for the specified time frame.

You can do this by checking [global frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) in the dashboard. If the campaign is set to abide by frequency capping rules, there will be a number of users impacted by these settings

![Campaign Details]({% image_buster /assets/img_archive/trouble3.png %})

#### Rate limits

If you have a rate limit set for your campaign or Canvas, you might be falling out of receiving messaging due to exceeding this limit. For more information, refer to [Rate Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Control group status

If this is a single channel campaign or a Canvas with a control group, it's possible you are falling into the control group.

  1. Check the [variant distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) to see if there is a control group.
  2. If so, create a segment filtering for [in campaign control group]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) then [export the segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) and check if your user ID is on this list.

#### Valid push token
A push token is an identifier that senders use to target specific devices with a push notification. So, if the device does not have a valid push token, then there is no way to send a push notification to it. 

#### Push notification type

Check that you're using the correct type of push notification. For example, if you want to target a FireTV, then you would use a Kindle push notification, not an Android push campaign. Likewise, if you want to target an Android, use an Android push notification and not an iOS push campaign. Check out the following articles for more information on understanding the Braze workflow for:
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Current app

When testing push sends with internal users, make sure that the user who you want to receive the push notification is currently logged into the relevant app. This can lead to the user either not receiving a push or receiving a push you believe they aren't segmented for.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

