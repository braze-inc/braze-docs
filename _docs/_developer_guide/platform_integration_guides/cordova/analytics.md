---
nav_title: Analytics
article_title: Analytics integration
page_order: 3
---

# Analytics integration

> Learn how to integrate analytics for the Cordova Braze SDK.

{% multi_lang_include cordova/prerequisites.md %}

## Logging custom events

To log custom events, use the `logCustomEvent()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) guides for logging custom events.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

## Logging purchases

To log purchases, use the `logPurchase()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) guides for logging purchases.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
BrazePlugin.logPurchase("product_id_with_null_currency", 10, null, 5, properties);
```

{% alert tip %}
If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more.
{% endalert %}

## Setting custom attributes

To set custom attributes, use the `setFirstName()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) guides setting custom attributes.

```javascript
BrazePlugin.setFirstName("firstName");
```

## Setting user IDs

To set user IDs, use the `changeUser()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) guides for setting user IDs.

```javascript
BrazePlugin.changeUser("USER_ID");
```
