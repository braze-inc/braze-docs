---
nav_title: Logging Purchases
article_title: Logging Purchases for Web
platform: Web
page_order: 4
page_type: reference
description: "This article describes how to log purchases for Web."

---

# Logging purchases for web

Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value. Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices][3].

To use this feature, add the [`logPurchase()`][8] call after a successful purchase in your app. Note that the `quantity` must be less than or equal to 100.

```javascript
braze.logPurchase(productId, price, "USD", quantity);
```

## Adding properties

You can add [metadata][8] about purchases by passing an object of key-value pairs with your purchase information. Keys are `string` objects, and values can be `string`, `numeric`, `boolean`, or `Date` objects.

```javascript
braze.logPurchase(productId, price, "USD", quantity, {key: "value"});
```

## REST API

You can also use our REST API to record purchases. Refer to the [users API][1] documentation for details.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[8]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase
