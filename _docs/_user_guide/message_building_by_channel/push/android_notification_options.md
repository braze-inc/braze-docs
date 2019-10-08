---
nav_title: Android Notification Options
platform: Message_Building_and_Personalization
subplatform: Push
page_order: 0.1
---

# Android Notification Options

If you want to categorize your messages and group them in your user's notification tray, you can utilize Androids's Notification Channels feature through Braze.

Create your Android Push Campaign, then look to the top of the composer. There, you'll see a dropdown labeled Notification Channels.

![notificationchanneldropdown][28]

From there, you can select any Notification Channels. You must select a Fallback channel in the event that your notification channel settings malfunction.

If you don't have any [Notification Channels]({{ site.baseurl }}/user_guide/message_building_by_channel/push/notification_channels/) listed here, you can add one using the Notification Channel ID. Contact your developers to identify what your Notification Channel IDs are or to create new IDs as needed. Then, add it to your Notification Channels by clicking __Manage Notification Channel__ in the dropdown and filling out the required fields in the __Manage Android Push Notification Channels__ window that appears. Notification Channels must be defined on the app before they may be used in the Braze platform.

![managenotchannel][29]
