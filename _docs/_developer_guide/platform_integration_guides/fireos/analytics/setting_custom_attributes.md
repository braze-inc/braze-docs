---
nav_title: Setting Custom Attributes
platform: FireOS
page_order: 3
search_rank: 4
---
## Setting Custom Attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by Custom Events vs. Custom Attributes vs Purchase Events in our [Analytics Overview][7].

### Assigning Standard User Attributes

To assign attributes to your users, call the `getCurrentUser()` method on your Braze instance to get a reference to the current user of your app. Once you have a reference to the current user, you can call methods to set predefined or custom attributes.

Braze provides predefined methods for setting the following user attributes within the [AppboyUser class][2]. See the [JavaDocs for method specifications][2]:

- First Name
- Last Name
- Country
- Language
- Date of Birth
- Email
- Avatar Image URLs for Braze User Profiles
- Gender
- Home City
- Phone Number
- Facebook Data
- Twitter Data

All string values such as first name, last name, country, and home city are limited to 255 characters. Avatar Image URLs are limited to 1024 characters.

__We strongly recommend collecting email addresses__ even if you're not sending emails through Braze. Email makes it easier to search for individual user profiles and troubleshoot issues as they arise.

**Implementation Example**
This is what setting a first name would look like in code:

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setFirstName("SomeFirstName");
```

See [`UserProfileDialog.java`][1] in the Droidboy sample app.

### Assigning Custom User Attributes

In addition to our predefined user attribute methods, Braze also provides custom attributes to track data from your applications. Braze Custom Attributes can be set with the following data types:

- Strings
- Arrays
  - Includes methods to set arrays, add items to existing arrays, and delete items from existing arrays.
- Integers
- Booleans
- Dates
- Longs
- Floats

Full method specifications for custom attributes can be found here within the [AppboyUser class within the Javadocs][2].

#### Setting a Custom Attribute with a String Value

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### Setting a Custom Attribute with an Integer Value

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
// Integer attributes may also be incremented using code like the following:
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### Setting a Custom Attribute with a Boolean Value

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_BOOLEAN_VALUE
);
```

#### Setting a Custom Attribute with a Long Value

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_LONG_VALUE
);
```

#### Setting a Custom Attribute with a Float Value

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_FLOAT_VALUE
);
```

#### Setting a Custom Attribute with a Date Value

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);
// This method will assign the current time to a custom attribute at the time the method is called:
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttributeToNow(
  YOUR_ATTRIBUTE_KEY_STRING
);
// This method will assign the date specified by secondsFromEpoch to a custom attribute:
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttributeToSecondsFromEpoch(
  YOUR_ATTRIBUTE_KEY_STRING,
  long secondsFromEpoch
);
);
```
>  Dates passed to Braze with this method must either be in the [ISO 8601][3] format, e.g `2013-07-16T19:20:30+01:00` or in the `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format e.g `2016-12-14T13:32:31.601-0800`

#### Setting a Custom Attribute with an Array Value
The maximum number of elements in Custom Attribute Arrays defaults to 25. The maximum for individual arrays can be increased to up to 100 in the Braze Dashboard, under "Manage App Group -> Custom Attributes". Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements. For more information on Custom Attribute Arrays and their behavior, see our [Documentation on Arrays][6].

```java
// Setting a custom attribute with an array value
appboyUser.setCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
appboyUser.addToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
appboyUser.removeFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```

#### Unsetting a Custom Attribute

Custom Attributes can also be unset using the following method:

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().unsetCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING
);
```

#### Setting a Custom Attribute via the REST API

You can also use our REST API to set user attributes. To do so refer to the [User API documentation][4].

#### Custom Attribute Length

Custom attribute keys and values have a maximum length of 255 characters.  Longer strings will be truncated to 255 characters.

Full class information can be found in the [javadocs][2].

### Setting Up User Subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both of these functions take the enum type 'NotificationSubscriptionType' as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Subscribed, and explicitly opted in |
| `SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |

>  No explicit opt-in is required by Android to send users push notifications. When a user is registered for push, they are set to `SUBSCRIBED` rather than `OPTED_IN` by default. For more information on implementing subscriptions and explicit opt-ins, visit the topic on [Braze Docs][10].

#### Sample Code

##### Setting Email Subscriptions

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setEmailNotificationSubscriptionType(
  "NotificationSubscriptionType"
);
```

##### Setting Push Notification Subscription

```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setPushNotificationSubscriptionType(
  "NotificationSubscriptionType"
);
```

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/UserProfileDialog.java
[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/AppboyUser.html "Javadocs"
[3]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-data
[6]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
