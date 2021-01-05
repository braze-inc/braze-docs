---
nav_title: Setting Custom Attributes
platform: Roku
page_order: 4
---
## Setting Custom Attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by Custom events vs. User attributes vs Purchase events in our [Best Practices section][7]. You should also check out our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

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
- `AvatarImageUrl`

**Example Implementation**

```
m.Braze.setFirstName("User's First Name")
```

### Assigning Custom User Attributes

Beyond the default attributes above, Braze also allows you to define Custom attributes using several different data types.
For more information regarding the segmentation options, and how each of these attributes will affect you, see our ["Best Practices" documentation][1] within this section.

#### Custom Attribute with a Boolean Value
```
m.Braze.setCustomAttribute("boolAttribute", true)
```

#### Custom Attribute with an Integer Value
```
m.Braze.setCustomAttribute("intAttribute", 5)
```

#### Custom Attribute with a Float Value
```
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
>  Braze treats FLOAT and DOUBLE values exactly the same within our database.

#### Custom Attribute with a String Value
```
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```

#### Custom Attribute with a Date Value
```
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```

#### Setting a Custom Attribute with an Array Value

```
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```

#### Incrementing/Decrementing Custom Attributes

This code is an example of an incrementing custom attribute. You may increment the value of a custom attribute by any positive or negative integer value.

```
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

#### Unsetting a Custom Attribute

Custom atributes can also be unset using the following method:

```
m.Braze.unsetCustomAttribute("attributeName")
```

#### Setting a Custom Attribute via the REST API

You can also use our REST API to set user attributes. To do so refer to the [user API documentation][4].

#### Custom Attribute Value Limits

Custom attribute values have a maximum length of 255 characters.

### Managing Email Subscription Status

You can set the following email subscription statuses for your users programmatically through the SDK.

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Subscribed, and explicitly opted in |
| `Subscribed` | Subscribed, but not explicitly opted in |
| `UnSubscribed` | Unsubscribed and/or explicitly opted out |

>  These types fall under `BrazeConstants().SUBSCRIPTION_STATES`

The method for setting email subscription status is `setEmailSubscriptionState()`. Users will be set to `Subscribed` automatically upon receipt of a valid email address, however, we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon receipt of explicit consent from your user. Visit our [Managing User Subscriptions][10] doc for more details.

Example usage:
```
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
