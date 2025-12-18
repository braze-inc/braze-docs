## Troubleshooting

### Push doesn't appear after app is closed from task switcher

If you observe that push notifications no longer appear after the app is closed from the task switcher, your app is likely in Debug mode. .NET MAUI adds scaffolding in Debug mode that prevents apps from receiving push after their process is killed. If you run your app in Release Mode, you should see push even after the app is closed from the task switcher.

### Custom notification factory not being set correctly

Custom notification factories (and all delegates) must extend [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) to work properly across the C# and Java divide. See [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) on implementing Java interfaces for more information.
