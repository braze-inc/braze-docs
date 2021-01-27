---
nav_title: Action Buttons
platform: iOS
page_order: 0.2

---

# Action Buttons {#push-action-buttons-integration}

Users may interact with your application via notification [categories][14]. Categories define a type of notification your application can send. Each category contains actions that a user can perform in response, which manifest as buttons on the push notification.

![Illustration of Notification Action][13]

The Braze iOS SDK supports default push categories, including URL handling support for each push action button. Currently, the default categories have four sets of push action buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` and `More`. To register Braze's default push categories, follow the integration instructions below:

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

Clicking on push action buttons with background activation mode will only dismiss the notification and will not open the app. Button click analytics for these actions will be flushed to the server the next time the user opens the app.

>  If you wish to create your own custom notification categories, see our [action button customization][37] documentation.

See our sample code [here][33] for `UserNotification.framework` and [here][32] for `UIUserNotificationSettings`.

## Step 2: Enable Interactive Push Handling

If you are using the UNNotification Framework and have implemented [Braze delegates][39], you should already have this method integrated. 

To enable Braze's push action button handling, including click analytics and URL routing, add the following code to your app's `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` delegate method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

If you are not using UNNotification Framework you will need to add the following code to your app's `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` to enable Braze's push action button handling:

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
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
We strongly recommend that people using `handleActionWithIdentifier` begin using UNNotification Framework. We recommend this due to the [deprecation of handleActionWithIdentifier](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

<br>



[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[14]: https://developer.apple.com/reference/usernotifications/unnotificationcategory "Categories Docs"
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L218-L223
[33]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m#L245-L249
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#push-action-buttons-customization
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
