---
nav_title: "Rich Notifications for Android"
article_title: Rich Notifications for Android
page_order: 3
page_layout: tutorial
description: "This tutorial covers how to set up Android Rich notifications for your Braze Campaigns."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Creating rich notifications for Android

> Rich notifications allow for more customization in your push notifications by adding additional content beyond just copy. Android notifications have included images in push notifications for some time now, referred to as an "expanded notification image".

## Requirements

- Note that the expanded notification view is only available on devices using Jelly Bean (Android 4.1) or later. If a user's device is not running on these systems, they will not see the notification image.
- Android Extended Notification images must be 2:1 ratio, but do not have a size limit.
- Android also allows for setting a separate image for the standard notification view. <br>Recommended size images: 512x256 for Small, 1024x512 for Medium, and 2048x1024 for Large.
- Currently, Android rich notifications only allow for static images including jpg and png file formats, gifs and other image formats are not yet supported.
- Note, adding Action Buttons to your push notification may affect the area of the image that is displayable. Test with the dashboard preview and live devices to ensure that results are as expected.

{% alert note %}
While Braze provides instructions on how to set up rich push, that actual rendering of rich push notifications can vary depending on outside factors such as device aspect ratio, android version, OEM- specific constraints, etc. 
<br><br>
We recommend doing a send test to multiple Android devices to make sure your rich push notifications are appearing as you intend them to.
{% endalert %}

## Setting up your Android rich notification

### Step 1: Create campaign

Follow the steps to [create a campaign][3] to compose a push notification for Android. You will be using the same composer for setting up push notifications that don't contain rich content.

### Step 2: Add captioning

Add the **Summary Text/Image Caption** that you'd like to display before the image in the notification.

![][9]

### Step 3: Add media

Add your image in the **Expanded Notification Image** field in the composer of the message. Images can be uploaded directly through the dashboard or by specifying a content URL that is hosted elsewhere.

![][8]

### Step 4: Continue creating your campaign

Once your rich notification content is uploaded to the dashboard, you can simply continue [scheduling your campaign][6].

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[8]: {% image_buster /assets/img_archive/android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/android_rich_summarytext.png %}
