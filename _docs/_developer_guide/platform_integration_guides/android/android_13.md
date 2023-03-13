---
nav_title: Android 13 Upgrade Guide
article_title: Android 13 Upgrade Guide
page_order: 9
platform: 
  - Android
  - FireOS
description: "This article covers Android 13, SDK updates, changes to push permission, SDK compatibility, and more."
---
<br>

# Android 13 SDK upgrade guide

This guide describes relevant changes introduced in Android 13 (2022) and the required upgrade steps for your Braze Android SDK integration.

Refer to the [Android 13 developer documentation][2] for a full migration guide.

## Android 13 Braze SDK

To prepare for Android 13, please upgrade your Braze SDK to the [latest version (v21.0.0+)][1]. Doing so will give you access to our new ["no-code" push primer feature][7].

## Changes in Android 13

### Push permission {#push-permission}

Android 13 introduces a [major change][3] in how users manage apps that send push notifications. In Android 13, apps are required to obtain permission before push notifications can be shown. 

![An Android push message asking "Allow Kitchenerie to send you notifications?" with two buttons "Allow" and "Don't allow" at the bottom of the message.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

This new permission follows a similar pattern to iOS and Web push, where you only have one attempt to obtain permission. If a user chooses `Don't Allow` or dismisses the prompt, your app cannot ask for permission again.

Note that apps are granted an [exemption][4] for users who previously had push notifications enabled prior to updating to Android 13. These users [will remain eligible][8] to receive push when they update to Android 13 without having to request permission.

#### Permission prompt timing {#push-permission-timing}

**Targeting Android 13**

Apps targeting Android 13 can control when to request permission and show the native push prompt. 

If your user upgrades from Android 12 to 13, your app was previously installed, and you were already sending push, the system automatically pre-grants the new notification permission to all eligible apps. In other words, these apps can continue to send notifications to users, and users don't see a runtime permission prompt.

For more details on this see Android's Developer Documentation for [effects on updates to existing apps][8].

**Targeting Android 12 or earlier**

If your app does not yet target Android 13, then a new user on Android 13 installs your app, they will automatically see a push permission prompt when your app creates its first notification channel (via `notificationManager.createNotificationChannel`). Users who already have your app installed and then upgrade to Android 13 are never shown a prompt and are automatically granted push permission.

{% alert note %}
Braze SDK v23.0.0 automatically creates a default notification channel if one does not already exist when a push notification is received. If you don't target Android 13, this will cause the push permission prompt to be shown, which is required to show the notification.
{% endalert %}

## Preparing for Android 13 {#next-steps}

It is strongly recommended that your app targets Android 13 in order to control when users are prompted for push permission.

This will allow you to optimize your [push opt-in rates][6] by prompting users at more appropriate times and will lead to a better user experience in how and when your app asks for push permission.

To start using our new ["no-code" push primer feature][7], upgrade your Android SDK to the [latest version (v23.0.0+)][1].

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300
[2]: https://developer.android.com/about/versions/13
[3]: https://developer.android.com/about/versions/13/changes/notification-permission
[4]: https://developer.android.com/about/versions/13/changes/notification-permission#eligibility
[5]: https://developer.android.com/about/versions/13/overview#platform_stability
[6]: https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[8]: https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps
