## Tracking purchases and revenue

To use this feature, add this method call after a successful purchase in your app:

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### Adding properties

You can add metadata about purchases by passing a properties dictionary with your purchase information.

Properties are defined as key-value pairs.  Keys are `String` objects and values can be `String` or `Integer`.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### Log purchases at the order level
If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

### REST API

You can also use our REST API to record purchases. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

