## Assigning default user attributes

To assign user attributes, you need to call the appropriate method on the BrazeBinding object. The following is a list of built-in attributes that can be called using this method.

### First name

```csharp
AppboyBinding.SetUserFirstName("first name");
```

### Last name

```csharp
AppboyBinding.SetUserLastName("last name");
```

### User email

```csharp
AppboyBinding.SetUserEmail("email@email.com");
```

{% alert tip %}
It's still valuable to set email addresses even if you're not sending emails through Braze. Email makes it easier to search for individual user profiles and troubleshoot issues as they arise.
{% endalert %}

### Gender

```csharp
AppboyBinding.SetUserGender(Appboy.Models.Gender);
```

### Birth date

```csharp
AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```

### User country

```csharp
AppboyBinding.SetUserCountry("country name");
```

### User home city

```csharp
AppboyBinding.SetUserHomeCity("city name");
```

### User email subscription

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```

### User push subscription

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```

### User phone number
```csharp
AppboyBinding.SetUserPhoneNumber("phone number");
```

## Assigning custom user attributes

Beyond the default user attributes, Braze also allows you to define custom attributes using a number of different data types:
For more information regarding the segmentation options each of these attributes will afford you see our ["Best Practices" documentation]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) within this section.

### Setting custom attribute values

{% tabs %}
{% tab Boolean Value %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
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

### Unsetting a custom attribute

Custom attributes can also be unset using the following method:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. To do so refer to the [user API documentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Custom attribute value limits

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions `AppboyBinding.SetUserEmailNotificationSubscriptionType()` or `AppboyBinding.SetPushNotificationSubscriptionType()`, respectively. Both of these functions take the parameters `Appboy.Models.AppboyNotificationSubscriptionType` as arguments. This type has three different states:

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

## Example code

### Email subscription:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Push notification subscription:

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
