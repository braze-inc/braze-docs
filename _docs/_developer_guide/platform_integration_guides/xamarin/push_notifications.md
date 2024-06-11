---
nav_title: Push Notifications
article_title: Push Notifications for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "This article covers Android, FireOS, and iOS push notification integration for the Xamarin platform."
channel: push 
---

# Push notifications integration

> This reference article covers how to set up Android, FireOS, and iOS push notifications for Xamarin. 

## Android

See the [Android integration instructions][1] for information on how to integrate push into your Xamarin Android app. Furthermore, you can look at the [Android MAUI][2] sample app to see how the namespaces change from Java to C#.

## iOS

### Step 1: Complete the initial setup

See the [Swift integration instructions][3] for information about setting up your application with push and storing your credentials on our server. Refer to the [iOS MAUI][4] sample app for more details.

### Step 2: Request push notifications permission

Set up push permissions by adding the following code to the ```FinishedLaunching``` section of your ```AppDelegate.cs```:

```csharp
application.RegisterForRemoteNotifications();

center.RequestAuthorization(UNAuthorizationOptions.Alert | UNAuthorizationOptions.Sound | UNAuthorizationOptions.Badge, (granted, error) => {
    Console.WriteLine($"Notification authorization, granted: {granted}, error: {error?.ToString() ?? "None"}");
    Appboy.SharedInstance.PushAuthorizationFromUserNotificationCenter(granted);
});
```
For more details, see the Xamarin documentation for [Enhanced User Notifications in Xamarin.iOS][5].

>  If you've implemented a custom push opt-in prompt, make sure that you're calling the preceding code EVERY time the app runs after they grant push permissions to your app. Apps need to re-register with APNs as device tokens can change arbitrarily.

### Step 3: Registering push tokens

Register for your push tokens by adding the following code in the ```RegisteredForRemoteNotifications``` method of your ```AppDelegate.cs```:

```csharp
public void RegisteredForRemoteNotifications(UIApplication application, NSData deviceToken)
{
    Appboy.SharedInstance.RegisterDeviceToken(deviceToken);
}
```

### Step 4: Enabling push analytics

Enable open tracking on push notifications by adding the following code to the `DidReceiveRemoteNotification` method of your `AppDelegate.cs`:

```csharp
public virtual void DidReceiveRemoteNotification(UIApplication application, NSDictionary userInfo, Action<UIBackgroundFetchResult> completionHandler)
{
    Appboy.SharedInstance.RegisterApplicationWithFetchCompletionHandler(application, userInfo, completionHandler);
}
```

### (Optional) Step 5: Utilizing badge count

If [badge counts are enabled][6], Braze will display a badge when a customer has unread notifications. By default, this number is 1. Braze will only clear the badge count when the app is opened directly from a Braze push notification. To clear the badge count, use the following code:

```csharp
var content = new UNMutableNotificationContent ();
content.Badge = 0;
```
For more details on updating notifications, refer to the Xamarin documentation for [Enhanced User Notifications in Xamarin.iOS][5].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration
[4]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui
[5]: https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos
[6]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#badge-count-with-braze


