---
nav_title: Badges
article_title: Push Notification Badge Counts for iOS
platform: iOS
page_order: 3.1
description: "This reference article covers how to implement badge counts in your iOS push notifications."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Badges

You can specify the desired badge count when you compose a push notification through the Braze dashboard. You may also update your badge count manually through your application's [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) property or the [remote notification payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). Braze will also clear the badge count when a Braze notification is received while the app is foregrounded. 

If you do not have a plan for clearing badges as part of normal app operation or by sending pushes that clear the badge, you should clear the badge when the app becomes active by adding the following code to your app's `applicationDidBecomeActive:` delegate method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Note that setting the badge number to 0 will also clear up notifications in the notification center. So even if you don't set badge number in push payloads, you can still set the badge number to 0 to remove the push notification(s) in the notification center after users click on the push.

