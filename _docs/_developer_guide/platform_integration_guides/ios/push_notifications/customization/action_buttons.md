---
nav_title: Action Buttons
article_title: Push Action Buttons for iOS
platform: iOS
page_order: 1
description: "This article covers how to implement action buttons in your iOS push notifications."
channel:
  - push

---

# Action buttons {#push-action-buttons-integration}

The Braze iOS SDK supports default push categories, including URL handling support for each push action button. Currently, the default categories have four sets of push action buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, and `More`. 

![A GIF of a push message being pulled down to display two customizable action buttons.][13]

To register Braze's default push categories, follow the integration instructions:

## Step 1: Adding Braze default push categories

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

Clicking on push action buttons with background activation mode will only dismiss the notification and not open the app. The next time the user opens the app, the button click analytics for these actions will be flushed to the server.

If you want to create your own custom notification categories, see [action button customization][37].

## Step 2: Enable interactive push handling

If you use the `UNNotification` framework and have implemented Braze [delegates][39], you should already have this method integrated. 

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

If you are not using UNNotification Framework, you will need to add the following code to your app's `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` to enable Braze's push action button handling:

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
We strongly recommend that people using `handleActionWithIdentifier` begin using `UNNotification` framework. We recommend this due to the deprecation of [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Push category customization

In addition to providing a set of [default push categories][2], Braze supports custom notification categories and actions. Once you register categories in your application, you can use the Braze dashboard to send notification categories to your users.

If you are not using the `UserNotifications` framework, see the [alternative categories][31] documentation.

These categories can then be assigned to push notifications via our dashboard to trigger the action button configurations of your design. Here's an example that leverages the `LIKE_CATEGORY` displayed on the device:

![A push message displaying two push action buttons "unlike" and "like".][17]


[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[14]: https://developer.apple.com/reference/usernotifications/unnotificationcategory "Categories Docs"
[17]: {% image_buster /assets/img_archive/push_example_category.png %}
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[31]: https://developer.apple.com/reference/uikit/uiusernotificationcategory
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/