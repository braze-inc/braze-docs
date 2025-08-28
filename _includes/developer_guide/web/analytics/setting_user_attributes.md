{% multi_lang_include developer_guide/prerequisites/web.md %}

## Default user attributes

### Predefined methods

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

### Setting default attributes

{% tabs %}
{% tab using methods %}
To set a default attribute for a user, call the `getUser()` method on your Braze instance to get a reference to the current user of your app. Then you can call methods to set a user attribute.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab google tag manager %}
Using Google Tag Manager, standard user attributes (such as a user's first name), should be logged in the same manner as custom user attributes. Ensure the values you're passing in for standard attributes match the expected format specified in the [User class](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) documentation.

For example, the gender attribute can accept any of the following as values: `"m" | "f" | "o" | "u" | "n" | "p"`. Therefore to set a user's gender as female, create a Custom HTML tag with the following content:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Unsetting default attributes

To unset a default user attribute, pass `null` to the related method. For example:

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Custom user attributes

### Setting custom attributes

{% tabs %}
{% tab using methods %}
In addition to the default user attribute methods, you can also set [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) for your users. Full method specifications, see [our JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
To set a custom attribute with a `string` value:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
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

{% endsubtab %}
{% subtab Date %}
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

{% endsubtab %}
{% subtab Array %}

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
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Custom attribute keys and values can only have a maximum of 255 characters. For more information about valid custom attribute values, refer to the [reference documentation](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab google tag manager %}
Custom user attributes are not available due to a limitation in Google Tag Manager's scripting language. To log custom attributes, create a Custom HTML tag with the following content:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
The GTM template does not support nested properties on events or purchases. You can use the preceding HTML to log any events or purchases that require nested properties.
{% endalert %}
{% endtab %}
{% endtabs %}

### Unsetting custom attributes

To unset a custom attribute, pass `null` to the related method.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Nesting custom attributes

You can also nest properties within custom attributes. In the following example, a `favorite_book` object with nested properties is set as a custom attribute on the user profile. For more details, refer to [Nested Custom Attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
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
