## Tracking purchases and revenue

To tracking purchases and review, call the [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) method after a successful purchase in your app. Note that the `quantity` must be less than or equal to 100.

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## Adding properties

You can add [metadata](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) about purchases by either passing an [event property array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) or by passing an object of key-value pairs with your purchase information. 

#### Object formatting

Keys are `string` objects, and values can be `string`, `numeric`, `boolean`, or `Date` objects.

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### Log purchases at the order level

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

## REST API

You can also use our REST API to record purchases. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

