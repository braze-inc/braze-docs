---
nav_title: "Notification Options (Android)"
article_title: Push Notification Options
page_order: 2
page_type: reference
description: "This reference article covers several Android notification options and how to best use them within Braze campaigns."

platform: Android
channel:
  - Push

---

# Android notification options

> If you want to categorize your messages and group them in your user's notification tray, you can utilize Android's Notification Channels feature through Braze.

Create your Android push campaign, then look to the top of the **Compose** tab for the **Notification Channel** dropdown.

![notificationchanneldropdown][28]{: style="max-width:60%;" }

Select your Notification Channel from the dropdown. You must also select a fallback channel in the event that your Notification Channel settings malfunction.

If you don't have any [Notification Channels]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) listed here, you can add one using the Notification Channel ID. Contact your developers to identify what your Notification Channel IDs are or to create new IDs as needed. 

To add a Notification ID to your Notification Channel, click **Manage Notification Channel** in the **Notification Channel** dropdown and fill out the required fields. Notification Channels must be defined on the app before they can be used in the Braze platform.

![managenotchannel][29]{: style="max-width:80%;" }


[28]: {% image_buster /assets/img_archive/notification_channel_dropdown.png %}
[29]: {% image_buster /assets/img_archive/notification_channels.png %}
