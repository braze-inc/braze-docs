{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Session tracking

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Based on the following session semantics, our SDK generates "start session" and "close session" data points that account for session length and session counts viewable within the Braze dashboard.

To set a user ID or start a session, use the `changeUser` method, which takes a user ID parameter.

```dart
braze.changeUser('user_id');
```

## Logging custom events

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions in the dashboard.

```dart
braze.logCustomEvent('my_custom_event');
```

You can add metadata about the event by passing a properties object with your custom event.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## Logging custom attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To set user attributes automatically collected by Braze, you can use setter methods that come with the SDK.

```dart
braze.setFirstName('Name');
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

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Setting custom attribute values

In addition to the default user attributes, Braze also allows you to define custom attributes using a number of different data types:

{% tabs %}
{% tab Boolean %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab Integer %}

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab String %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Date %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Array %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### Unsetting a custom attribute

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## Logging purchases

Record in-app purchases so that you can track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

For example:

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

