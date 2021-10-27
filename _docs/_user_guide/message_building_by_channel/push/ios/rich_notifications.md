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

# Create iOS rich notifications

> Rich Notifications allow for more customization in your push notifications by adding additional content beyond copy. Android notifications have included images in push notifications for some time now, messaged as an ‘Expanded Notification Image’. Starting with iOS 10, your customers will be able to receive iOS push notifications that include GIFs, images, videos, or audio.

![Rich Not Blog][7]

## Requirements

- To ensure your app can send rich notifications, please follow the [ios push integration][1] instructions, as your developer will need to add a service extension to your app.
- You should also reference [Apple's documentation][2] for media limitations and specs.

> As of January 2020, iOS Rich Push notifications can handle images 1038x1038 as long as they are under 10MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.

- iOS will scale images to fit in the screen and will scale Rich images for the active/locked view.
- File types that we currently support for direct uploading within our dashboard include JPG, PNG, or GIF. These files can also be entered into the templatable URL field along with these additional file types: AIF, M4A, MP3, MP4, or WAV.

### Character count

While there is no hard and fast rule for the exact number of characters to include in a push notification, we [provide some guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications) to consider while designing iOS messages. There may be some variance depending on the presence of an image, the notification state and display setting of the user's device, as well as the size of the device.

The following may impact how text is displayed in a push notification:

- Image thumbnails take over about 10 characters per line.
- Notification states affect how the user views the notification:
  - Messages on lock screen or in notification center will display four lines of text.
  - Messages on active devices will display two lines of text.
  - If a user long taps a message, they will see seven lines of text in the expanded view.
- Users can increase or decrease the global font size on their phone for accessibility reasons.
- Messages can be displayed differently based on device size (ie. narrow phone vs wide iPad).

Wondering how many characters you can use in a push notification without it being truncated? Check out our [iOS push notification design guide]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/push_design_guide/).

> As a general rule of thumb, Braze recommends keeping each line of text for both the optional title and message body to approximately 30-40 characters in a mobile push notification.

## Setting up your iOS rich notification

### Step 1: Create a campaign

Follow the [campaign steps][3] you normally do to compose a push notification for iOS. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

### Step 2: Add media

Add your image, gif, audio, or video file in the **Rich Notification Asset** field in the composer of the message. Refer to the [requirements](#requirements) on how to add your content files.

![Add Image][4]{: style="max-width:70%;" }

You can also limit this message to only send to users who have a device that runs on iOS 10. For users who have not upgraded to iOS 10, it will appear as text-only notifications without the rich content if you leave the box below unchecked.

![iOS 10 Checkbox][5]{: style="max-width:70%;" }

### Step 3: Continue creating your campaign

Once your rich notification content is uploaded to the dashboard, you can continue [scheduling your campaign][6] the way you always do.

When a user receives the push notification, they can hard press on the push message to expand the image.

![Rich Push Example][8]{: style="max-width:50%;" }

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/rich_notification_add_image.png %}
[5]: {% image_buster /assets/img_archive/rich_notification_ios10_select.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %}
[8]: {% image_buster /assets/img_archive/rich_notification_ios.gif %}
