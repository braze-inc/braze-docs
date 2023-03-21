---
nav_title: Action Buttons
article_title: Push Action Buttons for iOS
platform: Swift
page_order: 1
description: "This article covers how to implement action buttons in your iOS push notifications."
channel:
  - push

---

# Action buttons {#push-action-buttons-integration}

The Braze Swift SDK supports default push categories, including URL handling support for each push action button. Currently, the default categories have four sets of push action buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, and `More`. 

![A GIF of a push message being pulled down to display two customizable action buttons.][13]

To register Braze's default push categories, follow the integration instructions:

## Step 1: Adding Braze default push categories

Use the following code to register for Braze's default push categories when you [register for push][36]:

{% tabs %}
{% tab swift %}

```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

Clicking on push action buttons with background activation mode will only dismiss the notification and not open the app. The next time the user opens the app, the button click analytics for these actions will be flushed to the server.

If you want to create your own custom notification categories, see [action button customization][37].

## Step 2: Enable interactive push handling

If you use the `UNNotification` framework and have implemented the Braze [notification methods][39], you should already have this method integrated. 

To enable Braze's push action button handling, including click analytics and URL routing, add the following code to your app's `didReceive(_:completionHandler:)` delegate method:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

## Push category customization

In addition to providing a set of default push categories, Braze supports custom notification categories and actions. Once you register categories in your application, you can use the Braze dashboard to send notification categories to your users.

These categories can then be assigned to push notifications via our dashboard to trigger the action button configurations of your design. Here's an example that leverages the `LIKE_CATEGORY` displayed on the device:

![A push message displaying two push action buttons "unlike" and "like".][17]


[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[14]: https://developer.apple.com/reference/usernotifications/unnotificationcategory "Categories Docs"
[17]: {% image_buster /assets/img_archive/push_example_category.png %}
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/#push-category-customization
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling