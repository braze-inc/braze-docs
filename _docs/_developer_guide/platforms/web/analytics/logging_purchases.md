---
nav_title: Logging Purchases
article_title: Logging Purchases for Web
platform: Web
page_order: 4
page_type: reference
description: "This article describes how to log purchases and add properties to those purchases for Web."

---
 
# Logging purchases

> Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value. 

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

To use this feature, add the [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) call after a successful purchase in your app. Note that the `quantity` must be less than or equal to 100.

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

