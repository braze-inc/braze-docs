---
nav_title: Rich Notifications
platform: Message_Building_and_Personalization
subplatform: Push
page_order: 4
---
# Rich Notifications

Rich Notifications allow for more customization in your push notifications by adding additional content beyond just copy. Android notifications have included images in push notifications for some time now, messaged as an ‘Expanded Notification Image’. Starting with iOS 10, your customers will be able to receive iOS push notifications that include gifs, images, videos, or audio.

![Rich Not Blog][7]

## Android Rich Notifications

### Requirements

- Note that expanded notification view is only available on devices using Jelly Bean (Android 4.1) or higher. If a user's device is not running on these systems, they will not see the notification image.
- Currently, Android rich notifications only allow for static images including jpg and png file formats.

### Setting Up Your Android Rich Notification

1. Follow the [campaign steps][3] you normally do to compose a push notification for Android. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

2. Add your Summary Text/ Image Caption that you'd like to display above the image in the notification.

	![Add Android Summary Text][9]

3. Add your image in the 'Expanded Notification Image' field in the composer of the message. Images can be uploaded directly through the dashboard or by specifying a content URL that is hosted elsewhere.

	![Add Android Image][8]

4. Once your rich notification content is uploaded to the dashboard, you can simply continue [scheduling your campaign][6] the way you always do.

## iOS 10 Rich Notifications

### Requirements

- To ensure your app is able to send rich notifications, please follow these instructions [here][1], as your developer will need to add a service extension to your app.
- You should also reference [Apple's documentation][2] for media limitations and specs. We recommend using as small of a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.
- File types that we currently support for direct uploading within our dashboard include jpg, png, or gif. These files can also be entered into the templatable URL field along with these additional file types: aif, m4a, mp3, mp4, or wav.

### Setting Up Your iOS Rich Notification

1. Follow the [campaign steps][3] you normally do to compose a push notification for iOS. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

2. Add your image, gif, audio, or video file in the 'Rich Notification Asset' field in the composer of the message. Please reference the above requirements on how to add your content files.

	![Add Image][4]

	You can also limit this message to only send to users who have a device that runs on iOS 10. For users who have not upgraded to iOS 10 it will appear as a text only notifications without the rich content if you leave the below box unchecked.

	![iOS 10 Checkbox][5]

3. Once your rich notification content is uploaded to the dashboard, you can simply continue [scheduling your campaign][6] the way you always do.

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/RichNot_AddImage.png %}
[5]: {% image_buster /assets/img_archive/RichNot_iOS10_select.png %}
[6]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %}
[8]: {% image_buster /assets/img_archive/Android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/Android_Rich_SummaryText.png %}
