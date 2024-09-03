---
nav_title: Integration
article_title: Push Integration for iOS
platform: Swift
page_order: 0
description: "This reference article covers how to set up iOS push notifications for the Braze Swift SDK."
channel:
  - push
  
---

# Push notifications integration

> This reference article covers how to set up iOS push notifications for the Braze Swift SDK.

[Push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) allow you to send out notifications from your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. Push notifications can also be [silent]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), being used only to update your app's interface or trigger background work. 

Push notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable. Push notifications can also be much more efficient than background fetch, as your application only launches when necessary. 

Push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the Apple Push Notification service (APNs) servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification.

## Initial setup

### Step 1: Upload your APNs certificate

Before you can send an iOS push notification using Braze, you must provide your `.p8`  push notification file provided by Apple. As described on the Apple [developer documentation](https://developer.apple.com/documentation/usernotifications):

1. In your Apple developer account, go to [**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/ios/certificate).
2. Under **Keys**, select **All** and click the add button (+) in the upper-right corner.
3. Under **Key Description**, enter a unique name for the signing key.
4. Under **Key Services**, select the **Apple Push Notification service (APNs)** checkbox, then click **Continue**. Click **Confirm**.
5. Note the key ID. Click **Download** to generate and download the key. Make sure to save the downloaded file in a secure place, as you cannot download this more than once.
6. In Braze, go to **Settings** > **App Settings** and upload the `.p8` file under **Apple Push Certificate**. You can upload either your development or production push certificate. To test push notifications after your app is live in the App Store, its recommended to set up a separate workspace for the development version of your app.
7. When prompted, enter your app's [bundle ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), [key ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/), and [team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id), then click **Save**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can upload your `.p8` file from **Manage Settings** > **Settings**.
{% endalert %}

### Step 2: Enable push capabilities

In Xcode, add the Push Notifications capability using the **Signing & Capabilities** pane to the main app target.

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## Automatic push integration

The Swift SDK provides a configuration-only approach to automate the processing of remote notifications received from Braze. This approach is the simplest way to integrate push notifications and is recommended for most customers.

To enable the automatic push integration, set the `automation` property of the `push` configuration to `true`:

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

This instructs the SDK to:
- Register your application for push notification on the system.
- Request the push notification authorization/permission at initialization.
- Dynamically provide implementations for the push notification related system delegate methods.

{% alert note %}
The automation steps performed by the SDK are compatible with pre-existing push notification handling integrations in your codebase. The SDK only automates the processing of remote notification received from Braze. Any system handler implemented to process your own or another third party SDK remote notifications will continue to work when `automation` is enabled.
{% endalert %}

{% alert warning %}
The SDK must be initialized on the main thread to enable push notification automation. SDK initialization must happen before the application has finished launching or in your AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) implementation.
If your application requires additional setup before initializing the SDK, please refer to the [Delayed Initialization]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) documentation page.
{% endalert %}

### Overriding individual configurations

For more granular control, each automation step can be enabled or disabled individually:

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

See [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) for all available options and [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) for more information on the automation behavior.

You can skip the next section and continue to [deep linking](#deep-linking) if you are using the automatic push integration.

## Manual push integration

Push notifications can also be integrated manually. This section describes the steps necessary for this integration. 

{% alert note %}
If you rely on push notifications for additional behavior specific to your app, you may still be able to use automatic push integration instead of manual push notification integration. The [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) method provides a way to be notified of remote notifications processed by Braze.
{% endalert %}

### Step 1: Register for push notifications with APNs

Include the appropriate code sample within your app's [`application:didFinishLaunchingWithOptions:` delegate method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) so that your users' devices can register with APNs. Ensure that you call all push integration code in your application's main thread.

Braze also provides default push categories for push action button support, which must be manually added to your push registration code. Refer to [push action buttons]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/) for additional integration steps.

Add the following code to the `application:didFinishLaunchingWithOptions:` method of your app delegate. 

{% alert note %}
The following code sample includes integration for provisional push authentication (lines 5 and 6). If you are not planning on using provisional authorization in your app, you can remove the lines of code that add `UNAuthorizationOptionProvisional` to the `requestAuthorization` options.<br>Visit [iOS notification options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) to learn more about push provisional authentication.
{% endalert %}

