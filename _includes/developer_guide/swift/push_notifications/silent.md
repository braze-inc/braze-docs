{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## iOS limitations

The iOS operating system may gate notifications for some features. Note that if you are experiencing difficulties with these features, the iOS's silent notifications gate might be the cause. For more details, refer to Apple's [instance method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) and [unreceived notifications](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) documentation.

## Setting up silent push notifications

To use silent push notifications to trigger background work, you must configure your app to receive notifications even when it is in the background. To do this, add the Background Modes capability using the **Signing & Capabilities** pane to the main app target in Xcode. Select the **Remote notifications** checkbox.

![Xcode showing the "remote notifications" mode checkbox under "capabilities".]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Even with the remote notifications background mode enabled, the system will not launch your app into the background if the user has force-quit the application. The user must explicitly launch the application or reboot the device before the app can be automatically launched into the background by the system.

For more information, refer to [pushing background updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) and the `application:didReceiveRemoteNotification:fetchCompletionHandler:` [documentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## Sending silent push notifications

To send a silent push notification, set the `content-available` flag to `1` in a push notification payload. 

{% alert note %}
What Apple calls a remote notification is just a normal push notification with the `content-available` flag set.
{% endalert %}

The `content-available` flag can be set in the Braze dashboard as well as within our [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in the [messaging API]({{site.baseurl}}/api/endpoints/messaging/).

{% alert warning %}
Attaching both a title and body with `content-available=1` is not recommended because it can lead to undefined behavior. To ensure that a notification is truly silent, exclude both the title and body when setting the `content-available` flag to `1.` For further details, refer to the official [Apple documentation on background updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![The Braze dashboard showing the "content-available" checkbox found in the "settings" tab of the push composer.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

When sending a silent push notification, you might also want to include some data in the notification payload, so your application can reference the event. This could save you a few networking requests and increase the responsiveness of your app.

### Dashboard preview vs. actual behavior

{% alert note %}
**Important:** The Braze dashboard preview will display a visual representation of your push notification even for silent pushes. This is for preview purposes only and does not reflect how the notification will behave on a device. On the device, properly configured silent notifications will not display any UI or play any sounds.
{% endalert %}

## Using silent push with badge counts

To update your app's badge count with a silent push notification:

1. Enable the `content-available` flag in your push notification
2. Set a badge number in the dashboard or via the API
3. Do not include a title or message to ensure the notification remains silent

```swift
// Example handling of badge count from a silent push:
func application(
  _ application: UIApplication, 
  didReceiveRemoteNotification userInfo: [AnyHashable: Any],
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  if let badgeCount = userInfo["aps"]?["badge"] as? NSNumber {
    UIApplication.shared.applicationIconBadgeNumber = badgeCount.intValue
  }
  completionHandler(.newData)
}
```

{% alert important %}
To use badge count in the composer, the `badge_count_in_composer` feature flag must be enabled for your app group. Contact Braze support to enable this feature.
{% endalert %}

## Ignoring internal push notifications

Braze uses silent push notifications to internally handle certain advanced features, such as uninstall tracking or geofences. If your app takes automatic actions on application launches or background pushes, consider gating that activity so it's not triggered by any internal push notifications.

For example, if you have logic that calls your servers for new content upon every background push or application launch, you may want to prevent triggering Braze's internal pushes to avoid unnecessary network traffic. Because Braze sends certain kinds of internal pushes to all users at approximately the same time, significant server load may occur if on-launch network calls from internal pushes are not gated.

### Step 1: Check your app for automatic actions

Check your application for automatic actions in the following places and update your code to ignore Braze's internal pushes:

1. **Push Receivers.** Background push notifications will call `application:didReceiveRemoteNotification:fetchCompletionHandler:` on the `UIApplicationDelegate`.
2. **Application Delegate.** Background pushes can launch [suspended](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) apps into the background, triggering the `application:willFinishLaunchingWithOptions:` and `application:didFinishLaunchingWithOptions:` methods on your `UIApplicationDelegate`. Check the `launchOptions` of these methods to determine if the application has been launched from a background push.

### Step 2: Use the internal push utility method

You can use the static utility method in `Braze.Notifications` to check if your app has received or was launched by a Braze internal push. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) will return `true` on all Braze internal push notifications, which include uninstall tracking, feature flags sync, and geofences sync notifications.

For example:

{% tabs %}
{% tab swift %}

```swift
func application(_ application: UIApplication,
               didReceiveRemoteNotification userInfo: [AnyHashable : Any],
               fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}

## For more information

For a comprehensive guide on silent push notifications, including troubleshooting and best practices, see our [Silent Push Notifications Guide]({{site.baseurl}}/user_guide/message_building_by_channel/push/silent_push_notifications_guide/).