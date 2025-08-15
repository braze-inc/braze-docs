---
nav_title: Setting custom attributes
article_title: Setting Custom Attributes for Windows Universal
platform: Windows Universal
page_order: 3
description: "This reference article covers how to set custom attributes on the Windows Universal platform."
hidden: true
---

# Setting custom attributes
{% multi_lang_include archive/windows_deprecation.md %}

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

User attributes can be assigned to the current `IAppboyUser`. To obtain a reference to the current `IAppboyUser`, call `Appboy.SharedInstance.AppboyUser`

## Assigning default user attributes

The following attributes should be defined as properties of the `IAppboyUser`:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Example Implementation**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Assigning custom user attributes

Beyond the default user attributes, Braze also allows you to define custom attributes using a number of different data types. For more information regarding the segmentation options, and how each of these attributes will affect you, see our [Best practices]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Setting custom attribute values

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double or Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze treats FLOAT and DOUBLE values exactly the same within our database.
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Dates passed to Braze must either be in the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format, e.g `2013-07-16T19:20:30+01:00` or in the `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format e.g `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Array %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Incrementing/decrementing custom attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer value.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Unsetting a custom attribute

Custom attributes can also be unset using the following method:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Setting a custom attribute via the REST API

You can also use our REST API to set user attributes. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

### Custom attribute value limits

Custom attribute values have a maximum length of 255 characters; longer values will be truncated.

## Managing notification subscription statuses

To set up a subscription for your users (either email or push), you can set following the subscription statuses as properties of the `IAppboyUser`. Subscription statuses in Braze have three different states for both email and push:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Subscribed, and explicitly opted in |
| `Subscribed` | Subscribed, but not explicitly opted in |
| `UnSubscribed` | Unsubscribed and/or explicitly opted out |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

- `EmailNotificationSubscriptionType`
  - Users will be set to `Subscribed` automatically upon receipt of a valid email address, however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user.
- `PushNotificationSubscriptionType`
  - Users will be set to `Subscribed` automatically upon valid push registration, however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user.

>  These types fall under `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Visit [Managing user subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) for more details.

