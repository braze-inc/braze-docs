---
nav_title: Setting Custom Attributes
article_title: Setting Custom Attributes for Web
platform: Web
page_order: 3
description: "This reference article covers how to set custom attributes via the Braze Web SDK."

---

# Settings custom attributes for web

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices][7].

To assign attributes to your users, call the `braze.getUser()` method to get a reference to the current user of your app. Once you have a reference to the current user, you can call methods to set predefined or custom attributes.

## Assigning predefined user attributes

Braze provides predefined methods for setting the following user attributes within the [`User` class][1]:

- First Name
- Last Name
- Biographical Strings
- Country
- Date of Birth
- Email
- Gender
- Home City
- Phone Number

### Implementation examples

{% include archive/web-v4-rename.md %}

#### Setting a first name

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### Setting a gender

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### Setting a date of birth

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## Assigning custom user attributes

In addition to our predefined user attribute methods, Braze also provides custom attributes to track data from your applications. Braze custom attributes can be set with the following data types:

- Strings
- Arrays
  - Includes methods to set arrays, add items to existing arrays, and delete items from existing arrays.
- Integers
- Booleans
- Dates
- Longs
- Floats

Full method specifications for custom attributes can be found here within the [JSDocs][1].

### Custom attribute length

Custom attribute keys and values have a maximum length of 255 characters. Refer to the [full technical documentation][1] for details about valid custom attribute values.

### Implementation examples

#### Setting a custom attribute with a string value
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### Setting a custom attribute with an integer value
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### Setting a custom attribute with a date value
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```
>  Dates passed to Braze with this method must be JavaScript Date objects.

#### Setting a custom attribute with an array value

The maximum number of elements in custom attribute arrays defaults to 25. The maximum for individual arrays can be increased to up to 100. If you would like this maximum increased, reach out to your Customer Service Manager. [Arrays][6] exceeding the maximum number of elements will be truncated to contain the maximum number of elements.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray("custom_attribute_array_test", "value to be removed");
```

### Unsetting a custom attribute

Custom attributes can be unset by setting their value to `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. Refer to the [users API][4] documentation for details.

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both of these functions take the enum type `braze.User.NotificationSubscriptionTypes` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Subscribed, and explicitly opted in |
| `SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2}

When a user is registered for push, the browser forces them to choose to allow or block notifications, and if they choose to allow push, they are set `OPTED_IN` by default. 

Visit [Managing user subscriptions][10] for more information on implementing subscriptions and explicit opt-ins.

### Sample code

#### Unsubscribing a user from email:
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### Unsubscribing a user from push:
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

[1]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
