---
nav_title: Push Notifications
article_title: Push Notifications for React Native
platform: React Native
page_order: 2
description: "This article covers implementing push notifications on React Native."
channel: push

---

# Push notifications

> This reference article covers how to set push notifications for React Native. Integrating push notifications requires setting up each native platform separately. Follow the respective guides listed to finish the installation.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Setting up push notifications

### Step 1: Complete the initial setup

{% tabs local %}
{% tab Expo %}
#### Prerequisites

Before you can use Expo for push notifications, you'll need to [set up the Braze Expo plugin]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Step 1.1: Update your `app.json` file

Next update your `app.json` file for Android and iOS:

- **Android:** Add the `enableFirebaseCloudMessaging` option.
- **iOS:** Add the `enableBrazeIosPush` option.

#### Step 1.2: Add your Google Sender ID

First, go to Firebase Console, open your project, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Select **Cloud Messaging**, then under **Firebase Cloud Messaging API (V1)**, copy the **Sender ID** to your clipboard.

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Next, open your project's `app.json` file and set your `firebaseCloudMessagingSenderId` property to the Sender ID in your clipboard. For example:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Step 1.3: Add the path to your Google Services JSON

In your project's `app.json` file, add the path to your `google-services.json` file. This file is required when setting `enableFirebaseCloudMessaging: true` in your configuration.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```

Note that you will need to use these settings instead of the native setup instructions if you are depending on additional push notification libraries like [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
{% endtab %}

{% tab Android Native %}
If you are not using the Braze Expo plugin, or would like to configure these settings natively instead, register for push by referring to the [Native Android push integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab iOS Native %}
If you are not using the Braze Expo plugin, or would like to configure these settings natively instead, register for push by referring to the following steps from the [Native iOS push integration guide]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/):

#### Step 1.1: Request for push permissions

If you don't plan on requesting push permissions when the app is launched, omit the `requestAuthorizationWithOptions:completionHandler:` call in your AppDelegate. Then, skip to [Step 2](#step-2-request-push-notifications-permission). Otherwise, follow the [native iOS integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Step 1.2 (Optional): Migrate your push key

If you were previously using `expo-notifications` to manage your push key, run `expo fetch:ios:certs` from your application's root folder. This will download your push key (a .p8 file), which can then be uploaded to the Braze dashboard.
{% endtab %}
{% endtabs %}

### Step 2: Request push notifications permission

Use the `Braze.requestPushPermission()` method (available on v1.38.0 and up) to request permission for push notifications from the user on iOS and Android 13+. For Android 12 and below, this method is a no-op.

This method takes in a required parameter that specifies which permissions the SDK should request from the user on iOS. These options have no effect on Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Step 2.1: Listen for push notifications (optional)

You can additionally subscribe to events where Braze has detected and handled an incoming push notification. Use the listener key `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
iOS push received events will only trigger for foreground notifications and `content-available` background notifications. It will not trigger for notifications received while terminated or for background notifications without the `content-available` field.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### Push notification event fields

For a full list of push notification fields, refer to the table below:

| Field Name         | Type      | Description |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Specifies the notification payload type. The two values that are sent from the Braze React Native SDK are `push_opened` and `push_received`. |
| `url`              | String    | Specifies the URL that was opened by the notification. |
| `use_webview`      | Boolean   | If `true`, URL will open in-app in a modal webview. If `false`, the URL will open in the device browser. |
| `title`            | String    | Represents the title of the notification. |
| `body`             | String    | Represents the body or content text of the notification. |
| `summary_text`     | String    | Represents the summary text of the notification. This is mapped from `subtitle` on iOS. |
| `badge_count`      | Number   | Represents the badge count of the notification. |
| `timestamp`        | Number | Represents the time at which the payload was received by the application. |
| `is_silent`        | Boolean   | If `true`, the payload is received silently. For details on sending Android silent push notifications, refer to [Silent push notifications on Android]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/silent/). For details on sending iOS silent push notifications, refer to [Silent push notifications on iOS]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/silent/). |
| `is_braze_internal`| Boolean   | This will be `true` if a notification payload was sent for an internal SDK feature, such as geofences sync, Feature Flag sync, or uninstall tracking. The payload is received silently for the user. |
| `image_url`        | String    | Specifies the URL associated with the notification image. |
| `braze_properties` | Object    | Represents Braze properties associated with the campaign (key-value pairs). |
| `ios`              | Object    | Represents iOS-specific fields. |
| `android`          | Object    | Represents Android-specific fields. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 3: Enable deep linking (optional)

To enable Braze to handle deep links inside React components when a push notification is clicked, first implement the steps described in [React Native Linking](https://reactnative.dev/docs/linking) library, or with your solution of choice. Then, follow the additional steps below.

To learn more about what deep links are, see our [FAQ article]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android Native %}
For Android, setting up deep links is identical to [setting up deep links on native Android apps]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links).

If you are using the Expo plugin and want Braze to handle push deep links automatically, set `androidHandlePushDeepLinksAutomatically: true` in your `app.json`.

{% endtab %}
{% tab iOS Native %}
#### Step 3.1: Store the push notification payload on app launch
{% alert note %}
Skip this step if you're using the Braze Expo plugin, as this is functionality is handled automatically.
{% endalert %}

In your `iOS` directory, create `BrazeReactDelegate.h`, then add the following code snippet to your file. Replace `YOUR_DOMAIN_HOST` with your actual domain, such as `braze.com`.

```objc
// BrazeReactDelegate.h
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Next, create `BrazeReactDelegate.m`, then add the following code snippet to your file. Replace `YOUR_DOMAIN_HOST` with your actual domain, such as `braze.com`.

