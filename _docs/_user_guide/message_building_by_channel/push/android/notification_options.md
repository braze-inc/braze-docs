---
nav_title: "Notification Options (Android)"
page_order: 2
page_type: reference
description: "This reference article covers several Android notification options and how to best use them within Braze campaigns."

platform: Android
channel:
  - Push
tool:
  - Dashboard
---

# Android Notification Options

> If you want to categorize your messages and group them in your user's notification tray, you can utilize Android's Notification Channels feature through Braze.

Create your Android Push Campaign, then look to the top of the composer. There, you'll see a dropdown labeled Notification Channels.

![notificationchanneldropdown][28]

From there, you can select any Notification Channels. You must select a Fallback channel in the event that your notification channel settings malfunction.

If you don't have any [Notification Channels]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) listed here, you can add one using the Notification Channel ID. Contact your developers to identify what your Notification Channel IDs are or to create new IDs as needed. Then, add it to your Notification Channels by clicking __Manage Notification Channel__ in the dropdown and filling out the required fields in the __Manage Android Push Notification Channels__ window that appears. Notification Channels must be defined on the app before they may be used in the Braze platform.

![managenotchannel][29]


[28]: {% image_buster /assets/img_archive/notchannclickdropdown.gif %}
[29]: {% image_buster /assets/img_archive/notchannels.png %}
