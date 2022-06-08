---
nav_title: Analytics
article_title: Analytics for React Native
platform: React Native
page_order: 5
description: "This article covers how to set up and track basic analytics in the React Native app."

---

# Analytics

This article covers how to set up and track basic analytics in your React Native app.

Before you start, read our [Analytics Overview][0] article to learn more about Braze analytics and what is already tracked by default. We also recommend familiarizing yourself with our [event naming conventions][1].

## Session tracking

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. based on the following session semantics, our SDK generates “start session” and “close session” data points that account for session length and session counts viewable within the Braze dashboard.

To set a user ID or start a session, use the `changeUser` method, which takes a user ID parameter.

```javascript
ReactAppboy.changeUser("user_id");
```

## Logging custom events

You can record custom events in Braze to learn more about your app’s usage patterns and to segment your users by their actions in the dashboard.

```javascript
ReactAppboy.logCustomEvent("react_native_custom_event");
```

You can add metadata about the event by passing a properties object with your custom event.

```javascript
reactAppboy.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## Logging custom attributes

Braze provides methods for assigning attributes to users. You’ll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To assign user attributes automatically collected by Braze, you can use setter methods that come with the SDK.

```javascript
ReactAppboy.setFirstName("Name");
```

The following attributes are supported:

- First Name
- Last Name
- Gender
- Date of Birth
- Home City
- Country
- Phone Number
- Language
- Email
- Twitter Data
- Facebook Data

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Custom user attributes

Beyond the default user attributes, Braze also allows you to define custom attributes for your users. Supported data types for values include `Date`, `Array`, `boolean`, `string`, `number`, and `float`.
String values have a maximum length of 255 characters.

```javascript
ReactAppboy.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Unsetting a custom attribute

```javascript
ReactAppboy.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

## Logging purchases

Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

```javascript
ReactAppboy.logPurchase(productId, price, currencyCode, quantity, properties);
```

For example:

```javascript
ReactAppboy.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
If you pass in a value of `10 USD` and a quantity of `3`, this will log three purchases of 10 dollars for a total of 30 dollars to the user's profile. Quantities must be less than or equal to 100. Values of purchases can be negative.
{% endalert %}

### Reserved keys

The following keys are **reserved** and **cannot** be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/
[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/