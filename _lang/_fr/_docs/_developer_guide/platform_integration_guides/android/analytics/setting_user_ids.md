---
nav_title: Setting User IDs
article_title: Setting User IDs for Android/FireOS
platform:
  - Android
  - FireOS
page_order: 1
description: "This article shows how to set user IDs in your Android app, suggested user ID naming conventions, and some best practices."
---
 
# Setting user IDs for Android/FireOS

{% include archive/setting_user_ids/setting_user_ids.md %}

## Suggested user ID naming convention

{% include archive/setting_user_ids/naming_convention.md %}

### Assigning a user ID

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user id:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
__Do not call `changeUser()` when a user logs out. `changeUser()` should only be called when the user logs into the application.__ Setting `changeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.
{% endalert %}

Additionally, we recommend __against__ changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with reengagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

Refer to the [changeUser documentation][4] for more information.

**Implementation Example**

Full class information can be found in the [javadocs][4].

## User ID integration best practices and notes

{% include archive/setting_user_ids/best_practices.md %}

## Aliasing users

An alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID:

* Set a consistent identifier for analytics that will follow a given user both before and after they have logged in to a mobile app or website.
* Add the identifiers used by a third-party vendor to your Braze users in order to more easily reconcile your data externally.

Each alias consists of two parts: a _name_ for the identifier itself, and a _label_ indicating the type of alias. Users can have multiple aliases with _different_ labels, but only one name per label.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```

{% endtab %}
{% endtabs %}

[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-
[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-
