---
nav_title: Logging Purchases
platform: React Native
subplatform: Android and FireOS
page_order: 3
---
## Logging Purchases

See [the Android integration instructions][1] for in depth discussion of revenue tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
ReactAppboy.logPurchase("productId", "10.99", "USD", 5, properties);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases
