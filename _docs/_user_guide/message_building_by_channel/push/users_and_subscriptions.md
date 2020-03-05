---
nav_title: Subscription States
platform: Message_Building_and_Personalization
subplatform: Push
page_order: 10
---

# Push Subscription States

Push subscription states are filters that allow your users to control whether they receive messages or not. For your user to receive your messages through push, they must be `Subscribed` or `Opted-In`, as well as [Push Enabled](#push-enabled).

![opt-in][56]{: height="50%" width="50%"}


|Opt-in State|Description|
|---|---|
|Subscribed| Default status.|
|Opted-In| A user has explicitly allowed Braze will automatically move a user's opt-in state to “Opted-In”. |
|Unsubscribed| A user has explicitly disallowed push notifications.|
{: .reset-td-br-1 .reset-td-br-2}

Braze determines these states with __push tokens__, which can grant permission to send push notifications to your user - this is called ["Push Enabled"](#push-enabled).

Individual user profiles can be exported in the JSON format using the users/export/ endpoints using Braze’s Rest API. Braze will return a push tokens object, that contains push enablement information per device, as well as an additional `notifications_enabled` parameter that will signify if a user blocked notifications from displaying (the [previous Android SDK](#before-android-sdk) version does not have the `notifications_enabled` parameter).

{% alert note %}
  __Bounces__

  Occasionally, a push message will bounce (not be received by a user). This can happen because a user has either uninstalled the app, or because iOS or Android has changed the push token, as they have a right to do.
{% endalert %}

## Push Enabled

A user is "Push Enabled" or "Push Registered" if they have an *active push token* for an app in your app group.

On the User Engagement tab in the dashboard you will see: **Push Registered For** followed by an **App Name(s)** or followed by **No Apps**. There will be an entry for every device that belongs to the user.

![img][1]{: height="50%" width="50%"}

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive background push and can not display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.

If a push token is moved a different user on the same device, that first user will no longer be push registered.

![img2][2]{: height="50%" width="50%"}

# iOS & Android Details

{% tabs %}
  {% tab iOS %}
__iOS Push__

In iOS 12, Apple introduced Provisional Authorization, allowing brands the option to send quiet push notifications to their users' Notification Centers _before_ they officially, explicitly opt-in, giving you a chance to demonstrate the value of your messages early.

On devices running iOS 11 or below, your users _must explicitly opt-in to receive your push messages_. You must request whether the user would like to receive push from you.

If your app is provisionally authorized or the user allows push, you will receive a token and be able to send remote notifications to that user that appear in the foreground. If your user does not allow push notifications, you will still receive a token, but this token will only be able to send silent push which permits the app to carry out actions in the background (you must have "Remote Notifications" enabled in __Xcode__).

iOS users are considered "Push Enabled" only if they have allowed notifications in the foreground, either explicitly or provisionally.

  {% endtab %}
  {% tab Android %}
__Android Push__

You do not need to request permission to send push notifications to Android users. As the user has not explicitly requested to receive push, Braze will not automatically [update the user's opt-in state]({{ site.baseurl }}/developer_guide/rest_api/user_data/#braze-user-profile-fields). Upon a user’s first session on Android, Braze will automatically request for a new token and upon successfully receiving update the user’s push enabled state.

If the user disables push, Braze will mark them as foreground push disabled no longer attempt to send them push messages. The filter `Push Enabled` will result in `false` for this user. You may continue to send background (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

On Android, Braze will move a user to be __push disabled__ if:
- A user uninstalls the app from their device.
- Braze receives a bounce when sending to a specific token (sometimes caused by app updates, uninstalls, new push token version or format).
- Push registration fails to FCM (sometimes caused by poor network connections or a failure to connect to or on FCM to return a valid token).
- (For Android SDK v2.2.2+) The user blocks push notifications for the app within their device settings and subsequently log a session.

  {% endtab %}
{% endtabs %}

## Before Android SDK v2.2.2 {#before-android-sdk}

Here are some details you should know if you aren't using our most up to date Android SDK.
- The previous version of the Android SDK does not detect that a user has disabled push and so the user's push enabled state remains enabled. When you attempt to send to a device in this state the push is 'sent' and the device receives the payload but is suppressed by the device so is not displayed to a user. Braze refers to this as ‘silently failing’.
- The previous version of the Android SDK does not have the `notifications_enabled` parameter and will not return a value for it if user data is called using the Braze REST API.

[1]: https://cloud.githubusercontent.com/assets/20304883/25244744/cd16d324-25b6-11e7-9d7c-d37b74690cf8.png
[2]: https://cloud.githubusercontent.com/assets/20304883/25244775/ec6e0ae4-25b6-11e7-846d-4bf8f38c3057.png
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
