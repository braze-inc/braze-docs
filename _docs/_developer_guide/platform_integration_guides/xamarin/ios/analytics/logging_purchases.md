---
nav_title: Logging Purchases
platform: Xamarin
subplatform: iOS
page_order: 3
---
## Logging Purchases

See [the iOS integration instructions][1] for in depth discussion of revenue tracking best practices and interfaces.

**Xamarin C#**

```csharp
Appboy.SharedInstance ().LogPurchase ("myProduct", "USD", new NSDecimalNumber("10"));
```

**Implementation Example**

You can see user properties being set in the sample application's `EventsAndPurchasesButtonHandler` method inside `AppboySampleViewController.cs`.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/
