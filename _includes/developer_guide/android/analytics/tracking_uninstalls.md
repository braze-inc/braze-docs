## Setting up uninstall tracking

### Step 1: Set up FCM

The Android Braze SDK uses Firebase Cloud Messaging (FCM) to send silent push notifications, which are used to collect uninstall tracking analytics. If you haven't already, [set up]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) or [migrate to]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) the Firebase Cloud Messaging API for push notifications.

### Step 2: Manually detect uninstall tracking (optional)

By default, the Android Braze SDK will automatically detect and ignore silent push notifications related to uninstall tracking. However, you choose to manually detect uninstall tracking using the [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) method.

{% alert important %}
Because silent notifications for uninstall tracking are not forwarded to any Braze push callbacks, you can only use this method before you pass a push notification to Braze.
{% endalert %}

### Step 3: Remove automatic server pings

A silent push notification will wake your app and instantiate the `Application` component if it app isn't already running. So, if you have a custom [`Application`](https://developer.android.com/reference/android/app/Application) subclass, remove any logic that automatically pings your servers during your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) lifecycle method.

### Step 4: Enable uninstall tracking

Finally, enable uninstall tracking in Braze. For a full walkthrough, see [Enable uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Tracking uninstalls can be imprecise. The metrics you see on Braze may be delayed or inaccurate.
{% endalert %}
