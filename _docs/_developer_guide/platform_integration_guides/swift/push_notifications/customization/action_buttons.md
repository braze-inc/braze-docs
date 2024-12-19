---
nav_title: Action Buttons
article_title: Push Action Buttons for iOS
platform: Swift
description: "This article covers how to implement action buttons in your iOS push notifications for the Swift SDK."
channel:
  - push

---

# Custom action buttons {#push-action-buttons-integration}

> The Braze Swift SDK provides URL handling support for push action buttons. 

There are four sets of default push action buttons for Braze default push categories: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, and `More`. 

![A GIF of a push message being pulled down to display two customizable action buttons.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

If you want to create your own custom notification categories, see [action button customization](#push-category-customization).

## Automatic integration (recommended)

When integrating push using the `configuration.push.automation` configuration option, Braze automatically registers the action buttons for the default push categories and handles the push action button click analytics and URL routing.

## Manual integration

To manually enable these push action buttons, first register for the default push categories. Then, use the `didReceive(_:completionHandler:)` delegate method to enable push action buttons.

### Step 1: Adding Braze default push categories {#registering}

Use the following code to register for the default push categories when you [register for push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

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

### Step 2: Enable interactive push handling {#enable-push-handling}

To enable our push action button handling, including click analytics and URL routing, add the following code to your app's `didReceive(_:completionHandler:)` delegate method:

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

If you use the `UNNotification` framework and have implemented the Braze [notification methods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling), you should already have this method integrated. 

## Push category customization

In addition to providing a set of default push categories, Braze supports custom notification categories and actions. After you register categories in your application, you can use the Braze dashboard to send these custom notification categories to your users.

These categories can then be assigned to push notifications via our dashboard to trigger the action button configurations of your design. 

### Example custom push category

Here's an example that leverages the `LIKE_CATEGORY` displayed on the device:

![A push message displaying two push action buttons "unlike" and "like".]({% image_buster /assets/img_archive/push_example_category.png %})

#### Step 1: Register a category

To register a category in your app, use a similar approach to the following:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
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
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
When you create a `UNNotificationAction`, you can specify a list of action options. For example, `UNNotificationActionOptions.foreground` let's your users open your app after tapping the action button. This is necessary for navigational on-click behaviors, such as "Open App" and "Deep Link into Application". For more information, see [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

#### Step 2: Select your categories

After you register a category, use the Braze dashboard to send notifications of that type to users.

{% alert tip %}
You only need to define custom notification categories for action buttons with _special actions_, such as deep linking into your app or opening a URL. You do not need to define them for action buttons that only dismiss a notification.
{% endalert %}

1. In the Braze dashboard, select **Messaging** > **Push Notifications**, then choose your iOS [push campaign]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message).
2. Under **Compose push notification**, turn on **Action Buttons**.
3. In the **iOS Notification Category** dropdown, select **Enter pre-registered custom iOS Category**.
4. Finally, enter one of the categories you created earlier. The following example, uses the custom category: `LIKE_CATEGORY`.

![The push notification campaign dashboard with the setup for custom categories.]({% image_buster /assets/img_archive/ios-notification-category.png %})

