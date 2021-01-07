---
nav_title: Additional Android Push Best Practices
page_order: 0
---

# Additional Android Push Best Practices

## Android Push Priority

Android push notifications provide the option of dictating where notifications are displayed relative to other apps' notifications.  When composing the message for your push campaign, select "Notification Priority" in the settings tab to set a priority for your notification.

![Dashboard Push Priority Location][41]

The provided options correspond to different priorities with which the notification will be displayed if a receiving user has multiple notifications. A more in-depth explanation of Android Push Priority and the priority options can be found [here][40].

## Android Push Category
Android push notifications provide the option to specify if your notification falls into a predefined category. The Android system UI may use this Category to make ranking or filtering decisions about where to place the notification in the user's notification tray.

![Dashboard Push Priority Location][52]

| Category       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| None           | Default                                                                     |
| Alarm          | Alarm or timer                                                              |
| Call           | Incoming call (voice or video) or similar synchronous communication request |
| Email          | Asynchronous bulk message (email)                                           |
| Error          | Error in background operation or authentication status                      |
| Event          | Calendar event                                                              |
| Message        | Incoming direct message (SMS, instant message, etc.)                        |
| Progress       | Progress of a long-running background operation                             |
| Promotion      | Promotion or advertisement                                                  |
| Recommendation | A specific, timely recommendation for a single thing                        |
| Reminder       | User-scheduled reminder                                                     |
| Service        | Indication of running background service                                    |
| Social         | Social network or sharing update                                            |
| Status         | Ongoing information about device or contextual status                       |
| System         | System or device status update. Reserved for system use.                    |
| Transport      | Media transport control for playback                                        |
{: .reset-td-br-1 .reset-td-br-2}


[See Android Documentation for more info][51]

## Android Push Visibility
Android push notifications provide an optional field to determine how a notification appears on the user's lock screen. Notifications can be set to appear on the lock screen *(Public)*, to appear with the message "Contents Hidden" *(Private)*, or to be hidden entirely *(Secret)*.

Additionally, Android users can override how push notifications appear on their lock screen by changing the notification privacy setting on their device. This setting will override the Visibility from the push notification.

![Dashboard Push Priority Location][53]

Note that regardless of the Visibility, all notifications will be shown on the user's lock screen if the notification privacy setting on their device is *Show all content* (default setting). Likewise, notifications will not be shown on their lock screen if their notification privacy is set to *Do not show notifications*. The Visibility only has an effect if their notification privacy is set to *Hide sensitive content*. In that case, the notification will be displayed as follows:

* *Public* - Notification is shown on the lock screen
* *Private* - Notification is shown with "Contents hidden" as the message
* *Secret* - Notification is **not** shown on the lock screen

The Visibility has no effect on devices earlier than Android Lollipop 5.0.0; all notifications will be shown on such devices.

[See Android Documentation for more info][50]

[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[13]: {{site.baseurl}}/help/best_practices/spam_regulations/#can-spam
[14]: {% image_buster /assets/img_archive/circa_push1.png %}
[15]: {% image_buster /assets/img_archive/circa_push2.png %}
[16]: {% image_buster /assets/img_archive/bn_push1.png %}
[17]: {% image_buster /assets/img_archive/bn_push2.png %}
[19]: {{site.baseurl}}/help/best_practices/email/#email-sunset-policies
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[24]: {% image_buster /assets/img_archive/textplus_prompt.png %}
[25]: {% image_buster /assets/img_archive/textplus_reminder.png %}
[26]: {% image_buster /assets/img_archive/textplus_directions.png %}
[27]: {% image_buster /assets/img_archive/android_push_img2.png %}
[29]: {% image_buster /assets/img_archive/braze_campaignresults.png %}
[34]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[35]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[36]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[37]: {% image_buster /assets/img_archive/PushPrimeFandango.png %}
[38]: #bounced-push-notifications
[39]: https://developers.google.com/cloud-messaging/
[40]: https://www.braze.com/blog/breakdown-android-lollipops-new-notification-priorities-push-flexibility/
[41]: {% image_buster /assets/img_archive/braze_default.png %}
[42]: {% image_buster /assets/img_archive/iOS_push_notification_small.png %}
[43]: {% image_buster /assets/img_archive/Push_Android_2.png %}
[44]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/
[45]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[48]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[49]: https://medium.com/@hopper_travel/the-notification-problem-50267cbabad2#.auax13q52
[50]: http://developer.android.com/design/patterns/notifications.html
[51]: http://developer.android.com/design/patterns/notifications.html
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
[54]: {% image_buster /assets/img_archive/braze_richpush1.png %}
[55]: {% image_buster /assets/img_archive/braze_richpush2.png %}
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
[59]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
