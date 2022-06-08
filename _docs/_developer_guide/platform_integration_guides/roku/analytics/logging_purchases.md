---
nav_title: Logging Purchases
article_title: Logging Purchases for Roku
platform: Roku
page_order: 3
page_type: reference
description: "This page provides methods to log purchase events via the Braze SDK."

---

# Logging purchases

Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best Practices][3] article. We also recommend familiarizing yourself with our [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Tracking purchases and revenue

To use this feature, add this method call after a successful purchase in your app:

```javascript
m.Braze.logPurchase("PURCHASE_NAME", "CURRENCY_CODE", Double price, Integer quantity)
```

### Adding properties

You can add metadata about purchases by passing a properties dictionary with your purchase information.

Properties are defined as key-value pairs.  Keys are `String` objects and values can be `String` or `Integer`.

```javascript
m.Braze.logPurchase("PURCHASE_NAME", "CURRENCY_CODE", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### REST API

You can also use our REST API to record purchases. Refer to the [users API][2] documentation for details.

[2]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
