---
nav_title: Ignoring Internal Push
article_title: Ignoring Braze's Internal Push Notifications for iOS
platform: Swift
page_order: 6
description: "This article covers how to ignore Braze's internal push notifications."
channel:
  - push

---

# Ignoring Braze's internal push notifications for iOS

Braze uses [silent push notifications][2] for the internal implementation of certain advanced features. For most integrations, this requires no changes on your app's behalf. However, if you integrate a Braze feature that relies on internal push notifications (such as uninstall tracking or geofences), you may want to update your app to ignore Braze's internal pushes.

If your app takes automatic actions on application launches or background pushes, consider gating that activity so that it's not triggered by Braze's internal push notifications. For example, if you have logic that calls your servers for new content upon every background push or application launch, you likely would not want Braze’s internal pushes triggering that because you would incur unnecessary network traffic. Furthermore, because Braze sends certain kinds of internal pushes to all users at approximately the same time, not gating network calls on launch from internal pushes could introduce significant server load.

## Checking your app for automatic actions

Check your application for automatic actions in the following places and update your code to ignore Braze’s internal pushes:

1. **Push Receivers.** Background push notifications will call `application:didReceiveRemoteNotification:fetchCompletionHandler:` on the `UIApplicationDelegate`.
2. **Application Delegate.** Background pushes can launch [suspended][4] apps into the background, triggering the `application:willFinishLaunchingWithOptions:` and `application:didFinishLaunchingWithOptions:` methods on your `UIApplicationDelegate`. Check the `launchOptions` of these methods to determine if the application has been launched from a background push.

## Using Braze's internal push utility method

You can use the static utility method in `Braze.Notifications` to check if your app has received or was launched by a Braze internal push. [`Braze.Notifications.isInternalNotification(_:)`][1] will return `true` on all Braze internal push notifications, which include uninstall tracking, feature flags sync, and geofences sync notifications.

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

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[4]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3