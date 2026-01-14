## Rate limits

Push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the Apple Push Notification service (APNs) servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification.

## Setting up push notifications

### Step 1: Upload your APNs token

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Step 2: Enable push capabilities

In Xcode, go to the **Signing & Capabilities** section of the main app target and add the push notifications capability.

![The 'Signing & Capabilities' section in an Xcode project.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Step 3: Set up push handling

You can use the Swift SDK to automate the processing of remote notifications received from Braze. This is the simplest way to handle push notifications and is the recommended handling method.

{% tabs local %}
{% tab Automatic %}
#### Step 3.1: Enable automation in the push property

To enable the automatic push integration, set the `automation` property of the `push` configuration to `true`:

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

This instructs the SDK to:
- Register your application for push notification on the system.
- Request the push notification authorization/permission at initialization.
- Dynamically provide implementations for the push notification related system delegate methods.

{% alert note %}
The automation steps performed by the SDK are compatible with pre-existing push notification handling integrations in your codebase. The SDK only automates the processing of remote notification received from Braze. Any system handler implemented to process your own or another third party SDK remote notifications will continue to work when `automation` is enabled.
{% endalert %}

{% alert warning %}
The SDK must be initialized on the main thread to enable push notification automation. SDK initialization must happen before the application has finished launching or in your AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) implementation.
If your application requires additional setup before initializing the SDK, please refer to the [Delayed Initialization]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) documentation page.
{% endalert %}

#### Step 3.2: Override individual configurations (optional)

For more granular control, each automation step can be enabled or disabled individually:

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

See [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) for all available options and [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) for more information on the automation behavior.
{% endtab %}

{% tab Manual %}
{% alert note %}
If you rely on push notifications for additional behavior specific to your app, you may still be able to use automatic push integration instead of manual push notification integration. The [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) method provides a way to be notified of remote notifications processed by Braze.
{% endalert %}

#### Step 3.1: Register for push notifications with APNs

Include the appropriate code sample within your app's [`application:didFinishLaunchingWithOptions:` delegate method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) so that your users' devices can register with APNs. Ensure that you call all push integration code in your application's main thread.

Braze also provides default push categories for push action button support, which must be manually added to your push registration code. Refer to [push action buttons]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) for additional integration steps.

Add the following code to the `application:didFinishLaunchingWithOptions:` method of your app delegate. 

{% alert note %}
The following code sample includes integration for provisional push authentication (lines 5 and 6). If you are not planning on using provisional authorization in your app, you can remove the lines of code that add `UNAuthorizationOptionProvisional` to the `requestAuthorization` options.<br>Visit [iOS notification options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) to learn more about push provisional authentication.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

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

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
You must assign your delegate object using `center.delegate = self` synchronously before your app finishes launching, preferably in `application:didFinishLaunchingWithOptions:`. Not doing so may cause your app to miss incoming push notifications. Visit Apple's [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) documentation to learn more.
{% endalert %}

#### Step 3.2: Register push tokens with Braze

Once APNs registration is complete, pass the resulting `deviceToken` to Braze to enable for push notifications for the user.  

{% subtabs %}
{% subtab Swift %}

Add the following code to your app's `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Add the following code to your app's `application:didRegisterForRemoteNotificationsWithDeviceToken:` method:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
The `application:didRegisterForRemoteNotificationsWithDeviceToken:` delegate method is called every time after `application.registerForRemoteNotifications()` is called. <br><br>If you are migrating to Braze from another push service and your user's device has already registered with APNs, this method will collect tokens from existing registrations the next time the method is called, and users will not have to re-opt-in to push.
{% endalert %}

#### Step 3.3: Enable push handling

Next, pass the received push notifications along to Braze. This step is necessary for logging push analytics and link handling. Ensure that you call all push integration code in your application's main thread.

##### Default push handling

{% subtabs %}
{% subtab Swift %}
To enable the Braze default push handling, add the following code to your app's `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method:

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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
To enable the Braze default push handling, add the following code to your application's `application:didReceiveRemoteNotification:fetchCompletionHandler:` method:

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
{% endsubtab %}
{% endsubtabs %}

##### Foreground push handling

{% subtabs %}
{% subtab Swift %}
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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Testing notifications {#push-testing}

If you'd like to test in-app and push notifications via the command line, you can send a single notification through the terminal via CURL and the [messaging API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available at **Settings** > **API Keys**.
- `YOUR_EXTERNAL_USER_ID` - available on the **Search Users** page. See [assigning user IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id) for more information.
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

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

## Subscribing to push notifications updates

To access the push notification payloads processed by Braze, use the [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/) method.

You can use the `payloadTypes` parameter to specify whether you'd like to subscribe to notifications involving push open events, push received events, or both.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Keep in mind, push received events will only trigger for foreground notifications and `content-available` background notifications. It will not trigger for notifications received while terminated or for background notifications without the `content-available` field.
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Keep in mind, push received events will only trigger for foreground notifications and `content-available` background notifications. It will not trigger for notifications received while terminated or for background notifications without the `content-available` field.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
When using the automatic push integration, `subscribeToUpdates(_:)` is the only way to be notified of remote notifications processed by Braze. The `UIAppDelegate` and `UNUserNotificationCenterDelegate` system methods are not called when the notification is automatically processed by Braze.
{% endalert %}

{% alert tip %}
Create your push notification subscription in `application(_:didFinishLaunchingWithOptions:)` to ensure your subscription is triggered after an end-user taps a notification while your app is in a terminated state.
{% endalert %}

## Push primers {#push-primers}

Push primer campaigns encourage your users to enable push notifications on their device for your app. This can be done without SDK customization using our [no code push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Dynamic APNs gateway management

Dynamic Apple Push Notification Service (APNs) gateway management enhances the reliability and efficiency of iOS push notifications by automatically detecting the correct APNs environment. Previously, you would manually select APNs environments (development or production) for your push notifications, which sometimes led to incorrect gateway configurations, delivery failures, and `BadDeviceToken` errors.

With dynamic APNs gateway management, you'll have:

- **Improved reliability:** Notifications are always delivered to the correct APNs environment, reducing failed deliveries.
- **Simplified configuration:** You no longer need to manually manage APNs gateway settings.
- **Error resilience:** Invalid or missing gateway values are gracefully handled, providing uninterrupted service.

### Prerequisites

Braze supports Dynamic APNs gateway management for push notifications on iOS with the following SDK version requirement:

{% sdk_min_versions swift:10.0.0 %}

### How it works

When an iOS app integrates with the Braze Swift SDK, it sends device-related data, including [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) to the Braze SDK API, if available. The `apns_gateway` value indicates whether the app is using the development (`dev`) or production (`prod`) APNs environment.

Braze also stores the reported gateway value for each device. If a new, valid gateway value is received, Braze updates the stored value automatically.

When Braze sends a push notification:

- If a valid gateway value (dev or prod) is stored for the device, Braze uses it to determine the correct APNs environment.
- If no gateway value is stored, Braze defaults to the APNs environment configured in the **App Settings** page.

### Frequently asked questions

#### Why was this feature introduced?

With dynamic APNs gateway management, the correct environment is selected automatically. Previously, you had to manually configure the APNs gateway, which could lead to `BadDeviceToken` errors, token invalidation, and potential APNs rate-limiting issues.

#### How does this impact push delivery performance?

This feature improves delivery rates by always routing push tokens to the correct APNs environment, avoiding failures caused by misconfigured gateways.

#### Can I disable this feature?

Dynamic APNs Gateway Management is turned on by default and provides reliability improvements. If you have specific use cases that require manual gateway selection, contact [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/).
