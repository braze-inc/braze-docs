{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Default user attributes

To set user attributes, you need to call the appropriate method on the `BrazeBinding` object. The following is a list of built-in attributes that can be called using this method.

| Attribute                 | Code Sample |
|---------------------------|-------------|
| First name                | `AppboyBinding.SetUserFirstName("first name");` |
| Last name                 | `AppboyBinding.SetUserLastName("last name");` |
| User email                | `AppboyBinding.SetUserEmail("email@email.com");` |
| Gender                    | `AppboyBinding.SetUserGender(Appboy.Models.Gender);` |
| Birth date                | `AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");` |
| User country              | `AppboyBinding.SetUserCountry("country name");` |
| User home city            | `AppboyBinding.SetUserHomeCity("city name");` |
| User email subscription   | `AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| User push subscription    | `AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| User phone number         | `AppboyBinding.SetUserPhoneNumber("phone number");` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Custom user attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute's segmentation option, see [User data collection]({{site.baseurl}}/developer_guide/analytics).

### Setting custom attributes

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

To unset a custom user attribute, use the following method:

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
