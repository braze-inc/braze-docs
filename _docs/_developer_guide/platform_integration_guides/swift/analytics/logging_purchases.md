---
nav_title: Logging Purchases
article_title: Logging Purchases for iOS
platform: Swift
page_order: 4
description: "This reference article shows how to track in-app purchases and revenue and assign purchase properties for the Swift SDK."

---

# Logging purchases

Record in-app purchases so that you can track your revenue over time and across revenue sources and segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Tracking purchases and revenue

To use this feature, add this method call after a successful purchase in your app:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endtab %}
{% endtabs %}

- Supported currency symbols include: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, and more.
  - Any other provided currency symbol will result in a logged warning and no other action taken by the SDK.
- The product ID can have a maximum of 255 characters
- Note that if the product identifier is empty, the purchase will not be logged to Braze.

### Adding properties {#properties-purchases}
You can add metadata about purchases by passing a Dictionary populated with `Int`, `Double`, `String`, `Bool`, or `Date` values.

Refer to the [iOS class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "logpurchase documentation") for additional details.

### Adding quantity
You can add a quantity to your purchases if customers make the same purchase multiple times in a single checkout. You can accomplish this by passing in an `Int` for the quantity.

* A quantity input must be in the range of [0, 100] for the SDK to log a purchase.
* Methods without a quantity input will have a default quantity value of 1.

Refer to the [iOS class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "logpurchase documentation") for additional details.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logPurchase(productId: "product_id", currency: "USD", price: price, quantity: quantity, properties: ["key1":"value1"])
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logPurchase:productId
                      currency:@"USD"
                         price:price
                      quantity:quantity
                    properties:@{@"checkout_id" : self.checkoutId}];
```

{% endtab %}
{% endtabs %}

{% alert tip %}
If you pass in a value of 10 USD and a quantity of 3, that will log to the user's profile as three purchases of 10 dollars for a total of 30 dollars.
{% endalert %}

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

