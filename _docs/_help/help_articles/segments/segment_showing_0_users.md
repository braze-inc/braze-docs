---
nav_title: Segment is Showing 0 Users
page_order: 0
---
# Segment Is Showing 0 Users

There are two possible solutions when you are seeing ```0``` users, but you anticipated more:
* [Calculate Exact Statistics](#calculate-exact-statistics)
* [Verify Data Transfer](#verify-data-transfer)

## Calculate Exact Statistics

The Segment statistics could be providing an estimate. The estimation is calculated based on a random sample with a 95% confidence interval that the result is within ```+/- 1%```. The smaller your user base is, the more likely it is that the size of your segment is a rough estimate. Click on “Calculate Exact Statistics” on the Segment page. This will calculate the *exact* number of users in your segment.

![trouble8][28]


## Verify Data Transfer

It is possible that the data you are filtering on is not being sent to Braze. To check which Custom events are being sent to Braze, select “Custom Events” on the left hand menu in the “Data” section. Select the Custom event along with the specific dates and App to see what data is actually being transferred to Braze. If you notice that ```0``` data is being sent to Braze, the next step is to evaluate how you are sending the events to Braze.

![trouble9][29]

{% alert important %} 
The data that you see in the Braze dashboard might not have the identical syntax as what you are sending to Braze. Ensure that these two match exactly.
{% endalert %}

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
