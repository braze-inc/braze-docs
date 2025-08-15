---
nav_title: "Advanced push campaign settings"
article_title: Advanced Push Campaign Settings
page_order: 5
page_layout: reference
description: "This reference article covers some Advanced Push Campaign settings like priority, custom URLs, delivery options, and more."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Advanced push campaign settings

> There are many advanced settings available for Android and Fire OS push notifications sent through the Braze dashboard. This article will describe these features and how to use them successfully.

## Notification ID {#notification-id}

A notification ID is a unique identifier for a message category of your choosing that informs the messaging service to only respect the most recent message from that ID. Setting a notification ID allows you to send just the most recent and relevant message, rather than a stack of outdated, irrelevant ones.

To assign a notification ID, navigate to the composition page of the push you'd like to add the ID to select the **Settings** tab. Enter an integer in the **Notification ID** section. To update this notification after you've issued it, send another notification with the same ID that you used previously.

![Notification ID field.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Time to live (TTL) {#ttl}

The **Time to Live** field allows you to set a custom length of time to store messages with the push messaging service. If the device remains offline beyond the TTL, the message will expire and not be delivered.

To edit the time to live for your Android push, go to the composer and select the **Settings** tab. Find the **Time to Live** field and enter a value in days, hours, or seconds.

The default values for time to live are defined by your admin on the [Push Settings]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/) page. By default, Braze sets Push TTL to the maximum value for each push messaging service. While default TTL settings apply globally, you can override them at the message level during campaign creation. This is helpful when different campaigns require varying urgency or delivery windows.

For example, let's say your app hosts a weekly trivia contest. You send a push notification an hour before it starts. By setting the TTL to 1 hour, you make sure that users who open the app after the contest starts won’t receive a notification about an event that has already begun.

{% details Best practices %}

#### When to use shorter TTL

Shorter TTLs make sure users receive timely notifications for events or promotions that quickly lose relevance. For example:

- **Retail:** Sending a push for a flash sale that ends in 2 hours (TTL: 1–2 hours)
- **Food delivery:** Notifying users when their order is nearby (TTL: 10–15 minutes)
- **Transportation apps:** Sharing ride arrival updates (TTL: a few minutes)
- **Event reminders:** Notifying users when a webinar is starting soon (TTL: under 1 hour)

#### When to avoid shorter TTL

- If your campaign’s message remains relevant for several days or weeks, such as subscription renewal reminders or ongoing promotions.
- When maximizing reach is more important than urgency, like with app update announcements or feature promotions.

{% enddetails %}

## Firebase messaging delivery priority {#fcm-priority}

The **Firebase Messaging Delivery Priority** field lets you control whether a push is sent with "normal" or "high" priority to Firebase Cloud Messaging. This setting determines how quickly messages are delivered and how they affect device battery life.

| Priority | Description | Best for |
|---------|-------------|----------|
| Normal | Battery-optimized delivery that may be delayed to conserve battery | Non-urgent content, promotional offers, news updates |
| High | Immediate delivery with higher battery consumption | Time-sensitive notifications, critical alerts, live event updates, account alerts, breaking news, or urgent reminders |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Considerations

- **Default setting**: You can set a default FCM priority for all Android campaigns in your [Push Settings]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). This campaign-level setting will override the default if needed.
- **Deprioritization**: If FCM detects that your app frequently sends high-priority messages that don't result in user-visible notifications or user engagement, those messages may be automatically deprioritized to normal priority.
- **Battery impact**: High-priority messages wake sleeping devices more aggressively and consume more battery. Use this priority judiciously.

