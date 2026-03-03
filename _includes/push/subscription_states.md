## Push subscription states {#push-sub-states}

A "Push Subscription State" in Braze identifies a **user's** global preference for their desire to receive push notifications. Because the subscription state is user-based, it is not specific to any individual app. Subscription states become helpful flags when deciding which users to target for push notifications.

{% alert note %}
A user's push subscription state applies to their entire user profile, which includes all of the user's devices. 
{% endalert %}

There are three push subscription state options: `Subscribed`, `Opted-In`, and `Unsubscribed`.

By default, for your user to receive your messages through push, their push subscription state must be either `Subscribed` or `Opted-In`, and they must be [push enabled](#foreground-push-enabled). You can override this setting if needed when composing a message.

|Opt-in State|Description|
|---|---|
|`Subscribed`| Default push subscription state when a user profile is created in Braze. |
|`Opted-In`| A user has explicitly expressed a preference to receive push notifications. Braze will automatically move a user's opt-in state to `Opted-In` if a user accepts an OS-level push prompt.<br><br>This does not apply to Android 12 or below users.|
|`Unsubscribed`| A user explicitly unsubscribed from push through your application or other methods your brand provides. By default, Braze push campaigns only target users that are `Subscribed` or `Opted-in` for push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze does not automatically change a user's push subscription state to `Unsubscribed`. Remember that if a user's push subscription state is `Unsubscribed`, then the user's `Foreground Push Enabled` filter in segmentation will be `false`.
{% endalert %}

### Updating push subscription states {#update-push-subscription-state}

There are three ways you can update a user's push subscription state:

#### Automatic opt-in (default)

By default, Braze sets a user's push subscription state to `Opted-In` when they first authorize push notifications for your app. Braze also does this when a user re-enables push permissions in their system settings after previously disabling them.

{% tabs local %}
{% tab android %}
To disable this default behavior, add the following property to your Android Studio project's `braze.xml` file:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
Starting with [Braze Swift SDK version 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), you can disable or further customize this behavior by adding the `optInWhenPushAuthorized` configuration to your Xcode project's `AppDelegate.swift` file:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK integration

You can update a user's subscription state with the Braze SDK using the `setPushNotificationSubscriptionType` method on [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html), or [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). For example, you can use this method to create a settings page in your app where users can manually enable or disable push notifications.

#### REST API

You can update a user's subscription state with the Braze REST API using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update their [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) attribute.

### Checking push subscription state

![User profile for John Doe with their push subscription state set to Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

There are two ways you can check a user's push subscription state with Braze:

1. **User profile:** You can access individual user profiles through the Braze dashboard on the **[User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** page. After finding a user's profile (via email address, phone number, or external user ID), you can select the **Engagement** tab to view and manually adjust a user's subscription state.
2. **REST API export:** You can export individual user profiles in JSON format using the export [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) or [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoints. Braze will return a push tokens object that contains push enablement information per device.