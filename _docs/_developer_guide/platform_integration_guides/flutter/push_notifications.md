---
nav_title: Push Notifications
article_title: Push Notifications for Flutter
platform: Flutter
page_order: 2
description: "This article covers implementing push notifications on Flutter."
channel: push

---

# Push notifications for Flutter

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

{% alert important %}
Braze does not support using the Flutter wrapper layer for sending push notifications or deep links. To use this feature with your Flutter app, you will need to configure push notifications for each native platform separately. 
- **Android:** Follow the [Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/).
- **iOS:** Follow the [iOS integration instructions](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications).
{% endalert %}


## Test push notifications

Once you've configured push notifications in the native layer, follow these steps to test your push integration.

{% alert important %}
You can't test push notification related app behavior on an iOS simulator because simulators don't support the device tokens required to send and receive a push notification.
{% endalert %}

1. Set an active user in the Flutter application. To do so, initialize your plugin by calling `braze.changeUser('your-user-id')`.
2. Head to **Campaigns** and create a new push notification campaign. Choose the platforms that you'd like to test.
3. Compose your test notification and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. You should receive the notification on your device shortly. You may need to check in the Notification Center or update Settings if it doesn't display.
