---
nav_title: Integration
article_title: Push Integration for iOS
platform: iOS
page_order: 0
description: "This reference article covers how to integrate push notifications in your iOS application."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
  
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Push integration

## Step 1: Upload your APNs token

{% multi_lang_include developer_guide/swift/apns_token.md %}

## Step 2: Enable push capabilities

In your project settings, ensure that under the **Capabilities** tab, your **Push Notifications** capability is toggled on.

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

If you have separate development and production push certificates, make sure to uncheck the **Automatically manage signing** box in the **General** tab. This will allow you to choose different provisioning profiles for each build configuration, as Xcode's automatic code signing feature only does development signing.

![Xcode project settings showing the "general" tab. In this tab, the option "Automatically manage signing" is unchecked.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Step 3: Register for push notifications

The appropriate code sample must be included within your app's `application:didFinishLaunchingWithOptions:` delegate method for your users' device to register with APNs. Ensure that you call all push integration code in your application's main thread.

Braze also provides default push categories for push action button support, which must be manually added to your push registration code. Refer to [push action buttons]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons/) for additional integration steps.

{% alert warning %}
If you've implemented a custom push prompt as described in our [push best practices]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting/), make sure that you're calling the following code **every time the app runs** after they grant push permissions to your app. **Apps need to re-register with APNs as [device tokens can change arbitrarily](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Using UserNotification framework (iOS 10+)

If you are using the `UserNotifications` framework (recommended) introduced in iOS 10, add the following code to the `application:didFinishLaunchingWithOptions:` method of your app delegate.

{% alert important %}
The following code sample includes integration for provisional push authentication (lines 5 and 6). If you are not planning on using provisional authorization in your app, you can remove the lines of code that add `UNAuthorizationOptionProvisional` to the `requestAuthorization` options.<br>Visit [iOS notification options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) to learn more about push provisional authentication.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
You must assign your delegate object using `center.delegate = self` synchronously before your app finishes launching, preferably in `application:didFinishLaunchingWithOptions:`. Not doing so may cause your app to miss incoming push notifications. Visit Apple's [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) documentation to learn more.
{% endalert %}

### Without UserNotifications framework

If you are not using the `UserNotifications` framework, add the following code to the `application:didFinishLaunchingWithOptions:` method of your app delegate:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}


## Step 4: Register push tokens with Braze

Once APNs registration is complete, the following method must be altered to pass the resulting `deviceToken` to Braze so the user becomes enabled for push notifications:

{% tabs %}
{% tab OBJECTIVE-C %}

Add the following code to your `application:didRegisterForRemoteNotificationsWithDeviceToken:` method:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Add the following code to your app's `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
The `application:didRegisterForRemoteNotificationsWithDeviceToken:` delegate method is called every time after `[[UIApplication sharedApplication] registerForRemoteNotifications]` is called. If you are migrating to Braze from another push service and your user's device has already registered with APNs, this method will collect tokens from existing registrations the next time the method is called, and users will not have to re-opt-in to push.
{% endalert %}

## Step 5: Enable push handling

The following code passes received push notifications along to Braze and is necessary for logging push analytics and link handling. Ensure you call all push integration code in your application's main thread.

### iOS 10+

When building against iOS 10+, we recommend you integrate the `UserNotifications` framework and do the following:

{% tabs %}
{% tab OBJECTIVE-C %}

Add the following code to your application's `application:didReceiveRemoteNotification:fetchCompletionHandler:` method:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Next, add the following code to your app's `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` method:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Foreground Push Handling**

To display a push notification while the app is in the foreground, implement `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

If the foreground notification is clicked, the iOS 10 push delegate `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` will be called, and Braze will log a push click event.

{% endtab %}
{% tab swift %}

Add the following code to your app's `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Next, add the following code to your app's `userNotificationCenter(_:didReceive:withCompletionHandler:)` method:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Foreground Push Handling**

To display a push notification while the app is in the foreground, implement `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

If the foreground notification is clicked, the iOS 10 push delegate `userNotificationCenter(_:didReceive:withCompletionHandler:)` will be called, and Braze will log a push click event.

{% endtab %}
{% endtabs %}

### Pre-iOS 10

iOS 10 updated behavior such that it no longer calls `application:didReceiveRemoteNotification:fetchCompletionHandler:` when a push is clicked. For this reason, if you don't update to building against iOS 10+ and use the `UserNotifications` framework, you have to call Braze from both old-style delegates, which is a break from our previous integration.

For apps building against SDKs < iOS 10, use the following instructions:

{% tabs %}
{% tab OBJECTIVE-C %}

To enable open tracking on push notifications, add the following code to your app's `application:didReceiveRemoteNotification:fetchCompletionHandler:` method:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

To support push analytics on iOS 10, you must also add the following code to your app's `application:didReceiveRemoteNotification:` delegate method:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

To enable open tracking on push notifications, add the following code to your app's `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

To support push analytics on iOS 10, you must also add the following code to your app's `application(_:didReceiveRemoteNotification:)` delegate method:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Step 6: Deep linking

Deep linking from a push into the app is automatically handled via our standard push integration documentation. If you'd like to learn more about how to add deep links to specific locations in your app, see our [advanced use cases]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation).

## Step 7: Unit tests (optional)

To add test coverage for the integration steps you've just followed, implement [push unit testing]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/).

