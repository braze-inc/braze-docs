---
nav_title: No Push Notification Was Received
page_order: 0

page_type: solution
description: "This help article walks you through troubleshooting steps you can take if users are not receiving your push notifications."
channel: push
---
# No Push Notification Was Received

There are a number of steps you can take to troubleshoot this issue:

* [Check User Profiles](#check-user-profiles)
* [Check Segment](#check-segment)
* [Check Push Notification Caps](#check-push-notification-caps)
* [Check Rate Limits](#check-rate-limits)
* [Check Control Group Status](#check-control-group-status)


## Check User Profiles

Check your user profile within the [“Engagement” tab] [1] in the “User Profile” to see if you are actively registered for push for the App group that you are testing. If you are registered for multiple Apps, you will see them listed within the “Push Registered For” field:

![trouble1][2]

## Check Seqment

Ensure you fall into the Segment that you are targeting (if this is a live campaign and not a test). In the “User Profile” you will see a list of segments that the user currently falls into. Remember, this is an ever-changing variable as segmentation is updated in real time.

![trouble2][3]

## Check Push Notification Caps

Check the Global Frequency Caps. It’s possible you did not receive the push notification because your App group has global frequency capping in place and you’ve already hit your push notification cap for the specified time frame.

You can do this by checking [global frequency capping][4] within the dashboard. NB if the campaign is set to abide by frequency capping rules, there will be a number of users impacted by these settings

![trouble3][5]

## Check Rate Limits

If you have a rate limit set for your Campaign or Canvas, you might be falling out of receiving messaging due to exceeding this limit. Check out this section of Academy to learn more about [rate limits][47].

## Check Control Group Status

If this is a single channel Campaign or a Canvas with a control group, it’s possible you are falling into the control group.

  * Check the [distribution][6] to see if there is a control group.
  * Additionally, create a segment [using this filter][7], and [export the segment][8] and see if your user ID is on this list.

  Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).


[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
