---
nav_title: Uninstall Tracking
platform: Android
page_order: 7
search_rank: 5
---
## Uninstall Tracking

Uninstall Tracking utilizes a silent push from Firebase Cloud Messaging to detect uninstalled devices. However, If the app is still installed, then this silent push is received by your app. Starting in Braze Android SDK v3.1.0, we will intelligently drop the uninstall tracking notification and not wake up any custom broadcast receivers in your app.

If you wish to detect if the push notification is uninstall tracking yourself, please use [`isUninstallTrackingPush()`][3].

If you have a custom [Application][1] subclass, make sure you do not have automatic logic that pings your servers in your [`Application.onCreate()`][2] lifecycle method. This is because silent push wakes up your app, if it's not already running.

For more information, see the [Uninstall Tracking][4] page in our User Guide.

[1]: https://developer.android.com/reference/android/app/Application
[2]: https://developer.android.com/reference/android/app/Application#onCreate()
[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/push/AppboyNotificationUtils.html#isUninstallTrackingPush-android.os.Bundle-
[4]: {{ site.baseurl }}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
