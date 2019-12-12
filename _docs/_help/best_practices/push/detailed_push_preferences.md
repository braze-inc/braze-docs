---
nav_title: Detailed Push Preferences
page_order: 1
---

# Detailed Push Preferences

Push notifications should be treated with care to target users with timely and relevant notifications. Braze will collect useful device and usage information that can be used to target relevant segments. This should be supplemented with custom events and attributes specific to your app. Using that data you can carefully target messages to increase open rates and decrease instances of users disabling push.

![Circa Message Settings][15]

Additionally, you can create a settings page in your app that allows users to directly tell you which notifications they want to receive. This can be set as a boolean attribute in Braze that corresponds to the app setting status. For example, a news app could have subscription settings for the following:

- Breaking News
- Sports News
- Politics
- Business News

When the news app wants to create a campaign targeting only users interested in Politics, they simply add the 'Subscribes to Politics' attribute filter to the segment. When set to true, only users who subscribe to notifications will receive them.

![Example of Opt-In Prompts][14]

The general stats that you see for push enabled will relate to whether the user has approved notifications with the OS. If users disable notifications on iOS they'll be automatically removed from our system since Apple won't allow the push token to be sent. Android subscribes users to notifications by default.

Documentation for setting custom attributes:

- [iOS][4]
- [Android][5]
- [Windows Universal][6]
- [REST API][10]

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
[34]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[35]: {{ site.baseurl }}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
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
[59]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
