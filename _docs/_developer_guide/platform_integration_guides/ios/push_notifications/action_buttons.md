---
nav_title: Action Buttons
platform: iOS
page_order: 0.2
search_rank: 5
---

# Action Buttons {#push-action-buttons-integration}

iOS 8+ introduces the ability for users to interact with your application via notification [categories][14]. Categories define a type of notification your application can send. Each category contain actions that a user can perform in response, which manifest as buttons on the push notification.

![Illustration of Notification Action][13]

iOS SDK version 2.27.0 introduced default Braze push categories, including URL handling support for each push action button. Currently, the default categories have four sets of push action buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` and `More`. To register Braze's default push categories, follow the integration instructions below:

## Step 1: Adding Braze Default Push Categories

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

## Step 2: Enable Interactive Push Handling

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
[36]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#push-action-buttons-customization
[38]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift
