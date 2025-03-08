{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Tracking purchases and revenue

To track purchases and revenue, call the `logPurchase()` method after a successful purchase in your app.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

Keep in mind, Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported. For example:

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
If you pass in a value of `10 USD` and a quantity of `3`, this will log three purchases of 10 dollars for a total of 30 dollars to the user's profile. Quantities must be less than or equal to 100. Values of purchases can be negative.
{% endalert %}

### Tracking at the order level

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

### Reserved keys

The following keys are reserved and cannot be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`
