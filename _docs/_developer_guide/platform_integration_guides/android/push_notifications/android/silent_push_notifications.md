---
nav_title: Silent Push Notifications
article_title: Silent Push Notifications for Android
platform: Android
page_order: 3
description: "This article covers how to implement silent push notifications in your Android application."
channel:
  - push

---

# Silent push notifications

Silent notifications allow you to notify your app in the background when important events occur. You might have new instant messages to deliver, new issues of a magazine to publish, breaking news alerts to send, or the latest episode of your user’s favorite TV show ready for them to download for offline viewing. Silent notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable.

Silent notifications are available through our [Messaging RESTful API][2]. You need only set the `send_to_sync` flag to `true` within the [Android Push Object][3]. You should ensure there are no `title` or `alert` fields set within the [Android Push Object][3] as it will cause errors when `send_to_sync` is set to `true`. You can however still include data `extras` within the [Android Push Object][3].

Silent notifications are also available within the dashboard. To send a silent notification, you need only to ensure the title and body fields of the notification are blank as pictured below:

![Android Silent Push Example][6]

This message will cause an intent to be received with an action `BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED`. Handling of this intent to cause any action such as a refresh of app content must be defined within the broadcast receiver you defined during the [standard Android integration][4]. Please see [CustomBroadcastReceiver.java][5] for an example of this receiver.

[2]: {{site.baseurl}}/api/endpoints/messaging/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[5]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/braze/custombroadcast/CustomBroadcastReceiver.java
[6]: {% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android"
