---
nav_title: "Create Rich Notifications for iOS"
article_title: Create Rich Push Notifications
page_order: 3
page_type: tutorial
description: "This tutorial covers the requirements and steps on how to create iOS Rich Notifications for your Braze Campaigns."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Create iOS Rich Notifications

> Rich Notifications allow for more customization in your push notifications by adding additional content beyond just copy. Android notifications have included images in push notifications for some time now, messaged as an ‘Expanded Notification Image’. Starting with iOS 10, your customers will be able to receive iOS push notifications that include gifs, images, videos, or audio.

![Rich Not Blog][7]

## Requirements

- To ensure your app can send rich notifications, please follow these instructions [here][1], as your developer will need to add a service extension to your app.
- You should also reference [Apple's documentation][2] for media limitations and specs.<br>As of January 2020, iOS Rich Push notifications can handle images 1038x1038 as long as they are under 10MB, but we recommend using as small a file size as possible.<br>In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.
- iOS will scale images to fit in the screen and will scale Rich images for the active/locked view.
- File types that we currently support for direct uploading within our dashboard include jpg, png, or gif. These files can also be entered into the templatable URL field along with these additional file types: aif, m4a, mp3, mp4, or wav.

## Setting Up Your iOS Rich Notification

### Step 1: Create a Campaign
Follow the [campaign steps][3] you normally do to compose a push notification for iOS. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

### Step 2: Add Media
Add your image, gif, audio, or video file in the 'Rich Notification Asset' field in the composer of the message. Please reference the above requirements on how to add your content files.

![Add Image][4]

You can also limit this message to only send to users who have a device that runs on iOS 10. For users who have not upgraded to iOS 10, it will appear as text-only notifications without the rich content if you leave the box below unchecked.

![iOS 10 Checkbox][5]

### Step 3: Continue Creating Your Campaign
Once your rich notification content is uploaded to the dashboard, you can simply continue [scheduling your campaign][6] the way you always do.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/RichNot_AddImage.png %}
[5]: {% image_buster /assets/img_archive/RichNot_iOS10_select.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %}
