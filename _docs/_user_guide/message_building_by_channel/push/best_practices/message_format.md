---
nav_title: Message Formats
article_title: Push Message and Image Formats
page_order: 5
page_type: reference
description: "This article describes message and image formats for push notifications."
channel: push

---

# Push message and image formats

> This reference article describes message and image formats for push notifications.

For best results, refer to the following image size and message length guidelines when crafting your push messages. There may be some variance depending on the presence of an image, the notification state (iOS) and display setting of the user's device, as well as the size of the device. When in doubt, keep your copy short and sweet.


## iOS

{% tabs local %}
{% tab General %}

- **Message Length:**
  - iOS Lock Screen: 110 Characters
  - iOS Notification Center: 110 Characters
  - iOS Banner Alert: 62 Characters
  - iOS Pop Up Alert: 235 Characters
- **Payload Size:**
  - iOS: 2&nbsp;KB 
- **Number of Lines:**
  - iOS Lock Screen: 4 Lines
  - iOS Notification Center: 4 Lines
  - iOS Banner Alert: 2 Lines
  - iOS Pop Up Alert: 8 Lines
- **Customizable UI:** No
- **Deep Link Capable:** Yes

{% alert tip %}
Wondering how many characters you can use in an iOS push notification without it being truncated? Check out our [iOS character count guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).
{% endalert %}

{% endtab %}
{% tab Image Sizes %}

|    Aspect Ratio   | Recommended Image Size | Maximum Image Size |   File Types  |
|:-----------------:|:----------------------:|:------------------:|:-------------:|
| 2:1 (recommended) |          500&nbsp;KB         |         5&nbsp;MB        | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Text Example %}

![iOS push notification with text that reads: "Hi! This is an iOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endtab %}
{% tab Image Example %}

![iOS push notification with text that reads: "Hi! This is an iOS Push with an image" with an emoji. There is a small image beside the text.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS push notification on a hard push with the same text as the previous message with an expanded image preceding the text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

## Android

{% tabs local %}
{% tab General %}

- **Message Length:**
  - Lock Screen: 1 line (estimated 49 characters max)
  - Notification Drawer: 1 line, up to 8 lines when expanded (estimated 597 characters max)
- **Payload Size:**
  - FCM: 4&nbsp;KB 
- **Customizable UI:** Yes
- **Deep Link Capable:** Yes

{% endtab %}
{% tab Image Sizes %}

#### Push icon

|         Aspect Ratio         | Recommended Image Size |                         Maximum Image Size                         | File Types |
|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
| 1:1 (400x400 pixels minimum) |          500&nbsp;KB         | N/A - however a balance should be  struck between quality and size |  PNG, JPG  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

#### Expanded notification image

|         Aspect Ratio         | Recommended Image Size |                         Maximum Image Size                         | File Types |
|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
| 2:1 (600x300 pixels minimum) |          500&nbsp;KB         | N/A - however a balance should be  struck between quality and size |  PNG, JPG  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
Smaller, high quality images will load faster, so it's recommended to use the smallest asset possible to achieve your desired output.
{% endalert %}

{% endtab %}
{% tab Text Example %}

![Android push notification displayed on the home screen.]({% image_buster /assets/img_archive/Push_Android_2.png %})

{% endtab %}
{% tab Image Example %}

![Android push notification with a large image under the message text.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Large image notifications display best when using an image of at least 600x300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

## Web

{% tabs local %}
{% tab General %}

- **Message Length:** Message length for web push notifications varies depending on the both the platform and browser that the user views your message from. Refer to the following table for details.
- **Customizable UI:** Yes
- **Deep Link Capable:** No

#### Message length

| **Browser** | **Platform** | **Maximum Title Length**  | **Maximum Message Body Length**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Image sizes %}

| **Browser** | **Recommended Icon Size**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Icons are configurable on a per-campaign basis with Safari 16 on macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **Browser** | **Platform** | **Large Image Size**
| --- | --- | ---
Chrome | Android | 2:1 aspect ratio
Firefox | Android | N/A
Chrome | Windows | 2:1 aspect ratio
Edge | Windows | 2:1 aspect ratio
Firefox | Windows | N/A
Firefox | Windows | 2:1 aspect ratio
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}