```objc
// BrazeReactDelegate.m
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

In your project's `AppDelegate`, add `populateInitialPayloadFromLaunchOptions` to your `didFinishLaunchingWithOptions` method, then register your `BrazeReactDelegate`.

When you're finished, your `AppDelegate` should be similar to the following:

```objc
[...]
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

[...]

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

[...]

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

#### Step 3.2: Handle deep links from a closed state

In addition to the base scenarios handled by [React Native Linking](https://reactnative.dev/docs/linking), implement the `Braze.getInitialPushPayload` method and retrieve the `url` value to account for deep links from push notifications that open your app when it isn't running. For example:

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Braze provides this workaround since React Native's Linking API does not support this scenario due to a race condition on app startup.
{% endalert %}
{% endtab %}
{% endtabs %}

### Step 4: Send a test push notification

At this point, you should be able to send notifications to the devices. Adhere to the following steps to test your push integration.

{% alert note %}
Starting in macOS 13, on certain devices, you can test iOS push notifications on an iOS 16+ simulator running on Xcode 14 or higher. For further details, refer to the [Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Set an active user in the React Native application by calling `Braze.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and create a new push notification campaign. Choose the platforms that you'd like to test.
3. Compose your test notification and head over to the **Test** tab. Add the same `user-id` as the test user and click **Send Test**. You should receive the notification on your device shortly.

![A Braze push campaign showing you can add your own user ID as a test recipient to test your push notification.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Using the Expo plugin

After you [set up push notifications for Expo](#setting-up-push-notifications), you can use it to handle the following push notifications behaviors&#8212;without needing to write any code in the native Android or iOS layers.

### Forwarding Android push to additional FMS

If you want to use an additional Firebase Messaging Service (FMS), you can specify a fallback FMS to call if your application receives a push that isn't from Braze. For example:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

### Using app extensions with Expo Application Services {#app-extensions}

If you are using Expo Application Services (EAS) and have enabled `enableBrazeIosRichPush` or `enableBrazeIosPushStories`, you will need to declare the corresponding bundle identifiers for each app extension in your project. There are multiple ways you can approach this step, depending on how your project is configured to manage code signing with EAS.

One approach is to use the `appExtensions` configuration in your `app.json` file by following Expo's [app extensions documentation](https://docs.expo.dev/build-reference/app-extensions/). Alternatively, you can set up the `multitarget` setting in your `credentials.json` file by following Expo's [local credentials documentation](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project).

### Enabling rich push notifications for iOS

{% alert tip %}
Rich push notifications are available for Android by default.
{% endalert %}

To enable rich push notifications on iOS using Expo, configure the `enableBrazeIosRichPush` property to `true` in your `expo.plugins` object in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Lastly, add the bundle identifier for this app extension to your project's credentials configuration: `<your-app-bundle-id>.BrazeExpoRichPush`. For further details on this process, refer to [Using app extensions with Expo Application Services](#app-extensions).

### Enabling Push Stories for iOS

{% alert tip %}
Push stories are available for Android by default.
{% endalert %}

To enable Push Stories on iOS using Expo, ensure you have an app group defined for your application. For more information, see [Adding an App Group]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Next, configure the `enableBrazeIosPushStories` property to `true` and assign your app group ID to `iosPushStoryAppGroup` in your `expo.plugins` object in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Lastly, add the bundle identifier for this app extension to your project's credentials configuration: `<your-app-bundle-id>.BrazeExpoPushStories`. For further details on this process, refer to [Using app extensions with Expo Application Services](#app-extensions).

{% alert warning %}
If you are using Push Stories with Expo Application Services, be sure to use the `EXPO_NO_CAPABILITY_SYNC=1` flag when running `eas build`. There is a known issue in the command line which removes the App Groups capability from your extension's provisioning profile.
{% endalert %}
