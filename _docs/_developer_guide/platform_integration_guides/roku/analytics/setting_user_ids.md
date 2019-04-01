---
nav_title: Setting User IDs
platform: Roku
page_order: 0
---
## Setting User IDs

User IDs should be set for each of your users. These should never change per user and be readily accessible when a user opens the app. A database ID or a hashed email address/username is usually a good reference to use. We __strongly recommend__ providing this identifier as it will allow you to:

- Track your users across devices and platforms, improving the quality of your behavioral and demographic data.
- Import data about your users using the [User Data API][1].
- Target specific users with the [Messaging API][2] for both general and transactional messages.

>  If such an identifier is not available, Braze will assign a unique identifier to your users, but you will lack the capabilities above. You should avoid setting User IDs for users who lack a unique identifier that is tied to them as an individual. Passing a device identifier offers no benefit versus the automatic anonymous user tracking Braze offers by default.

>  These User IDs should be private and not easily obtained (e.g. not a plain email address or username).

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user ID:

```
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

### User ID Integration Best Practices & Notes

#### Automatic Preservation of Anonymous User History

| Identification Context | Preservation Behavior |
| ---------------------- | -------------------------- |
| User __has not__ been previously identified | Anonymous history __is merged__ with user profile upon identification |
| User __has been__ previously identified in-app or via API | Anonymous history __is not merged__ with user profile upon identification |

#### Additional Notes and Best Practices

Please note the following:

- __If your app is used by multiple people, you can assign each user a unique identifier to track them.__
- __Once a user ID has been set, you cannot revert that user to an anonymous profile.__
- __Do Not change the user ID upon a user "log out".__
  - Doing so separates the device from the user profile. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.
- __Switching from one identified user to another is a relatively costly operation.__
  - When you request the user switch, the current session for the previous user is automatically closed and a new session is started.

> If you opt to use a hash of a unique identifier as your user ID take care to ensure that you're normalizing the input to your hashing function. For example, if you're going to use a hash of an email address, ensure that you're stripping leading and trailing whitespace from the input, and taking localization into account.

[1]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-data
[2]: {{ site.baseurl }}/developer_guide/rest_api/messaging/
