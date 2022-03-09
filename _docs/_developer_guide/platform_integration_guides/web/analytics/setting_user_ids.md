---
nav_title: Setting User IDs
article_title: Setting User IDs for Web
platform: Web
page_order: 1

page_type: reference
description: "This article describes how to set user IDs for each of your users, including best practices and important points to consider before making any changes."
 
---

# Setting user IDs for web

{% include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) to set the user ID:

```javascript
appboy.changeUser(YOUR_USER_ID_STRING);
```

>  __Do not call `changeUser()` when a user logs out.__ Setting `changeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.<br><br>Additionally, we recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with reengagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

Refer to the [`changeUser()` documentation][4] for more information.

## Suggested user ID naming convention

{% include archive/setting_user_ids/naming_convention.md %}

## User ID integration best practices and notes

{% include archive/setting_user_ids/best_practices.md %}

## Aliasing users

{% include archive/setting_user_ids/aliasing.md platform="Web" %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.changeUser "Javadocs"
[5]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases
