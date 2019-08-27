---
nav_title: Integration
platform: iOS
page_order: 0
search_rank: 5
---

{% alert tip %}
We strongly recommend that you implement the SDK via a [CocoaPod](http://cocoapods.org/). It will save you a lot of time and automate much of the process for you. However, if you are unable to do so you may complete integration manually without CocoaPods by using our manual integration instructions [here]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/manual_integration_options/#manual-integration-options).
{% endalert %}

## Integration {#push-integration}

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

Sample push notification:

![Sample Push iOS][17]

For more information and best practices on push, visit our [Braze Academy][0] page.

## Basic Push Integration

### Step 1: Configure Push Notifications

#### Recommended Option: Using a .p8 File (Authentication Tokens)

As described on [this page](https://help.apple.com/developer-account/#/devcdfbb56a3),

1. In your developer account, go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/ios/certificate).
2. Under Keys, select All and click the Add button (+) in the upper-right corner.
3. Under Key Description, enter a unique name for the signing key.
4. Under Key Services, select the APNs checkbox, then click Continue. Click Confirm.
5. Note the Key ID. Click Download to generate and download the key now.

>  When you download the key, it is saved as a text file with a .p8 file extension. Save the file in a secure place because the key is **not saved in your developer account and you won’t be able to download it again**.

6. Navigate to the [app settings page][5] in the dashboard and upload the .p8 file.
7. When prompted, also enter your [app's Bundle Id](https://developer.apple.com/account/ios/identifier/bundle/), the [Key Id](https://developer.apple.com/account/ios/authkey), and your [Team Id](https://developer.apple.com/account/#/membership). Click Save.

#### Alternate Option: Using a .p12 Certificate (Legacy)

Alternately, you may utilize Apple's older authentication scheme (.p12 SSL certificates). Unlike the .p8 solution described above, these certificates automatically expire every year and will require you to regenerate and re-upload them. Braze will send you email reminders as the certificate approaches expiration to help your notifications continue uninterrupted, but because this is a manual process we recommend utilizing the above-described .p8 authentication scheme instead.  However, if you still wish to, you may configure and upload .p12 certificates as described here:

##### Generate Certificate Signing Request

1. Navigate to the [iOS Provisioning Portal][1]
2. Select Identifiers > App IDs in the left sidebar

 ![iOSPush3][2]

3. Select your application.
4. If push notifications are not enabled, click Edit to update the app settings
  ![AppleProvisioningOptions][3]
5. Tick the Enable check box and click Create Certificate under the Production SSL Certificate
  ![iOSPush3][4]
6. Follow the instructions from the SSL certificate assistant. You should now see a green status to indicate that push is enabled.
>  You must update your provisioning profile for the app after you create your SSL certificates. A simple "Refresh" in the organizer will accomplish this.

##### Export Certificate

1. Download the production push certificate that you just created and open it with the Keychain Access application
2. In Keychain Access, click on My Certificates and locate your push certificate
3. Export it as a `.p12` file and use a temporary, unsecure password (you will need this password when uploading your certificate to Braze)
4. Navigate to the [app settings page][5] in the dashboard and upload your production certificate.

 ![push upload example][6]

>  You can upload either your development or production push certificates to the dashboard for your distribution provisioning profile apps, but you can only have one active at a time. As such, if you wish to do repeated testing of push notifications once your app goes live in the App Store, we recommend setting up a separate App Group or App for the development version of your app.

### Step 2: Enable Push Capabilities

In your project settings, ensure that under the `Capabilities` tab your `Push Notifications` capability is toggled on, as described on [this page](https://help.apple.com/developer-account/#/devcdfbb56a3).

![enable push notification][24]

>  If you are using Xcode 8 and have separate development and production push certificates, please make sure to uncheck the `Automatically manage signing` box in the `General` tab. This will allow you to choose different provisioning profiles for each of your build configurations, as Xcode's automatic code signing feature only does development signing.
![xcode 8 auto signing][34]

### Step 3: Register for Push Notifications

The appropriate code sample below must be included within your app's `application:didFinishLaunchingWithOptions:` delegate method for your users' device to register with APNs.

Braze also provides default push categories for push action button support, which must be manually added to your push registration code. See our [push action buttons documentation][35] for additional integration steps.

> If you've implemented a custom push prompt as described in our [push best practices][0], make sure that you're calling the following code **EVERY time the app runs** after they grant push permissions to your app. **Apps need to re-register with APNs as [device tokens can change arbitrarily][19].**

{% alert warning %}
Be sure to call all push integration code in your application's main thread.
{% endalert %}

##### Using UserNotification Framework (iOS 10+)

If you are using the UserNotifications framework (recommended) that was introduced in iOS 10,  use the following code:

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
    print("Permission granted.")
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

> If you are not planning on using provisional authorization in your app, you can remove the lines of code that add `UNAuthorizationOptionProvisional` to the `requestAuthorization` options in the above code snippet.

###### iOS 8+ without UserNotifications Framework

When building against iOS 8+ and not using the `UserNotifications` framework, use the following:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_7_1) {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
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


### Step 4: Register Push Tokens With Braze

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

>  The `application:didRegisterForRemoteNotificationsWithDeviceToken:` delegate method is called every time after `[[UIApplication sharedApplication] registerForRemoteNotifications]` is called. If you are migrating to Braze from another push service and your user's device has already registered with APNs, this method will collect tokens from existing registrations the next time the method is called, and users will not have to re-opt-in to push.

### Step 5: Enable Push Handling

The following code passes received push notifications along to Braze and is necessary for logging push analytics and link handling.

{% alert warning %}
Be sure to call all push integration code in your application's main thread.
{% endalert %}

###### iOS 10+

When building against iOS 10+ we recommend you integrate the `UserNotifications` framework and do the following:

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

In iOS 10, you can display a push notification while the app is in the foreground by implementing the following delegate method and returning `UNNotificationPresentationOptionAlert` to the `completionHandler`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler
```

In this case, if the user clicks the displayed foreground push, the new iOS 10 push delegate method `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` will be called and Braze will log a click for that push.

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

In iOS 10, you can display a push notification while the app is in the foreground by implementing the following delegate method and returning `UNNotificationPresentationOptionAlert` to the `completionHandler` in the appropriate view controller class:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                willPresent notification: UNNotification,
      withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
    completionHandler([.alert, .badge, .sound])
}

```

In this case, if the user clicks the displayed foreground push, the new iOS 10 push delegate method `userNotificationCenter(_:didReceive:withCompletionHandler:)` will be called and Braze will log a click for that push.

{% endtab %}
{% endtabs %}

##### Pre-iOS 10

iOS 10 updated behavior such that it no longer calls `application:didReceiveRemoteNotification:fetchCompletionHandler:` when a push is clicked.  For this reason, if you don't update to building against iOS 10+ and use the `UserNotifications` framework, you have to call Braze from both old-style delegates, which is a break from our previous integration.

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

### Step 6: Verify Code Modifications

Verify the code modifications you made against this [sample AppDelegate.m file][7]. We also strongly advise looking through the below section on customization to determine if any additional changes need to be implemented.

### Step 7: Deep Linking

Deep linking from a push into the app is automatically handled via our standard push integration documentation. If you'd like to learn more about how to add deep links to specific locations in your app, see our [Advanced Use Cases section on Deep Linking for iOS][10].

## iOS 10 Rich Notifications

iOS 10 introduces the ability to send push notifications with images, gifs, and video. To enable this functionality, clients must create a `Service Extension`, a new type of extension that enables modification of a push payload before it is displayed.

### Creating A Service Extension
To create a [Notification Service Extension][23], navigate to `File > New > Target` and select `Notification Service Extension`.

![Adding a Service Extension][26]

Ensure that `Embed In Application` is set to embed the extension in your application.

### Setting Up The Service Extension
A `Notification Service Extension` is its own binary that is bundled with your app. As such, it must be set up in the [Apple Developer Portal][27] with its own App ID and Provisioning Profile. Typically extensions are named with a suffix on the main application's ID (e.g., `com.appboy.stopwatch.stopwatchnotificationservice`).

#### Configuring The Service Extension To Work With Braze
Braze sends down an attachment payload in the APNS payload under the `ab` key that we use to configure, download and display rich content:

For example:

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

The relevant payload values are:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

To manually display push with a Braze payload, download the content from the value under `AppboyAPNSDictionaryAttachmentURLKey`, save it as a file with the file type stored under the `AppboyAPNSDictionaryAttachmentTypeKey` key, and add it to the notification attachments.
We provide sample code that you can copy into your `Notification Service Extension`. Simply changing the class name to the one you picked will automatically provide this functionality.

You can write the Service Extension in either Objective-C or Swift. If you don't wish to modify our default behavior, we'd recommend using our provided sample code, which is written in Objective-C. If you want to use Swift in your Service Extension, you should create a separate file with methods for our sample code, then create a bridging header file to call those methods.

For our sample code, see the [Stopwatch sample application][30]. For Swift sample code, see the [Hello Swift sample application][38].

### Creating A Rich Notification In Your Dashboard

To create a rich notification in your Braze dashboard, simple create an iOS push and attach an image or gif, or provide a url that hosts an image, gif, or video.  Note that assets are downloaded on the receipt of push notifications, so that if you are hosting your own content you should plan for large, synchronous spikes in requests.

Also note the supported file types and sizes, listed [here][28].

## Action Buttons {#push-action-buttons-integration}

iOS 8+ introduces the ability for users to interact with your application via notification [categories][14]. Categories define a type of notification your application can send. Each category contain actions that a user can perform in response, which manifest as buttons on the push notification.

![Illustration of Notification Action][13]

iOS SDK version 2.27.0 introduced default Braze push categories, including URL handling support for each push action button. Currently, the default categories have four sets of push action buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` and `More`. To register Braze's default push categories, follow the integration instructions below:

### Step 1: Adding Braze Default Push Categories

Use the following code to register for Braze's default push categories when you [register for push][36]:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

>  Clicking on push action buttons with background activation mode will only dismiss the notification and will not open the app. Button click analytics for these actions will be flushed to the server the next time the user opens the app.

>  If you wish to create your own custom notification categories, see our [action button customization][37] documentation.

See our sample code [here][33] for `UserNotification.framework` and [here][32] for `UIUserNotificationSettings`.

### Step 2: Enable Interactive Push Handling

To enable Braze's push action button handling, including click analytics and URL routing, add the following code to your app's `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` delegate method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                         forRemoteNotification: userInfo,
                             completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}



[0]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/
[1]: https://developer.apple.com/ios/manage/overview/index.action "iOS Provisioning Portal"
[2]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png"
[3]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions.png"
[4]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png"
[5]: https://dashboard-01.braze.com/app_settings/app_settings
[6]: {% image_buster /assets/img_archive/push_cert_upload.png %} "push upload example image"
[7]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L34-62 "sample AppController.mm"
[10]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation
[11]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3 "iOS Lifecycle Methods"
[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[14]: https://developer.apple.com/reference/usernotifications/unnotificationcategory "Categories Docs"
[17]: {{ site.baseurl }}/assets/img_archive/push_example_category.png
[18]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:
[19]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[29]: {% image_buster /assets/img_archive/ios10_se_db.png %}
[30]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L218-L223
[33]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L245-L249
[34]: {% image_buster /assets/img_archive/xcode8_auto_signing.png %}
[35]: #push-action-buttons-integration
[36]: #step-4-register-for-push-notifications
[37]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#push-action-buttons-customization
[38]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift
