{% multi_lang_include developer_guide/prerequisites/web.md %}

## Default user attributes

To set a default attribute for a user, call the `getCurrentUser()` method on your Braze instance to get a reference to the current user of your app. Then you can call methods to set a user attribute.

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endtab %}
{% endtabs %}

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

## Custom user attributes

In addition to the default user attribute methods, you can also set [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) for your users. Full method specifications, see [our JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% tabs local %}
{% tab String %}
To set a custom attribute with a `string` value:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endtab %}
{% tab Integer %}
To set a custom attribute with a `integer` value:

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

{% endtab %}
{% tab Date %}
To set a custom attribute with a `date` value:

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

{% endtab %}
{% tab Array %}

You can have up to 25 elements in custom attribute arrays. Individual arrays that are manually set (not automatically detected) for **Data Type** can be increased up to 100 in the Braze dashboard under **Data Settings** > **Custom Attributes**. If you want this maximum increased, contact your Braze account manager.

[Arrays]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) exceeding the maximum number of elements will be truncated to contain the maximum number of elements.

To set a custom attribute with an `array` value:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Dates passed to Braze with this method must be JavaScript Date objects.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Custom attribute keys and values can only have a maximum of 255 characters. For more information about valid custom attribute values, refer to the [reference documentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}

### Unsetting a custom attribute

Custom attributes can be unset by setting their value to `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Setting user subscriptions

To set up a subscription for your users (either email or push), call the functions `setEmailNotificationSubscriptionType()`  or `setPushNotificationSubscriptionType()`, respectively. Both functions take the `enum` type `braze.User.NotificationSubscriptionTypes` as arguments. This type has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Subscribed, and explicitly opted in |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

When a user is registered for push, the browser forces them to choose to allow or block notifications, and if they choose to allow push, they are set `OPTED_IN` by default. 

Visit [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) for more information on implementing subscriptions and explicit opt-ins.

### Unsubscribing a user from email

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Unsubscribing a user from push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