For more detailed information on message handling and deprioritization, see [FCM documentation](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) and [Message handling and deprioritization on Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Summary text

The summary text allows you to set additional text in the expanded notification view. It also serves as a caption for notifications with images.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

The summary text will display under the body of the message in the expanded view. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

For push notifications that include images, the message text will be shown in the collapsed view, while the summary text will be displayed as the image caption when the notification is expanded. 

## Custom URIs

The **Custom URI** feature allows you to specify a Web URL or an Android resource to navigate to when the notification is clicked. If no custom URI is specified, clicking on the notification brings users into your app. You can use the custom URI to deep-link inside your app as well as direct users to resources that exist outside of your app as well. This can be specified via our [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) or in the **Compose** tab of the the push composer.

![Custom URI field.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Notification display priority

{% alert important %}
The Notification Display Priority setting is no longer used on devices running Android O or newer. For newer devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

The priority level of a push notification affects how your notification is displayed in the notification tray relative to other notifications. It can also affect the speed and manner of delivery, as normal and lower priority messages may be sent with slightly higher latency or batched to preserve battery life, whereas high priority messages are always sent immediately.

This feature is useful for differentiating your messages based on how critical or time-sensitive they are. For example, a notification about dangerous road conditions would be a good candidate to receive a high priority, while a notification about an ongoing sale should receive a lower priority. You should consider whether or not using a disruptive priority is actually necessary for the notification that you are sending, as constantly taking the top spot in your users' inbox or interrupting their other activities may have a negative impact.

In Android O, notification priority became a property of notification channels. You will need to work with your developer to define the priority for a channel during its configuration and then use the dashboard to select the proper channel when sending your notification sounds. For devices running versions of Android before O, specifying a priority level for Android and Fire OS notifications is possible via the Braze dashboard and Messaging API.

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance) (to target O+ devices) and send the individual priority from the dashboard (to target &#60;O devices).

Refer to the following table for priority levels that you can set on Android or Fire OS push notifications:

| Priority | Description| `priority` value (for API messages) |
|------|-----------|----------------------------|
| Max | Urgent or time-critical messages. | `2` |
| High | Important communication, such as a new message from a friend. | `1` |
| Default | Most notifications. Use if your message doesn't explicitly fall under any of the other priority types. | `0` |
| Low | Information that you want users to know about but does not require immediate action. | `-1`|
| Min | Contextual or background information. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more information, refer to Google's documentation on [Android notifications](http://developer.android.com/design/patterns/notifications.html).

## Push category

Android push notifications provide the option to specify if your notification falls into a predefined category. The Android system UI may use this category to make ranking or filtering decisions about where to place the notification in the user's notification tray.

![Settings tab with the Category set to None, which is the default setting.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Category | Description |
|---|-------|
| None | Default option. |
| Alarm | Alarm or timer. |
| Call | Incoming call (voice or video) or similar synchronous communication request. |
| Email | Asynchronous bulk message (email). |
| Error | Error in background operation or authentication status. |
| Event | Calendar event. |
| Message | Incoming direct message (SMS, instant message, etc.). |
| Progress | Progress of a long-running background operation. |
| Promotion | Promotion or advertisement. |
| Recommendation | A specific, timely recommendation for a single thing. |
| Reminder | User-scheduled reminder. |
| Service | Indication of running background service. |
| Social | Social network or sharing update. |
| Status | Ongoing information about device or contextual status. |
| System | System or device status update. Reserved for system use. |
| Transport | Media transport control for playback. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Push visibility

Android push notifications provide an optional field to determine how a notification appears on the user's lock screen. Refer to the following table for visibility options and descriptions.

| Visibility | Description |
|---|-----|
| Public | Notification appears on the lock screen |
| Private | Notification is shown with "Content hidden" as the message |
| Secret | Notification is not shown on the lock screen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Additionally, Android users can override how push notifications appear on their lock screen by changing the notification privacy setting on their device. This setting will override the visibility from the push notification.

![Dashboard push priority location with Set Visibility enabled and set to Private.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Regardless of the visibility, all notifications will be shown on the user's lock screen if the notification privacy setting on their device is **Show all content** (default setting). Likewise, notifications will not be shown on their lock screen if their notification privacy is set to **Do not show notifications**. The visibility only has an effect if their notification privacy is set to **Hide sensitive content**.

The visibility has no effect on devices earlier than Android Lollipop 5.0.0, meaning all notifications will be shown on these devices.

Refer to our [Android documentation](https://developer.android.com/guide/topics/ui/notifiers/notifications) for more information.

## Notification sounds

In Android O, notification sounds became a property of notification channels. You will need to work with your developer to define the sound for a channel during its configuration and then use the dashboard to select the proper channel when sending your notifications.

For devices running versions of Android before Android O, Braze allows you to set the sound of an individual push message through the dashboard composer. You can do so by specifying a local sound resource on the device (for example, `android.resource://com.mycompany.myapp/raw/mysound`). 

Selecting **Default** in this field will play the default notification sound on the device. This can be specified via our [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) or in the **Settings** in the push composer.

![The "Sound" field.]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Next, enter the full sound resource URI (for example, `android.resource://com.mycompany.myapp/raw/mysound`) into the dashboard prompt.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration](https://developer.android.com/training/notify-user/channels) (to target O+ devices) and send the individual sound from the dashboard (to target &#60;O devices).

