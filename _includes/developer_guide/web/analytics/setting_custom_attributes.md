## Referencing the current user

In order to assign attributes to your users, you'll need to get a reference to the current user of your app. To get a reference, call the `braze.getUser()` method. After you have a reference to the current user, you can call methods to set predefined or custom attributes.

## Assigning predefined user attributes

Braze provides predefined methods for setting the following user attributes within the [`User` class](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html):

- First Name
- Last Name
- Language
- Country
- Date of Birth
- Email
- Gender
- Home City
- Phone Number

### Implementation examples

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

In addition to our predefined user attribute methods, Braze also provides [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) to track data from your applications. 

Full method specifications for custom attributes can be found here within the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

### Custom attribute length

Custom attribute keys and values can have up to 255 characters. Refer to the [full technical documentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) for details about valid custom attribute values.

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

{% alert important %}
Dates passed to Braze with this method must be JavaScript Date objects.
{% endalert }

#### Setting a custom attribute with an array value

You can have up to 25 elements in custom attribute arrays. Individual arrays that are manually set (not automatically detected) for **Data Type** can be increased up to 100 in the Braze dashboard under **Data Settings** > **Custom Attributes**. If you want this maximum increased, contact your Braze account manager.

[Arrays]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) exceeding the maximum number of elements will be truncated to contain the maximum number of elements.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### Unsetting a custom attribute

Custom attributes can be unset by setting their value to `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both functions take the `enum` type `braze.User.NotificationSubscriptionTypes` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Subscribed, and explicitly opted in |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

When a user is registered for push, the browser forces them to choose to allow or block notifications, and if they choose to allow push, they are set `OPTED_IN` by default. 

Visit [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) for more information on implementing subscriptions and explicit opt-ins.

### Example code

#### Unsubscribing a user from email

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### Unsubscribing a user from push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
