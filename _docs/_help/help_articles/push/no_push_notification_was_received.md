---
nav_title: No Push Notification Was Received
page_order: 0
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

  Still need help? [Open a support ticket]({{ site.baseurl }}/support_contact/).


[1]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{ site.baseurl }}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{ site.baseurl }}/help/release_notes/2016/september/#segment-changelogs
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#logging-impressions-and-clicks
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/in-app_messaging/#setting-custom-listeners
[14]: {% image_buster /assets/img_archive/trouble6.png %}
[15]: {{ site.baseurl }}/help/best_practices/in-app_messages/#in-app-message-specs
[16]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/
[17]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[18]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/
[19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#minimum-time-interval-between-triggers
[20]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#minimum-time-interval-between-triggers
[21]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#minimum-time-interval-between-triggers
[22]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[23]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/#properties-purchases
[24]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[27]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[28]: {% image_buster /assets/img_archive/trouble8.png %}
[29]: {% image_buster /assets/img_archive/trouble9.png %}
[30]: {% image_buster /assets/img_archive/trouble10.png %}
[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[34]: {% image_buster /assets/img_archive/VennDiagram.png %}
[35]: {{ site.baseurl }}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#user-preview
[36]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[37]: {{ site.baseurl }}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}
[43]: {% image_buster /assets/img_archive/trouble17.png %}
[44]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rules
[46]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[47]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[48]: {% image_buster /assets/img_archive/targeting_error.png %}
[49]: {% image_buster /assets/img_archive/us_canada.png %}
[50]: {% image_buster /assets/img_archive/not_us_not_canada.png %}
