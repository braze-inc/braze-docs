---
nav_title: Additional Android Push Best Practices
page_order: 0

page_type: reference
description: "This article covers additional best practices for Android push messages, including priority, category, and visiblity."
channel: push
no_index: true
---

# Additional Android Push Best Practices

## Android Push Priority

Android push notifications provide the option of dictating where notifications are displayed relative to other apps' notifications.  When composing the message for your push campaign, select "Notification Priority" in the settings tab to set a priority for your notification.

![Dashboard Push Priority Location][41]

The provided options correspond to different priorities with which the notification will be displayed if a receiving user has multiple notifications. A more in-depth explanation of Android Push Priority and the priority options can be found [here][40].

## Android Push Category
Android push notifications provide the option to specify if your notification falls into a predefined category. The Android system UI may use this Category to make ranking or filtering decisions about where to place the notification in the user's notification tray.

![Dashboard Push Priority Location][52]

| Category       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| None           | Default                                                                     |
| Alarm          | Alarm or timer                                                              |
| Call           | Incoming call (voice or video) or similar synchronous communication request |
| Email          | Asynchronous bulk message (email)                                           |
| Error          | Error in background operation or authentication status                      |
| Event          | Calendar event                                                              |
| Message        | Incoming direct message (SMS, instant message, etc.)                        |
| Progress       | Progress of a long-running background operation                             |
| Promotion      | Promotion or advertisement                                                  |
| Recommendation | A specific, timely recommendation for a single thing                        |
| Reminder       | User-scheduled reminder                                                     |
| Service        | Indication of running background service                                    |
| Social         | Social network or sharing update                                            |
| Status         | Ongoing information about device or contextual status                       |
| System         | System or device status update. Reserved for system use.                    |
| Transport      | Media transport control for playback                                        |
{: .reset-td-br-1 .reset-td-br-2}


[See Android Documentation for more info][51]

## Android Push Visibility
Android push notifications provide an optional field to determine how a notification appears on the user's lock screen. Notifications can be set to appear on the lock screen *(Public)*, to appear with the message "Contents Hidden" *(Private)*, or to be hidden entirely *(Secret)*.

Additionally, Android users can override how push notifications appear on their lock screen by changing the notification privacy setting on their device. This setting will override the Visibility from the push notification.

![Dashboard Push Priority Location][53]

Note that regardless of the Visibility, all notifications will be shown on the user's lock screen if the notification privacy setting on their device is *Show all content* (default setting). Likewise, notifications will not be shown on their lock screen if their notification privacy is set to *Do not show notifications*. The Visibility only has an effect if their notification privacy is set to *Hide sensitive content*. In that case, the notification will be displayed as follows:

* *Public* - Notification is shown on the lock screen
* *Private* - Notification is shown with "Contents hidden" as the message
* *Secret* - Notification is **not** shown on the lock screen

The Visibility has no effect on devices earlier than Android Lollipop 5.0.0; all notifications will be shown on such devices.

[See Android Documentation for more info][50]

[40]: https://www.braze.com/blog/breakdown-android-lollipops-new-notification-priorities-push-flexibility/
[41]: {% image_buster /assets/img_archive/braze_default.png %}
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[50]: http://developer.android.com/design/patterns/notifications.html
[51]: http://developer.android.com/design/patterns/notifications.html
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
