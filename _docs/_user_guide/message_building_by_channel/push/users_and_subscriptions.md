---
nav_title: "Push Enablement and Subscription"
article_title: Push Enablement and Subscription
page_order: 3
page_type: reference
description: "This reference article covers the concepts of push enabled and push subscription states in Braze, including the fundamental differences in behavior across iOS, Android, and web."
channel:
  - push

---

# Push enablement and subscription

> This reference article covers the concepts of push enablement and push subscription states in Braze, including the fundamental differences in behavior across iOS, Android, and web.

## Push enablement {#push-enabled}

**Push Enabled** is a segmentation filter in Braze that allows marketers to easily identify users that allow Braze to send push notifications and users that haven't expressed preferences to not receive push notifications. By definition, this **Push Enabled** filter takes into account the following:
- The ability for Braze to send a push notification
- The user's push subscription state

![][1]{: style="float:right;max-width:50%;margin-left:15px;"}

A user is considered "push enabled" or "push registered" if they have an active push token for an app within your app group, meaning push enablement status is app-specific. 

### Types of push tokens

There are two different types of [push tokens][4] that are essential to understanding how a push notification is successfully sent to your users:
- Foreground push tokens
- Background push tokens

Foreground push tokens provide the ability to send regular push notifications to the foreground of a user's device. Background, or silent, push tokens are assigned to all devices that have a brand’s app downloaded, regardless of that particular device has opted-in to receive push notifications from that brand. Background push tokens allow brands to send silent push notifications, which are push notifications that intentionally won’t be displayed to devices in order to support key functionalities like uninstall tracking.

When a user profile has a valid foreground push token associated with an app, Braze considers the user "push registered" for the given app. Braze, then, provides a specific segmentation filter `Push enabled for App` to help identify these users.

Note that `Push enabled for App` only considers the presence of a valid a foreground push token for the given app. However, the more generic `Push Enabled` filter considers the presence of any valid foreground push token as well as the push subscription state having a value of “subscribed” or “opted-in”.

### Check user's push enablement status

On the **Engagement** tab in a user's profile, you will see **Push Registered For** followed by an app name. If no app information exists for that device, you will see two dashes (**&#45;&#45;**). There will be an entry for every device that belongs to the user.

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.
![Push Changelog with an example push token.][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive [background push]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) and cannot display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.

If a push token is moved to a different user on the same device, that first user will no longer be push registered.

## Push subscription states {#push-sub-states}

![Push subscription state set to Opted In.][56]{: style="float:right;max-width:50%;margin-left:15px;"}

Push subscription states in Braze identify a user’s global preference for their desire to receive push notifications or not. Subscription states become helpful flags when deciding which users to target for push notifications. 

