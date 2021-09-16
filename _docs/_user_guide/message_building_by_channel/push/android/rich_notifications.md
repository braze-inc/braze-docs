---
nav_title: "Create Rich Notifications for Android"
article_title: Create Rich Push Notifications
page_order: 3
page_layout: tutorial
description: "This tutorial covers how to set up Android Rich notifications for your Braze Campaigns."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Create Rich Notifications for Android

> Rich Notifications allow for more customization in your push notifications by adding additional content beyond just copy. Android notifications have included images in push notifications for some time now, messaged as an ‘Expanded Notification Image’.

![Rich Not Blog][7]

## Requirements

- Note that the expanded notification view is only available on devices using Jelly Bean (Android 4.1) or higher. If a user's device is not running on these systems, they will not see the notification image.
- Android Extended Notification images must be 2:1 ratio, but __do not have a size limit__. 
- Android also allows for setting a separate image for the standard notification view. <br>Recommended size images: 512x256 for Small, 1024x512 for Medium, and 2048x1024 for Large.
- Currently, Android rich notifications only allow for static images including jpg and png file formats, gifs and other image formats are not yet supported.

{% alert note %}
While Braze provides instructions on how to set up rich push, that actual rendering of rich push notifications can vary depending on outside factors such as device aspect ratio, android version, OEM- specific constraints, etc. 
<br><br>
We recommend doing a send test to multiple Android devices to make sure your rich push notifications are appearing as you intend them to.
{% endalert %}


## Setting Up Your Android Rich Notification

### Step 1: Create Campaign
Follow the [campaign steps][3] you normally do to compose a push notification for Android. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

### Step 2: Add Captioning
Add the **Summary Text/Image Caption** that you'd like to display above the image in the notification.

![Add Android Summary Text][9]

### Step 3: Add Media
Add your image in the **Expanded Notification Image** field in the composer of the message. Images can be uploaded directly through the dashboard or by specifying a content URL that is hosted elsewhere.

![Add Android Image][8]

### Step 4: Continue Creating Your Campaign
Once your rich notification content is uploaded to the dashboard, you can simply continue [scheduling your campaign][6] the way you always do.

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %}
[8]: {% image_buster /assets/img_archive/android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/android_rich_summarytext.png %}
