---
nav_title: Logging Custom Events
platform: Xamarin
subplatform: iOS
page_order: 1

---

# Logging Custom Events

See [the iOS integration instructions][1] for in depth discussion of event tracking best practices and interfaces.

**Xamarin C#**

```csharp
Appboy.SharedInstance ().LogCustomEvent ("YOUR_EVENT_NAME");
```

**Implementation Example**

`logCustomEvent` is utilized within the `AppboySampleViewController.cs` within the [TestApp.XamariniOS][2] sample application.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[2]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS
