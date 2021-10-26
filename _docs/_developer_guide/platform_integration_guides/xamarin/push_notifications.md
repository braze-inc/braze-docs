---
nav_title: Push Notifications
article_title: Push Notifications for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "This article covers Android and FireOS push notification integration for the Xamarin platform."
channel: push 
---

# Push notifications

## Android

See [the Android integration instructions][11] for information on how to integrate push into your Xamarin Android app. Furthermore, you can look at the [sample application][12] to see how the namespaces change from java to c#.

## iOS

See [the iOS integration instructions][1] for information about setting up your application with push and storing your credentials on our server.

### Requesting push permissions

Set up push permissions by adding the following code to the ```FinishedLaunching``` section of your ```AppDelegate.cs```:

```csharp
// C#
UIUserNotificationSettings settings = UIUserNotificationSettings.GetSettingsForTypes(UIUserNotificationType.Badge | UIUserNotificationType.Alert | UIUserNotificationType.Sound, null);
UIApplication.SharedApplication.RegisterForRemoteNotifications();
UIApplication.SharedApplication.RegisterUserNotificationSettings(settings);
```

>  If you’ve implemented a custom push opt-in prompt, make sure that you’re calling the above code EVERY time the app runs after they grant push permissions to your app. Apps need to reregister with APNs as device tokens can change arbitrarily.

### Registering push tokens

Register for your push tokens by adding the following code in the ```RegisteredForRemoteNotifications``` method of your ```AppDelegate.cs```:

```csharp
// C#
Appboy.SharedInstance().RegisterDeviceToken (deviceToken);
```

### Enabling push analytics

Enable open tracking on push notifications by adding the following code to the `DidReceiveRemoteNotification` method of your `AppDelegate.cs`:

```csharp
// C#
public override void DidReceiveRemoteNotification (UIApplication application, NSDictionary userInfo, Action<UIBackgroundFetchResult> completionHandler)
  {
    Appboy.SharedInstance().RegisterApplicationWithFetchCompletionHandler(application, userInfo, completionHandler);
  }
```

### Badge count

If [badge counts are enabled][2], Braze will display a badge when a customer has unread notifications. By default, this number is 1. Braze will only clear the badge count when the app is opened directly from a Braze push notification. To clear the badge count, you can refer to the [Xamarin documentation][3] and use the following code:

```csharp
// C#
UIApplication.SharedApplication.ApplicationIconBadgeNumber = 0;
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#badge-count-with-braze
[3]: https://developer.xamarin.com/guides/cross-platform/application_fundamentals/notifications/ios/local_notifications_in_ios/#Handling_Notifications
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[12]: https://github.com/Appboy/appboy-xamarin-bindings

