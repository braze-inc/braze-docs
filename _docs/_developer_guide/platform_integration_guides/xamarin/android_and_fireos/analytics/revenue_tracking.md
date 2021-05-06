---
nav_title: Logging Purchases
platform: Xamarin
subplatform: Android and FireOS
page_order: 3
---
# Logging Purchases

See [the Android integration instructions][1] for in depth discussion of revenue tracking best practices and interfaces.

```csharp
Appboy.GetInstance(context).LogPurchase("YOUR_PURCHASE_NAME", 100);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases
