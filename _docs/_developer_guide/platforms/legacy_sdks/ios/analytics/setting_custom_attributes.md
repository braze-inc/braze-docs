---
nav_title: Setting custom attributes
article_title: Setting Custom Attributes for iOS
platform: iOS
page_order: 3
description: "This reference article shows how to set custom attributes in your iOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Setting custom attributes for iOS

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Assigning default user attributes

To assign user attributes, you need to set the appropriate field on the shared `ABKUser` object.

The following is an example of setting the first name attribute:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

The following attributes should be set on the `ABKUser` object:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## Assigning custom user attributes

Beyond the default user attributes, Braze also allows you to define custom attributes using several different data types. See our [user data collection]({{site.baseurl}}/developer_guide/analytics/) for more information on the segmentation options each of these attributes will afford you.

### Custom attribute with a string value

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### Custom attribute with an integer value

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Custom attribute with a double value

Braze treats `float` and `double` values the same within our database.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### Custom attribute with a boolean value

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Custom attribute with a date value

Dates passed to Braze with this method must either be in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (e.g `2013-07-16T19:20:30+01:00`) or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format (`2016-12-14T13:32:31.601-0800`).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### Custom attribute with an array value

The maximum number of elements in [custom attribute arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) defaults to 25. Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements. The maximum for individual arrays can be increased to up to 100. If you would like this maximum increased, reach out to your customer service manager. 


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### Unsetting a custom attribute

Custom attributes can also be unset using the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Incrementing/decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer or long value:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. Refer to the [User API documentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) for details.

### Custom attribute value limits

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

#### Additional information

- More details can be found within the [`ABKUser.h` file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Refer to the [`ABKUser` documentation](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html) for more information.

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType` or `setPushNotificationSubscriptionType`, respectively. Both of these functions take the enum type `ABKNotificationSubscriptionType` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `ABKOptedin` | Subscribed, and explicitly opted in |
| `ABKSubscribed` | Subscribed, but not explicitly opted in |
| `ABKUnsubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Users who grant permission for an app to send them push notifications default to the status of `ABKOptedin` as iOS requires an explicit opt-in.

Users will be set to `ABKSubscribed` automatically upon receipt of a valid email address; however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user. Refer to [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details.

### Setting email subscriptions

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Setting push notification subscriptions

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Refer to [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details.

