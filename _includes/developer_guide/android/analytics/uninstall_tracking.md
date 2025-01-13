# Uninstall tracking

> Uninstall tracking uses a silent push from Firebase Cloud Messaging to detect uninstalled devices. Braze will intelligently drop the uninstall tracking notification and not wake up any custom push callbacks in your app with the regular silent push intent. This article covers how to configure uninstall tracking for your Android or FireOS application.

If you wish to detect if the push notification is uninstall-tracking yourself, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html).

{% alert important %}
Since uninstall tracking silent push is not forwarded to any Braze push callbacks, this method can only be used before the push notification is passed to Braze, such as when using a custom [Firebase Messaging Service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service).
{% endalert %}

If you have a custom [`Application`](https://developer.android.com/reference/android/app/Application) subclass, make sure you do not have automatic logic that pings your servers in your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) lifecycle method. This is because a silent push will wake your app and instantiate the`Application` component if the app is not already running.

See [Uninstall Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) in our User Guide for more information.

