{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Default user attributes

### Predefined methods

Braze provides predefined methods for setting the following user attributes using the `BrazeBinding` object. For more information, see [Braze Unity declaration file](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- First name
- Last name
- User email
- Gender
- Birth date
- User country
- User home city
- User email subscription
- User push subscription
- User phone number

### Setting default attributes

To set a default attribute, call the relevant method on the `BrazeBinding` object.

{% tabs local %}
{% tab First name %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Last name %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab Email %}
```csharp
BrazeBinding.SetUserEmail("email@email.com");
```
{% endtab %}
{% tab Gender %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Birth date %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Country %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Home city %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Email subscription %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Push subscription %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Phone number %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Unsetting default attributes

To unset a default user attribute, pass `null` to the relevant method.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute's segmentation option, see [User data collection]({{site.baseurl}}/developer_guide/analytics).

### Setting custom attributes

To set a custom attribute, use the corresponding method for the attribute type: 

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Integer %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Boolean %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Dates passed to Braze must either be in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (such as `2013-07-16T19:20:30+01:00`) or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format (such as`2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}

{% tab Array %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
Custom attribute values have a maximum length of 255 characters; longer values will be truncated.
{% endalert %}

### Unsetting custom attributes

To unset a custom attribute, pass the relevant attribute key to the `UnsetCustomUserAttribute` method. 

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Using the REST API

You can also use our REST API to set or unset user attributes. For more information, refer to [User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Setting user subscriptions

To set up an email or push subscription for your users, call one of the following functions.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Both functions take `Appboy.Models.AppboyNotificationSubscriptionType` as arguments, which has three different states:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OPTED_IN` | Subscribed, and explicitly opted in |
| `SUBSCRIBED` | Subscribed, but not explicitly opted in |
| `UNSUBSCRIBED` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
No explicit opt-in is required by Windows to send users push notifications. When a user is registered for push, they are set to `SUBSCRIBED` rather than `OPTED_IN` by default. To learn more, check out our documentation on [implementing subscriptions and explicit opt-ins]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Subscription Type                        | Description |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Users will be set to `SUBSCRIBED` automatically upon receipt of a valid email address. However, we suggest that you establish an explicit opt-in process and set this value to `OPTED_IN` upon receipt of explicit consent from your user. Visit our [Changing User Subscriptions]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) doc for more details. |
| `PushNotificationSubscriptionType`       | Users will be set to `SUBSCRIBED` automatically upon valid push registration. However, we suggest that you establish an explicit opt-in process and set this value to `OPTED_IN` upon receipt of explicit consent from your user. Visit our [Changing User Subscriptions]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) doc for more details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
These types fall under `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Setting email subscriptions

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Setting push notification subscriptions

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
