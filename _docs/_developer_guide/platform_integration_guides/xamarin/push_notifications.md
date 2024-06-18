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

See the [Android integration instructions][1] for information on how to integrate push into your Xamarin Android app. Furthermore, you can look at the [Android MAUI][2] sample application to see how the namespaces change from Java to C#.

## iOS

### Step 1: Complete the initial setup

See the [Swift integration instructions][3] for information about setting up your application with push and storing your credentials on our server. Refer to the [iOS MAUI][4] sample application for more details.

### Step 2: Request push notifications permission

Our Xamarin SDK now supports automatic push set up. Set up push automation and permissions by adding the following code to your Braze instance configuration:

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```
Refer to the [iOS MAUI][4] sample application for more details. For more details, see the Xamarin documentation for [Enhanced User Notifications in Xamarin.iOS][5].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration
[4]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp
[5]: https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos


