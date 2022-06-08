---
nav_title: Push Notifications
article_title: Push Notifications for React Native
platform: React Native
page_order: 2
description: "This article covers implementing push notifications on React Native."
channel: push

---

# Push notifications

Integrating push notifications in React Native requires setting up each native platform separately. Follow the respective guides listed to finish the installation.

## Step 1: Complete native setup

- Android: Follow the [Android integration instructions][1].
- iOS: Follow the [iOS integration instructions][2].

## Step 2: Test displaying push notifications

At this point, you should be able to send notifications to the devices. Adhere to the following steps to test your push integration.

{% alert important %}
You can't test push notification related app behavior on an iOS simulator because simulators don't support the device tokens required to send and receive a push notification.
{% endalert %}

1. Set an active user in the React application by calling `ReactAppboy.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and create a new push notification campaign. Choose the platforms that you'd like to test.
3. Compose your test notification and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**. You should receive the notification on your device shortly.

![A Braze push campaign showing you can add your own user ID as a test recipient to test your push notification.][3]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[3]: {% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test"

