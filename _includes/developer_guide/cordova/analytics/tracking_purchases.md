{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Tracking purchases and revenue

To track purchases and revenue, use the `logPurchase()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) and [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/logging_purchases/) guides for logging purchases.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more.
{% endalert %}
