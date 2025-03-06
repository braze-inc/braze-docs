## About user IDs for web

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) to set the user ID:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**Do not call `changeUser()` when a user logs out.** Setting `changeUser()` to a static default value will associate ALL user activity with that default "user" until the user logs in again.
{% endalert %}

We recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with re-engagement campaigns. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

Refer to the [`changeUser()` documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "Javadocs") for more information.

## Suggested user ID naming convention

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## User ID integration best practices and notes

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing users

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Web" %}

