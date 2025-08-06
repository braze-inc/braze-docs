{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes using the `m.Braze` object.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Setting default attributes

To set a default attribute, call the relevant method on the `m.Braze` object.

{% tabs local %}
{% tab First name %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Last name %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab Email %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Gender %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Birth date %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab Country %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Language %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Home city %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Phone number %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types.

### Settings custom attributes

{% tabs %}
{% tab String %}
To set a custom attribute a `string` value:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Integer %}
To set a custom attribute with an `integer` value:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Floating-points %}
Braze treats `float` and `double` values exactly the same. To set a custom attribute with either value:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Boolean %}
To set a custom attribute with a `boolean` value:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Date %}
To set a custom attribute with a `date` value:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Array %}
To set a custom attribute with an `array` value:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Custom attribute values have a maximum length of 255 characters; longer values will be truncated.
{% endalert %}

### Incrementing and decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer value.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `unsetCustomAttribute` method.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Setting email subscriptions

You can set the following email subscription statuses for your users programmatically through the SDK.

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Subscribed, and explicitly opted in |
| `Subscribed` | Subscribed, but not explicitly opted in |
| `UnSubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
These types fall under `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

The method for setting email subscription status is `setEmailSubscriptionState()`. Users will be set to `Subscribed` automatically upon receipt of a valid email address, however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user. For more details, visit [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
