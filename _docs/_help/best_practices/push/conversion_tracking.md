---
nav_title: Conversion Tracking
page_order: 4
---

# Conversion Tracking

When assigning [conversion events][34] to a push campaign, you'll have the option to track app opens for a certain period after the campaign is received. Setting app opens as a conversion event provides different insight from the results statistics you normally receive after after a push campaign. While all push campaigns results break down a message's direct opens and opens ([which include both direct and influenced opens][35]), conversion tracking will track any type of open, whether it is direct or influenced.

In addition, by using the conversion event "opens app," you are tracking app opens that occur before that conversion deadline (for instance, 3 days). This differs from an influenced open in that the time a user has to register an influenced open can vary from individual to individual, and is on each user's past engagement behavior. For more information, see [this][48] deep dive on influenced opens.


[3]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[6]: {{ site.baseurl }}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/
[10]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[13]: {{ site.baseurl }}/help/best_practices/spam_regulations/#can-spam
[14]: {% image_buster /assets/img_archive/circa_push1.png %}
[15]: {% image_buster /assets/img_archive/circa_push2.png %}
[16]: {% image_buster /assets/img_archive/bn_push1.png %}
[17]: {% image_buster /assets/img_archive/bn_push2.png %}
[19]: {{ site.baseurl }}/help/best_practices/email/#email-sunset-policies
[23]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[24]: {% image_buster /assets/img_archive/textplus_prompt.png %}
[25]: {% image_buster /assets/img_archive/textplus_reminder.png %}
[26]: {% image_buster /assets/img_archive/textplus_directions.png %}
[27]: {% image_buster /assets/img_archive/android_push_img2.png %}
[29]: {% image_buster /assets/img_archive/braze_campaignresults.png %}
[30]: {% image_buster /assets/img_archive/Push_Reporting_Campaign_Statistics.png %}
[31]: {% image_buster /assets/img_archive/Push_Reporting_iOS_Push_Metric.png %}
[32]: {% image_buster /assets/img_archive/Push_Reporting_Message_Deliveries.png %}
[34]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[35]: {{ site.baseurl }}/user_guide/data_and_analytics/tracking/influenced_opens/#influenced-opens
[36]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[37]: {% image_buster /assets/img_archive/PushPrimeFandango.png %}
[38]: #bounced-push-notifications
[39]: https://developers.google.com/cloud-messaging/
[40]: https://www.braze.com/blog/breakdown-android-lollipops-new-notification-priorities-push-flexibility/
[41]: {% image_buster /assets/img_archive/braze_default.png %}
[42]: {% image_buster /assets/img_archive/iOS_push_notification_small.png %}
[43]: {% image_buster /assets/img_archive/Push_Android_2.png %}
[44]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/
[45]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[48]: {{ site.baseurl }}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[49]: https://medium.com/@hopper_travel/the-notification-problem-50267cbabad2#.auax13q52
[50]: http://developer.android.com/design/patterns/notifications.html
[51]: http://developer.android.com/design/patterns/notifications.html
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
[54]: {% image_buster /assets/img_archive/braze_richpush1.png %}
[55]: {% image_buster /assets/img_archive/braze_richpush2.png %}
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
[57]: {% image_buster /assets/img_archive/braze_subscribed.png %}
[58]: {% image_buster /assets/img_archive/braze_pushenabled.png %}
[59]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
