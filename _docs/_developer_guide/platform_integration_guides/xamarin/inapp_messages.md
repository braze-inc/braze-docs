---
nav_title: In-App Messaging
article_title: In-App Messaging for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "This article covers iOS, Android, and FireOS in-app messaging for the Xamarin platform."
channel: in-app messages

---

# In-app messaging integration

> This article covers how to set up a iOS, Android, and FireOS in-app messages for the Xamarin platform.

## Android
See the [Android integration instructions][11] for information on how to integrate in-app messages into your Xamarin Android app.  Furthermore, you can look at the [sample application][12] for implementation samples.

## iOS

### Step 1: Set up the in-app message presenter

#### Using the default UI

To use Braze's default in-app message UI, first create a new `BrazeInAppMessageUI`:
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

Then, register the `BrazeInAppMessageUI` as the in-app message presenter when setting up your Braze instance:
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

### Step 2: Create a new in-app message

There are 4 in-app message types supported on the Xamarin SDK: `slideup`, `modal`, `full`, and `HTML`.

To create a new in-app message, use the `BRZInAppMessageRaw` class and properties:
```csharp
BRZInAppMessageRaw slideup = new BRZInAppMessageRaw();
slideup.Type = BRZInAppMessageRawType.Slideup;
slideup.Message = "This is the message";
slideup.ClickAction = BRZInAppMessageRawClickAction.Url;
slideup.Url = new NSUrl("https://braze.com");
```

### Step 3: Display in-app messages

To display new in-app messages, use the method `PresentMessage(message)`:
```csharp
App.inAppMessageUI?.PresentMessage(slideup);
```

See the [iOS integration instructions][1] for information on in-app best practices. Furthermore, you can look at the [iOS MAUI][2] sample application for implementation samples.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/
[2]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/overview/
[12]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp
