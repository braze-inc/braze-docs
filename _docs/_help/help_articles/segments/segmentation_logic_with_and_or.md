---
nav_title: Using Segmentation Logic with And/Or
page_order: 1
---

# Using Segmentation Logic With And/Or

The And/Or operators enable some very powerful filtering. There are 2 scenarios you may wish to apply:
* [Using AND or OR](#using-and-or-or)
* [Using Both](#using-both)

## Using AND or OR

### AND

Use **AND** if you are interested in the intersection of two groups. This is, what is similar between the two groups. For example let’s compare two animals. What dogs **AND** cats both have in common is fur, are mammals, and are human pets (highlighted in red in the photo below):

![trouble10][30]

### OR

Use **OR** if you want to target users who meet at least one condition in a group of conditions. If you have three conditions linked together by "OR", one, two or all of the conditions could be true in order for the statement to be true.

For example, imagine that you want to send a message to all your users __except__ those users on version ```1.0``` or ```1.1``` of your App. You want to target the overlap of users that are not on version ```1.0``` and not on version ```1.1.``` You can create this segment in one of two ways:

    
* You can use two filters “is not ```1.0```” OR “is not ```1.1```”. Using this **OR** filter you are targeting all users that do not have those versions.
	
* The alternative may be a longer route. You will need to add a filter for every version of your app using the OR statement, making sure to exclude app versions ```1.0``` and ```1.1```.


# Using Both

Finally, look at the example below where we are using both the **AND** and **OR**. The target audience here are users who've purchased Nike Sneakers **OR** Adidas sneakers **AND** are opted in to receive email notifications.

![trouble13][33]

![trouble14][34]

Another way to ensure you’re building the right logic, is to create your segment and [preview the users][35] who are falling into it based on your filters. This way, you can make sure that their attributes, App version, or any other segmentation matches what you are seeing.

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
[35]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
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
