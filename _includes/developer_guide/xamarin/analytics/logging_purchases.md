{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Logging purchases

Record in-app purchases using `LogPurchase` to track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platforms/android/analytics/logging_purchases/) for an in-depth discussion of revenue tracking best practices and interfaces.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platforms/swift/analytics/logging_purchases/) for an in-depth discussion of revenue tracking best practices and interfaces.

{% endtab %}
{% endtabs %}

### Log purchases at the order level

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

### Reserved keys

The following keys are reserved and **cannot** be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`
