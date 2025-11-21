---
nav_title: Logging purchases
article_title: Logging Purchases for Windows Universal
platform: Windows Universal
page_order: 4
description: "This reference article covers how to log purchases on the Windows Universal platform."
hidden: true
---
 
# Logging purchases
{% multi_lang_include archive/windows_deprecation.md %}

Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) article. We also recommend familiarizing yourself with our [event naming conventions]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

To use this feature, add this method call after a successful purchase in your app:

Purchases are logged by using the `EventLogger`, which is a property exposed in IAppboy. To obtain a reference to the `EventLogger`, call `Appboy.SharedInstance.EventLogger`.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Log purchases at the order level
If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

## REST API

You can also use our REST API to record purchases. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

