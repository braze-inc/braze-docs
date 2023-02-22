---
nav_title: Push Primer
article_title: Push Primer for iOS
page_order: 6
page_type: reference
description: "This article covers how to integrate iOS push primers."
platform: Swift
channel:
  - push
---

# Push primer integration

Push primer campaigns encourage your users to enable push on their device for your app. Getting permission from users to send messages directly to their devices can be complex, but our guides can help! This guide shows the steps developers must make to integrate push priming.

## Step 1: Append custom event checker to AppDelegate

The following code snippet checks if a custom event needs to be fired. Add the following line of code to your `AppDelegate`.

{% tabs %}
{% tab swift %}
```swift
let center = UNUserNotificationCenter.current()
center.getNotificationSettings(completionHandler: { (settings) in
  if settings.authorizationStatus == .notDetermined {
    // Fire custom event
  }
})
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
  if (settings.authorizationStatus == UNAuthorizationStatusNotDetermined) {
    // Fire custom event
  }
}];
```
{% endtab %}
{% endtabs %}

## Step 2: Set up an authorization request primer

Place this following code snippet within `if` block from step 1:

{% tabs %}
{% tab swift %}

```swift
center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
center.delegate = self as? UNUserNotificationCenterDelegate
center.setNotificationCategories(Braze.Notifications.categories)
application.registerForRemoteNotifications()
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                        @"error: %@)",
                        granted, error);
}];
center.delegate = self;
[center setNotificationCategories:BRZNotifications.categories];
[application registerForRemoteNotifications];
```
{% endtab %}
{% endtabs %}
