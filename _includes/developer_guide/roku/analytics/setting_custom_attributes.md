## Assigning default user attributes

User attributes will be assigned to the currently active user. The following default fields may be set:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**Implementation Example**<br>This is what setting a first name would look like in code:

```brightscript
m.Braze.setFirstName("User's First Name")
```

## Assigning custom user attributes

Beyond the default user attributes, Braze also allows you to define custom attributes using several different data types.

### Settings custom attribute values
{% tabs %}
{% tab Boolean %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab Integer %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab Float or Double %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze treats FLOAT and DOUBLE values exactly the same within our database.
{% endtab %}
{% tab String %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab Date %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab Array %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### Incrementing/decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer value.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Unsetting a custom attribute

Custom attributes can also be unset using the following method:

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

### Custom attribute value limits

Custom attribute values have a maximum length of 255 characters.

## Managing email subscription status

You can set the following email subscription statuses for your users programmatically through the SDK.

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Subscribed, and explicitly opted in |
| `Subscribed` | Subscribed, but not explicitly opted in |
| `UnSubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  These types fall under `BrazeConstants().SUBSCRIPTION_STATES`

The method for setting email subscription status is `setEmailSubscriptionState()`. Users will be set to `Subscribed` automatically upon receipt of a valid email address, however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user. For more details, visit [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

Example usage:
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

