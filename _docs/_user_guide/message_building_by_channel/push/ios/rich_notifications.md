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

- To ensure your app can send rich notifications, please follow the [iOS push integration][1] instructions, as your developer will need to add a service extension to your app.
- You should also reference [Apple's documentation][2] for media limitations and specs.

> As of January 2020, iOS Rich Push notifications can handle images 1038x1038 as long as they are under 10MB, but we recommend using as small a file size as possible. In practice, sending large files can cause both unnecessary network stress and make download timeouts more common.

- iOS will scale images to fit in the screen and will scale Rich images for the active/locked view.
- File types that we currently support for direct uploading within our dashboard include JPG, PNG, or GIF. These files can also be entered into the templatable URL field along with these additional file types: AIF, M4A, MP3, MP4, or WAV.

### Character count

While we can't provide a hard and fast rule for the precise number of characters to include in a push, we [provide some guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications) to consider while designing iOS messages. There may be some variance depending on the presence of an image, the notification state and display setting of the user's device, as well as the size of the device. 

When in doubt, keep it short and sweet. Play it safe, targeting about 30–40 characters per line for both the message title and body.

#### Notification states

Your users may view push notifications in a variety of different situations, and could see different lengths of text as follows.

<table>
<thead>
  <tr>
    <th>Lock screen or Notification Center</th>
    <th>Expanded</th>
    <th>Device active</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">This is the most common scenario.<br><br><b>Title:</b> 1 line of text<br><b>Body:</b> 4 lines of text<br><b>Image:</b> square thumbnail</td>
    <td width="33%">When a user long-presses a message.<br><br><b>Title:</b> 1 line of text<br><b>Body:</b> 7 lines of text<br><b>Image:</b> 2:1 aspect ratio (recommended, see note below)</td>
    <td width="33%">When a user receives a push while their phone is unlocked and active.<br><br><b>Title:</b> 1 line of text<br><b>Body:</b> 2 lines of text</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Example push notifications for push displayed on the lock screen, when expanded, and when device is active]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
While we recommend a 2:1 aspect ratio for expanded push notifications, nearly any aspect ratio is supported. Images will always span the full width of the notification, and the height will adjust accordingly.
{% endalert %}

#### Variables in text truncation

When creating content, consider the following scenarios that may impact how much text is displayed.

{% tabs %}
{% tab Timing %}

##### Timing

Depending on when a user engages with a push notification, the timestamp can shorten the title text.

![Example push notification with a timestamp of "now" and title character count of 35]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Title character count: **35**

![Example push notification with a timestamp of "3h ago" and title character count of 33]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Title character count: **33**

![Example push notification with a timestamp of "Yesterday, 8:37 AM" and title character count of 22]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Title character count: **22**

{% endtab %}
{% tab Images %}

##### Images

Body text is shortened by about 10 characters per line when an image is present.

![Example push notification with no image and a body character count of 179]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Body character count: **179**

![Example push notification with an image and a body character count of 154]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Body character count: **154**

{% endtab %}
{% tab Interruption level %}

##### Interruption level (iOS 15)

Time Sensitive and Critical denotations push the title down to a new line without the timestamp, giving it a little more space.

![Example push notification with no Time Sensitive or Critical denotation and a title character count of 35]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Title character count: **35**

![Example push notification with a Time Sensitive denotation and a title character count of 39]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Title character count: **39**

{% endtab %}
{% tab More %}

##### And more

The following also impact text truncation:

- **Phone display settings:** a user can increase or decrease the global UI font size on their phone, typically for accessibility reasons.
- **Device width:** the message could be displayed on a small phone, or a wide iPad.
- **Content types:** emojis and wide characters like "m" and "w" take up more space than "i" or "t", and longer words like "engagement" may line-wrap more abruptly than shorter words.

{% endtab %}
{% endtabs %}

## Setting up your iOS rich notification

### Step 1: Create a campaign

Follow the [campaign steps][3] you normally do to compose a push notification for iOS. You will be using the same composer that you use for setting up push notifications that do not contain rich content.

### Step 2: Add media

Add your image, GIF, audio, or video file in the **Rich Notification Asset** field in the composer of the message. Refer to the [requirements](#requirements) on how to add your content files.

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
