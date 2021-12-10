---
nav_title: Setting Custom Attributes
article_title: Setting Custom Attributes for Unity
platform:
  - Unity
  - iOS
  - Android
page_order: 2
description: "This reference article covers how to set custom attributes on Unity platform."
---

# Setting custom attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events vs. custom attributes vs. purchase events in our [Best Practices section][1].

## Assigning default user attributes

To assign user attributes, you need to call the appropriate method on the BrazeBinding object. The following is a list of built-in attributes that can be called using this method.

### First name
`AppboyBinding.SetUserFirstName("first name");`

### Last name
`AppboyBinding.SetUserLastName("last name");`

### User email
`AppboyBinding.SetUserEmail("email@email.com");`

> It's still valuable to set email addresses even if you're not sending emails through Braze. Email makes it easier to search for individual user profiles and troubleshoot issues as they arise.

### Gender
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### Birth date
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### User country
`AppboyBinding.SetUserCountry("country name");`

### User home city
`AppboyBinding.SetUserHomeCity("city name");`

### User email subscription
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### User push subscription
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### User phone number
`AppboyBinding.SetUserPhoneNumber("phone number");`

## Assigning custom user attributes

Beyond the attributes above, Braze also allows you to define custom attributes using a number of different data types: For more information regarding the segmentation options each of these attributes will afford you see our ["Best Practices" documentation][1] within this section.

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

> Dates passed to Braze must either be in the [ISO 8601][2] format, e.g `2013-07-16T19:20:30+01:00` or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format e.g `2016-12-14T13:32:31.601-0800`

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
You can also use our REST API to set user attributes. To do so refer to the [user API documentation][3].

## Custom attribute value limits
Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

## Setting up user subscriptions

To set up a subscription for your users (either email or push), call the functions     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` or `AppboyBinding.SetPushNotificationSubscriptionType()`, respectively. Both of these functions take the parameters `Appboy.Models.AppboyNotificationSubscriptionType` as arguments. This type has three different states:

| Subscription Status | Definition                               |
| ------------------- | ---------------------------------------- |
| `OPTED_IN`          | Subscribed, and explicitly opted in      |
| `SUBSCRIBED`        | Subscribed, but not explicitly opted in  |
| `UNSUBSCRIBED`      | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2}

> No explicit opt-in is required by Windows to send users push notifications. When a user is registered for push, they are set to `SUBSCRIBED` rather than `OPTED_IN` by default. To learn more, check out our documentation on [implementing subscriptions and explicit opt-ins][10].

- `EmailNotificationSubscriptionType`
  - Users will be set to `SUBSCRIBED` automatically upon receipt of a valid email address. However, we suggest that you establish an explicit opt-in process and set this value to `OPTED_IN` upon receipt of explicit consent from your user. Visit our [Changing User Subscriptions][8] doc for more details.
- `PushNotificationSubscriptionType`
  - Users will be set to `SUBSCRIBED` automatically upon valid push registration. However, we suggest that you establish an explicit opt-in process and set this value to `OPTED_IN` upon receipt of explicit consent from your user. Visit our [Changing User Subscriptions][8] doc for more details.

> These types fall under `Appboy.Models.AppboyNotificationSubscriptionType`.

## Sample code

### Email subscription:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Push notification subscription:

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
