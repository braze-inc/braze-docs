---
nav_title: Set user IDs
article_title: Set User IDs for iOS
platform: iOS
page_order: 1
description: "This reference article shows how to set user IDs in your iOS app, suggested user ID naming conventions, and some best practices."
 
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Set user IDs for iOS

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Suggested user ID naming convention

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Assigning a user ID

You should make the following call as soon as the user is identified (generally after logging in) to set the user ID:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.changeUser("YOUR_USER_ID")
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**Do not call `changeUser()` when a user logs out. `changeUser()` should only be called when the user logs into the application.** Setting [`changeUser()`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69%20%22changeuser%22) to a static default value will associate ALL user activity with that default "user" until the user logs in again.
{% endalert %}

Be sure to call this method in your application's main thread. Calling the method asynchronously can lead to undefined behavior.

Additionally, we recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with re-engagement campaigns. If you anticipate multiple users on the same device but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

## User ID integration best practices and notes

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing users

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="iOS" %}

