---
nav_title: Integration
article_title: Push Integration for iOS
platform: Swift
page_order: 0
description: "This article covers how to integrate push notifications in your iOS application."
channel:
  - push

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
  
---

# Push integration for iOS

Push notifications allow you to notify your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. Push notifications can also be [silent][1], being used only to update your app's interface or trigger background work. 

Push notifications are great for sporadic but immediately important content, where the delay between background fetches might not be acceptable. Push notifications can also be much more efficient than background fetch, as your application only launches when necessary. 

Push notifications are rate-limited, so don't be afraid of sending as many as your application needs. iOS and the Apple Push Notification service (APNs) servers will control how often they are delivered, and you won't get into trouble for sending too many. If your push notifications are throttled, they might be delayed until the next time the device sends a keep-alive packet or receives another notification.

## Step 1: Configure push notifications

Before you can send an iOS push notification using Braze, you must provide your push notification file or certificate from Apple. You may present either a `.p8` file (recommended) or a `.p12` certificate.

{% tabs local %}
  {% tab .p8 File (Recommended) %}
**Using a .p8 file (authentication token)**

1. In your developer account, go to [**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/ios/certificate).
2. Under **Keys**, select **All** and click the **Add button** (+) in the upper-right corner.
3. Under **Key Description**, enter a unique name for the signing key.
4. Under **Key Services**, select the **Apple Push Notification service (APNs) checkbox**, then click **Continue**. Click **Confirm**.
5. Note the key ID. Click **Download** to generate and download the key. Make sure to save the downloaded file in a secure place, as you cannot download this more than once.
6. Navigate to **Manage Settings > Settings** in the dashboard and upload the .p8 file under **Apple Push Certificate**.
7. When prompted, also enter your app's [bundle ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), [key ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/), and [team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id). Click **Save**.<br><br>

{% endtab %}
{% tab .p12 Certificate (Legacy) %}
**Using a .p12 certificate (legacy)**

You may choose to use Apple's older authentication scheme (.p12 SSL certificates). Unlike the .p8 solution, these certificates automatically expire every year and will require you to regenerate and re-upload them. Braze will send you email reminders as the certificate approaches expiration to help your notifications continue uninterrupted, but because this is a manual process, we recommend utilizing the .p8 authentication scheme instead. However, if you still wish to, you may configure and upload .p12 certificates as described in the following section:

**Generate Certificate Signing Request**

1. Navigate to the [iOS Provisioning Portal](https://developer.apple.com/ios/manage/overview/index.action).
2. Select **Identifiers** in the sidebar.
3. Select your application.
4. If push notifications are not enabled, click **Edit** to update the app settings.<br>![]({% image_buster /assets/img_archive/AppleProvisioningOptions.png %})
5. Tick the **Enable** check box and click **Configure** to create a **Production SSL Certificate**<br>![]({% image_buster /assets/img_archive/push_cert_gen.png %})
6. Follow the instructions from the SSL certificate assistant. You should now see an "Enabled" status to indicate that push is enabled.
7. You must update your provisioning profile for the app after you create your SSL certificates. A simple refresh in the organizer will accomplish this.

**Export Certificate**

1. Download the production push certificate you just created and open it with the Keychain Access application.
2. In Keychain Access, click on **My Certificates** and locate your push certificate.
3. Export it as a `.p12` file and use a temporary, unsecure password (you will need this password when uploading your certificate to Braze).
4. Navigate to **Manage Settings > Settings** in the dashboard and upload your production certificate under **Apple Push Certificate**.

{% endtab %}
{% endtabs %}

>  You can upload either your development or production push certificates to the dashboard for your distribution provisioning profile apps, but you can only have one active at a time. If you wish to do repeated testing of push notifications once your app goes live in the App Store, we recommend setting up a separate app group or app for the development version of your app.

## Step 2: Enable push capabilities

In Xcode, add the Push Notifications capability using the **Signing & Capabilities** pane to the main app target.

![][24]

## Step 3: Register for push notifications with APNs

The appropriate code sample must be included within your app's [`application:didFinishLaunchingWithOptions:` delegate method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) for your users' device to register with APNs. Ensure that you call all push integration code in your application's main thread.

Braze also provides default push categories for push action button support, which must be manually added to your push registration code. Refer to [push action buttons][35] for additional integration steps.

Add the following code to the `application:didFinishLaunchingWithOptions:` method of your app delegate.

{% alert important %}
The following code sample includes integration for provisional push authentication (lines 5 and 6). If you are not planning on using provisional authorization in your app, you can remove the lines of code that add `UNAuthorizationOptionProvisional` to the `requestAuthorization` options.<br>Visit [iOS notification options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) to learn more about push provisional authentication.
{% endalert %}

{% alert important %}
If you've implemented a custom push prompt, as described in our [push best practices]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/), make sure that you're calling the following code every time the app runs after push permissions are granted. Apps need to re-register with APNs as device tokens can change arbitrarily.
{% endalert %}

{% tabs %}
{% tab swift %}

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

## Step 4: Register push tokens with Braze

Once APNs registration is complete, pass the resulting `deviceToken` to Braze to enable for push notifications for the user.  

{% tabs %}
{% tab swift %}

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

## Step 5: Enable push handling

Next, pass the received push notifications along to Braze. This step is necessary for logging push analytics and link handling. Ensure that you call all push integration code in your application's main thread.

{% tabs %}
{% tab swift %}

Add the following code to your app's `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Next, add the following code to your app's `userNotificationCenter(_:didReceive:withCompletionHandler:)` method:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**Foreground Push Handling**

To display a push notification while the app is in the foreground, implement `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                            willPresent notification: UNNotification,
                            withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```

If the foreground notification is clicked, the push delegate `userNotificationCenter(_:didReceive:withCompletionHandler:)` will be called, and Braze will log a push click event.

{% endtab %}
{% tab OBJECTIVE-C %}

Add the following code to your application's `application:didReceiveRemoteNotification:fetchCompletionHandler:` method:

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

If the foreground notification is clicked, the push delegate `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` will be called, and Braze will log a push click event.

{% endtab %}
{% endtabs %}

## Step 6: Deep linking

Deep linking from a push into the app is automatically handled via our standard push integration documentation. If you'd like to learn more about how to add deep links to specific locations in your app, see our [advanced use cases][10].


## Testing {#push-testing}

If you'd like to test in-app and push notifications via the command line, you can send a single notification through the terminal via CURL and the [messaging API][29]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the **Developer Console** page.
- `YOUR_EXTERNAL_USER_ID` - available on the **User Search** page. See [assigning user IDs][32] for more information.
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

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
The preceding example is for customers on the `US-01` instance. If you are not on this instance, refer to our [API documentation][66] to see which endpoint to make requests to.

## Push Primers {#push-primers}

Push primer campaigns encourage your users to enable push notifications on their device for your app. This can be done without SDK customization using our new [no code push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

[1]:  {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[29]: {{site.baseurl}}/api/endpoints/messaging/
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[34]: {% image_buster /assets/img_archive/xcode8_auto_signing.png %}
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/