---
nav_title: "Push Enablement and Subscription"
article_title: Push Enablement and Subscription
page_order: 3
page_type: reference
description: "This reference article covers the different push subscription states as well as a push enablement overview, covering the fundamental push difference across iOS and Android."
channel:
  - push

---

# Push enablement and subscription

> This reference article covers the different push subscription states as well as a push enablement overview, covering the fundamental push difference across iOS and Android.

![Opt-in Option][56]{: style="float:right;max-width:50%;margin-left:15px;"}

Push subscription states are filters that allow your users to control whether they receive messages or not. For your user to receive your messages through push, they must be `Subscribed` or `Opted-In`, as well as [push enabled](#push-enabled).

## Push subscription state

Subscription states are helpful flags when deciding which users to target for push notifications. Braze recommends providing toggles in your app to make it simple for users to determine their push notification status. This helps prevent users from going into device settings and removing push tokens completely.

|Opt-in State|Description|
|---|---|
|Subscribed| Default state.|
|Opted-In| A user has explicitly expressed a preference to receive push notifications. Braze will automatically move a user's opt-in state to "Opted-In". |
|Unsubscribed| A user explicitly unsubscribed from push through your application UI or other methods that your brand provides. By default, Braze push campaigns only target users that are "Subscribed" or "Opted-in" for push.|
{: .reset-td-br-1 .reset-td-br-2}

If a user doesn't have a push token (that is, they turn off push tokens at the device level through settings, opting not to receive messages), they still may be subscribed to push. Being subscribed does not guarantee that a push will be delivered—users must also be push enabled or push registered to receive these notifications.

This is mainly because users have a single push subscription state but may have multiple devices with different levels of push permissions.

### Check user's push subscription state

![Push Example][3]{: style="float:right;max-width:35%;margin-left:15px;"}

There are two ways you can check a user's push subscription state with Braze:

1. __User Profile:__ You can access individual user profiles through the Braze dashboard on the **User Search** page. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, you can select the **Engagement** tab to view and manually adjust a user's subscription state. <br><br>
2. __Rest API Export:__ You can export individual user profiles in JSON format using the export [Users by segment][segment] or [Users by identifier][identifier] endpoints. Braze will return a push tokens object that contains push enablement information per device.

## Push enablement {#push-enabled}

A user is "Push Enabled" or "Push Registered" if they have an active push token for an app in your app group.

![Push Enablement][1]{: style="float:right;max-width:50%;margin-left:15px;"}

On the **Engagement** tab in a user's profile, you will see **Push Registered For** followed by an app name or two dashes (**&#45;&#45;**), if no app information exists for that device. There will be an entry for every device that belongs to the user.

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive [background push]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) and can not display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.
![Push Changelog][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

If a push token is moved to a different user on the same device, that first user will no longer be push registered.

## Push details {#ios-android-details}

The following sections detail some differences on how push enablement is handled between Android and iOS.

### Android

You don't need to request permission to send push notifications to Android users. However, Braze won't automatically update the user's [opt-in state]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) until the user explicitly requests to receive push. Upon a user's first session on Android, Braze automatically requests a new token. Upon successfully receiving that token, the user's push enabled state is then updated. At this point, the user is push enabled at both the app-level and the device-level.

If the user disables push, Braze marks them as foreground push disabled and no longer attempts to send them push messages. The filter `Push Enabled` will result in `false` for this user. You can still continue to send background (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

On Android, Braze will move a user to be push disabled if:

- A user uninstalls the app from their device.
- Braze receives a bounce when sending to a specific token (sometimes caused by app updates, uninstalls, new push token version, or format).
- Push registration fails to Firebase Cloud Messaging (sometimes caused by poor network connections or a failure to connect to or on FCM to return a valid token).
- The user blocks push notifications for the app within their device settings and subsequently logs a session.

### iOS

#### iOS push states

To receive a push token for iOS, you must request whether the user would like to receive push. Depending on the user’s response, Braze adjusts the user’s push subscription state to `opted in` if accepted, or keeps the push subscription state as `subscribed` if rejected. Before this, the opt-in state is `subscribed`. Upon receiving a response, Braze attempts to register the user for push. After Braze successfully receives a token, we update the user's push-enabled state.

- Push Enabled: Braze has a push token for the device.
- Push Opted-In: The user has expressed a preference to send them push notifications.

#### Enabled state

There are two enabled states:

- Foreground push enabled (opted-in)
- Background push enabled (opted-out)

Regardless of the response to the opt-in prompt, the user receives a background push token (you must have "Remote Notifications" enabled in Xcode), allowing you to send them silent push. If your app is provisionally authorized or if the user has opted into push, they receive a foreground push token as well, allowing you to send them all types of push. Within Braze, we consider a user on iOS who is foreground push enabled to be "push enabled", either explicitly (app-level) or provisionally (device-level).

#### Enabled state and opt-in

On the next app open in iOS, the SDK will detect that push has been disabled and will notify Braze. At this point, Braze will update the push-enabled state to disabled. When you attempt to send a push to a user, Braze is already aware of whether we have a token, so notifications only get sent to the people who explicitly state they want them.

#### Provisional Authorization and Quiet Push

In iOS 12, Apple introduced Provisional Authorization, allowing brands the option to send quiet push notifications to their users' Notification Centers before they explicitly opt-in, giving you a chance to demonstrate the value of your messages early. Check out our documentation to learn more about [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

On devices running iOS 11 or below, your users must explicitly opt-in to receive your push messages. You must request whether the user would like to receive push from you.

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
[3]: {% image_buster /assets/img/push_example.png %}
