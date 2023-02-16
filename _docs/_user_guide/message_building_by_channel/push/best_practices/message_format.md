---
nav_title: Message Format
article_title: Push Message Format
page_order: 5
page_type: reference
description: "This article describes message and image formats for iOS and Android push notifications."
channel: push

---

# Message format

> This reference article describes message and image formats for iOS and Android push notifications.

## iOS

{% tabs local %}
{% tab General %}

- **Message Length:**
  - iOS Lock Screen: 110 Characters
  - iOS Notification Center: 110 Characters
  - iOS Banner Alert: 62 Characters
  - iOS Pop Up Alert: 235 Characters
- **Payload Size:**
  - iOS: 2KB
- **Number of Lines:**
  - iOS Lock Screen: 4 Lines
  - iOS Notification Center: 4 Lines
  - iOS Banner Alert: 2 Lines
  - iOS Pop Up Alert: 8 Lines
- **Customizable UI:** No
- **Deep Link Capable:** Yes

{% endtab %}
{% tab Image Sizes %}

|    Aspect Ratio   | Recommended Image Size | Maximum Image Size |   File Types  |
|:-----------------:|:----------------------:|:------------------:|:-------------:|
| 2:1 (recommended) |          500KB         |         5MB        | PNG, JPG, GIF |
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
  - FCM: 4KB
- **Customizable UI:** Yes
- **Deep Link Capable:** Yes

{% endtab %}
{% tab Image Sizes %}

#### Push icon

|         Aspect Ratio         | Recommended Image Size |                         Maximum Image Size                         | File Types |
|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
| 1:1 (400x400 pixels minimum) |          500KB         | N/A - however a balance should be  struck between quality and size |  PNG, JPG  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

#### Expanded notification image

|         Aspect Ratio         | Recommended Image Size |                         Maximum Image Size                         | File Types |
|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
| 2:1 (600x300 pixels minimum) |          500KB         | N/A - however a balance should be  struck between quality and size |  PNG, JPG  |
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


