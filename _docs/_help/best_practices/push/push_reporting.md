---
nav_title: Reporting
page_order: 7
---

# Push Reporting

The Braze SDK provides you with a detailed report of each of your push campaigns. Navigate to the 'Campaigns' tab on your dashboard and click on the 'Details' tab of your desired campaign as shown below:

![Campaign Details][29]

On this page, you will be able to comprehensively view and analyze the success of your campaign in an organized format. Please find definitions of the different push-specific metrics below

| Statistic | Description |
| --------- | --- |
| Bounces | The push notifications sent to these users were undeliverable. These users have been automatically unsubscribed from all future push notifications. See [Bounced Push Notifications][38]. |
| Direct Opens | Instances in which a user opened your app by interacting directly with a push notification. |
| Opens | Instances including both Direct Opens (defined above) and Influenced Opens in which the Braze SDK has determined, using a proprietary algorithm, that a push notification has caused a user to open the app. |
{: .reset-td-br-1 .reset-td-br-2}

> Delivery of notifications is a “best effort” by APNs. It is not intended to deliver data to your app, only to notify the user that there is new data available. The important distinction is that we will display how many messages we successfully delivered to APNs, not necessarily how many APNs successfully delivered to devices.

## Bounced Push Notifications

### Apple Push Notification Service

Bounces occur in the APNs when a push notification attempts delivery to a device that does not have the intended app installed. APNs also has the right to change tokens for devices arbitrarily. If you attempt to send to a user’s device in which their push token has changed in between when we previously registered their token (i.e. at the beginning of each session when we register a user for a push token) and the time of send, this would cause a bounce.

If a user disables push within their device settings on subsequent app open the SDK will detect that push has been disabled and notify Braze. At this point we will update the push enabled state to be disabled. When a disabled user receives a push campaign before having a new session, the campaign would successfully send and appear as delivered. The push will not bounce for this user. Following a subsequent session, when you attempt to send a push to the user Braze is already aware of whether we have a token as such no notification is sent.

Push notifications that expire before delivery are not considered as failed and will not be recorded as a bounce.

### Firebase Cloud Messaging

FCM bounces could occur in three cases:

- **Uninstalled Applications**

When a message attempts delivery to a device and the intended app is uninstalled on that device, the message will be discarded and the device's registration ID will be invalidated. Any future attempts at messaging the device will return a NotRegistered error.

- **Backed Up Applications**

When an application is backed up, its registration ID could become invalid before the application is restored. In this case, FCM will no longer store the application's registration ID and the application will no longer receive messages. As such, registration IDs should _not_ be saved when an application is backed up.

- **Updated Applications**

When an application is updated, the previous version's registration ID may no longer work. As such, an updated application should replace its existing registration ID.


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
