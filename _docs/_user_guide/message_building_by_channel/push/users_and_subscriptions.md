---
nav_title: "Subscription States"
page_order: 3
page_type: reference
description: "This reference article covers the different push subscription states."

channel:
  - push
tool:
  - Docs
  - Dashboard
  - Campaigns
---

# Push Subscription States

> Push subscription states are filters that allow your users to control whether they receive messages or not. For your user to receive your messages through push, they must be `Subscribed` or `Opted-In`, as well as [Push Enabled](#push-enabled).

![opt-in][56]{: height="50%" width="50%"}

|Opt-in State|Description|
|---|---|
|Subscribed| Default status.|
|Opted-In| A user has explicitly allowed Braze will automatically move a user's opt-in state to “Opted-In”. |
|Unsubscribed| A user has explicitly disallowed push notifications.|
{: .reset-td-br-1 .reset-td-br-2}

Subscription states are filters that let Braze know if users are subscribed to receive Push Messages. Note that even though users __may not have a Push Token__ (e.g They turn off push tokens at the device level through settings, opting not to receive messages) they still may be subscribed. Being subscribed does not guarantee that a push will be delivered, users must also be Push enabled or Push registered to receive these notifications. This is done in part because users have a single Push Subscription State but may have multiple devices with different levels of push permissions. 

### Three ways to Check a Users Push Subscription State:
1. __User Profile__: Individual user profiles can be accessed through the Braze dashboard by selecting User Search from the right sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, under the Engagement tab, you can view and manually adjust a user's subscription state. <br><br>
2. __CSV Export__: User profiles can be accessed through doing a CSV User Data Export. This can be done by selecting a campaign and then selecting User Data in the upper right corner. In the window that pops up, you may select what custom attributes or events you would like to choose. <br><br>
3. __Rest API Export__: Individual user profiles can be exported in the JSON format using the users/export/ [segment][segment] or [identifier][identifier] endpoints by using Braze’s REST API. Braze will return a push tokens object, that contains push enablement information per device.

## Push Enabled

A user is "Push Enabled" or "Push Registered" if they have an *active push token* for an app in your app group.

![img][1]{: style="float:right;max-width:50%;margin-left:15px;"}

On the User Engagement tab in the dashboard you will see: **Push Registered For** followed by an **App Name(s)** or followed by **No Apps**. There will be an entry for every device that belongs to the user.

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive background push and can not display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.
![img2][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

If a push token is moved a different user on the same device, that first user will no longer be push registered.

## iOS & Android Push Details {#ios-android-details}

{% tabs %}
  {% tab iOS %}
__iOS Push__

In iOS 12, Apple introduced Provisional Authorization, allowing brands the option to send quiet push notifications to their users' Notification Centers _before_ they officially, explicitly opt-in, giving you a chance to demonstrate the value of your messages early.

On devices running iOS 11 or below, your users _must explicitly opt-in to receive your push messages_. You must request whether the user would like to receive push from you.

If your app is provisionally authorized or the user allows push, you will receive a token and be able to send remote notifications to that user that appears in the __foreground__. If your user does not allow push notifications, you will still receive a token, but this token will only be able to send silent push which permits the app to carry out actions in the __background__ (you must have "Remote Notifications" enabled in __Xcode__). These users with provisional authorization have push enabled at the device-level. 

iOS users are considered "Push Enabled" only if they have allowed notifications in the __foreground__, either explicitly (app-level) or provisionally (device-level).

  {% endtab %}
  {% tab Android %}
__Android Push__

You do not need to request permission to send push notifications to Android users. As the user has not explicitly requested to receive push, Braze will not automatically [update the user's opt-in state]({{ site.baseurl }}/developer_guide/rest_api/user_data/#braze-user-profile-fields). Upon a user’s first session on Android, Braze will automatically request a new token and upon successfully receiving that token, an update to the user’s push enabled state will happen. At this point, a user has push enabled at both the app-level and the device-level.

If the user disables push, Braze will mark them as __foreground__ push disabled no longer attempt to send them push messages. The filter `Push Enabled` will result in `false` for this user. You may continue to send __background__ (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

On Android, Braze will move a user to be __push disabled__ if:
- A user uninstalls the app from their device.
- Braze receives a bounce when sending to a specific token (sometimes caused by app updates, uninstalls, new push token version or format).
- Push registration fails to FCM (sometimes caused by poor network connections or a failure to connect to or on FCM to return a valid token).
- (For Android SDK v2.2.2+) The user blocks push notifications for the app within their device settings and subsequently log a session.

  {% endtab %}
{% endtabs %}

## Before Android SDK v2.2.2 {#before-android-sdk}

Here are some details you should know if you aren't using our most up to date Android SDK.
- The previous version of the Android SDK does not detect that a user has disabled push and so the user's push enabled state remains enabled. When you attempt to send to a device in this state the push is 'sent' and the device receives the payload but is suppressed by the device so it is not displayed to a user. Braze refers to this as ‘silently failing’.
- The previous version of the Android SDK does not have the `notifications_enabled` parameter and will not return a value for it if user data is called using the Braze REST API.

[1]: https://cloud.githubusercontent.com/assets/20304883/25244744/cd16d324-25b6-11e7-9d7c-d37b74690cf8.png
[2]: https://cloud.githubusercontent.com/assets/20304883/25244775/ec6e0ae4-25b6-11e7-846d-4bf8f38c3057.png
[identifier]: {{ site.baseurl }}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{ site.baseurl }}/api/endpoints/export/user_data/post_users_segment/
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
