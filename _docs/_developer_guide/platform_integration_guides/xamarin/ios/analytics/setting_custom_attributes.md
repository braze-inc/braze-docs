---
nav_title: Setting Custom Attributes
platform: Xamarin
subplatform: iOS
page_order: 2

---

# Setting Custom Attributes

See [the iOS integration instructions][1] for in depth discussion of attribute tracking best practices and interfaces.

**Xamarin C#**

```csharp
Appboy.SharedInstance ().User.FirstName = "YOUR_NAME";
```

**Implementation Example**

You can see user properties being set in the sample application's `UserPropertyButtonHandler` method inside `AppboySampleViewController.cs`.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
