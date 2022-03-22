---
nav_title: Logging Purchases
article_title: Logging Purchases for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "This reference article shows how to track in-app purchases and revenue and assign purchase properties in your Android application."

---

# Logging purchases for Android and FireOS

Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [analytics overview][3].

## Tracking purchases and revenue

To use this feature, call [`logPurchase()`][6] after a successful purchase in your app. If the product Identifier is empty, the purchase will not be logged to Braze.

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

You can add metadata about purchases by passing a [Braze Properties][4] object with your purchase information.

Properties are defined as key-value pairs. Keys are `String` objects, and values can be `String`, `int`, `float`, `boolean`, or [`Date`][5] objects.

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

Refer to our [KDoc][6] for more information.

### Reserved keys

The following keys are reserved and cannot be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

You can also use our REST API to record purchases. Refer to the [User API documentation][1] for details.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html
[5]: http://developer.android.com/reference/java/util/Date.html
[6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-purchase.html
