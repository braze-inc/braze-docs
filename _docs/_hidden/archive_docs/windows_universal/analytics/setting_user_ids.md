---
nav_title: Setting user IDs
article_title: Setting User IDs for Windows Universal
platform: Windows Universal
page_order: 1
description: "This reference article covers how to set user ids on the Windows Universal platform."
hidden: true
---

# Setting user IDs
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) to set the user ID:

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**Do not call `changeUser()` when a user logs out. `changeUser()` should only be called when the user logs into the application.** Setting `changeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.
{% endalert %}

Additionally, we recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with re-engagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

## Suggested user ID naming convention

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## User ID integration best practices and notes

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

