---
nav_title: Setting User IDs
article_title: Setting User IDs
platform: Unity
page_order: 0
description: "This reference article covers how to set user ids on Unity platform."
 
---

# Setting User IDs

{% include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user id:

```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```

>  __Do not call `ChangeUser()` when a user logs out. `ChangeUser()` should only be called when the user logs into the application.__ Setting `ChangeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.

Additionally, we recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with reengagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

## Suggested User ID Naming Convention

{% include archive/setting_user_ids/naming_convention.md %}

## User ID Integration Best Practices & Notes

{% include archive/setting_user_ids/best_practices.md %}

> If you opt to use a hash of a unique identifier as your userID take care to ensure that you're normalizing the input to your hashing function. For example,if you're going to use a hash of an email address, ensure that you're stripping leading and trailing whitespace from the input, and taking [localization problems][6] into account.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[6]: http://developer.android.com/reference/java/util/Locale.html#default_locale "Android Developer Docs - Localization"
