---
nav_title: Troubleshooting
article_title: Troubleshooting for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 6
description: "This article covers iOS and Android troubleshooting for the Xamarin platform."

---

# Troubleshooting

## Android

### Push doesn't appear after app is closed from task switcher

If you observe that push notifications no longer appear after the app is closed from the task switcher, your app is likely in Debug mode. Xamarin adds scaffolding in Debug mode that prevents apps from receiving push after their process is killed. If you run your app in Release Mode, you should see push even after the app is closed from the task switcher.

### Custom notification factory not being set correctly

Custom notification factories (and all delegates) must extend [`Java.Lang.Object`][2] to work properly across the C# and Java divide. See [Xamarin][1] on implementing Java interfaces for more information.

[1]: https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces
[2]: https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/
