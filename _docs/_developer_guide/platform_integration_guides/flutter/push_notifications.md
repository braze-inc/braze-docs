---
nav_title: Push Notifications
article_title: Push Notifications for Flutter
platform: Flutter
page_order: 2
description: "This article covers implementing push notifications on Flutter."
channel: push

---

# Push notifications

Integrating push notifications in Flutter requires setting up each native platform separately. Follow the respective integration guides to finish the installation.

## Step 1: Complete native setup

- **Android:** Follow the [Android integration instructions][1].
- **iOS:** Follow the [iOS integration instructions][2].

## Step 2: Test displaying push notifications

Follow these steps to test your push integration.

{% alert important %}
You can't test push notification related app behavior on an iOS simulator because simulators don't support the device tokens required to send and receive a push notification.
{% endalert %}

1. Set an active user in the Flutter application. To do so, initialize your plugin by calling `braze.changeUser('your-user-id')`.
2. Head to **Campaigns** and create a new push notification campaign. Choose the platforms that you'd like to test.
3. Compose your test notification and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**.
4. You should receive the notification on your device shortly. You may need to check in the Notification Center or update Settings if it doesn't display.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
