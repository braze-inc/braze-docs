---
nav_title: Why is my Campaign/Canvas Not Triggering?
page_order: 4
---

# Why Is My Campaign/Canvas Not Triggering?

There are a number of reasons why you did not get the expected trigger behavior.

The solution to the most common error, is to ensure that the campaign that you are triggering does not use the same trigger event in the segment.


## Campaign Triggers

Remember, if the user does not fall into the segment first, they will not receive the campaign even if they perform the trigger.

If your campaign is triggering off of a custom event, you will want to make sure that this event is not pre-filtered by a segment you want to input into the campaign. 

For example, if the Segment includes the event Session Start “Has Used App more than once” and the event the campaign triggers off of is Session Start, the user will receive the message, it just won’t necessarily be for the first session. This is because the first step when checking to see if a user should receive a campaign is reviewing the segment target audience. 

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).


[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-to-csv
[9]: {{site.baseurl}}/help/release_notes/2016/september/#segment-changelogs
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#logging-impressions-and-clicks
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/in-app_messaging/#setting-custom-listeners
[14]: {% image_buster /assets/img_archive/trouble6.png %}
[15]: {{site.baseurl}}/help/best_practices/in-app_messages/#in-app-message-specs
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#minimum-time-interval-between-triggers
[22]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/#properties-purchases
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[28]: {% image_buster /assets/img_archive/trouble8.png %}
[29]: {% image_buster /assets/img_archive/trouble9.png %}
[30]: {% image_buster /assets/img_archive/trouble10.png %}
[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[34]: {% image_buster /assets/img_archive/VennDiagram.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#user-preview
[36]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}
[43]: {% image_buster /assets/img_archive/trouble17.png %}
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rules
[46]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[48]: {% image_buster /assets/img_archive/targeting_error.png %}
[49]: {% image_buster /assets/img_archive/us_canada.png %}
[50]: {% image_buster /assets/img_archive/not_us_not_canada.png %}
