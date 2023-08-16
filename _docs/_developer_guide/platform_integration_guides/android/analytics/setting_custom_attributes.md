---
nav_title: Setting Custom Attributes
article_title: Setting Custom Attributes for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "This reference article shows how to set custom attributes in your Android or FireOS application."

---

# Setting custom attributes

> Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard. This reference article shows how to set custom attributes in your Android or FireOS application.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [analytics overview][7], as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Assigning user attributes

To assign attributes to your users, call the `getCurrentUser()` method on your Braze instance to get a reference to the current user of your app. After you have a reference to the current user, you can call methods to set predefined or custom attributes.

### Standard user attributes

Braze provides predefined methods for setting the following user attributes within the [BrazeUser class][2]. Refer to our KDoc for [method specifications][2]:

- First name
- Last name
- Country
- Language
- Date of birth
- Email
- Gender
- Home city
- Phone number

All string values such as first name, last name, country, and home city are limited to 255 characters.

#### Setting standard attribute value

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setFirstName("first_name");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setFirstName("first_name")
```

{% endtab %}
{% endtabs %}

#### Setting custom attribute values

{% tabs local %}
{% tab String %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", "your_attribute_value");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Integer %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
// Integer attributes may also be incremented using code like the following:
Braze.getInstance(context).getCurrentUser().incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)
// Integer attributes may also be incremented using code like the following:
Braze.getInstance(context).currentUser?.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Boolean %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Long %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Float %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Double %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
// This method will assign the current time to a custom attribute at the time the method is called:
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToNow("your_attribute_key");
// This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
// This method will assign the current time to a custom attribute at the time the method is called:
Braze.getInstance(context).currentUser?.setCustomUserAttributeToNow("your_attribute_key")
// This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
Braze.getInstance(context).currentUser?.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Dates passed to Braze with this method must either be in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (e.g `2013-07-16T19:20:30+01:00`) or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format (e.g `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Array %}

The maximum number of elements in custom attribute arrays defaults to 25. The maximum for individual arrays can be increased to up to 100 in the Braze dashboard, under **Manage Settings > Custom Attributes**. Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements. For more information on custom attribute arrays and their behavior, see our documentation on [Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays).

{% subtabs global %}
{% subtab JAVA %}

```java
// Setting a custom attribute with an array value
Braze.getInstance(context).getCurrentUser().setCustomAttributeArray("your_attribute_key", testSetArray);
// Adding to a custom attribute with an array value
Braze.getInstance(context).getCurrentUser().addToCustomAttributeArray("your_attribute_key", "value_to_add");
// Removing a value from an array type custom attribute
Braze.getInstance(context).getCurrentUser().removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Setting a custom attribute with an array value
Braze.getInstance(context).currentUser?.setCustomAttributeArray("your_attribute_key", testSetArray)
// Adding to a custom attribute with an array value
Braze.getInstance(context).currentUser?.addToCustomAttributeArray("your_attribute_key", "value_to_add")
// Removing a value from an array type custom attribute
Braze.getInstance(context).currentUser?.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Unsetting a custom attribute

Custom attributes can also be unset using the following method:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().unsetCustomUserAttribute("your_attribute_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.unsetCustomUserAttribute("your_attribute_key")
```

{% endtab %}
{% endtabs %}

#### Custom attribute via the REST API

You can also use our REST API to set user attributes. To do so, refer to the [User API documentation][4].

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both of these functions take the enum type `NotificationSubscriptionType` as arguments. This type has three different states:

| Subscription status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Subscribed, and explicitly opted in |
| `SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
No explicit opt-in is required by Android to send users push notifications. When a user is registered for push, they are set to `SUBSCRIBED` rather than `OPTED_IN` by default. Refer to [managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) for more information on implementing subscriptions and explicit opt-ins.
{% endalert %}

### Setting email subscriptions

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Setting push notification subscription

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
