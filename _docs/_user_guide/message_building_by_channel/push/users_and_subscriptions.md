---
nav_title: "Push Enablement and Subscription"
article_title: Push Enablement and Subscription
page_order: 3
page_type: reference
description: "This reference article covers the concepts of push enabled and push subscription states in Braze, including the fundamental differences in behavior across iOS, Android, and web."
channel:
  - push

---

# Push enablement and push subscription

> This reference article covers the concepts of push enablement and push subscription states in Braze, including the fundamental differences in behavior across iOS, Android, and web.


## Push subscription states {#push-sub-states}

A "Push Subscription State" in Braze identify a **user’s** global preference for their desire to receive push notifications or not. Because the subscription state is user-based, it is not specific to any individual app. Subscription states become helpful flags when deciding which users to target for push notifications. 

{% alert note %}
A user's push subscription state applies to their entire user profile, which includes all of the user's devices. 
{% endalert %}

There are three push subscription state options: `Subscribed`, `Opted-In`, and `Unsubscribed`.

By default, in order for your user to receive your messages through push, their push subscription state must be either `Subscribed` or `Opted-In`, and they must be [push enabled](#push-enabled). You can override this setting if needed when composing a message.

|Opt-in State|Description|
|---|---|
|Subscribed| Default push subscription state when a user profile is created in Braze. |
|Opted-In| A user has explicitly expressed a preference to receive push notifications. Braze will automatically move a user's opt-in state to `Opted-In` if a user accepts an OS-level push prompt. This does not apply to users on Android 12 or below.|
|Unsubscribed| A user explicitly unsubscribed from push through your application UI or other methods that your brand provides. By default, Braze push campaigns only target users that are `Subscribed` or `Opted-in` for push.|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Braze does not automatically change a user's push subscription state to `Unsubscribed`. Keep in mind that if a user's push subscription state is `Unsubscribed`, then the user's `Push Enabled` filter in segmentation will be `false`.
{% endalert %}


### Updating Push Subscription States {#update-push-subscription-state}

There are three ways a user's Push Subscription State can be updated:

**1. SDK Integration**

Use the Braze SDK to update a user's subscription state. For example, you can add a settings page to your app where a user can turn on/off push notifications for their profile.

To do this, use the `setPushNotificationSubscriptionType` method on [web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [android](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html), or [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#afb2c11d1889fd08537f90ee64c94efb3).

**2. REST API**

Use the [`/users/track` endpoint][users-track] to update the `push_subscribe` attribute for a given user.

**3. Automatically during Opt-In** 

When a user accepts the native OS push permission prompt, Braze will automatically change that user's subscription state to `Opted In`.


## Push Permission

All push-enabled platforms - iOS, Web, and Android - require explicit opt-in via an OS level system prompt, with some slight differences described below.

Because a user's decision is final and you can't ask again once they decline, using [Push Primer][push-primers] in-app messages is an important strategy to increasing your opt-in rates.

**Native OS Push Permission Prompts**

|Platform|Screenshot|Description|
|--|--|--|
|iOS| ![An iOS native push prompt asking "My App would like to send you notifications" with two buttons "Don't Allow" and "Allow" at the bottom of the message.][ios-push-prompt]{: style="max-width:410px;"} | Note: This does not apply when requesting [provisional push](#provisional-push) permission.|
|Android| ![An Android push message asking "Allow Kitchenerie to send you notifications?" with two buttons "Allow" and "Don't allow" at the bottom of the message.][android-push-prompt]{: style="max-width:410px;"} | This push permission was introduced in Andoid 13. Prior to Android 13, permission was not required to send push.|
|Web| ![A web browser's native push prompt asking "Braze.com wants to show notification" with two buttons "Block" and "Allow" at the bottom of the message.][web-push-prompt]{: style="max-width:410px;"} | |

### Android

Prior to Android 13, permission was not needed to send push notifications. On Android 12 and below, all users are considered `subscribed` upon their first session, when Braze automatically requests a push token. At this point, the user is **push enabled** with a valid push token for that device, and a default subscription state of `subscribed`.

Starting with [Android 13][android-13], push permission must be asked of and granted by the user. Your app can manually request permission from the user at opportune times, but if not, users will be prompted automatically once your app creates a ["Notification Channel"](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

Your app can request Provisional Push, or Authorized Push. 

Authorized Push requires explicit permission from a user prior to sending any notifications, whereas [Provisional Push][provisional-blog] lets you send notifications __quietly__, directly to the Notification Center without any sound or alert.

#### Provisional Authorization and Quiet Push {#provisional-push}

Prior to iOS 12 (released in 2018), all users must explicitly opt-in to receive push notifications.

![A notification in the system Notification Center with a message at the bottom asking, "Keep receiving notifications from the Yachtr app?" with two buttons below to "Keep" or "Turn Off"][ios-provisional-push]{: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

In iOS 12, Apple introduced [Provisional Authorization][provisional-blog], allowing brands the option to send quiet push notifications to their users' Notification Center before they explicitly opt-in, giving you a chance to demonstrate the value of your messages early. Check out our documentation to learn more about [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications).

### Web

On the web, you must request explicit opt-in from users via the native browser permission dialog.

Unlike iOS and Android which lets your app show the permission prompt at any time, some modern browsers will only show the prompt if it was triggered off of a "user gesture" (mouse click or keystroke). If your site tries to request Push Notification permission on pageload, it will likely be ignored or silenced by the browser.

As a result, you should ask for permission only when a user clicks somewhere on your website and not randomly when a page loads.

## Push Tokens

[Push tokens][push-tokens] are a unique anonymous identifier generated by a user's device and sent to Braze to identify where to send each recipient's notification.

There are two different ways a [push token][push-tokens] can be classified that are essential to understanding how a push notification can be sent to your users.

**Foreground push** provide the ability to send regular push notifications to the foreground of a user's device.

**Background push** are assigned to all devices that have a brand’s app downloaded, regardless of if that particular device has opted-in to receive push notifications from that brand. Background push tokens allow brands to send silent push notifications - push notifications that intentionally won’t be displayed to devices in order to support key functionalities like uninstall tracking.

When a user profile has a valid foreground push token associated with an app, Braze considers the user "push registered" for the given app. Braze, then, provides a specific segmentation filter `Push enabled for App` to help identify these users.

Note that `Push enabled for App` only considers the presence of a valid a foreground or background push token for the given app. However, the more generic `Push Enabled` filter segments users who have explicitly activated push notifications for any of the apps in your app group. This count includes only foreground push, and doesn't include users who have unsubscribed. You can learn more about these and other filters in [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

## Push Enabled Filter {#push-enabled}

**Push Enabled** is a segmentation filter in Braze that allows marketers to easily identify users that allow Braze to send push notifications and users that haven't expressed preferences to not receive push notifications. 

The **Push Enabled** filter takes into account the following:
- The ability for Braze to send a push notification (__foreground push token__)
- The user's overall preference to receive push on any of their devices (__push subscription state__)

![A screenshot of the dashboard showing a user is "Push Registered for Marketing (iOS)"][1]{: style="float:right;max-width:50%;margin-left:15px;"}

A user is considered "push enabled" or "push registered" if they have an active foreground push token for an app within your app group, meaning push enablement status is app-specific. 

### Checking push registration status

On the **Engagement** tab in a user's profile, you will see **Push Registered For** followed by an app name. If no app information exists for that device, you will see two dashes (**&#45;&#45;**). There will be an entry for every device that belongs to the user.

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.
![Push Changelog with an example push token.][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive [background push]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) and cannot display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.

If a push token is moved to a different user on the same device, that first user will no longer be push registered.

### Checking push subscription state

![User profile for John Doe with their push subscription state set to Subscribed.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

There are two ways you can check a user's push subscription state with Braze:

1. **User Profile**: You can access individual user profiles through the Braze dashboard on the [User Search][5] page. After finding a user's profile (via email address, phone number, or external user ID) you can select the **Engagement** tab to view and manually adjust a user's subscription state. 
<br>

2. **Rest API Export**: You can export individual user profiles in JSON format using the export [Users by segment][segment] or [Users by identifier][identifier] endpoints. Braze will return a push tokens object that contains push enablement information per device.


## Best Practices and Tips

**Add Push Subscription Controls To Your App**
To avoid a user from disabling notifications at the device level which removes their foreground push token completely, Braze recommends letting users control their push subscription directly within your app. See the section on [updating push subscription states](#update-push-subscription-state) for more details.


**Prime Users For Push Before Showing the System Prompt**

You only get one chance to ask a user for push permission, and once they decline it's very hard to convince a user to re-enable push in their device settings. For this reason, you should prime users for push using an in-app message prior to showing the system prompt. To learn more about increasing opt-ins using this strategy, see our guide on [Push Primers][push-primers].

**Subscription State does not always mean a user is reachable**

If a user doesn't have a valid foreground push token for an app (that is, they turn off push tokens at the device level through settings, opting not to receive notifications), their __Subscription State__ can still be considered `subscribed` to push. However, this user would not be **Push Enabled for App** in Braze since the foreground push token is not valid. 

Additionally, if a user profile doesn't have __any__ valid or registered push token for any other apps, their **Push Enabled** filter in segmentation will also be `false`. 

Push __Subscription State__ does not guarantee that a push will be delivered. Users must also be **Push Enabled** to receive notifications. This is because a user profile has a single push subscription state, but may have multiple devices with different foreground push permissions.


## Other Platform Specific Scenarios

### Android

If a foreground push enabled user disables push in their OS settings then at the start of the next session:
- Braze marks them as foreground push disabled and no longer attempts to send them push messages.
- The `Push Enabled for App (Android)` filter and the `Push Enabled` segmentation filter (assuming no other apps on the user profile have a valid foreground push token) will return `false`.

In this scenario, since a background push token will still exist, you can still continue to send background (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

For Android, Braze will consider a user to be push disabled if:

- A user uninstalls the app from their device.
- Braze receives a bounce when sending to a specific token (sometimes caused by app updates, uninstalls, new push token version, or format).
- Push registration fails to Firebase Cloud Messaging (sometimes caused by poor network connections or a failure to connect to or on FCM to return a valid token).
- The user blocks push notifications for the app within their device settings and subsequently logs a session.

### iOS

Regardless of the response to the foreground push opt-in prompt, users receive a background push token if you have "Remote Notifications" enabled in Xcode. This allows you to send silent push to the device. 

If your app is provisionally authorized or if the user has opted into push, they receive a foreground push token as well, allowing you to send them all types of push. Within Braze, we consider a user on iOS who is foreground push enabled to be "push enabled", either explicitly (app-level) or provisionally (device-level).

If a user declines to receive push notifications on an OS level, then their push subscription state will be `Subscribed` and their profile will not show that a foreground push token has been registered. 

In the scenario that a user, who initially opted-in on the OS level, disables push notifications in their OS settings, at the next session start, the following will occur:
- Braze marks them as foreground push disabled and no longer attempts to send push messages.
- The `Push Enabled for App (iOS)` filter and the `Push Enabled` segmentation filter (assuming no other apps on the user profile have a valid foreground push token) will return `false`.

In this scenario, since a background push token will still exist, you can still continue to send background (silent) push notifications with the segmenting filter `Background Push Enabled = true`.

### Web

When a user accepts the native push permission prompt, their subscription status will be changed to `opted in`.

To manage subscriptions, you can use the user method [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) to create a preference settings page on your site, after which you can filter users by opt-out status on the dashboard.

If a user disables notifications within their browser, the next push notification sent to that user will bounce and Braze will update the user's push token accordingly. This is used to manage eligibility for the push enabled filters (`Background Push Enabled`, `Push Enabled` and `Push Enabled for App`). The subscription status set on the user's profile is a user-level setting and doesn't change when a push bounces.

Note: Web platforms do not allow background or silent push.

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[3]: {% image_buster /assets/img/push_example.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[ios-push-prompt]: {% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}
[android-push-prompt]: {% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}
[web-push-prompt]: {% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}
[ios-provisional-push]: {% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}
[push-primers]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[android-13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/
[provisional-blog]: https://www.braze.com/resources/articles/mastering-provisional-push
[users-track]: https://www.braze.com/docs/api/objects_filters/user_attributes_object
