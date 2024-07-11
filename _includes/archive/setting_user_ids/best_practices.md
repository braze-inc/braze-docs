### Automatic preservation of anonymous user history

| Identification Context | Preservation Behavior |
| ---------------------- | -------------------------- |
| User **has not** been previously identified | Anonymous history **is merged** with user profile upon identification. |
| User **has been** previously identified in-app or via API | Anonymous history **is not merged** with user profile upon identification. |
{: .reset-td-br-1 .reset-td-br-2}

Refer to [Identified user profiles]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) for more information on what occurs when you identify anonymous users.

### Additional notes and best practices

Note the following:

- If your app is used by multiple people, you can assign each user a unique identifier to track them.
- After a user ID has been set, you cannot revert that user to an anonymous profile.
- Do not change the user ID when a user logs out as this can separate the device from the user profile.
  - As a result, you won't be able to target the previously logged out user with re-engagement messages. If you anticipate multiple users on the same device, but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process. By default, only the last user that was logged in will receive push notifications from your app.
- Switching from one identified user to another is a relatively costly operation.
  - When you request the user switch, the current session for the previous user is automatically closed and a new session is started. Braze will automatically make a data refresh request for in-app messages and other Braze resources for the new user.

{% alert tip %}
If you opt to use a hash of a unique identifier as your user ID, be sure that you're normalizing the input to your hashing function. For example, if you're going to use a hash of an email address, confirm that you're stripping leading and trailing whitespace from the input, and taking localization into account.
{% endalert %}