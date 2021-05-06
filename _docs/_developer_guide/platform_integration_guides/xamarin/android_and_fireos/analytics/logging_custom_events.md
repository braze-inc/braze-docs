---
nav_title: Logging Custom Events
platform: Xamarin
subplatform: Android and FireOS
page_order: 1
---
# Logging Custom Events

See [the Android integration instructions][1] for in depth discussion of event tracking best practices and interfaces.

```csharp
Appboy.GetInstance(context).LogCustomEvent("YOUR_EVENT_NAME");
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
