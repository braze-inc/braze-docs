---
nav_title: Push Notifications
platform: Xamarin
subplatform: Android and FireOS
page_order: 1
---
# Push Notifications

See [the Android integration instructions][1] for information on how to integrate push into your Xamarin Android app.  Furthermore, you can look at the [sample application][2] to see how the namespaces change from java to c#.

In particular, look at:

- [braze.xml][5] to see how to set up credentials and set up automatic deep link handling
- [AndroidManifest.xml][6] to see how to set permissions for Braze FCM.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/
[2]: https://github.com/Appboy/appboy-xamarin-bindings
[5]: https://github.com/Appboy/appboy-xamarin-bindings/blob/master/appboy-component/samples/android/TestApp.XamarinAndroid/Resources/values/braze.xml
[6]: https://github.com/Appboy/appboy-xamarin-bindings/blob/master/appboy-component/samples/android/TestApp.XamarinAndroid/Properties/AndroidManifest.xml
