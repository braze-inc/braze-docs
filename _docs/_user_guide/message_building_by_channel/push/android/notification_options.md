---
nav_title: "Notification options"
article_title: Android Notification Options
page_order: 2
page_type: reference
description: "This reference article covers several Android notification options and how to best use them within Braze campaigns."

platform: Android
channel:
  - Push

---

# Notification options

> These are the some of the Android-specific push notification options available through Braze.

## Silent notifications

When you [compose your push notification message]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), you **cannot** send an Android push message without a title&#8212;however, you can enter a single space instead. Keep in mind, if your message only contains a single space, it will be sent as a silent push notification. For more information, see [Silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Notification groups

If you want to categorize your messages and group them in your user's notification tray, you can utilize Android's Notification Channels feature through Braze.

First, create your Android push campaign, then look to the top of the **Compose** tab for the **Notification Channel** dropdown.

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Select your Notification Channel from the dropdown. You must also select a fallback channel in the event that your Notification Channel settings malfunction.

If you don't have any [Notification Channels]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) listed here, you can add one using the Notification Channel ID. Contact your developers to identify what your Notification Channel IDs are or to create new IDs as needed. 

To add a Notification ID to your Notification Channel, click **Manage Notification Channel** in the **Notification Channel** dropdown menu and fill out the required fields. Notification Channels must be defined on the app before they can be used in the Braze platform.

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


