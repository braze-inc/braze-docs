---
nav_title: Setting Custom Attributes
platform: Roku
page_order: 4
---
## Setting Custom Attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by Custom Events vs. User Attributes vs Purchase Events in our [Best Practices section][7].

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

>  It's still valuable to set `email` addresses even if you're not sending emails through Braze. Email makes it easier to search for individual user profiles and troubleshoot issues as they arise.

**Example Implementation**

```
m.Braze.setFirstName("User's First Name")
```

### Assigning Custom User Attributes

Beyond the default attributes above, Braze also allows you to define Custom Attributes using a number of different data types.
For more information regarding the segmentation options each of these attributes will afford you see our ["Best Practices" documentation][1] within this section.

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

Custom Attributes can also be unset using the following method:

```
m.Braze.unsetCustomAttribute("attributeName")
```

#### Setting a Custom Atttribute via the REST API

You can also use our REST API to set user attributes. To do so refer to the [user API documentation][4].

#### Custom Attribute Value Limits

Custom attribute values have a maximum length of 255 characters.

### Managing Notification Subscription Statuses

To set up a subscription for your users (either email or push), you can set the subscription statuses below. Subscription statuses in Braze have three different states for both Email and Push:

| Subscription Status | Definition |
| ------------------- | ---------- |
| `OptedIn` | Subscribed, and explicitly opted in |
| `Subscribed` | Subscribed, but not explicitly opted in |
| `UnSubscribed` | Unsubscribed and/or explicitly opted out |

- `EmailNotificationSubscriptionType`
  - Users will be set to `Subscribed` automatically upon receipt of a valid email address, however we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon reciept of explicit consent from your user. [See Braze Academy for details][10].
- `PushNotificationSubscriptionType`
  - Users will be set to `Subscribed` automatically upon valid push registration, however we suggest that you establish an explicit opt-in process and set this value to `OptedIn` upon reciept of explicit consent from your user. [See Braze Academy for details][10].

>  These types fall under `BrazeConstants().SUBSCRIPTION_STATES`

Example usage:
```
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
m.Braze.setPushNotificationSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/roku/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[4]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-data
[7]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
