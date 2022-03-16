---
nav_title: Android Push Best Practices
article_title: Android Push Best Practices
page_order: 0
page_type: reference
description: "This article covers additional best practices for Android push messages, including priority, category, and visiblity."
channel: push
platform: Android

---

# Android push best practices

## Android push priority

Android push notifications provide the option of dictating where notifications are displayed relative to other apps' notifications. When composing the message for your push campaign, select **Notification Display Priority** in the **Settings** tab to set a priority for your notification.

![][41]

The provided options correspond to different priorities with which the notification will be displayed if a receiving user has multiple notifications. A more in-depth explanation of Android push priority and the priority options can be found [here][40].

## Android push category

Android push notifications provide the option to specify if your notification falls into a predefined category. The Android system UI may use this category to make ranking or filtering decisions about where to place the notification in the user's notification tray.

![Settings tab t][52]

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
{: .reset-td-br-1 .reset-td-br-2}

## Android push visibility

Android push notifications provide an optional field to determine how a notification appears on the user's lock screen. Notifications can be set to appear on the lock screen *(Public)*, to appear with the message "Contents Hidden" *(Private)*, or to be hidden entirely *(Secret)*.

Additionally, Android users can override how push notifications appear on their lock screen by changing the notification privacy setting on their device. This setting will override the visibility from the push notification.

![Dashboard push priority location with Set Visibility enabled and set to Private.][53]{: style="float:right;max-width:60%;margin-left:15px;"}

Note that regardless of the visibility, all notifications will be shown on the user's lock screen if the notification privacy setting on their device is **Show all content** (default setting). Likewise, notifications will not be shown on their lock screen if their notification privacy is set to **Do not show notifications**. The visibility only has an effect if their notification privacy is set to **Hide sensitive content**. In that case, the notification will be displayed as follows:

* Public: Notification is shown on the lock screen
* Private: Notification is shown with "Contents hidden" as the message
* Secret: Notification is not shown on the lock screen

The visibility has no effect on devices earlier than Android Lollipop 5.0.0. All notifications will be shown on such devices.

Refer to our [Android documentation][51] for more information.

[40]: https://www.braze.com/blog/breakdown-android-lollipops-new-notification-priorities-push-flexibility/
[41]: {% image_buster /assets/img_archive/braze_default.png %}
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[51]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
