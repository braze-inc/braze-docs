---
nav_title: "Advanced Push Campaign Settings"
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

A **"Notification ID"** is a unique identifier for a message category of your choosing that informs the messaging service to only respect the most recent message from that ID. Setting a Notification ID allows you to send just the most recent and relevant message, rather than a stack of outdated, irrelevant ones.

## Time to live (TTL) {#ttl}

The **"Time to Live"** (TTL) field allows you to set a custom length of time to store messages with the push messaging service. Braze's default values for time to live are 4 weeks for FCM and 31 days for ADM. 

For example, suppose your app is a game and you offer your users an in-game currency bonus if they maintain a streak of playing the game daily. You could send a push alerting a user that that streak is in danger of being broken if they’ve exceeded a certain number of days. However, if a user was to reconnect their device to the game app 4 weeks later with the time to live set to the default, then those messages would have already expired in the messaging service and would not be delivered.

## Firebase messaging delivery priority {#fcm-priority}

The **Firebase Messaging Delivery Priority** field lets you control whether a push is sent with "normal" or "high" priority to Firebase Cloud Messaging. See [FCM documentation](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) to learn more.

## Summary text

The summary text allows you to set additional text in the **Expanded Notification** view. The summary text will display under the body of the message in the expanded view. It also serves as a caption for notifications with images.

![][9]

For push notifications that include images, the message text will be shown in the collapsed view, while the summary text will be displayed as the image caption when the notification is expanded. Check out the following animation for an example of this behavior.

![Summary Text Behavior][15]

## Custom URIs

The **Custom URI** feature allows you to specify a Web URL or an Android resource to navigate to when the notification is clicked. If no custom URI is specified, clicking on the notification brings users into your app. You can use the custom URI to deep-link inside your app as well as direct users to resources that exist outside of your app as well. This can be specified via our [Messaging API][13] or in the **Settings** in the push composer wizard.

> To enable Custom URI, your app's `BroadcastReceiver` must be configured to properly handle opening the URI.  This involves parsing incoming message contents for the custom URI and navigating to it.  Our [example receiver][14] provides a sample implementation.

![Custom URI][12]

## Notification display priority

{% alert important %}
The Notification Display Priority setting is no longer used on devices running Android O or newer. For newer devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

The priority level of a push notification affects how your notification is displayed in the notification tray relative to other notifications. It can also affect the speed and manner of delivery, as normal and lower priority messages may be sent with slightly higher latency or batched to preserve battery life, whereas high priority messages are always sent immediately.

This feature is useful for differentiating your messages based on how critical or time-sensitive they are. For example, a notification about dangerous road conditions would be a good candidate to receive a high priority, while a notification about an ongoing sale should receive a lower priority. You should consider whether or not using a disruptive priority is actually necessary for the notification that you are sending, as constantly taking the top spot in your users' inbox or interrupting their other activities may have a negative impact.

In Android O, notification priority became a property of notification channels. You will need to work with your developer to define the priority for a channel during its configuration and then use the dashboard to select the proper channel when sending your notification sounds. For devices running versions of Android before O, specifying a priority level for Android and Fire OS notifications is possible via the Braze dashboard and Messaging API.

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration][17] (to target O+ devices) and send the individual priority from the dashboard (to target &#60;O devices).

Refer to the following table for priority levels that you can set on Android or Fire OS push notifications:

| Priority | Description| `priority` value (for API messages) |
|------|-----------|----------------------------|
| Max | Urgent or time-critical messages. | `2` |
| High | Important communication, such as a new message from a friend. | `1` |
| Default | Most notifications. Use if your message doesn't explicitly fall under any of the other priority types. | `0` |
| Low | Information that you want users to know about but does not require immediate action. | `-1`|
| Min | Contextual or background information. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

For more information, refer to Google's documentation on [Android notifications][2].

## Notification sounds

In Android O, notification sounds became a property of notification channels. You will need to work with your developer to define the sound for a channel during its configuration and then use the dashboard to select the proper channel when sending your notifications.

For devices running versions of Android before Android O, Braze allows you to set the sound of an individual push message through the dashboard composer. You can do so by specifying a local sound resource on the device (e.g., `android.resource://com.mycompany.myapp/raw/mysound`). 

Selecting **Default** in this field will play the default notification sound on the device. This can be specified via our [Messaging API][13] or in the **Settings** in the push composer wizard.

![][11]

Next, enter the full sound resource URI (e.g., `android.resource://com.mycompany.myapp/raw/mysound`) into the dashboard prompt.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration][16] (to target O+ devices) and send the individual sound from the dashboard (to target &#60;O devices).

[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[14]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/java/com/braze/custombroadcast/CustomBroadcastReceiver.java
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
[17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels