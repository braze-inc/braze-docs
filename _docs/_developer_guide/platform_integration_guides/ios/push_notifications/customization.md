---
nav_title: Customization
platform: iOS
ex_push_payload: archive/apple/push_payload.json
page_order: 1

---
# Customization {#push-customization}

## Badge Counts

You can specify the desired badge count when you compose a push notification through Braze's dashboard. You may also update your badge count manually through your application's [`applicationIconBadgeNumber`][20] property or through the [remote notification payload][21]. Braze will also clear the badge count when a Braze notification is received while the app is foregrounded. If you do not have a plan for clearing badges as part of normal app operation or by sending pushes which clear the badge, you should clear the badge when the app becomes active by adding the following code to your app's `applicationDidBecomeActive:` delegate method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Please note that setting the badge number to 0 will also clear up notifications in the notification center. So even if you don't set badge number in push payloads, you can still set the badge number to 0 to remove the push notification(s) in the notification center after users clicked on the push.

## Action Buttons {#push-action-buttons-customization}

In addition to providing a set of [default push categories][2], Braze supports custom notification categories and actions. Once you register categories in your application, you can use the Braze dashboard to send notification categories to your users.

>  If you are not using the `UserNotifications` framework, please see this [alternative categories documentation][31].

These categories can then be assigned to push notifications via our dashboard to trigger the action button configurations of your design. Here's an example that leverages the "LIKE_CATEGORY" displayed on the device!

![Push Example with Buttons][17]

## Sample Braze Apple Push Payload

When Braze sends a push notification, the payload will look like this. You should avoid handling a top-level dictionary called `ab` or `aps` in your application:

{% include {{ page.ex_push_payload}} %}

>  the `alert` can also just be a string, which will be the push message text.

In the case that your push notification does not have a campaign ID, the key `c` will have the value `NSNull`. This value is necessary and should not be sanitized or removed. Some cases where there is no campaign ID are sending a push from an API campaign, a test push from the dashboard, or a test curl.

## Custom Sounds and Push

### Step 1: Hosting the Sound in the App

Custom push notification sounds must be hosted locally within the main bundle of the client application. The following audio data formats are accepted:

- Linear PCM
- MA4
- µLaw
- aLaw

You can package the audio data in an aiff, wav, or caf file. Then, in Xcode, add the sound file to your project as a nonlocalized resource of the application bundle.

You may use the afconvert tool to convert sounds. For example, to convert the 16-bit linear PCM system sound Submarine.aiff to IMA4 audio in a CAF file, use the following command in the Terminal application:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

You can inspect a sound to determine its data format by opening it in QuickTime Player and choosing Show Movie Inspector from the Movie menu.

Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.

### Step 2: Providing the Dashboard with a Protocol URL for the Sound

Your sound must be hosted locally within the app. You must specify a Protocol URL that directs to the location of the sound file in the app within the "Sound" field in the push composer. Specifying “default” in this field will play the default notification sound on the device. This can be specified via our [Messaging API][25] or our dashboard under “Advanced Settings” in the push composer wizard as pictured below:

![Push Notification Sound][8]

If the specified sound file doesn’t exist or the keyword ‘default’ is entered, Braze will use the default device alert sound. Aside from our dashboard, sound can also be configured via our our [Messaging API][12]. For additional information see the Apple Developer Documentation regarding ["Preparing Custom Alert Sounds"][9].

## Ignoring Braze's Internal Push Notifications
Braze uses silent push notifications for internal implementation of certain advanced features. For most integrations, this requires no changes on your app's behalf. However, if you integrate a Braze feature that relies on internal push notifications (i.e., uninstall tracking or geofences), you may want to update your app to ignore Braze's internal pushes.

If your app takes automatic actions on application launches or background pushes, you should consider gating that activity so that it's not triggered by Braze's internal push notifications. For example, if you have logic that calls your servers for new content upon every background push or application launch, you likely would not want Braze’s internal pushes triggering that because you would incur unnecessary network traffic. Furthermore, because Braze sends certain kinds of internal pushes to all users at approximately the same time, not gating network calls on launch from internal pushes could introduce significant server load.

### Checking Your App for Automatic Actions

You should check your application for automatic actions in the following places and update your code to ignore Braze’s internal pushes:

1. **Push Receivers.** Background push notifications will call `application:didReceiveRemoteNotification:fetchCompletionHandler:` on the `UIApplicationDelegate`.
2. **Application Delegate.** Background pushes can launch [suspended][4] apps into the background, triggering the `application:willFinishLaunchingWithOptions:` and `application:didFinishLaunchingWithOptions:` methods on your `UIApplicationDelegate`. You can check the `launchOptions` of these methods to determine if the application has been launched from a background push.

### Using Braze's Internal Push Utility Methods

You can use the utility methods in `ABKPushUtils` to check if your app has received or was launched by a Braze internal push. `isAppboyInternalRemoteNotification:` will return `YES` on all Braze internal push notifications, while `isUninstallTrackingRemoteNotification:` and `isGeofencesSyncRemoteNotification:` will return `YES` for uninstall tracking and geofences sync notifications, respectively.
See [`ABKPushUtils.h`][1] for method declarations.

### Implementation Example {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (e.g., pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (e.g., pinging server for content) ...
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] as? NSDictionary as? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (e.g., pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (e.g., pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

## Extracting Data from Push Notification Key Value Pairs

Braze allows you to send custom-defined string key value pairs, known as extras, along with a push notification to your application. Extras can be defined via the dashboard or API and will be available as key value pairs within the notification dictionary passed to your push delegate implementations.

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKPushUtils.h
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#push-action-buttons-integration
[4]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3
[8]: {% image_buster /assets/img_archive/sound_push_ios.png %}
[9]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html
[12]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[17]: {{site.baseurl}}/assets/img_archive/push_example_category.png
[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1
[25]: {{site.baseurl}}/developer_guide/rest_api/messaging/#messaging
[31]: https://developer.apple.com/reference/uikit/uiusernotificationcategory
