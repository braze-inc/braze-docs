## Ignoring internal push notifications

Braze uses [silent push notifications]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/silent/) for the internal implementation of certain advanced features. For most integrations, this requires no changes on your app's behalf. However, if you integrate a Braze feature that relies on internal push notifications (such as uninstall tracking or geofences), you may want to update your app to ignore internal pushes from Braze.

If your app takes automatic actions on application launches or background pushes, consider gating that activity so that it's not triggered by our internal push notifications. For example, if you have logic that calls your servers for new content upon every background push or application launch, you likely would not want Braze’s internal pushes triggering that because you would incur unnecessary network traffic. Furthermore, because Braze sends certain kinds of internal pushes to all users at approximately the same time, not gating network calls on launch from internal pushes could introduce significant server load.

## Checking your app for automatic actions

Check your application for automatic actions in the following places and update your code to ignore Braze’s internal pushes:

1. **Push Receivers.** Background push notifications will call `application:didReceiveRemoteNotification:fetchCompletionHandler:` on the `UIApplicationDelegate`.
2. **Application Delegate.** Background pushes can launch [suspended](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) apps into the background, triggering the `application:willFinishLaunchingWithOptions:` and `application:didFinishLaunchingWithOptions:` methods on your `UIApplicationDelegate`. Check the `launchOptions` of these methods to determine if the application has been launched from a background push.

## Using the internal push utility method

You can use the static utility method in `Braze.Notifications` to check if your app has received or was launched by a Braze internal push. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) will return `true` on all Braze internal push notifications, which include uninstall tracking, feature flags sync, and geofences sync notifications.

## Implementation example {#internal-push-implementation-example}

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
