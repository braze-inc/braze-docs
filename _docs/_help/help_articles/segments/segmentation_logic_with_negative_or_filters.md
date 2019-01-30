---
nav_title: Segmentation Logic With Negative Or Filters
page_order: 2
---

# Segmentation Logic With Negative OR Filters

The OR operator must be used with care, especially when considering:
* [When to apply the OR operator](#using-or)
* [When not to apply the OR operator](#when-not-to-apply-the-or-operator)
* [When to apply the AND operator](when-to-apply-the-and-operator)

# Using OR

The "OR" operator allows you to create a statement that will evaluate to true if a user meets the criteria for one or more filters in the statement. For example, consider a promotion that is valid for your US and Canadian customers. You want to make sure that only customers in areas where the promotion is valid receive the promotion. You can use the following statement to target your campaign: `Country is United States OR Country is Canada`

![us_or_canada][49]

A customer who meets one or more of the country filters will receive your campaign so your campaign will only go to customers whose country is Canada or whose country is United States.

# When Not to Apply the OR Operator

In certain circumstances, the "OR" operator should not be used, it is possible to break the logic. For example, let's say that you have a campaign that is valid in every country EXCEPT for the US and Canada. Inverting our logic from the last scenario leads to a segment that targets **all** customers: `Country is not United States OR Country is not Canada`


![not_us_or_canada][50]

The above statement will target all customers, because all customers will meet the criteria for one or more of the filters. Canadian customers meet the criteria for "Country is not United states". US customers meet the criteria for "Country is not Canada".

The negative targeting criteria "is not" and "does not equal" **should not** be used with the "OR" operator when two or more filters are referencing the same attribute. If "is not" or "does not equal" is used with the "OR" operator two or more times in a statement, customers will all values for the relevant attribute will be targeted.

## When To Apply the AND Operator

If you'd like to include customers with two or more values for a particular attribute, you should use the "AND" operator. Let's return to our use case - targeting customers from every country except for Canada and the United States.

`Country is not United States AND Country is not Canada` will only include customers who are not from the United States AND who are not from Canada. Therefore, both United States customers and Canadian customers will be excluded.

Because there are no valid use cases for using "Or" operands with two or more negative filters that have the same attribute, Braze will not allow you to continue creating your campaign or segment if you use this configuration with "does not equal" or "is not" comparisons.

![targeting_error][48]

If you received this warning message and aren't sure how to correct your campaign, canvas or segment, please get in touch with your Customer Success Manager or write to our support team.

Still need help? [Open a support ticket]({{ site.baseurl }}/docs/support_contact/).

[1]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#overview-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-to-csv
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
[31]: {% image_buster /assets/img_archive/trouble11.png %}
[32]: {% image_buster /assets/img_archive/trouble12.png %}
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
