---
nav_title: Uninstall Tracking
article_title: Uninstall Tracking for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "This article covers how to configure uninstall tracking for your Android application."

---

# Uninstall tracking for Android and FireOS

Uninstall tracking utilizes a silent push from Firebase Cloud Messaging to detect uninstalled devices. Starting in Braze Android SDK v3.1.0, we will intelligently drop the uninstall tracking notification and not wake up any custom broadcast receivers in your app with the regular silent push intent.

If you wish to detect if the push notification is uninstall-tracking yourself, use [`isUninstallTrackingPush()`][3].

{% alert important %}
Since uninstall tracking silent push is not forwarded to your custom broadcast receiver, this method can only be used before the push notification is passed to Braze, such as when using a custom [Firebase Messaging Service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-register-braze-firebase-messaging-service).
{% endalert %}

If you have a custom [`Application`][1] subclass, make sure you do not have automatic logic that pings your servers in your [`Application.onCreate()`][2] lifecycle method. This is because a silent push will wake your app and instantiate the`Application` component if the app is not already running.

See [Uninstall Tracking][4] in our User Guide for more information.

[1]: https://developer.android.com/reference/android/app/Application
[2]: https://developer.android.com/reference/android/app/Application#onCreate()
[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
