---
nav_title: Setting user IDs
article_title: Setting user IDs through the Braze SDK
page_order: 1.1
description: "Learn how to set user IDs through the Braze SDK."

---

# Setting user IDs

> Learn how to set user IDs through the Braze SDK. These are unique identifiers that let you track users across devices and platforms, import their data through the [user data API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data), and send targeted messages through the [messaging API]({{site.baseurl}}/api/endpoints/messaging/). If you don't assign a unique ID to a user, Braze will assign them an anonymous ID instead&#8212;however, you won't be able to use these features until you do.

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android or Swift method instead.
{% endalert %}

## About anonymous users

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## Setting a user ID

To set a user ID, call the `changeUser()` method after the user initially log ins. IDs should be unique and follow our [naming best practices](#naming-best-practices).

If you're hashing a unique identifier instead, be sure to normalize the input of your hashing function. For example, when hashing an email address, remove any leading or trailing spaces and account for localization.

{% tabs local %}
{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab WEB %}
For a standard Web SDK implementation, you can use the following method:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

If you'd like to use Google Tag Manager instead, you can use the **Change User** tag type to call the [`changeUser` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Use it whenever a user logs in or is otherwise identified with their unique `external_id` identifier.

Be sure to enter the current user's unique ID in the **External User ID** field, typically populated using a data layer variable sent by your website.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type" and "external user ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab UNREAL ENGINE %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**Do not assign a static default ID or call `changeUser()` when a user logs out.** Doing so will prevent you from re-engaging any previously logged-in users on shared devices. Instead, keep track of all user IDs separately and ensure your app's logout process allows for switching back to a previously logged-in user. When a new session starts, Braze will automatically refresh the data for the newly-active profile.
{% endalert %}

## User aliases

### How they work

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Setting a user alias

A user alias consists of two parts: a name and a label. The name refers to the identifier itself, while the label refers to the type of identifier it belongs to. For example, if you have a user in a third-party customer support platform with the external ID `987654`, you can assign them an alias in Braze with the name `987654` and the label `support_id`, so you can track them across platforms.

{% tabs local %}
{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## ID Naming best practices {#naming-best-practices}

We recommend that you create user IDs using the [Universally Unique Identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier) standard, meaning they are 128-bit strings that are random and well distributed.

Alternatively, you can hash an existing unique identifier (such as a name or email address) to generate your user IDs instead. If you do so, be sure to implement [SDK authentication]({{site.baseurl}}/developer_guide/authentication/), so you can prevent user impersonation.

While it's essential that you correctly name your user IDs from the start, you can always rename them in the future using the [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) endpoint.

| Recommended | Not Recommended |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Avoid sharing details about how you create user IDs, as this may expose your organization to malicious attacks or data removal.
{% endalert %}
