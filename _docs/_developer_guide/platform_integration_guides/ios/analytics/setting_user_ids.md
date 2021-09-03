---
nav_title: Setting User IDs
article_title: Setting User IDs for iOS
platform: iOS
page_order: 1
description: "This article shows how to set user IDs in your iOS app, suggested user ID naming conventions, and some best practices."
 
---

# Setting User IDs

{% include archive/setting_user_ids/setting_user_ids.md %}

## Suggested User ID Naming Convention

{% include archive/setting_user_ids/naming_convention.md %}

## Assigning a User ID

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user id:

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
Be sure to call this method in your application's main thread. Calling the method asynchronously can lead to undefined behavior.
{% endalert %}

>  __Do not call `changeUser()` when a user logs out. `changeUser()` should only be called when the user logs into the application.__ Setting `changeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.
Additionally, we recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with reengagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

**Additional Information**

- See the method declaration within the [`Appboy.h` file][4]. - In addition, you can refer to the [`changeUser` class documentation][5] for more information.

## User ID Integration Best Practices & Notes

{% include archive/setting_user_ids/best_practices.md %}

## Aliasing Users

{% include archive/aliasing.md platform="iOS" %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69 "changeuser"