{% tabs %}
{% tab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
You must assign your delegate object using `center.delegate = self` synchronously before your app finishes launching, preferably in `application:didFinishLaunchingWithOptions:`. Not doing so may cause your app to miss incoming push notifications. Visit Apple's [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) documentation to learn more.
{% endalert %}

### Step 2: Register push tokens with Braze

Once APNs registration is complete, pass the resulting `deviceToken` to Braze to enable for push notifications for the user.  

{% tabs %}
{% tab Swift %}

Add the following code to your app's `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab OBJECTIVE-C %}

Add the following code to your app's `application:didRegisterForRemoteNotificationsWithDeviceToken:` method:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
The `application:didRegisterForRemoteNotificationsWithDeviceToken:` delegate method is called every time after `application.registerForRemoteNotifications()` is called. <br><br>If you are migrating to Braze from another push service and your user's device has already registered with APNs, this method will collect tokens from existing registrations the next time the method is called, and users will not have to re-opt-in to push.
{% endalert %}

### Step 3: Enable push handling

Next, pass the received push notifications along to Braze. This step is necessary for logging push analytics and link handling. Ensure that you call all push integration code in your application's main thread.

#### Default push handling

{% tabs %}
{% tab Swift %}
To enable Braze's default push handling, add the following code to your app's `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Next, add the following to your app's `userNotificationCenter(_:didReceive:withCompletionHandler:)` method:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endtab %}

{% tab OBJECTIVE-C %}
To enable Braze's default push handling, add the following code to your application's `application:didReceiveRemoteNotification:fetchCompletionHandler:` method:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

Next, add the following code to your app's `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` method:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endtab %}
{% endtabs %}

#### Foreground push handling

{% tabs %}
{% tab Swift %}
To enable foreground push notifications and let Braze recognize them when they're received, implement `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. If a user taps your foreground notification, the `userNotificationCenter(_:didReceive:withCompletionHandler:)` push delegate will be called and Braze will log the push click event.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endtab %}

{% tab OBJECTIVE-C %}
To enable foreground push notifications and let Braze recognize them when they're received, implement `userNotificationCenter:willPresentNotification:withCompletionHandler:`. If a user taps your foreground notification, the `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` push delegate will be called and Braze will log the push click event.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endtab %}
{% endtabs %}

## Deep linking

Deep linking from a push into the app is automatically handled via our standard push integration documentation. If you'd like to learn more about how to add deep links to specific locations in your app, see our [advanced use cases]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation).

## Subscribing to push notifications updates

{% tabs %}
{% tab Swift %}
To access the push notification payloads processed by Braze, use the [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/) method.

You can use the `payloadTypes` parameter to specify whether you'd like to subscribe to notifications involving push open events, push received events, or both.

{% alert important %}
Keep in mind, push received events will only trigger for foreground notifications and `content-available` background notifications. It will not trigger for notifications received while terminated or for background notifications without the `content-available` field.
{% endalert %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```
{% endtab %}

{% tab OBJECTIVE-C %}
To access the push notification payloads processed by Braze, use the [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/) method.

You can use the `payloadTypes` parameter to specify whether you'd like to subscribe to notifications involving push open events, push received events, or both.

{% alert important %}
Keep in mind, push received events will only trigger for foreground notifications and `content-available` background notifications. It will not trigger for notifications received while terminated or for background notifications without the `content-available` field.
{% endalert %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```
{% endtab %}

{% endtabs %}
{% alert note %}
When using the automatic push integration, `subscribeToUpdates(_:)` is the only way to be notified of remote notifications processed by Braze. The `UIAppDelegate` and `UNUserNotificationCenterDelegate` system methods are not called when the notification is automatically processed by Braze.
{% endalert %}

## Testing {#push-testing}

If you'd like to test in-app and push notifications via the command line, you can send a single notification through the terminal via CURL and the [messaging API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available at **Settings** > **API Keys**.
- `YOUR_EXTERNAL_USER_ID` - available on the **Search Users** page. See [assigning user IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id) for more information.
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), these pages are in a different location: <br>- **API Keys** is located at **Developer Console** > **API Settings** <br>- **Search Users** is located at **Users** > **User Search**
{% endalert %}

In the following example, the `US-01` instance is being used. If you're not on this instance, refer to our [API documentation]({{site.baseurl}}/api/basics/) to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Push primers {#push-primers}

Push primer campaigns encourage your users to enable push notifications on their device for your app. This can be done without SDK customization using our [no code push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

