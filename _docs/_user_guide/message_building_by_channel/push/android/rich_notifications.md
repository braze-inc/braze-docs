---
nav_title: "Create Rich Notifications for Android"
page_order: 9
page_layout: tutorial
description: "This tutorial covers how to set up Android Rich notifications for your Braze Campaigns."

platform: Android
channel:
  - Push
tool:
  - Docs
  - Dashboard
  - Campaigns
---

# Create Rich Notifications for Android

> Rich Notifications allow for more customization in your push notifications by adding additional content beyond just copy. Android notifications have included images in push notifications for some time now, messaged as an ‘Expanded Notification Image’.

![Rich Not Blog][7]

## Requirements

- Note that the expanded notification view is only available on devices using Jelly Bean (Android 4.1) or higher. If a user's device is not running on these systems, they will not see the notification image.
- Currently, Android rich notifications only allow for static images including jpg and png file formats.

## Setting Up Your Android Rich Notification

### Step 1: Create Campaign
Follow the [campaign steps][3] you normally do to compose a push notification for Android. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

### Step 2: Add Captioning
Add your Summary Text/ Image Caption that you'd like to display above the image in the notification.

    ![Add Android Summary Text][9]

### Step 3: Add Media
Add your image in the 'Expanded Notification Image' field in the composer of the message. Images can be uploaded directly through the dashboard or by specifying a content URL that is hosted elsewhere.

    ![Add Android Image][8]

### Step 4: Continue Creating Your Campaign
Once your rich notification content is uploaded to the dashboard, you can simply continue [scheduling your campaign][6] the way you always do.

[3]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %}
[8]: {% image_buster /assets/img_archive/Android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/Android_Rich_SummaryText.png %}
