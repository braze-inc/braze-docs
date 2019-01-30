---
nav_title: Push Subscription Status
page_order: 9
---

# Push Subscription Status

For a user to receive your messages through push, they must be Subscribed or Opted-In **AS WELL AS** Push Registered.

## Subscribed, Opted-In, and Unsubscribed

For **iOS**: A user has to explicitly opt-in to receive push notifications to their device after being prompted by the app.<br>

![opt-in][56]

For **Android**: no explicit opt-in is required to send users push notifications. When a user is registered for push on Android, they are set to subscribed.  An Android user must explicitly unsubscribe to push to stop receiving notifications.<br>

![subscribed][57]

For **Both**: the unsubscribed setting applies to those users who have unsubscribed from previously receiving push notifications.

## Where Does Push Registered Come Into Play?

A user is "Push Registered" if they have an active push token for an app in your app group.

On the User Engagement tab in the dashboard you will see: “**Push Registered For**” followed by an **App Name(s)** or followed by **No Apps**. There will be an entry for every device that belongs to the user.

<img width="329" alt="screen shot 2017-04-20 at 10 47 35 am" src="https://cloud.githubusercontent.com/assets/20304883/25244744/cd16d324-25b6-11e7-9d7c-d37b74690cf8.png">

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive background push and can not display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.

If a push token is moved a different user on the same device, that first user will no longer be push registered.

<img width="263" alt="screen shot 2017-04-20 at 10 48 29 am" src="https://cloud.githubusercontent.com/assets/20304883/25244775/ec6e0ae4-25b6-11e7-846d-4bf8f38c3057.png">

## Push Enabled

A Push enabled user is one who both is registered and subscribed/opted-in. This term is also used as a filter in our dashboard to target users who actually can receive messages.

To be specific, users who are "**push enabled is true**" have an active push token for their device, are Opted-In/Subscribed and are push registered so they can currently receive push notifications to their device..
Subsequently, "**push enabled is false**" means the user does not currently have a push token, are unsubscribed or not push registered and therefore will not receive a push campaign in their current state.

![push enabled][58]

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
[57]: {% image_buster /assets/img_archive/braze_subscribed.png %}
[58]: {% image_buster /assets/img_archive/braze_pushenabled.png %}
[59]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
