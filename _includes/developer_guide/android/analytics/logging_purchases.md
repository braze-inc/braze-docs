 
# Logging purchases

> Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value. This reference article shows how to track in-app purchases and revenue and assign purchase properties in your Android or FireOS application.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [analytics overview]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

## Tracking purchases and revenue

To use this feature, call [`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) after a successful purchase in your app. If the product Identifier is empty, the purchase will not be logged to Braze.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
If you pass in a value of `10 USD` and a quantity of `3`, that will log to the user's profile as three purchases of 10 dollars for a total of 30 dollars. Quantities must be less than or equal to 100. Values of purchases can be negative.
{% endalert %}

### Adding properties

You can add metadata about purchases by either passing an [event property array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) or a [Braze Properties](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) object with your purchase information.

#### Braze properties object formatting

Properties are defined as key-value pairs. Keys are `String` objects, and values can be `String`, `int`, `float`, `boolean`, or [`Date`](http://developer.android.com/reference/java/util/Date.html) objects.

{% tabs %}
{% tab JAVA %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endtab %}
{% endtabs %}

Refer to our [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) for more information.

### Log purchases at the order level
If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

### Reserved keys

The following keys are reserved and cannot be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

You can also use our REST API to record purchases. Refer to the [User API documentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) for details.

