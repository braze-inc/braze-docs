---
nav_title: In-App Messaging
article_title: In-App Messaging for Xamarin
platform: Xamarin
page_order: 2
description: "This article covers iOS, Android, and FireOS in-app messaging for the Xamarin platform."

---

# In-App Messaging

## Android
See [the Android integration instructions][11] for information on how to integrate in-app messages into your Xamarin Android app.  Furthermore, you can look at the [sample application][12] for implementation samples.

## iOS

In-app messages will work by default if you've included the Appboy.bundle folder in your application.  On Xamarin we don't currently support in-app message custom styling.  If you would like to customize your in-app message UI, please implement the ABKInAppMessageControllerDelegate method `ABKInAppMessageViewController InAppMessageViewControllerWithInAppMessage(ABKInAppMessage inAppMessage);` and return your custom view controller. That will make sure Braze passes you the in-app message object rather than displaying it for you. You will then have the option of displaying the in-app message object's content manually.

See [the iOS integration instructions][1] for information on In-App best practices.  Furthermore, you can look at the [sample application][2] for implementation samples.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#in-app-messaging
[2]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/overview/
[12]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples
