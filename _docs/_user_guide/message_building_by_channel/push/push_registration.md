---
nav_title: "Push registration"
article_title: Push Registration
page_order: 2
page_type: reference
description: "This reference article discusses what it means to be registered for push and how we send push messages and deal with push tokens and push registration at Braze."
channel:
 - push

---

# Push registration

> This article covers the process through which a user gets assigned a push token, and how Braze sends push messages to your users.

## About push tokens {#push-tokens}

When an app requests push permissions from a device, the device's push service provider will generate a push token for that app. Each app is given its own unique, anonymous push token which is how it identifies the device and current app instance when sending a push notification.

Keep in mind, push tokens aren't static identifiers that last forever&#8212;they can be updated and they can [expire](#push-token-expire).

{% alert tip %}
For platform-specific details, see [Push token registration](#push-token-registration).
{% endalert %}

### Foreground vs. background push {#foreground-vs-background}

Push tokens are used to send both foreground and background push notifications.

| Type       | Requires Opt-In? | Description                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Foreground push | Yes       | A notification is visibly displayed to the user while the app is in the foreground.           |
| Background push | No        | A notification is silently delivered in the background without being displayed. Often used for functionality like uninstall tracking. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When a user opts-in to push notifications for your app, they'll be considered "push registered", meaning they can now be targeted using the `Foreground Push Enabled for App` segmentation filter in Braze.

{% alert note %}
This is different from the `Foreground Push Enabled` segmentation filter, which is used to identify users who have opted-in to at least one of your apps—not one specific app. For more information, see [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#foreground-push-enabled).
{% endalert %}

### Multiple users on a device

Push tokens are unique to both the device and the app, meaning push tokens can't be used to target specific user's if multiple users are using the same device.

For example, say you have two users: Charlie and Kim. If Charlie has enabled push notifications for your app on his phone and Kim uses Charlie's phone to log out of Charlie's profile and log into her own, the push token will be re-assigned to Kim's profile. The push token will then remain assigned to Kim's profile on that device until she logs out and Charlie logs back in again.

An app or website can only have one push subscription per device. So when a user logs out of a device or website, and a new user logs in, the push token gets reassigned to the new user. This is reflected on the user's profile in **Contact Settings** section of the **Engagement** tab:

![Push token changelog on the **Engagement** tab of a user's profile, which lists when the push token was moved to another user, and what the token was.]({% image_buster /assets/img/push_token_changelog.png %})

Because there isn't a way for push providers (APNs/FCM) to distinguish between multiple users on one device, we pass the push token to the last user who was logged in to determine which user to target on the device for push.

## Push token registration

Each device platform handles push token registration differently. Refer to the following for platform-specific details:

{% tabs local %}
{% tab android %}
When your app is installed, a push token is automatically generated for your app&#8212;however, it can only be used for [background push notifications](#foreground-vs-background) until the user explicitly opts-in. Additionally, registration is handled differently across different Android versions:

| Version       | Details                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | Push permission must be requested and granted by the user. Your app can request permission manually, or users will be prompted automatically after a [notification channel](https://developer.android.com/reference/android/app/NotificationChannel) is created. |
| **Android 12 and earlier** | All users are considered `Subscribed` after their first session. Braze automatically requests a push token at this point, making the user push enabled with a valid token and a default subscription state of `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab ios %}
iOS does not automatically generate push tokens for an app when it's installed. Additionally, registration is handled differently across different iOS versions: 

| Version                         | Provisional Authorization? | Details                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Yes                         | When a user opts-in to push notifications, you're given standard authorization, allowing you to send [foreground push notifications](#foreground-vs-background). However, you can also request [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), which let's you send silent [background push notifications](#foreground-vs-background) directly to the notification center. |
| **iOS 11 and later** | No                          | All users must explicitly opt-in to receive push notifications. A push token is generated only after permission is granted.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab web %}
You must request explicit opt-in from users via the native browser permission dialog. Will receive a token after users opt-ed in. Unlike iOS and Android, which let your app show the permission prompt at any time, some modern browsers will only show the prompt if triggered by a "user gesture" (mouse click or keystroke). If your site tries to request push notification permission on page load, it will likely be ignored or silenced by the browser.
{% endtab %}
{% endtabs %}

### Checking user's push subscription state

![User profile for John Doe with their push subscription state set to Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

There's two ways you can check a user's push subscription state with Braze:

- **User Profile**: You can access individual user profiles through the Braze dashboard on the [User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) page. After finding a user's profile (via email address, phone number, or external user ID), you can select the **Engagement** tab to view and manually adjust a user's subscription state.
- **Rest API Export**: You can export individual user profiles in JSON format using the export [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) or [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoints. Braze will return a push tokens object that contains push enablement information per device.

### Checking push registration status

On the **Engagement** tab in a user's profile, you will see **Push Registered For** followed by an app name. If no app information exists for that device, you will see two dashes (**&#45;&#45;**). There will be an entry for every device that belongs to the user.

If the device entry's app name is prefixed by `Foreground:`, the app is authorized to receive both foreground push notifications (visible to the user) and background push notifications (not visible to the user) on that device.

![Push Changelog with an example push token.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

On the other hand, if the device entry's app name is prefixed by `Background:`, the app is only authorized to receive [background push]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) and cannot display user-visible notifications on that device. This usually indicates the user has disabled notifications for the app on that device.

If a push token is moved to a different user on the same device, that first user will no longer be push registered.

## Push token management

Check out the following chart for actions that lead to push tokens changes or removal from user profiles. 

| Action | Description |
| ------ | ----------- |
| `changeUser()` method called | The Braze `changeUser()` method switches the user ID that the SDKs are assigning user behavior data to. This method is usually called when a user logs into an application. When `changeUser()` is called with a different or new user ID on a specific device, that device's push token will be moved to the appropriate Braze profile with corresponding user ID. |
| Push error occurs | Some common push errors that lead to token removal include `MismatchSenderId`, `InvalidRegistration`, and other types of push bounces. <br><br>Check out our full list of common [push errors]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid). |
| User uninstalls | When a user uninstalls the application from a device, Braze will remove the user's push token from the profile. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### What does this look like on a broader scale?

When a user opens a new application and grants push access from a push prompt, a call is made from the Braze SDK to the push providers. When that call is made, the push provider runs a check to see if everything is set up correctly. If so, a push token gets passed into your device. When that token arrives, the SDK communicates this to Braze. After Braze has received the token from the push provider, we update or create a new user profile. These users are now considered registered.

If we want to launch a campaign, we create a campaign in Braze that generates a push payload to send to the push provider. From there, the provider delivers the push payload to the user's device and the SDK passes the messaging state to Braze.

![A flow chart that maps the aforementioned push process between Braze, the customer, and Apple Push Notification Service or Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

| Registration steps | Messaging steps |
| ------------------ | --------------- |
| 1. Customer (device) registers to push provider<br>2. Provider generates and delivers push token<br>3. Flush tokens in Braze |1. Braze sends push payload to provider<br>2. Provider delivers the push payload to the device<br>3. SDK passes messaging stats to Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### What happens when an opted-in user deletes and then redownloads my app?

Suppose a user opts-in for push, receives some push messaging, and then later deletes the app. This will remove the push consent at the device level. From here, the first bounced push after the uninstall will automatically result in that user being opted-out of future push messaging. After this, if a user were to reinstall the app but not launch it, Braze won't be able to send a push to the user because push tokens have not been re-granted for your app.

Additionally, if a user were to re-enable foreground push, it would require a session start to update this information in their user profile to begin receiving push messaging.
 
### When do push tokens expire? {#push-token-expire}

Unfortunately, APNs and FCM don't really define this. Push tokens can expire when an app is updated, when users transfer their data to a new device, or when they re-install an operating system. For the most part, we don't really have insight into why push providers will expire certain push tokens.

To account for that ambiguity, our SDK push integrations always register and flush tokens on session start to ensure we have the most up-to-date token.