{% alert important %}
In order for your user to receive your messages through push, their push subscription state must be either `Subscribed` or `Opted-In`, and they must be [push enabled](#push-enabled). 
{% endalert %}

Braze recommends providing toggles in your app to make it simple for users to determine their push notification status. This helps prevent users from going into their device settings and disabling push at the app level, which causes the removal of the foreground push token in Braze completely.

{% alert note %}
A user's push subscription state applies to their entire user profile, which includes all of the user's devices. 
{% endalert %}

There are three push subscription state options: `Subscribed`, `Opted-In`, and `Unsubscribed`. Braze suggests that brands follow the following subscription state definitions when managing their users’ push preferences.

|Opt-in State|Description|
|---|---|
|Subscribed| Default push subscription state when a user profile is created in Braze. |
|Opted-In| A user has explicitly expressed a preference to receive push notifications. For both iOS and web, Braze will automatically move a user's opt-in state to `Opted-In` if a user accepts an OS-level push prompt. This doesn't apply to Android. |
|Unsubscribed| A user explicitly unsubscribed from push through your application UI or other methods that your brand provides. By default, Braze push campaigns only target users that are `Subscribed` or `Opted-in` for push.|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Braze will never automatically change a user's push subscription state to `Unsubscribed`. Keep in mind that if a user's push subscription state is `Unsubscribed`, then the user's `Push Enabled` filter in segmentation will be `false`.
{% endalert %}

If a user doesn't have a foreground push token registered (that is, they turn off push tokens at the device level through settings, opting not to receive messages), they can still be subscribed to push. However, the user would not be **Push Enabled for App** in Braze since the foreground push token is not valid. Additionally, if a user profile doesn't have another valid or registered push token for any other apps, their `Push Enabled` filter in segmentation will also be `false`. 

Push subscription state does not guarantee that a push will be delivered. Users must also be push enabled or push registered to receive these notifications. This is mainly because users have a single push subscription state but may have multiple devices with different levels of push permissions.

### Check user's push subscription state

![User profile for John Doe with their push subscription state set to Subscribed.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

There are two ways you can check a user's push subscription state with Braze:

1. **User Profile**: You can access individual user profiles through the Braze dashboard on the **User Search** page. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, you can select the **Engagement** tab to view and manually adjust a user's subscription state. <br><br>
2. **Rest API Export**: You can export individual user profiles in JSON format using the export [Users by segment][segment] or [Users by identifier][identifier] endpoints. Braze will return a push tokens object that contains push enablement information per device.

## Push behavior differences {#ios-android-details}

The following sections detail some differences on how push enablement is handled between Android, iOS, and web. 

### Android

You don't need to request permission to send push notifications to Android users. However, Braze won't automatically update the user's [opt-in state]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) until the user explicitly requests to receive push. Upon a user's first session on Android, Braze automatically requests a new token. Upon successfully receiving that token, the user's push enabled state is then updated. At this point, the user is push enabled at both the app-level and the device-level.

Foreground push tokens can be registered immediately during the app’s first session without any user preferences captured in the OS. This means that for new Android users, after their first session in the app, the user’s push subscription state will show as `Subscribed`, and the profile will show `Push registered for App: Android`.

If the Android user subsequently disables push in their OS settings, at the start of the next session, the following events take place:
- Braze marks them as foreground push disabled and no longer attempts to send them push messages.
- The `Push Enabled for App (Android)` filter and the `Push Enabled` segmentation filter (assuming no other apps on the user profile have a valid foreground push token) will return `false`.

In this scenario, since a background push token will still exist, you can still continue to send background (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

For Android, Braze will consider a user to be push disabled if:

- A user uninstalls the app from their device.
- Braze receives a bounce when sending to a specific token (sometimes caused by app updates, uninstalls, new push token version, or format).
- Push registration fails to Firebase Cloud Messaging (sometimes caused by poor network connections or a failure to connect to or on FCM to return a valid token).
- The user blocks push notifications for the app within their device settings and subsequently logs a session.

### iOS

The key push behavior difference between Android and iOS is that, in order to register a push token for iOS, users must explicitly opt-in at the OS level via the iOS push prompt.

When this prompt occurs, if a user explicitly chooses to opt-in, Braze will automatically update the user's push subscription state from `Subscribed`, which is the default state, to `Opted in`. This is the only scenario where Braze will actively change the push subscription state. If the user decides to not opt-in, then their push subscription state remains as `Subscribed`. 

So for new iOS users, if they have actively opted-in to receive push notification using the OS prompt, then their push subscription state will be `Opted in` and their profile will show `Push registered for App: iOS`.

If a user declines to receive push notifications on an OS level, then their push subscription state will be `Subscribed` and their profile will not show that a foreground push token has been registered. 

In the scenario that a user, who initially opted-in on the OS level, disables push notifications in their OS settings, at the next session start, the following will occur:
- Braze marks them as foreground push disabled and no longer attempts to send push messages.
- The `Push Enabled for App (iOS)` filter and the `Push Enabled` segmentation filter (assuming no other apps on the user profile have a valid foreground push token) will return `false`.

In this scenario, since a background push token will still exist, you can still continue to send background (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

#### Background push

Regardless of the response to the opt-in prompt, the user receives a background push token (you must have "Remote Notifications" enabled in Xcode), allowing you to send them silent push. If your app is provisionally authorized or if the user has opted into push, they receive a foreground push token as well, allowing you to send them all types of push. Within Braze, we consider a user on iOS who is foreground push enabled to be "push enabled", either explicitly (app-level) or provisionally (device-level).

#### Provisional Authorization and Quiet Push

In iOS 12, Apple introduced Provisional Authorization, allowing brands the option to send quiet push notifications to their users' Notification Centers before they explicitly opt-in, giving you a chance to demonstrate the value of your messages early. Check out our documentation to learn more about [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

On devices running iOS 11 or earlier, your users must explicitly opt-in to receive your push messages. You must request whether the user would like to receive push from you.

### Web

The behavior for web push subscription functions similar to that of iOS. The default subscription status for web users once they've opted-in via the `appboy.registerAppboyPushMessages()` is `subscribed`. This default status is sufficient for you to send push messages to web users. The `opted in` state implies a user has explicity opted in to push notifications via web, if permittable. However, this explicit opt-in is not required to send push to web users.

To manage subscriptions, you can use the user method [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#setpushnotificationsubscriptiontype) to create a preference settings page on your site, after which you can filter users by opt-out status on the dashboard.

If a user disables notifications within their browser, the next push notification sent to that user will bounce and Braze will update the user's push token accordingly. This is used to manage eligibility for the push enabled filters (`Background Push Enabled`, `Push Enabled` and `Push Enabled for App`). The subscription status set on the user's profile is a user-level setting and doesn't change when a push bounces.

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[56]: {% image_buster /assets/img_archive/braze_optedin.png %}
