---
nav_title: Action Buttons
article_title: Push Action Buttons for iOS
platform: Swift
page_order: 1
description: "This article covers how to implement action buttons in your iOS push notifications."
channel:
  - push

---

# Push action buttons for iOS {#push-action-buttons-integration}

The Braze Swift SDK provides URL handling support for push action buttons. There are four sets of default push action buttons for Braze's default push categories: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, and `More`. 

![A GIF of a push message being pulled down to display two customizable action buttons.][13]{: style="max-width:60%"}

To enable these push action buttons, first register for Braze's default push categories. Then, use the `didReceive(_:completionHandler:)` delegate method to enable push action buttons.

If you want to create your own custom notification categories, see [action button customization](#push-category-customization).

## Step 1: Adding Braze default push categories {#registering}

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

{% alert note %}
Clicking on push action buttons with background activation mode will only dismiss the notification and not open the app. The next time the user opens the app, the button click analytics for these actions will be flushed to the server.
{% endalert %}

## Step 2: Enable interactive push handling {#enable-push-handling}

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

If you use the `UNNotification` framework and have implemented the Braze [notification methods][39], you should already have this method integrated. 

## Push category customization

In addition to providing a set of default push categories, Braze supports custom notification categories and actions. Once you register categories in your application, you can use the Braze dashboard to send these custom notification categories to your users.

These categories can then be assigned to push notifications via our dashboard to trigger the action button configurations of your design. 

### Example custom push category

Here's an example that leverages the `LIKE_CATEGORY` displayed on the device:

![A push message displaying two push action buttons "unlike" and "like".][17]

To register categories in your application, refer to the following code snippet:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like"),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike")
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];
UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionNone];
UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionNone];
UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction,
                                                                                        unlikeAction
                                                                                      ]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone
];
[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

Once you register categories in your application, use the Braze dashboard to send notifications of that type to your users. Define your custom notification category in **Compose** step of the push composer. 

1. Make sure **Action Buttons** are turned on. 
2. For **iOS Notification Category**, select **Enter pre-registered custom iOS Category**.
3. Enter the category you previously defined (for example `LIKE_CATEGORY`).

![The push notification campaign dashboard with the setup for custom categories.][18]

[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[17]: {% image_buster /assets/img_archive/push_example_category.png %}
[18]: {% image_buster /assets/img_archive/ios-notification-category.png %}
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling