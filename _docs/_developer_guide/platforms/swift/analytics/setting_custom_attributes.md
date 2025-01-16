---
nav_title: Setting Custom Attributes
article_title: Setting Custom Attributes for iOS
platform: Swift
page_order: 3
description: "This reference article shows how to set custom attributes for the Swift SDK."

---

# Setting custom attributes

> Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Assigning default user attributes

To assign user attributes, you need to set the appropriate field on the shared `ABKUser` object.

The following is an example of setting the first name attribute:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

The following attributes should be set on the `Braze.User` object:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

## Assigning custom user attributes

Beyond the default user attributes, Braze also allows you to define custom attributes using several different data types. See our [user data collection]({{site.baseurl}}/developer_guide/getting_started/analytics_overview/) for more information on the segmentation options each of these attributes will afford you.

### Custom attribute with a string value

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### Custom attribute with an integer value

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### Custom attribute with a double value

Braze treats `float` and `double` values the same within our database.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### Custom attribute with a boolean value

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### Custom attribute with a date value

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### Custom attribute with an array value

The maximum number of elements in [custom attribute arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) defaults to 25. Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements. The maximum for individual arrays can be increased to up to 100. If you would like this maximum increased, reach out to your customer service manager. 


{% tabs %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% endtabs %}

### Unsetting a custom attribute

Custom attributes can also be unset using the following method:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Incrementing/decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer or long value:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. Refer to the [User API documentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) for details.

### Custom attribute value limits

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

#### Additional information

- Refer to the [`Braze.User` documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class) for more information.

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions `set(emailSubscriptionState:)` or `set(pushNotificationSubscriptionState:)`, respectively. Both of these functions take the enum type `Braze.User.SubscriptionState` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `optedIn` | Subscribed, and explicitly opted in |
| `subscribed` | Subscribed, but not explicitly opted in |
| `unsubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Users who grant permission for an app to send them push notifications default to the status of `optedIn` as iOS requires an explicit opt-in.

Users will be set to `subscribed` automatically upon receipt of a valid email address; however, we suggest that you establish an explicit opt-in process and set this value to `optedIn` upon receipt of explicit consent from your user. Refer to [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details.

### Setting email subscriptions

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Setting push notification subscriptions

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Refer to [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details.

