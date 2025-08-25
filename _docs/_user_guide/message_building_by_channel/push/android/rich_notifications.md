---
nav_title: "Creating rich notifications"
article_title: "Creating rich push notifications for Android"
page_order: 3
page_layout: tutorial
description: "This tutorial covers how to set up Android Rich notifications for your Braze campaigns."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Creating rich push notifications for Android

> Rich notifications allow for more customization in your push notifications by adding additional content beyond just copy. Android notifications have included images in push notifications for some time now, referred to as an "expanded notification image."

## Prerequisites

Before you create a rich push notification for Android, note the following details:

- Android rich notifications aren't available when creating a quick push campaign.
- Android Extended Notification images must be 2:1 ratio, but do not have a size limit.
- Android also allows for setting a separate image for the standard notification view. These are the recommended size images: 
  - **Small:** 512x256
  - **Medium:** 1024x512 
  - **Large:** 2048x1024
- Currently, Android rich notifications only allow for static images, including JPEG and PNG image formats. GIF and other image formats are not yet supported.
- Adding action buttons to your push notification may affect the area of the image that is displayable. Test with the dashboard preview and live devices to confirm that results are as expected.
- The Braze Android SDK must be enabled for the image to render.

{% alert note %}
While Braze provides instructions on how to set up rich push, the actual rendering of rich push notifications can vary depending on outside factors such as device aspect ratio, Android version, OEM-specific constraints, and others. We recommend doing a send test to multiple Android devices to make sure your rich push notifications appear as you intend them to.
{% endalert %}

## Setting up your Android rich notification

### Step 1: Create a push campaign

Follow the steps to [create a campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) to compose a push notification for Android. You will be using the same composer for setting up push notifications that don't contain rich content.

### Step 2: Add captioning

Add the **Summary Text/Image Caption** that you'd like to display before the image in the notification.

![The Expanded notification image section where you can add an image or enter an image URL.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Step 3: Add media

Add your image in the **Expanded Notification Image** field in the composer of the message. Images can be uploaded directly through the dashboard or by specifying a content URL that is hosted elsewhere.

For details about supported images, check out [Image specifications]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![A user receives a push notification for iOS with "Hi there" as the title and "Thanks for joining out loyalty program!" as the text.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Step 4: Continue creating your campaign

After your rich notification content is uploaded to the dashboard, you can continue [scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

