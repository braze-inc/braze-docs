---
nav_title: Badges
article_title: Push Notification Badge Counts for iOS
platform: Swift
page_order: 2
description: "This article covers how to implement badge counts in your iOS push notifications."
channel:
  - push

---

# Push notification badge counts for iOS

Badges are small icons that are ideal for getting a user's attention. You can specify a badge count in the [**Settings**][1] tab when you compose a push notification using Braze's dashboard. You may also update your badge count manually through your application's [`applicationIconBadgeNumber`][20] property or the [remote notification payload][21]. 

Braze will automatically clear the badge count when a Braze notification is received while the app is in the foreground. Manually setting the badge number to 0 will also clear notifications in the notification center. 

If you do not have a plan for clearing badges as part of normal app operation or by sending pushes that clear the badge, you should clear the badge when the app becomes active by adding the following code to your app's `applicationDidBecomeActive:` delegate method:

{% tabs %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/
[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1